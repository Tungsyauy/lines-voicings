// Program to print out all CELLS2_down2 cells
// This shows CELLS2 transposed down 2 semitones (whole step)

// BASE_CELLS (dominant 7sus4 cells)
const BASE_CELLS = [
    ["Bb4", "D4", "F4", "F#4", "A4"],
    ["D4", "F4", "E4", "D4", "C4"],
    ["A4", "G4", "F#4", "G4", "C5"],
    ["E4", "G4", "Bb4", "D5", "C5"],
    ["C5", "B4", "Bb4", "A4", "G4"],
    ["C4", "D4", "E4", "G4", "Bb4"],
    ["Bb4", "A4", "G4", "F4", "E4"],
    ["Bb3", "C4", "D4", "F4", "E4"],
    ["G4", "D4", "F4", "Eb4", "E4"],
    ["D4", "F4", "D4", "Eb4", "E4"],
    ["E4", "D4", "C4", "B3", "Bb3"],
    ["E5", "F5", "D5", "Bb4", "A4"],
    ["A4", "Bb4", "F#4", "A4", "G4"],
    ["Bb4", "F4", "F#4", "A4", "G4"],
    ["F#4", "A4", "G#4", "F#4", "G4"],
    ["D4", "F4", "F#4", "A4", "G4"],
    ["G4", "A4", "Bb4", "C5", "D5"],
    ["G4", "F4", "E4", "D4", "C4"],
    ["G4", "Bb4", "D5", "F5", "E5"],
    ["D5", "Ab4", "A4", "C5", "Bb4"],
    ["G4", "F4", "E4", "F4", "D4"],
    ["D5", "Bb4", "A4", "G4", "C5"],
    ["D5", "Bb4", "G4", "F4", "E4"],
    ["Bb3", "C4", "D4", "E4", "F4"],
    ["C5", "B4", "Bb4", "D4", "F4"],
    ["F4", "F#4", "A4", "Ab4", "G4"],
    ["F4", "D4", "C4", "Bb3", "A3"],
    ["Bb3", "C4", "D4", "F4", "F#4"],
    ["F#4", "A4", "G4", "F4", "E4"],
    ["F#4", "A4", "G4", "E4", "C4"],
    ["A4", "Bb4", "D5", "F5", "F#5"],
    ["Bb4","F#4","A4","Ab4","G4"],
    ["A4","G4","D4","F4","E4"],
    ["A4","G4","D4","F4","F#4"],
    ["C5", "B4", "Bb4", "F4", "F#4"],
    ["C5","B4","Bb4","C5","D5"],
    ["Bb4", "D4", "Db4", "D4", "A4"],
    ["Bb3", "F4", "D4", "Bb3", "A3"],
    ["F#4", "D4", "F4", "Eb4", "E4"],
];

// Additional cells unique to CELLS2 (these are only in CELLS2, not in base CELLS)
const BASE_CELLS2_ADDITIONAL = [
    ["D5", "Bb4", "A4", "G4", "F#4"],
    ["G4", "A4", "Bb4", "C5", "Db5"],
    ["G4", "A4", "Bb4", "C5", "Eb5"],
    ["C5", "Bb4", "A4", "Bb4", "Eb5"],
    ["G4", "F4", "E4", "F4", "Db4"],
    ["D5", "Bb4", "A4", "G4", "Ab4"],
    ["C5", "B4", "Bb4", "A4", "Ab4"],
    ["Bb3", "D4", "F4", "A4", "Ab4"],
    ["Bb4", "D4", "F4", "A4", "Ab4"],
    ["D4", "F4", "F#4", "A4", "Ab4"],
];

// CELLS2 = BASE_CELLS + BASE_CELLS2_ADDITIONAL
const CELLS2 = [...BASE_CELLS, ...BASE_CELLS2_ADDITIONAL];

// Note: The problematic cell ["G4", "F4", "E4", "F4", "Db4"] is filtered out
// So we have 49 cells total (50 original - 1 filtered)

// Correct transposition function (matching music-utils.js logic)
function transposeNoteDown2(note) {
    // Note to pitch conversion
    function noteToPitch(note) {
        const pitchClasses = {
            "C": 0, "Db": 1, "C#": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4,
            "F": 5, "Gb": 6, "F#": 6, "G": 7, "Ab": 8, "G#": 8, "A": 9,
            "Bb": 10, "A#": 10, "B": 11
        };
        
        const name = note.slice(0, -1);
        const octaveStr = note.slice(-1);
        const octave = parseInt(octaveStr);
        
        if (!(name in pitchClasses) || isNaN(octave)) {
            console.error('Invalid note:', note);
            return [undefined, undefined];
        }
        
        return [pitchClasses[name], octave];
    }
    
    const [pitchClass, octave] = noteToPitch(note);
    
    if (pitchClass === undefined || octave === undefined) {
        return note;
    }
    
    // Transpose down 2 semitones
    const newPitch = ((pitchClass - 2) % 12 + 12) % 12;
    const newOctave = octave + Math.floor((pitchClass - 2) / 12);
    
    // Use flat names for consistency with the codebase
    const PITCH_CLASSES_FLAT = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
                                6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"};
    
    const pitchName = PITCH_CLASSES_FLAT[newPitch];
    return `${pitchName}${newOctave}`;
}

// Generate CELLS2_down2
function generateCells2Down2() {
    const cells = [];
    
    for (const cell of CELLS2) {
        // Skip the problematic cell that gets filtered out
        if (JSON.stringify(cell) === JSON.stringify(["G4", "F4", "E4", "F4", "Db4"])) {
            continue;
        }
        
        const transposedCell = cell.map(note => transposeNoteDown2(note));
        cells.push(transposedCell);
    }
    
    return cells;
}

// Print all cells
console.log("=== CELLS2_down2 ===");
console.log("These are CELLS2 transposed down 2 semitones (whole step)");
console.log("Used in short_backdoor_25 phrases as the first cell");
console.log("");

const cells2Down2 = generateCells2Down2();

console.log(`Total cells: ${cells2Down2.length}`);
console.log("");
console.log("BASE_CELLS (first 35 cells):");
console.log("");

for (let i = 0; i < BASE_CELLS.length; i++) {
    const originalCell = BASE_CELLS[i];
    const transposedCell = cells2Down2[i];
    
    console.log(`Cell ${i + 1}:`);
    console.log(`  Original:  [${originalCell.join(', ')}]`);
    console.log(`  Down 2:    [${transposedCell.join(', ')}]`);
    console.log("");
}

console.log("BASE_CELLS2_ADDITIONAL (cells 36-49):");
console.log("");

for (let i = 0; i < BASE_CELLS2_ADDITIONAL.length; i++) {
    const originalCell = BASE_CELLS2_ADDITIONAL[i];
    const transposedCell = cells2Down2[BASE_CELLS.length + i];
    
    if (transposedCell) {
        console.log(`Cell ${BASE_CELLS.length + i + 1}:`);
        console.log(`  Original:  [${originalCell.join(', ')}]`);
        console.log(`  Down 2:    [${transposedCell.join(', ')}]`);
        console.log("");
    }
}

console.log("=== Summary ===");
console.log(`Original BASE_CELLS: ${BASE_CELLS.length} cells`);
console.log(`Original BASE_CELLS2_ADDITIONAL: ${BASE_CELLS2_ADDITIONAL.length} cells`);
console.log(`Original CELLS2 total: ${CELLS2.length} cells`);
console.log(`CELLS2_down2: ${cells2Down2.length} cells`);
console.log("(1 cell filtered out: [\"G4\", \"F4\", \"E4\", \"F4\", \"Db4\"])");
console.log("");
console.log("Transposition: Down 2 semitones (whole step)");
console.log("Usage: First cell in short_backdoor_25 phrases");
console.log("Chord context: Representing the ivm7 chord in backdoor progressions"); 