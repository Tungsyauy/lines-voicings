# data.py
from music_utils import transpose_note
from constants import LILYPOND_PITCHES, PITCH_CLASSES_SHARP, PITCH_CLASSES_FLAT, FLAT_KEYS, KEYS

# Unified cells for 7sus4 (dominant) phrases
CELLS = [
    ["Bb4", "D4", "F4", "F#4", "A4"],
    ["D4", "F4", "E4", "D4", "C4"],
    ["A4", "G4", "F#4", "G4", "C5"],
    ["E4", "G4", "Bb4", "D5", "C5"],
    ["C5", "B4", "Bb4", "A4", "G4"],
    ["C4", "D4", "E4", "G4", "Bb4"],
    ["Bb4", "A4", "G4", "F4", "E4"],
    ["Bb3", "C4", "D4", "F4", "E4"],
    ["G4", "D4", "F4", "D4", "E4"],
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
    ["F4", "D4", "Bb3", "G3", "E4"],
    ["F4", "D4", "C4", "Bb3", "A3"],
    ["Bb3", "C4", "D4", "F4", "F#4"],
    ["Bb4", "A4", "G4", "F4", "F#4"],
    ["F#4", "A4", "G4", "F4", "E4"],
    ["F#4", "A4", "G4", "E4", "C4"],
]

# Unified cells for short 25 phrases
# Additional cells unique to CELLS2
CELLS2_ADDITIONAL = [
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
]

# Unified cells for short 25 phrases, combining CELLS and additional cells
CELLS2 = CELLS + CELLS2_ADDITIONAL

# Cells for major phrases (C major cells)
MAJOR_CELLS = [
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
    ["C5", "G4", "Ab4", "B4", "A4"]
]

# Cells for major resolution (C dominant resolving to F major)
MAJOR_RESOLUTION_CELLS = [
    ["C5", "Bb4", "Eb5", "Db5", "C5"],
    ["C5", "Ab4", "E4", "C4", "G4"],
    ["E4", "Db4", "C4", "Bb3", "A3"],
    ["E4", "Db5", "C5", "Bb4", "A4"],
    ["E4", "G4", "Bb4", "Db5", "C5"],
    ["E4", "G4", "Db4", "B3", "C4"],
    ["G4", "E4", "C4", "Bb3", "A3"],
    ["G4", "Ab4", "E4", "Db4", "C4"],
    ["Bb4", "Ab4", "E4", "C4", "G4"],
    ["Bb4", "Ab4", "E4", "Db4", "C4"],
    ["Db4", "Eb4", "C4", "Bb3", "A3"],
    ["Eb4", "Db4", "C4", "Bb3", "A3"],
    ["Eb4", "Db4", "Ab3", "Bb3", "C4"],
    ["Eb4", "Db4", "Ab3", "E3", "C4"],
    ["F#4", "E4", "Eb4", "Db4", "C4"],
    ["F#4", "A4", "G4", "E4", "C4"],
    ["A4", "G4", "Gb4", "G4", "C5"],
    ["A4", "Ab4", "E4", "C4", "G4"],
    ["A4", "G4", "Eb4", "E4", "G4"],
    ["A4", "Ab4", "E4", "Db4", "C4"],
    ["Ab4", "E4", "Eb4", "Db4", "C4"],
    ["Ab4", "E5", "Eb5", "Db5", "C5"],
]

# Cells for minor phrases
minor_B_cells = [
    ["D4", "C4", "B3", "A3", "G#3"],
    ["B3", "D4", "F4", "A4", "G#4"],
    ["A4", "F4", "D4", "B3", "G#4"],
    ["F4", "D4", "B3", "A3", "G#3"],
    ["B4", "F4", "A4", "G4", "G#4"],
]

minor_C_cells = [
    ["G#4", "F4", "E4", "D4", "C4"],
    ["G#3", "F4", "E4", "D4", "C4"],
    ["G#3", "B3", "E4", "D4", "C4"],
    ["G#3", "B3", "D4", "F4", "E4"],
    ["G#4", "F4", "D4", "D#4", "E4"],
    ["G#3", "F4", "D4", "D#4", "E4"],
    ["G#4", "B4", "F4", "D#4", "E4"],
]

# cells for Gsus7
# Cells for CELLS transposed down five semitones
CELLSM5 = [
    [transpose_note(note, -5, "C") for note in cell] for cell in CELLS
]

# minor_C_cells transposed down 2 semitones
minor_C_cells_down2 = [
    [transpose_note(note, -2, "C") for note in cell] for cell in minor_C_cells
]

# Turnaround cells as provided
turnaround_cells_1 = [
    ["A4", "G4", "E4", "F4", "Gb4"],
    ["A4", "E4", "G4", "F4", "Gb4"],
    ["A4", "C4", "E4", "G4", "Gb4"],
    ["A4", "C5", "E5", "G5", "Gb5"],
    ["C5", "Bb4", "A4", "G4", "Gb4"],
    ["C4", "D4", "E4", "G4", "Gb4"],
]
# Cells for rhythm changes bar 5-6 resolution (DFB)
DFB = [
    ["A4", "C5", "Eb5", "F#5", "G5"],
    ["C4", "Eb4", "F#4", "A4", "G4"],
    ["F#4", "A4", "G#4", "F#4", "G4"],
    ["D#4", "F#4", "B4", "A4", "G4"],
    ["D#4", "A4", "G#4", "F#4", "G4"],
    ["D#4", "C4", "A3", "F#3", "G3"]
]

# CELLS in F
# CELLS transposed up 5 semitones, excluding cells that start with note "F"
CELLS_up5 = [
    [transpose_note(note, 5, "C") for note in cell] for cell in CELLS if cell[0][:-1] != "F"
]

# CELLS transposed up 2 semitones, excluding cells that start with note "F"
CELLS_up2 = [
    [transpose_note(note, 2, "C") for note in cell] for cell in CELLS if cell[0][:-1] != "F"
]

# CELLS transposed down 5 semitones, excluding cells that start with note "F"
CELLS_down5 = [
    [transpose_note(note, -5, "C") for note in cell] for cell in CELLS if cell[0][:-1] != "F"
]


# Chord mappings for each key
KEY_CHORD_MAP = {
    "7sus4": {
        "C": "usable on Gm, C7, Eø7, F#7Alt",
        "G": "usable on Dm, G7, Bø7, Db7Alt",
        "D": "usable on Am, D7, F#ø7, Ab7Alt",
        "A": "usable on Em, A7, C#ø7, Eb7Alt",
        "E": "usable on Bm, E7, G#ø7, Bb7Alt",
        "B": "usable on F#m, B7, D#ø7, F7Alt",
        "F#": "usable on C#m, F#7, A#ø7, C7Alt",
        "Db": "usable on Abm, Db7, Fø7, G7Alt",
        "Ab": "usable on Ebm, Ab7, Cø7, D7Alt",
        "Eb": "usable on Bbm, Eb7, Gø7, A7Alt",
        "Bb": "usable on Fm, Bb7, Dø7, E7Alt",
        "F": "usable on Cm, F7, Aø7, B7Alt"
    },
    "major": {
        "C": "usable on C",
        "G": "usable on G",
        "D": "usable on D",
        "A": "usable on A",
        "E": "usable on E",
        "B": "usable on B",
        "F#": "usable on F#",
        "Db": "usable on Db",
        "Ab": "usable on Ab",
        "Eb": "usable on Eb",
        "Bb": "usable on Bb",
        "F": "usable on F"
    },
    "short_25_major": {
        "C": "in the key of F",
        "G": "in the key of C",
        "D": "in the key of G",
        "A": "in the key of D",
        "E": "in the key of A",
        "B": "in the key of E",
        "F#": "in the key of B",
        "Db": "in the key of F#",
        "Ab": "in the key of Db",
        "Eb": "in the key of Ab",
        "Bb": "in the key of Eb",
        "F": "in the key of Bb"
    },
    "long_25_major": {
        "C": "in the key of F",
        "G": "in the key of C",
        "D": "in the key of G",
        "A": "in the key of D",
        "E": "in the key of A",
        "B": "in the key of E",
        "F#": "in the key of B",
        "Db": "in the key of F#",
        "Ab": "in the key of Db",
        "Eb": "in the key of Ab",
        "Bb": "in the key of Eb",
        "F": "in the key of Bb"
    },
    "short_25_minor": {
        "C": "in the key of Am",
        "G": "in the key of Em",
        "D": "in the key of Bm",
        "A": "in the key of F#m",
        "E": "in the key of C#m",
        "B": "in the key of Abm",
        "F#": "in the key of Ebm",
        "Db": "in the key of Bbm",
        "Ab": "in the key of Fm",
        "Eb": "in the key of Cm",
        "Bb": "in the key of Gm",
        "F": "in the key of Dm"
    },
    "long_25_minor": {
        "C": "in the key of Am",
        "G": "in the key of Em",
        "D": "in the key of Bm",
        "A": "in the key of F#m",
        "E": "in the key of C#m",
        "B": "in the key of Abm",
        "F#": "in the key of Ebm",
        "Db": "in the key of Bbm",
        "Ab": "in the key of Fm",
        "Eb": "in the key of Cm",
        "Bb": "in the key of Gm",
        "F": "in the key of Dm"
    },
    "turnaround": {
        "C": "in the key of C",
        "G": "in the key of G",
        "D": "in the key of D",
        "A": "in the key of A",
        "E": "in the key of E",
        "B": "in the key of B",
        "F#": "in the key of F#",
        "Db": "in the key of Db",
        "Ab": "in the key of Ab",
        "Eb": "in the key of Eb",
        "Bb": "in the key of Bb",
        "F": "in the key of F"
    },
    "rhythm_changes_56": {
        "C": "in the key of C",
        "G": "in the key of G",
        "D": "in the key of D",
        "A": "in the key of A",
        "E": "in the key of E",
        "B": "in the key of B",
        "F#": "in the key of F#",
        "Db": "in the key of Db",
        "Ab": "in the key of Ab",
        "Eb": "in the key of Eb",
        "Bb": "in the key of Bb",
        "F": "in the key of F"
    },
    "ii7_to_v7": {
        "C": "in the key of C",
        "G": "in the key of G",
        "D": "in the key of D",
        "A": "in the key of A",
        "E": "in the key of E",
        "B": "in the key of B",
        "F#": "in the key of F#",
        "Db": "in the key of Db",
        "Ab": "in the key of Ab",
        "Eb": "in the key of Eb",
        "Bb": "in the key of Bb",
        "F": "in the key of F"
    }
}