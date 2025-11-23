import random
from data import CELLS, MAJOR_CELLS, MAJOR_RESOLUTION_CELLS, KEYS, CELLS2, LILYPOND_PITCHES
from music_utils import Cycler, adjust_right_cell, transpose_note, note_to_pitch

def validate_resolution_cell(phrase, phrase_type):
    """Ensure resolution cell matches database, preserving original pitch classes and octaves."""
    if phrase_type in ["short_25_major", "long_25_major"]:
        resolution_cell = phrase[-5:]
        resolution_cell_str = " ".join(resolution_cell)
        
        for cell in MAJOR_RESOLUTION_CELLS:
            cell_str = " ".join(cell)
            if resolution_cell_str == cell_str:
                return phrase
        
        resolution_pitch_classes = [note[:-1] for note in resolution_cell]
        for cell in MAJOR_RESOLUTION_CELLS:
            cell_pitch_classes = [note[:-1] for note in cell]
            if cell_pitch_classes == resolution_pitch_classes:
                adjusted_cell = []
                ref_octave = note_to_pitch(resolution_cell[0])[1]
                for i, note in enumerate(cell):
                    pitch_class, octave = note_to_pitch(note)
                    new_octave = ref_octave + (note_to_pitch(cell[i])[1] - note_to_pitch(cell[0])[1])
                    for key in LILYPOND_PITCHES:
                        if note_to_pitch(key) == (pitch_class, new_octave):
                            adjusted_cell.append(key)
                            break
                phrase = phrase[:-5] + adjusted_cell
                return phrase
    
    return phrase

def generate_phrase(left_cycler, right_cycler, key_cycler, phrase_type="7sus4"):
    if phrase_type == "7sus4":
        cell_set = CELLS
        left_cell = left_cycler.next_item()
        last_note_left = left_cell[-1][:-1]
        compatible_right = [cell for cell in cell_set if cell[0][:-1] == last_note_left]
        
        if compatible_right:
            right_cell = right_cycler.next_item()
            while right_cell[0][:-1] != last_note_left:
                right_cell = right_cycler.next_item()
        else:
            right_cell = right_cycler.next_item()
        
        adjusted_right = adjust_right_cell(left_cell, right_cell)
        phrase = left_cell + adjusted_right[1:]
        phrase_length = len(phrase)
        key_name = key_cycler.next_item()

    elif phrase_type == "major":
        cell_set = MAJOR_CELLS
        left_cell = left_cycler.next_item()
        last_note_left = left_cell[-1][:-1]
        compatible_right = [cell for cell in cell_set if cell[0][:-1] == last_note_left]
        
        if compatible_right:
            right_cell = right_cycler.next_item()
            while right_cell[0][:-1] != last_note_left:
                right_cell = right_cycler.next_item()
        else:
            right_cell = right_cycler.next_item()
        
        adjusted_right = adjust_right_cell(left_cell, right_cell)
        phrase = left_cell + adjusted_right[1:]
        phrase_length = len(phrase)
        key_name = key_cycler.next_item()

    elif phrase_type == "short_25_major":
        right_cell = right_cycler.next_item() #resolution cell
        first_note_right = right_cell[0][:-1]
        compatible_left = [cell for cell in CELLS2 if cell[-1][:-1] == first_note_right]
        
        if compatible_left:
            left_cell = left_cycler.next_item()
            attempts = 0
            while left_cell[-1][:-1] != first_note_right and attempts < len(CELLS2):
                left_cell = left_cycler.next_item()
                attempts += 1
            if attempts >= len(CELLS2):
                left_cell = compatible_left[0]
        
        adjusted_right = adjust_right_cell(left_cell, right_cell) # adjust the resolution cell
        phrase = left_cell + adjusted_right[1:] # phrase = leftcell + adjusted resolution cell
        phrase_length = len(phrase)
        key_name = key_cycler.next_item()

    elif phrase_type == "long_25_major":
        resolution_cell = right_cycler.next_item()  # Right hand cell (resolution)
        phrase = resolution_cell
        cell_sets = [CELLS2, CELLS, CELLS]
        
        for cell_set in cell_sets:
            first_note_current = phrase[0][:-1]
            compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
            
            if compatible_cells:
                left_cell = Cycler(compatible_cells).next_item()
            
            adjusted_new_cell = adjust_right_cell(left_cell, phrase)  
            phrase = left_cell[:-1] + adjusted_new_cell  # Prepend left_cell and append adjusted remainder
        
        phrase_length = len(phrase)
        key_name = key_cycler.next_item()
        
    """
    # Transpose to keep within readable range (C3 to C6)
    min_octave = 3  # C3
    max_octave = 6  # C6
    octaves = [int(note[-1]) for note in phrase]
    lowest_octave = min(octaves)
    highest_octave = max(octaves)
    
    while lowest_octave < min_octave or highest_octave > max_octave:
        if lowest_octave < min_octave:
            phrase = [f"{note[:-1]}{int(note[-1]) + 1}" for note in phrase]  # Transpose up
        elif highest_octave > max_octave:
            phrase = [f"{note[:-1]}{int(note[-1]) - 1}" for note in phrase]  # Transpose down
        octaves = [int(note[-1]) for note in phrase]
        lowest_octave = min(octaves)
        highest_octave = max(octaves)
    """
    
    
    key_semitones = KEYS[key_name]
    transposed_phrase = [transpose_note(note, key_semitones, key_name) for note in phrase]

    return transposed_phrase, key_name, phrase_length