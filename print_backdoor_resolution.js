// Program to print out all BACKDOOR_RESOLUTION cells
// This shows the new resolution cells for short backdoor 25 phrases

// New BACKDOOR_RESOLUTION cells (replacing MAJOR_RESOLUTION_CELLS_down5)
const BACKDOOR_RESOLUTION = [
    ["G4", "F4", "Bb4", "Ab4", "G4"],
    ["C4", "Ab3", "G3", "F3", "E3"],
    ["D4", "C4", "Ab3", "F3", "E3"],
    ["D4", "Eb4", "C4", "Ab3", "G3"],
    ["F4", "G4", "Ab4", "Bb4", "G4"],
    ["Ab3", "Bb3", "G3", "F3", "E3"],
    ["Bb3", "Ab3", "G3", "F3", "E3"],
    ["Bb3", "Ab3", "Eb3", "F3", "G3"],
    ["Bb3", "Ab3", "Eb3", "C3", "G3"],
    ["E4", "D4", "Db4", "D4", "G4"],
    ["E4", "C4", "Ab3", "E3", "B3"],
    ["Eb4", "C4", "Bb3", "Ab3", "G3"],
    ["Ab4", "C4", "Eb4", "E4", "G4"],
    ["Ab4", "C4", "B3", "C4", "G4"],
    ["Ab3", "Eb4", "C4", "Ab3", "G3"],
];

// Print all cells
console.log("=== BACKDOOR_RESOLUTION ===");
console.log("New resolution cells for short backdoor 25 phrases");
console.log("Replaces MAJOR_RESOLUTION_CELLS_down5");
console.log("");

console.log(`Total cells: ${BACKDOOR_RESOLUTION.length}`);
console.log("");

for (let i = 0; i < BACKDOOR_RESOLUTION.length; i++) {
    const cell = BACKDOOR_RESOLUTION[i];
    
    console.log(`Cell ${i + 1}: [${cell.join(', ')}]`);
}

console.log("");
console.log("=== Summary ===");
console.log(`BACKDOOR_RESOLUTION: ${BACKDOOR_RESOLUTION.length} cells`);
console.log("");
console.log("Usage: Resolution cells in short_backdoor_25 phrases");
console.log("Chord context: Resolving to the tonic chord in backdoor progressions");
console.log("Structure: 5-note resolution patterns that work for backdoor endings");
console.log("");
console.log("Note: These cells are designed specifically for backdoor progressions");
console.log("and provide more appropriate resolution patterns than the generic");
console.log("MAJOR_RESOLUTION_CELLS_down5 that were used before."); 