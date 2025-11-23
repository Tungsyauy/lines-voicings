// Program to show the updated short backdoor 25 phrase construction
// Now uses BACKDOOR_RESOLUTION instead of MAJOR_RESOLUTION_CELLS_down5

console.log("=== UPDATED SHORT BACKDOOR 25 PHRASE CONSTRUCTION ===");
console.log("");

// Show the new structure
console.log("OLD STRUCTURE:");
console.log("1 cell from CELLS2_down2 (representing Fm/Bb7) + resolution cell from MAJOR_RESOLUTION_CELLS_down5 (resolving to C)");
console.log("");

console.log("NEW STRUCTURE:");
console.log("1 cell from CELLS2_down2 (representing Fm/Bb7) + resolution cell from BACKDOOR_RESOLUTION (resolving to C)");
console.log("");

// Show the new BACKDOOR_RESOLUTION cells
console.log("=== NEW BACKDOOR_RESOLUTION CELLS ===");
console.log("These are the 15 new resolution cells specifically designed for backdoor progressions:");
console.log("");

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

for (let i = 0; i < BACKDOOR_RESOLUTION.length; i++) {
    const cell = BACKDOOR_RESOLUTION[i];
    console.log(`Cell ${i + 1}: [${cell.join(', ')}]`);
}

console.log("");
console.log("=== COMPARISON ===");
console.log("");

console.log("MAJOR_RESOLUTION_CELLS_down5 (OLD):");
console.log("- 21 cells transposed down 5 semitones from BASE_MAJOR_RESOLUTION_CELLS");
console.log("- Generic resolution patterns for major progressions");
console.log("- Not specifically designed for backdoor progressions");
console.log("");

console.log("BACKDOOR_RESOLUTION (NEW):");
console.log("- 15 cells specifically designed for backdoor progressions");
console.log("- Resolution patterns that work well for ivm7 → bVII7 → I progressions");
console.log("- More appropriate harmonic movement for backdoor endings");
console.log("");

console.log("=== BENEFITS OF THE CHANGE ===");
console.log("1. More appropriate resolution patterns for backdoor progressions");
console.log("2. Better harmonic coherence between the ivm7 chord and the tonic resolution");
console.log("3. Eliminates the need for transposition (no more -5 semitones)");
console.log("4. More direct and musical connection between the progression elements");
console.log("");

console.log("=== EXAMPLE PHRASE STRUCTURE ===");
console.log("For key C backdoor progression (Fm → Bb7 → C):");
console.log("- First cell: 4 notes from CELLS2_down2 (representing Fm/Bb7)");
console.log("- Resolution cell: 5 notes from BACKDOOR_RESOLUTION (resolving to C)");
console.log("- Total: 9 notes");
console.log("- No transposition needed"); 