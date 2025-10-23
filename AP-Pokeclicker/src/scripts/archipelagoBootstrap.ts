// Create a new Archipelago client
const client: Client = new Client();
// @ts-ignore
window.client = client;

let checked_locations: number[] = [];

type GameOptions = {
    DeathLink?: number,
    DeathLink_Amnesty?: number,
    MedalHunt?: number,
    ExtraCheckpoint?: number,
    ExtraChecks?: number
};
let options: GameOptions = {}

let thisPlayer: number = 0;
type Players = Record<number, {
    slot: number,
    name: string,
    game: string,
    alias: string
}>;
let players: Players = {};

// Set up event listeners
client.messages.on("connected", async (text: string, player: Player, tags: string[], nodes: MessageNode[]) => {
    console.log("Connected to server: ", player);
    thisPlayer = player.slot;
    const slots: Record<number, NetworkSlot> = client.players.slots;
    Object.entries(slots).forEach(([key, slot]: [string, NetworkSlot]) => {
        const slotNumber: number = parseInt(key)
        const slotPlayer: Player = client.players.findPlayer(slotNumber);
        players[slotNumber] = {
            slot: slotNumber,
            name: slot.name,
            game: slot.game,
            alias: slotPlayer.alias,
        }
    });

    // set up gpio options
    options = await player.fetchSlotData().then(res => res as GameOptions);
    console.log("Options: ", options);

    client.socket.send({ cmd: "Sync" });
});

async function login() {
    const host = document.getElementById('ap-host').innerHTML;
    const port = document.getElementById('ap-port').innerHTML;
    const slot = document.getElementById('ap-slot').innerHTML;

    await client.login(
        host.startsWith("ws") ?
            `${host}:${port}` :
            `wss://${host}:${port}`,
        slot,
        "Pokeclicker").then(() => {
            console.log("Connected to the server");
        }).catch(error => {
            console.error("Failed to connect:", error);
        });

}