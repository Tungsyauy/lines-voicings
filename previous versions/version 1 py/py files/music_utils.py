import random
from constants import LILYPOND_PITCHES, PITCH_CLASSES_SHARP, PITCH_CLASSES_FLAT, FLAT_KEYS, KEYS

def note_to_pitch(note):
    pitch_classes = {"C": 0, "Db": 1, "C#": 1, "D": 2, "Eb": 3, "D#": 3, "E": 4,
                     "F": 5, "Gb": 6, "F#": 6, "G": 7, "Ab": 8, "G#": 8, "A": 9,
                     "Bb": 10, "A#": 10, "B": 11}
    name, octave = note[:-1], int(note[-1])
    return pitch_classes[name], octave

def transpose_note(note, semitones, key):
    pitch_class, octave = note_to_pitch(note)
    new_pitch = (pitch_class + semitones) % 12
    new_octave = octave + ((pitch_class + semitones) // 12)
    pitch_classes = PITCH_CLASSES_SHARP if key not in FLAT_KEYS else PITCH_CLASSES_FLAT
    pitch_name = pitch_classes[new_pitch]
    if key in ["F#", "B", "E", "A", "D", "G"]:
        if pitch_name in ["Db", "Eb", "Gb", "Ab", "Bb"]:
            pitch_name = {1: "C#", 3: "D#", 6: "F#", 8: "G#", 10: "A#"}.get(new_pitch, pitch_name)
    return f"{pitch_name}{new_octave}"

def adjust_right_cell(left_cell, right_cell):
    left_end_pitch, left_end_octave = note_to_pitch(left_cell[-1])
    right_start_pitch, right_start_octave = note_to_pitch(right_cell[0])
    
    # Calculate octave shift based on the last note of the left cell and the first note of the right cell
    if left_end_pitch == right_start_pitch:
        octave_shift = left_end_octave - right_start_octave
    else:
        # If pitch classes differ, adjust based on the expected melodic step (e.g., +1 octave if ascending)
        pitch_diff = (right_start_pitch - left_end_pitch) % 12
        if pitch_diff > 6:  # Large interval, likely an octave + step
            octave_shift = left_end_octave + 1 - right_start_octave
        else:
            octave_shift = left_end_octave - right_start_octave
    
    adjusted_right = []
    for note in right_cell:
        pitch_class, octave = note_to_pitch(note)
        new_octave = octave + octave_shift
        for key in LILYPOND_PITCHES:
            if note_to_pitch(key) == (pitch_class, new_octave):
                adjusted_right.append(key)
                break
    return adjusted_right


class Cycler:
    def __init__(self, items):
        self.original_items = items
        self.permutation = []
        self.index = 0
        self.reset_permutation()

    def reset_permutation(self):
        self.permutation = list(range(len(self.original_items)))
        random.shuffle(self.permutation)
        self.index = 0

    def next_item(self):
        if self.index >= len(self.permutation):
            self.reset_permutation()
        item = self.original_items[self.permutation[self.index]]
        self.index += 1
        return item