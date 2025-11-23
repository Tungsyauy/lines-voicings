// print_major_cells_down4.js
// Program to print out all cells in MAJOR_CELLS_down4 using exact same logic as the program

console.log('=== MAJOR_CELLS_down4 CELLS ===');
console.log('These are the C major cells transposed down 4 semitones:');
console.log('');

// Copy the exact transpose logic from music-utils.js
function noteToPitch(note) {
    const pitchClasses = {
        "C": 0, "Db": 1, "C#": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4,
        "F": 5, "Gb": 6, "F#": 6, "G": 7, "Ab": 8, "G#": 8, "A": 9,
        "Bb": 10, "A#": 10, "B": 11
    };
    
    if (!note || typeof note !== 'string') {
        console.error('Invalid note input:', note);
        return [undefined, undefined];
    }
    
    const name = note.slice(0, -1);
    const octaveStr = note.slice(-1);
    const octave = parseInt(octaveStr);
    
    if (!(name in pitchClasses)) {
        console.error('Invalid note name:', name, 'in note:', note);
        return [undefined, undefined];
    }
    
    if (isNaN(octave)) {
        console.error('Invalid octave:', octaveStr, 'in note:', note);
        return [undefined, undefined];
    }
    
    return [pitchClasses[name], octave];
}

function transposeNote(note, semitones, key) {
    const [pitchClass, octave] = noteToPitch(note);
    
    if (pitchClass === undefined || octave === undefined) {
        console.error('Invalid note in transposeNote:', note);
        return note;
    }
    
    const newPitch = ((pitchClass + semitones) % 12 + 12) % 12;
    const newOctave = octave + Math.floor((pitchClass + semitones) / 12);
    
    const PITCH_CLASSES_SHARP = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
                                 6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"};
    const PITCH_CLASSES_FLAT = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
                                6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"};
    const FLAT_KEYS = new Set(["Db", "Ab", "Eb", "Bb", "F", "C"]);
    
    const pitchClasses = FLAT_KEYS.has(key) ? PITCH_CLASSES_FLAT : PITCH_CLASSES_SHARP;
    let pitchName = pitchClasses[newPitch];
    
    if (["F#", "B", "E", "A", "D", "G"].includes(key)) {
        if (["Db", "Eb", "Gb", "Ab", "Bb"].includes(pitchName)) {
            const sharpMap = {1: "C#", 3: "D#", 6: "F#", 8: "G#", 10: "A#"};
            pitchName = sharpMap[newPitch] || pitchName;
        }
    }
    
    return `${pitchName}${newOctave}`;
}

function transposeCells(baseCells, semitones, key = "C") {
    return baseCells.map(cell => 
        cell.map(note => transposeNote(note, semitones, key))
    );
}

// Copy the exact BASE_MAJOR_CELLS from data.js
const BASE_MAJOR_CELLS = [
    ["G4", "A4", "B4", "D5", "C5"],
    ["E4", "G4", "B4", "D5", "C5"],
    ["E4", "G4", "B4", "D5", "B4"],
    ["B4", "C5", "D5", "Db5", "C5"],
    ["E5", "Bb4", "B4", "D5", "C5"],
    ["C5", "B4", "A4", "Ab4", "G4"],
    ["C4", "D4", "E4", "G4", "B4"],
    ["C5", "E4", "G4", "B4", "A4"],
    ["B4", "A4", "G4", "F4", "E4"],
    ["D4", "C4", "B3", "C4", "E4"],
    ["E4", "G4", "A4", "B4", "D5"],
    ["D5", "C5", "B4", "A4", "G4"],
    ["E4", "G4", "B4", "A4", "G4"],
    ["B4", "A4", "G#4", "F#4", "G4"],
    ["G4", "F4", "E4", "D4", "B3"],
    ["G4", "E4", "D4", "C4", "B3"],
    ["G4", "E4", "B3", "G3", "A3"],
    ["B3", "C4", "E4", "G4", "B4"],
    ["D5", "C5", "E4", "G4", "B4"],
    ["E5", "D5", "Bb4", "B4", "D5"],
    ["B4", "A4", "G4", "E4", "D4"],
    ["D5", "Db5", "C5", "E5", "B4"],
    ["C5", "E4", "G4", "B4", "A4"],
    ["A4", "G4", "G#4", "F#4", "G4"],
    ["A4", "G#4", "G4", "F4", "E4"],
    ["A4", "G4", "C4", "F4", "E4"],
    ["G4", "B3", "C4", "F4", "E4"],
    ["G4", "F4", "D4", "Eb4", "E4"],
    ["B4", "C5", "G#4", "B4", "A4"],
    ["E4", "C4", "B3", "A3", "D4"],
    ["C5", "E4", "Eb4", "E4", "B4"],
    ["A4", "C5", "B4", "A4", "G4"],
    ["C5", "G4", "Ab4", "B4", "A4"],
    ["B4", "C5", "G4", "E4", "A4"]
];

// Generate MAJOR_CELLS_down4 using exact same logic as data.js
console.log('Generating MAJOR_CELLS_down4 using exact same logic as the program...');
const MAJOR_CELLS_down4 = transposeCells(BASE_MAJOR_CELLS, -4, "C");
console.log(`Total cells: ${MAJOR_CELLS_down4.length}`);
console.log('');

// Print each cell with its index
MAJOR_CELLS_down4.forEach((cell, index) => {
    console.log(`Cell ${index + 1}: [${cell.join(', ')}]`);
});

console.log('');
console.log('=== END OF MAJOR_CELLS_down4 ===');

// Analysis
console.log('');
console.log('=== CELL ANALYSIS ===');

// Count cells starting with each note
const startNoteCounts = {};
MAJOR_CELLS_down4.forEach(cell => {
    const startNote = cell[0].slice(0, -1); // Remove octave
    startNoteCounts[startNote] = (startNoteCounts[startNote] || 0) + 1;
});

console.log('Cells starting with each note:');
Object.entries(startNoteCounts).forEach(([note, count]) => {
    console.log(`  ${note}: ${count} cells`);
});

// Count cells ending with each note
const endNoteCounts = {};
MAJOR_CELLS_down4.forEach(cell => {
    const endNote = cell[cell.length - 1].slice(0, -1); // Remove octave
    endNoteCounts[endNote] = (endNoteCounts[endNote] || 0) + 1;
});

console.log('');
console.log('Cells ending with each note:');
Object.entries(endNoteCounts).forEach(([note, count]) => {
    console.log(`  ${note}: ${count} cells`);
});

console.log('');
console.log('=== END ANALYSIS ===');

// Check if MAJOR_CELLS_down4 is available in browser environment
if (typeof window !== 'undefined' && window.MAJOR_CELLS_down4) {
    console.log('');
    console.log('=== BROWSER COMPARISON ===');
    console.log('MAJOR_CELLS_down4 is available in browser environment');
    console.log(`Browser cells count: ${window.MAJOR_CELLS_down4.length}`);
    
    // Compare first few cells
    const browserCells = window.MAJOR_CELLS_down4;
    const matchCount = MAJOR_CELLS_down4.filter((cell, index) => 
        browserCells[index] && JSON.stringify(cell) === JSON.stringify(browserCells[index])
    ).length;
    
    console.log(`Matching cells: ${matchCount}/${Math.min(MAJOR_CELLS_down4.length, browserCells.length)}`);
    
    if (matchCount === MAJOR_CELLS_down4.length) {
        console.log('✅ All cells match!');
    } else {
        console.log('❌ Some cells do not match');
        console.log('First browser cell:', browserCells[0]);
        console.log('First calculated cell:', MAJOR_CELLS_down4[0]);
    }
    
    console.log('=== END BROWSER COMPARISON ===');
} else {
    console.log('');
    console.log('MAJOR_CELLS_down4 not available in browser environment');
    console.log('Run this in the browser console after loading the web application');
} 