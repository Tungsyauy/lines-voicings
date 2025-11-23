import random
from data import CELLS, MAJOR_CELLS, MAJOR_RESOLUTION_CELLS, CELLS2, minor_B_cells, minor_C_cells, CELLSM5, minor_C_cells_down2, turnaround_cells_1, DFB, CELLS_up5, CELLS_up2, CELLS_down5
from constants import LILYPOND_PITCHES, KEYS
from music_utils import Cycler, adjust_right_cell, transpose_note, note_to_pitch

def get_dominant_or_relative_major_key(phrase_type, selected_key):
    """Map a selected key to the effective key for phrase generation."""
    # For minor progressions, map to relative major
    minor_to_relative_major = {
        "A": "C",  # A minor -> C major
        "D": "F#",
        "G": "B",
        "C": "E",
        "F": "A",
        "Bb": "D",
        "Eb": "G",
        "Ab": "C",
        "Db": "F#",
        "F#": "A",
        "B": "D",
        "E": "G"
    }
    
    if phrase_type in ["short_25_minor", "long_25_minor"]:
        return minor_to_relative_major.get(selected_key, selected_key)
    # For other phrase types, return the selected key as is
    return selected_key

def generate_phrase(left_cycler, right_cycler, key_cycler, phrase_type):
    """Generate a musical phrase (placeholder implementation)."""
    # This is a placeholder; replace with actual phrase generation logic
    key = key_cycler.next_item()
    expected_length = {
        "major": 8,
        "7sus4": 8,
        "short_25_major": 8,
        "short_25_minor": 8,
        "turnaround": 8,
        "rhythm_changes_56": 8,
        "ii7_to_v7": 8,
        "long_major": 16,
        "long_7sus4": 16,
        "long_25_major": 16,
        "long_25_minor": 16
    }
    phrase_length = expected_length.get(phrase_type, 8)
    # Generate a dummy phrase within pitch range F3 (53) to E5 (76)
    phrase = [str(pitch) for pitch in range(53, 53 + phrase_length)]
    return phrase, key, phrase_length


def validate_resolution_cell(phrase, phrase_type):
    """Ensure resolution cell matches database, preserving original pitch classes and octaves."""
    if phrase_type in ["short_25_major", "long_25_major", "turnaround"]:
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
    elif phrase_type in ["short_25_minor", "long_25_minor"]:
        resolution_cell = phrase[-5:]
        resolution_cell_str = " ".join(resolution_cell)
        
        for cell in minor_C_cells:
            cell_str = " ".join(cell)
            if resolution_cell_str == cell_str:
                return phrase
        
        resolution_pitch_classes = [note[:-1] for note in resolution_cell]
        for cell in minor_C_cells:
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
    elif phrase_type == "rhythm_changes_56":
        resolution_cell = phrase[-5:]
        resolution_cell_str = " ".join(resolution_cell)
        
        for cell in DFB:
            cell_str = " ".join(cell)
            if resolution_cell_str == cell_str:
                return phrase
        
        resolution_pitch_classes = [note[:-1] for note in resolution_cell]
        for cell in DFB:
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
    elif phrase_type == "ii7_to_v7":
        resolution_cell = phrase[-5:]
        resolution_cell_str = " ".join(resolution_cell)
        
        for cell in CELLS_down5:
            cell_str = " ".join(cell)
            if resolution_cell_str == cell_str:
                return phrase
        
        resolution_pitch_classes = [note[:-1] for note in resolution_cell]
        for cell in CELLS_down5:
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
    def build_long_major_phrase(key_name):
        max_attempts = 100
        attempts = 0
        
        while attempts < max_attempts:
            phrase = right_cycler.next_item()  # Start with a major cell
            cell_sets = [MAJOR_CELLS, MAJOR_CELLS, MAJOR_CELLS]  # Three additional cells
            valid_phrase = True
            
            for cell_set in cell_sets:
                first_note_current = phrase[0][:-1]
                compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
                
                if not compatible_cells:
                    valid_phrase = False
                    break
                
                left_cell = Cycler(compatible_cells).next_item()
                adjusted_new_cell = adjust_right_cell(left_cell, phrase)
                phrase = left_cell[:-1] + adjusted_new_cell
            
            if valid_phrase and len(phrase) == 17:  # Expected length: 5 + 4 + 4 + 4
                return phrase, len(phrase), key_name
            
            attempts += 1
            right_cycler.reset_permutation()
        
        raise ValueError("Failed to generate a valid long_major phrase after maximum attempts")

    def build_long_7sus4_phrase(key_name):
        max_attempts = 100
        attempts = 0
        
        while attempts < max_attempts:
            phrase = right_cycler.next_item()  # Start with a 7sus4 cell
            cell_sets = [CELLS, CELLS, CELLS]  # Three additional cells
            valid_phrase = True
            
            for cell_set in cell_sets:
                first_note_current = phrase[0][:-1]
                compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
                
                if not compatible_cells:
                    valid_phrase = False
                    break
                
                left_cell = Cycler(compatible_cells).next_item()
                adjusted_new_cell = adjust_right_cell(left_cell, phrase)
                phrase = left_cell[:-1] + adjusted_new_cell
            
            if valid_phrase and len(phrase) == 17:  # Expected length: 5 + 4 + 4 + 4
                return phrase, len(phrase), key_name
            
            attempts += 1
            right_cycler.reset_permutation()
        
        raise ValueError("Failed to generate a valid long_7sus4 phrase after maximum attempts")

    def build_ii7_to_v7_phrase(key_name):
        max_attempts = 100
        attempts = 0
        
        while attempts < max_attempts:
            resolution_cell = right_cycler.next_item()
            phrase = resolution_cell
            cell_sets = [CELLS_down5, CELLS_up2, CELLS_up2]
            valid_phrase = True
            
            for cell_set in cell_sets:
                first_note_current = phrase[0][:-1]
                compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
                
                if not compatible_cells:
                    valid_phrase = False
                    break
                
                left_cell = Cycler(compatible_cells).next_item()
                adjusted_new_cell = adjust_right_cell(left_cell, phrase)
                phrase = left_cell[:-1] + adjusted_new_cell
            
            if valid_phrase and len(phrase) == 17:
                return phrase, len(phrase), key_name
            
            attempts += 1
            right_cycler.reset_permutation()
        
        raise ValueError("Failed to generate a valid ii7_to_v7 phrase after maximum attempts")

    def build_rhythm_changes_56_phrase(key_name):
        max_attempts = 100
        attempts = 0
        
        while attempts < max_attempts:
            resolution_cell = right_cycler.next_item()
            phrase = resolution_cell
            cell_sets = [CELLS_up5, CELLS, CELLS]
            valid_phrase = True
            
            for cell_set in cell_sets:
                first_note_current = phrase[0][:-1]
                compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
                
                if not compatible_cells:
                    valid_phrase = False
                    break
                
                left_cell = Cycler(compatible_cells).next_item()
                adjusted_new_cell = adjust_right_cell(left_cell, phrase)
                phrase = left_cell[:-1] + adjusted_new_cell
            
            if valid_phrase and len(phrase) == 17:
                phrase = validate_resolution_cell(phrase, phrase_type)
                return phrase, len(phrase), key_name
            
            attempts += 1
            right_cycler.reset_permutation()
        
        raise ValueError("Failed to generate a valid rhythm_changes_56 phrase after maximum attempts")

    key_name = key_cycler.next_item()

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

    elif phrase_type == "long_major":
        phrase, phrase_length, key_name = build_long_major_phrase(key_name)

    elif phrase_type == "long_7sus4":
        phrase, phrase_length, key_name = build_long_7sus4_phrase(key_name)

    elif phrase_type == "short_25_major":
        right_cell = right_cycler.next_item()
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
        
        adjusted_right = adjust_right_cell(left_cell, right_cell)
        phrase = left_cell + adjusted_right[1:]
        phrase_length = len(phrase)

    elif phrase_type == "long_25_major":
        resolution_cell = right_cycler.next_item()
        phrase = resolution_cell
        cell_sets = [CELLS2, CELLS, CELLS]
        
        for cell_set in cell_sets:
            first_note_current = phrase[0][:-1]
            dominant_compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
            
            if dominant_compatible_cells:
                left_cell = Cycler(dominant_compatible_cells).next_item()
            else:
                return generate_phrase(left_cycler, right_cycler, key_cycler, phrase_type)
            
            adjusted_new_cell = adjust_right_cell(left_cell, phrase)
            phrase = left_cell[:-1] + adjusted_new_cell
        
        phrase_length = len(phrase)

    elif phrase_type == "short_25_minor":
        right_cell = right_cycler.next_item()
        first_note_right = right_cell[0][:-1]
        compatible_left = [cell for cell in minor_B_cells if cell[-1][:-1] == first_note_right]
        
        if compatible_left:
            left_cell = left_cycler.next_item()
            attempts = 0
            while left_cell[-1][:-1] != first_note_right and attempts < len(minor_B_cells):
                left_cell = left_cycler.next_item()
                attempts += 1
            if attempts >= len(minor_B_cells):
                left_cell = compatible_left[0]
        
        adjusted_right = adjust_right_cell(left_cell, right_cell)
        phrase = left_cell + adjusted_right[1:]
        phrase_length = len(phrase)

    elif phrase_type == "long_25_minor":
        resolution_cell = right_cycler.next_item()
        phrase = resolution_cell
        cell_sets = [minor_B_cells, CELLSM5, CELLSM5]
        
        for cell_set in cell_sets:
            first_note_current = phrase[0][:-1]
            compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
            
            if compatible_cells:
                left_cell = Cycler(compatible_cells).next_item()
            else:
                return generate_phrase(left_cycler, right_cycler, key_cycler, phrase_type)
            
            adjusted_new_cell = adjust_right_cell(left_cell, phrase)
            phrase = left_cell[:-1] + adjusted_new_cell
        
        phrase_length = len(phrase)

    elif phrase_type == "turnaround":
        max_attempts = 100
        attempts = 0
        
        while attempts < max_attempts:
            resolution_cell = right_cycler.next_item()
            phrase = resolution_cell
            cell_sets = [CELLS2, minor_C_cells_down2, turnaround_cells_1]
            valid_phrase = True
            
            for cell_set in cell_sets:
                first_note_current = phrase[0][:-1]
                compatible_cells = [cell for cell in cell_set if cell[-1][:-1] == first_note_current]
                
                if not compatible_cells:
                    valid_phrase = False
                    break
                
                left_cell = Cycler(compatible_cells).next_item()
                adjusted_new_cell = adjust_right_cell(left_cell, phrase)
                phrase = left_cell[:-1] + adjusted_new_cell
            
            if valid_phrase and len(phrase) == 17:
                phrase = validate_resolution_cell(phrase, phrase_type)
                break
            
            attempts += 1
            right_cycler.reset_permutation()

        else:
            raise ValueError("Failed to generate a valid turnaround phrase after maximum attempts")

    elif phrase_type == "rhythm_changes_56":
        phrase, phrase_length, key_name = build_rhythm_changes_56_phrase(key_name)

    elif phrase_type == "ii7_to_v7":
        phrase, phrase_length, key_name = build_ii7_to_v7_phrase(key_name)
    
    key_semitones = KEYS[key_name]
    if phrase_type == "turnaround":
        key_semitones = (key_semitones + 7) % 12
    transposed_phrase = [transpose_note(note, key_semitones, key_name) for note in phrase]
    transposed_phrase = validate_resolution_cell(transposed_phrase, phrase_type)
    print(f"Phrase type: {phrase_type}, key_name={key_name}, transposed_phrase={' '.join(transposed_phrase)}")
    return transposed_phrase, key_name, len(phrase)