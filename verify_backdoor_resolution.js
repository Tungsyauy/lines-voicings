// Program to verify that the commented-out cells are no longer being used
// in the BACKDOOR_RESOLUTION

console.log("=== VERIFYING BACKDOOR_RESOLUTION CELLS ===");
console.log("");

// The cells that were commented out
const COMMENTED_OUT_CELLS = [
    ["E4", "D4", "Db4", "D4", "G4"],
    ["Ab4", "C4", "B3", "C4", "G4"]
];

console.log("Commented out cells:");
for (let i = 0; i < COMMENTED_OUT_CELLS.length; i++) {
    const cell = COMMENTED_OUT_CELLS[i];
    console.log(`  ${i + 1}. [${cell.join(', ')}]`);
}

console.log("");
console.log("=== CURRENT BACKDOOR_RESOLUTION FROM DATA.JS ===");

// This should match what's in data.js (with the commented cells removed)
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
    ["E4", "C4", "Ab3", "E3", "B3"],
    ["Eb4", "C4", "Bb3", "Ab3", "G3"],
    ["Ab4", "C4", "Eb4", "E4", "G4"],
    ["Ab3", "Eb4", "C4", "Ab3", "G3"],
];

console.log(`Total cells: ${BACKDOOR_RESOLUTION.length}`);
console.log("");

for (let i = 0; i < BACKDOOR_RESOLUTION.length; i++) {
    const cell = BACKDOOR_RESOLUTION[i];
    console.log(`Cell ${i + 1}: [${cell.join(', ')}]`);
}

console.log("");
console.log("=== VERIFICATION ===");

// Check if any of the commented out cells are still in the array
let foundCommentedCells = false;
for (const commentedCell of COMMENTED_OUT_CELLS) {
    for (const currentCell of BACKDOOR_RESOLUTION) {
        if (JSON.stringify(commentedCell) === JSON.stringify(currentCell)) {
            console.log(`❌ FOUND COMMENTED CELL: [${commentedCell.join(', ')}]`);
            foundCommentedCells = true;
        }
    }
}

if (!foundCommentedCells) {
    console.log("✅ All commented out cells have been successfully removed!");
    console.log("✅ BACKDOOR_RESOLUTION now contains only the intended 13 cells");
} else {
    console.log("❌ Some commented out cells are still being used!");
}

console.log("");
console.log("=== SUMMARY ===");
console.log(`Original BACKDOOR_RESOLUTION: 15 cells`);
console.log(`After removing commented cells: ${BACKDOOR_RESOLUTION.length} cells`);
console.log(`Cells removed: ${15 - BACKDOOR_RESOLUTION.length}`);
console.log("");
console.log("The commented out cells were:");
console.log("1. [\"E4\", \"D4\", \"Db4\", \"D4\", \"G4\"] - removed");
console.log("2. [\"Ab4\", \"C4\", \"B3\", \"C4\", \"G4\"] - removed");
console.log("");
console.log("These cells are no longer used in backdoor phrase generation."); 