// Program to print out all MAJOR_RESOLUTION_CELLS_down5
// This shows the original BASE_MAJOR_RESOLUTION_CELLS transposed down 5 semitones (perfect fourth)

// Original BASE_MAJOR_RESOLUTION_CELLS (C dominant resolving to F major)
const BASE_MAJOR_RESOLUTION_CELLS = [
    ["C5", "Bb4", "Eb5", "Db5", "C5"],
    ["C5", "Ab4", "E4", "C4", "G4"],
    ["E4", "Db4", "C4", "Bb3", "A3"],
    ["E4", "Db5", "C5", "Bb4", "A4"],
    ["E4", "G4", "Bb4", "Db5", "C5"],
    ["E4", "G4", "Db4", "B3", "C4"],
    ["G4", "F4", "Db4", "Bb3", "A3"],
    ["G4", "Ab4", "E4", "Db4", "C4"],
    ["Bb4", "Ab4", "E4", "C4", "G4"],
    ["Bb4", "Ab4", "E4", "Db4", "C4"],
    ["Db4", "Eb4", "C4", "Bb3", "A3"],
    ["Eb4", "Db4", "C4", "Bb3", "A3"],
    ["Eb4", "Db4", "Ab3", "Bb3", "C4"],
    ["Eb4", "Db4", "Ab3", "E3", "C4"],
    ["F#4", "A4", "G4", "E4", "C4"],
    ["A4", "G4", "Gb4", "G4", "C5"],
    ["A4", "Ab4", "E4", "C4", "G4"],
    ["A4", "G4", "Eb4", "E4", "G4"],
    ["A4", "Ab4", "E4", "Db4", "C4"],
    ["Ab4", "E4", "Eb4", "Db4", "C4"],
    ["Ab4", "E5", "Eb5", "Db5", "C5"],
];

// Note: The problematic cell ["F#4", "E4", "Eb4", "Db4", "C4"] is filtered out
// So we have 20 cells total (21 original - 1 filtered)

// Correct transposition function (matching music-utils.js logic)
function transposeNoteDown5(note) {
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
    
    // Transpose down 5 semitones
    const newPitch = ((pitchClass - 5) % 12 + 12) % 12;
    const newOctave = octave + Math.floor((pitchClass - 5) / 12);
    
    // Use flat names for consistency with the codebase
    const PITCH_CLASSES_FLAT = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
                                6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"};
    
    const pitchName = PITCH_CLASSES_FLAT[newPitch];
    return `${pitchName}${newOctave}`;
}

// Generate MAJOR_RESOLUTION_CELLS_down5
function generateMajorResolutionCellsDown5() {
    const cells = [];
    
    for (const cell of BASE_MAJOR_RESOLUTION_CELLS) {
        // Skip the problematic cell that gets filtered out
        if (JSON.stringify(cell) === JSON.stringify(["F#4", "E4", "Eb4", "Db4", "C4"])) {
            continue;
        }
        
        const transposedCell = cell.map(note => transposeNoteDown5(note));
        cells.push(transposedCell);
    }
    
    return cells;
}

// Print all cells
console.log("=== MAJOR_RESOLUTION_CELLS_down5 ===");
console.log("These are BASE_MAJOR_RESOLUTION_CELLS transposed down 5 semitones (perfect fourth)");
console.log("Used in short_backdoor_25 phrases as resolution cells");
console.log("");

const majorResolutionCellsDown5 = generateMajorResolutionCellsDown5();

console.log(`Total cells: ${majorResolutionCellsDown5.length}`);
console.log("");

for (let i = 0; i < majorResolutionCellsDown5.length; i++) {
    const originalCell = BASE_MAJOR_RESOLUTION_CELLS[i];
    const transposedCell = majorResolutionCellsDown5[i];
    
    console.log(`Cell ${i + 1}:`);
    console.log(`  Original:  [${originalCell.join(', ')}]`);
    console.log(`  Down 5:    [${transposedCell.join(', ')}]`);
    console.log("");
}

console.log("=== Summary ===");
console.log(`Original BASE_MAJOR_RESOLUTION_CELLS: ${BASE_MAJOR_RESOLUTION_CELLS.length} cells`);
console.log(`MAJOR_RESOLUTION_CELLS_down5: ${majorResolutionCellsDown5.length} cells`);
console.log("(1 cell filtered out: [\"F#4\", \"E4\", \"Eb4\", \"Db4\", \"C4\"])");
console.log("");
console.log("Transposition: Down 5 semitones (perfect fourth)");
console.log("Usage: Resolution cells in short_backdoor_25 phrases");
console.log("Chord context: Resolving to the tonic chord in backdoor progressions"); 