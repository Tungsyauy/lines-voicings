// Extract start notes from BASE_DFB cells
const BASE_DFB = [
    ["A4", "C5", "Eb5", "F#5", "G5"],
    ["C4", "Eb4", "F#4", "A4", "G4"],
    ["F#4", "A4", "G#4", "F#4", "G4"],
    ["D#4", "F#4", "B4", "A4", "G4"],
    ["D#4", "C4", "A3", "F#3", "G3"],
    ["F#4", "A4", "C5", "D#5", "E5"],
    ["A4", "F#4", "Eb4", "A4", "G4"],
    ["C5", "A4", "F#4", "D#4", "E4"],
    ["B4", "A4", "G#4", "A4", "C5"],
    ["D4", "C4", "B3", "A3", "C4"],
    ["D4", "Eb4", "B3", "D4", "C4"]
];

// Extract start notes (first note of each cell)
const startNotes = BASE_DFB.map(cell => cell[0]);

// Remove octave numbers to get pitch classes
const startPitchClasses = startNotes.map(note => note.slice(0, -1));

// Get unique start notes
const uniqueStartNotes = [...new Set(startPitchClasses)].sort();

console.log("All BASE_DFB start notes:", startNotes);
console.log("Start pitch classes:", startPitchClasses);
console.log("Unique start pitch classes in BASE_DFB:", uniqueStartNotes);
console.log("Count:", uniqueStartNotes.length);

// Check if F# and D# are present
console.log("Contains F#:", uniqueStartNotes.includes('F#'));
console.log("Contains D#:", uniqueStartNotes.includes('D#'));
