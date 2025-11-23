# data.py

# Unified cells for 7sus4 (dominant) phrases
CELLS = [
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
    #["E4", "D4", "C4", "Bb3", "A3"],
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
CELLS2 = [
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
    #["E5", "F5", "D5", "Bb4", "A4"],
    ["E4", "D4", "C4", "Bb3", "A3"],
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
    ["G4", "A4", "Bb4", "C5", "Db5"],
    ["G4", "A4", "Bb4", "C5", "Eb5"],
    ["G4", "F4", "E4", "F4", "Db4"],
    ["C5", "B4", "Bb4", "A4", "Ab4"],
    ["Bb3", "D4", "F4", "A4", "Ab4"]
]

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
MAJOR_RESOLUTION_CELLS = [ #C E G Bb Db Eb Gb A F#
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
    ["A4", "Ab4", "E4", "Db4", "C4"],
    ["Ab4", "E4", "Eb4", "Db4", "C4"]
]

# LilyPond pitch mapping
LILYPOND_PITCHES = {
    "C3": "c", "Db3": "des", "C#3": "cis", "D3": "d", "Eb3": "ees", "D#3": "dis", "E3": "e",
    "F3": "f", "Gb3": "ges", "F#3": "fis", "G3": "g", "Ab3": "aes", "G#3": "gis", "A3": "a",
    "Bb3": "bes", "A#3": "ais", "B3": "b",
    "C4": "c'", "Db4": "des'", "C#4": "cis'", "D4": "d'", "Eb4": "ees'", "D#4": "dis'", "E4": "e'",
    "F4": "f'", "Gb4": "ges'", "F#4": "fis'", "G4": "g'", "Ab4": "aes'", "G#4": "gis'", "A4": "a'",
    "Bb4": "bes'", "A#4": "ais'", "B4": "b'",
    "C5": "c''", "Db5": "des''", "C#5": "cis''", "D5": "d''", "Eb5": "ees''", "D#5": "dis''", "E5": "e''",
    "F5": "f''", "Gb5": "ges''", "F#5": "fis''", "G5": "g''", "Ab5": "aes''", "G#5": "gis''", "A5": "a''",
    "Bb5": "bes''", "A#5": "ais''", "B5": "b''",
    "C6": "c'''", "Db6": "des'''", "C#6": "cis'''", "D6": "d'''", "Eb6": "ees'''", "D#6": "dis'''", "E6": "e'''",
    "F6": "f'''", "Gb6": "ges'''", "F#6": "fis'''", "G6": "g'''", "Ab6": "aes'''", "G#6": "gis'''", "A6": "a'''",
    "Bb6": "bes'''", "A#6": "ais'''", "B6": "b'''"
}

# Transposition table (semitones from C)
KEYS = {
    "C": 0, "G": 7, "D": 2, "A": 9, "E": 4, "B": 11,
    "F#": 6, "Db": 1, "Ab": 8, "Eb": 3, "Bb": 10, "F": 5
}

# Pitch class mapping
PITCH_CLASSES_SHARP = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
                       6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}
PITCH_CLASSES_FLAT = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
                      6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"}

# Keys that prefer flats
FLAT_KEYS = {"Db", "Ab", "Eb", "Bb", "F", "C"}

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
    }
}