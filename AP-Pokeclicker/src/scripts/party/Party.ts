/// <reference path="../../declarations/GameHelper.d.ts" />
/// <reference path="../../declarations/DataStore/common/Feature.d.ts" />
///<reference path="../../declarations/enums/CaughtStatus.d.ts"/>

class Party implements Feature, TmpPartyType {
    name = 'Pokemon Party';
    saveKey = 'party';

    private _caughtPokemon: KnockoutObservableArray<PartyPokemon>;

    defaults = {
        caughtPokemon: [],
    };

    hasMaxLevelPokemon: KnockoutComputed<boolean>;

    hasShadowPokemon: KnockoutComputed<boolean>;

    private _caughtPokemonLookup: KnockoutComputed<Map<number, PartyPokemon>>;

    calculateBaseClickAttack: KnockoutComputed<number>;

    constructor(private multiplier: Multiplier) {
        this._caughtPokemon = ko.observableArray([]);

        this.hasMaxLevelPokemon = ko.pureComputed(() => {
            return this.caughtPokemon.some(p => p.level === 100);
        }).extend({rateLimit: 1000});

        this.hasShadowPokemon = ko.computed(() => {
            return this.caughtPokemon.some(p => p.shadow === GameConstants.ShadowStatus.Shadow);
        }).extend({rateLimit: 1000});

        // This will be completely rebuilt each time a pokemon is caught.
        // Use the RAW list for lookup so callers like the Pokédex can access entries even if not yet received
        this._caughtPokemonLookup = ko.computed(() => {
            return this._caughtPokemon().reduce((map, p) => {
                map.set(p.id, p);
                return map;
            }, new Map<number, PartyPokemon>());
        });

        this.calculateBaseClickAttack = ko.computed(() => {
            // Base power
            // Shiny pokemon help with a 100% boost
            // Resistant pokemon give a 100% boost
            const partyClickBonus = this.activePartyPokemon.reduce((total, p) => total + p.clickAttackBonus(), 1);
            return Math.pow(partyClickBonus, 1.4);
        });

    }

    // Whether a Pokémon has been received (visible party) by Name
    alreadyReceivedByName(name: PokemonNameType): boolean {
        const pokemon = pokemonMap[name];
        return this.alreadyReceived(pokemon.id);
    }

    // Whether a Pokémon has been received (visible party) by ID
    alreadyReceived(id: number): boolean {
        return this._caughtPokemon().some(p => p.id === id && p.received);
    }

    gainPokemonByName(name: PokemonNameType, shiny?: boolean, suppressNotification?: boolean, gender?: GameConstants.BattlePokemonGender, shadow?: GameConstants.ShadowStatus) {
        const pokemon = pokemonMap[name];
        this.gainPokemonById(pokemon.id, shiny, suppressNotification, gender, shadow);
    }

    gainPokemonById(id: number,
        shiny = false,
        suppressNewCatchNotification = false,
        gender: GameConstants.BattlePokemonGender = PokemonFactory.generateGenderById(id),
        shadow: GameConstants.ShadowStatus = GameConstants.ShadowStatus.None
    ) {
        const isShadow = shadow === GameConstants.ShadowStatus.Shadow;
        // Capture pre-increment stats to determine first capture
        const prevCaptured = +(App.game.statistics.pokemonCaptured[id]?.() ?? 0);
        let dexsanity = (window as any)?.APFlags?.dexsanity === true;
        if (dexsanity && id % 1 !== 0) {
            dexsanity = false; // Disable Dexsanity for alt forms
        }

        PokemonHelper.incrementPokemonStatistics(id, GameConstants.PokemonStatisticsType.Captured, shiny, gender, shadow);

        const newCatch = !this.alreadyCaughtPokemon(id); //prevCaptured === 0;
        const newShiny = shiny && !this._caughtPokemon().some(p => p.id === id && p.shiny);
        const newShadow = isShadow && !this._caughtPokemon().some(p => p.id === id && p.shadow > GameConstants.ShadowStatus.None);

        const existing = this._caughtPokemon().find(p => p.id === id);
        if (existing) {
            // Update existing entry (handles receive-before-catch and prior entries)
            existing.caught = true;
            if (newShiny) {
                existing.shiny = true;
            }
            if (newShadow) {
                existing.shadow = GameConstants.ShadowStatus.Shadow;
            }
        } else {
            // Create a new party entry
            const created = PokemonFactory.generatePartyPokemon(id, shiny, gender, shadow);
            created.received = dexsanity ? false : true;
            created.caught = true;
            this._caughtPokemon.push(created);
            this._caughtPokemon.sort((a, b) => a.id - b.id);
        }

        // Send location check on first capture under Dexsanity (applies to evolutions and normal captures)
        if (dexsanity && newCatch) {
            (window as any).sendLocationCheck(id, true);
        }

        // Resolve name info without assuming partyPokemon exists
        const dataMon = PokemonHelper.getPokemonById(id);
        const name = dataMon?.name;
        const displayName = name ? PokemonHelper.displayName(name)() : 'Pokemon';

        // Notifications
        if (newCatch && !suppressNewCatchNotification) {
            Notifier.notify({
                message: `You have captured ${GameHelper.anOrA(name)} ${displayName}!`,
                pokemonImage: PokemonHelper.getImage(id, shiny, gender, shadow),
                type: NotificationConstants.NotificationOption.success,
                sound: NotificationConstants.NotificationSound.General.new_catch,
                setting: NotificationConstants.NotificationSetting.General.new_catch,
            });
        }
        if (newShiny) {
            Notifier.notify({
                message: `✨ You have captured a shiny ${displayName}! ✨`,
                pokemonImage: PokemonHelper.getImage(id, shiny, gender, shadow),
                type: NotificationConstants.NotificationOption.warning,
                sound: NotificationConstants.NotificationSound.General.new_catch,
                setting: NotificationConstants.NotificationSetting.General.new_catch,
            });
        }
        if (newShadow) {
            Notifier.notify({
                message: `You have captured a shadow ${displayName}!`,
                pokemonImage: PokemonHelper.getImage(id, shiny, gender, shadow),
                type: NotificationConstants.NotificationOption.warning,
                sound: NotificationConstants.NotificationSound.General.new_catch,
                setting: NotificationConstants.NotificationSetting.General.new_catch,
            });
        }

        // Logbook entries
        if (newCatch && name) {
            App.game.logbook.newLog(LogBookTypes.CAUGHT, createLogContent.captured({ pokemon: name }));
        }
        if (shiny) {
            // Both new and duplicate shinies get logged
            const shinyLogContent = newShiny ? createLogContent.capturedShiny : createLogContent.capturedShinyDupe;
            if (name) {
                App.game.logbook.newLog(LogBookTypes.CAUGHT, shinyLogContent({ pokemon: name }));
            }
        }
        if (newShadow && name) {
            App.game.logbook.newLog(LogBookTypes.CAUGHT, createLogContent.capturedShadow({ pokemon: name }));
        }
    }

    // Called when AP server grants a Pokémon (receive path)
    receivePokemonById(id: number) {
        const dexsanity = (window as any)?.APFlags?.dexsanity === true;
        const existing = this._caughtPokemon().find(p => p.id === id);
        if (existing) {
            existing.received = true;
            return;
        }
        const created = PokemonFactory.generatePartyPokemon(id);
        created.received = true;

        // If the player is receiving a Pokémon before it has been counted as caught (edge case), leave caught=false
        this._caughtPokemon.push(created);
        this._caughtPokemon.sort((a, b) => a.id - b.id);
    }

    public removePokemonByName(name: PokemonNameType) {
        this._caughtPokemon.remove(p => p.name == name);
    }

    public gainExp(exp = 0, level = 1, trainer = false) {
        const multBonus = this.multiplier.getBonus('exp', true);
        const trainerBonus = trainer ? 1.5 : 1;
        const expTotal = Math.floor(exp * level * trainerBonus * multBonus / 9) * ((window as any).APFlags.options.exp_multiplier || 1);
        let shadowExpGained = 0;

        const dexsanity = (window as any)?.APFlags?.dexsanity === true;
        for (const pokemon of this.caughtPokemon) {
            if (dexsanity && !pokemon.received) {
                continue; // Unreceived should not gain EXP
            }
            const exp = pokemon.gainExp(expTotal);
            if (pokemon.shadow >= GameConstants.ShadowStatus.Shadow) {
                shadowExpGained += exp;
            }
        }
        App.game.purifyChamber.gainFlow(shadowExpGained);
    }

    /**
     * Calculate the attack of all your Pokémon
     * @param type1
     * @param type2 types of the enemy we're calculating damage against.
     * @returns {number} damage to be done.
     */

    public calculatePokemonAttack(
        type1: PokemonType = PokemonType.None,
        type2: PokemonType = PokemonType.None,
        ignoreRegionMultiplier = false,
        region: GameConstants.Region = player.region,
        includeBreeding = false,
        useBaseAttack = false,
        overrideWeather?: WeatherType,
        ignoreLevel = false,
        includeTempBonuses = true,
        subregion: GameConstants.SubRegions = player.subregion
    ): number {
        let attack = 0;
        const pokemon = this.partyPokemonActiveInSubRegion(region, subregion);
        const ignoreRegionMultiplierOrMKJ = ignoreRegionMultiplier || region == GameConstants.Region.alola && subregion == GameConstants.AlolaSubRegions.MagikarpJump;

        for (const p of pokemon) {
            attack += this.calculateOnePokemonAttack(p, type1, type2, region, ignoreRegionMultiplierOrMKJ, includeBreeding, useBaseAttack, overrideWeather, ignoreLevel, includeTempBonuses);
        }

        const bonus = this.multiplier.getBonus('pokemonAttack');
        return Math.round(attack * bonus);
    }

    public calculateOnePokemonAttack(
        pokemon: PartyPokemon,
        type1: PokemonType = PokemonType.None,
        type2: PokemonType = PokemonType.None,
        region: GameConstants.Region = player.region,
        ignoreRegionMultiplier = false,
        includeBreeding = false,
        useBaseAttack = false,
        overrideWeather?: WeatherType,
        ignoreLevel = false,
        includeTempBonuses = true
    ): number {
        let multiplier = 1, attack = 0;
        const pAttack = useBaseAttack ? pokemon.baseAttack : (ignoreLevel ? pokemon.calculateAttack(ignoreLevel) : pokemon.attack);
        const nativeRegion = PokemonHelper.calcNativeRegion(pokemon.name);
        const dataPokemon = PokemonHelper.getPokemonByName(pokemon.name);

        // Check if the pokemon is in their native region
        if (!ignoreRegionMultiplier && nativeRegion != region && nativeRegion != GameConstants.Region.none) {
            // Check if the challenge mode is active
            if (App.game.challenges.list.regionalAttackDebuff.active()) {
                // Pokemon only retain a % of their total damage in other regions based on highest region.
                multiplier = this.getRegionAttackMultiplier();
            }
        }

        // Check if the Pokemon is currently breeding (no attack)
        if (includeBreeding || !pokemon.breeding) {
            if (type1 == PokemonType.None) {
                attack = pAttack * multiplier;
            } else {
                attack = pAttack * TypeHelper.getAttackModifier(dataPokemon.type1, dataPokemon.type2, type1, type2) * multiplier;
            }
        }

        // Weather boost
        const weather = Weather.weatherConditions[overrideWeather ?? Weather.currentWeather()];
        weather.multipliers?.forEach(value => {
            if (value.type == dataPokemon.type1) {
                attack *= value.multiplier;
            }
            if (value.type == dataPokemon.type2) {
                attack *= value.multiplier;
            }
        });

        // Should we take flute boost into account
        if (includeTempBonuses) {
            FluteEffectRunner.activeGemTypes().forEach(value => {
                if (value == dataPokemon.type1) {
                    attack *= GameConstants.FLUTE_TYPE_ATTACK_MULTIPLIER;
                }
                if (value == dataPokemon.type2) {
                    attack *= GameConstants.FLUTE_TYPE_ATTACK_MULTIPLIER;
                }
            });
            attack *= App.game.zMoves.getMultiplier(dataPokemon.type1, dataPokemon.type2);
        }

        return attack;
    }

    public getRegionAttackMultiplier(highestRegion = player.highestRegion()): number {
        // between 0.2 -> 1 based on highest region
        return Math.min(1, Math.max(0.2, 0.1 + (highestRegion / 10)));
    }

    public calculateEffortPoints(pokemon: PartyPokemon, shiny: boolean, shadow: GameConstants.ShadowStatus, number = GameConstants.BASE_EP_YIELD, ignore = false): number {
        if (pokemon.pokerus < GameConstants.Pokerus.Contagious) {
            return 0;
        }

        if (ignore) {
            return 0;
        }

        let EPNum = number * App.game.multiplier.getBonus('ev');

        if (pokemon.heldItem() && pokemon.heldItem() instanceof EVsGainedBonusHeldItem) {
            EPNum *= (pokemon.heldItem() as EVsGainedBonusHeldItem).gainedBonus;
        }

        if (shiny) {
            EPNum *= GameConstants.SHINY_EP_MODIFIER;
        }

        if (shadow == GameConstants.ShadowStatus.Shadow) {
            EPNum *= GameConstants.SHADOW_EP_MODIFIER;
        }

        return Math.floor(EPNum);
    }

    public pokemonAttackObservable: KnockoutComputed<number> = ko.pureComputed(() => {
        return App.game.party.calculatePokemonAttack();
    }).extend({rateLimit: 1000});

    public getPokemon(id: number): PartyPokemon | undefined {
        // Always return the entry if it exists; views like the Pokédex should gate with alreadyReceived(id)
        return this._caughtPokemonLookup().get(id);
    }

    public getPokemonByName(name: PokemonNameType): PartyPokemon | undefined {
        return this._caughtPokemonLookup().get(pokemonMap[name].id);
    }

    public partyPokemonActiveInSubRegion(region: GameConstants.Region, subregion: GameConstants.SubRegions): Array<PartyPokemon> {
        let caughtPokemon = this.caughtPokemon.filter(p => p.received) as Array<PartyPokemon>;
        if (region == GameConstants.Region.alola && subregion == GameConstants.AlolaSubRegions.MagikarpJump) {
            // Only magikarps can attack in magikarp jump subregion
            caughtPokemon = caughtPokemon.filter((p) => Math.floor(p.id) == 129);
        }
        return caughtPokemon;
    }

    alreadyCaughtPokemonByName(name: PokemonNameType, shiny = false) {
        return this.alreadyCaughtPokemon(PokemonHelper.getPokemonByName(name).id, shiny);
    }

    alreadyCaughtPokemon(id: number, shiny = false, shadow = false, purified = false) {
        // Use the 'caught' flag to determine if this species has been caught before.
        // Additionally, when Dexsanity is ON, only consider as caught if the Pokémon has been received (for Pokédex/UI).
        const entry = this._caughtPokemon().find(p => p.id === id);
        if (!entry || !entry.caught) {
            return false;
        }
        // if ((window as any)?.APFlags?.dexsanity === true && !entry.received) return false;
        const shinyOkay = (!shiny || entry.shiny);
        const shadowOkay = (!shadow || (entry.shadow > GameConstants.ShadowStatus.None));
        const purifiedOkay = (!purified || (entry.shadow == GameConstants.ShadowStatus.Purified));
        return shinyOkay && shadowOkay && purifiedOkay;
    }

    calculateClickAttack(useItem = false): number {
        const clickAttack =  this.calculateBaseClickAttack();
        const bonus = this.multiplier.getBonus('clickAttack', useItem);
        return Math.floor(clickAttack * bonus);
    }

    public clickAttackBreakdown = ko.pureComputed((): ClickAttackBreakdown => {
        let numShiny = 0, numResistant = 0, numPurified = 0;
        this.activePartyPokemon.forEach((p) => {
            if (p.shiny) {
                numShiny += 1;
            }
            if (p.pokerus >= GameConstants.Pokerus.Resistant) {
                numResistant += 1;
            }
            if (p.shadow >= GameConstants.ShadowStatus.Purified) {
                numPurified += 1;
            }
        });

        return {
            caughtPokemon: this.activePartyPokemon.length,
            shinyPokemon: numShiny,
            resistantPokemon: numResistant,
            purifiedPokemon: numPurified,
            xClickModifier: EffectEngineRunner.isActive(ItemList.xClick.name)() ? (ItemList.xClick as BattleItem).multiplyBy : 1,
            blackFluteModifier: FluteEffectRunner.getFluteMultiplier(GameConstants.FluteItemType.Black_Flute),
            rockyHelmetModifier: App.game.oakItems.calculateBonus(OakItemType.Rocky_Helmet),
            baseClickAttack: Number(App.game.party.calculateBaseClickAttack().toFixed(4)),
        };
    });

    canAccess(): boolean {
        return true;
    }

    fromJSON(json: Record<string, any>): void {
        if (json == null) {
            return;
        }

        const caughtPokemonSave = json.caughtPokemon;
        const caughtPokemon = caughtPokemonSave.map(caughtPoke => {
            const partyPokemon = PokemonFactory.generatePartyPokemon(caughtPoke.id);
            partyPokemon.fromJSON(caughtPoke);
            return partyPokemon;
        });
        this._caughtPokemon(caughtPokemon);
    }

    initialize(): void {
    }

    toJSON(): Record<string, any> {
        return {
            caughtPokemon: this._caughtPokemon().map(x => x.toJSON()),
        };
    }

    update(delta: number): void {
        // This method intentionally left blank
    }

    get caughtPokemon(): ReadonlyArray<PartyPokemon> {
        // Always gate list visibility on received; when Dexsanity is disabled, all new catches are received immediately.
        return this._caughtPokemon().filter(p => p.received);
    }

    get activePartyPokemon(): ReadonlyArray<PartyPokemon> {
        return this.partyPokemonActiveInSubRegion(player.region, player.subregion);
    }

}
