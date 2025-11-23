# constants.py

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

# Pitch class mapping
PITCH_CLASSES_SHARP = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
                       6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}
PITCH_CLASSES_FLAT = {0: "C", 1: "Db", 2: "D", 3: "Eb", 4: "E", 5: "F",
                      6: "Gb", 7: "G", 8: "Ab", 9: "A", 10: "Bb", 11: "B"}

# Keys that prefer flats
FLAT_KEYS = {"Db", "Ab", "Eb", "Bb", "F", "C"}

# Transposition table (semitones from C)
KEYS = {
    "C": 0, "G": 7, "D": 2, "A": 9, "E": 4, "B": 11,
    "F#": 6, "Db": 1, "Ab": 8, "Eb": 3, "Bb": 10, "F": 5
}