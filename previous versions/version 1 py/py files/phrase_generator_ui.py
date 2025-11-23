import pygame
from data import CELLS, CELLS2, MAJOR_CELLS, MAJOR_RESOLUTION_CELLS, KEYS, KEY_CHORD_MAP, minor_B_cells, minor_C_cells, minor_C_cells_down2, turnaround_cells_1, DFB, CELLS_up5, CELLS_up2, CELLS_down5, find_7sus4_generation_key, find_7sus4_target_key_for_display, get_7sus4_chord_display
from random_cycler import random_7sus4_cycler
from music_utils import Cycler, note_to_pitch
from phrase_generator import generate_phrase
from score_generator import generate_score_png, generate_partial_score_png, cleanup_files
from constants import KEYS

def get_dominant_or_relative_major_key(phrase_type, tonic_key):
    """Map the tonic key to the dominant (for major 25) or relative major (for minor 25), or use tonic key directly."""
    if tonic_key not in KEYS:
        raise KeyError(f"Invalid tonic key: {tonic_key}")
    key_semitones = KEYS[tonic_key]
    if phrase_type in ["short_25_major", "long_25_major"]:
        dominant_semitones = (key_semitones + 7) % 12
        for key, semitones in KEYS.items():
            if semitones == dominant_semitones:
                return key
    elif phrase_type in ["short_25_minor", "long_25_minor"]:
        relative_major_semitones = (key_semitones + 3) % 12
        for key, semitones in KEYS.items():
            if semitones == relative_major_semitones:
                return key
    return tonic_key

def get_major_25_chord_progression(key):
    """Return the chord progression for Major 25 in the given key"""
    # Special cases with exact accidentals
    if key == "E":
        return "F#m B7 E"
    elif key == "Gb" or key == "F#":
        return "G#m C#7 F#"
    elif key == "B":
        return "C#m F#7 B"
    
    # For other keys, the progression is ii-V-I
    # Find the ii chord (minor)
    key_semitones = KEYS[key]
    ii_semitones = (key_semitones + 2) % 12
    ii_key = None
    for k, semitones in KEYS.items():
        if semitones == ii_semitones:
            ii_key = k
            break
    
    # Find the V chord (dominant)
    v_semitones = (key_semitones + 7) % 12
    v_key = None
    for k, semitones in KEYS.items():
        if semitones == v_semitones:
            v_key = k
            break
    
    if ii_key and v_key:
        return f"{ii_key}m {v_key}7 {key}"
    return f"in the key of {key}"

def get_minor_25_chord_progression(key):
    """Return the chord progression for Minor 25 in the given key"""
    # Special cases with exact accidentals
    if key == "F":
        return "Gø7 C7 Fm"
    elif key == "Ab":
        return "Bbø7 Eb7 Abm"
    elif key == "B":
        return "C#ø7 F#7 Bm"
    elif key == "F#":
        return "Abø7 Db7 Gbm"  # Use Gb instead of F# to match flat notation
    
    # For other keys, the progression is iiø7-V7-i
    # Find the ii chord (half-diminished)
    key_semitones = KEYS[key]
    ii_semitones = (key_semitones + 2) % 12
    ii_key = None
    for k, semitones in KEYS.items():
        if semitones == ii_semitones:
            ii_key = k
            break
    
    # Find the V chord (dominant)
    v_semitones = (key_semitones + 7) % 12
    v_key = None
    for k, semitones in KEYS.items():
        if semitones == v_semitones:
            v_key = k
            break
    
    if ii_key and v_key:
        return f"{ii_key}ø7 {v_key}7 {key}m"
    return f"in the key of {key}m"

def get_turnaround_chord_progression(key):
    """Return the chord progression for Turnaround in the given key"""
    # Special cases with exact accidentals
    if key == "Gb" or key == "F#":
        return "Gb Eb7 Abm Db7"
    elif key == "B":
        return "B G#7 C#m F#7"
    
    # For other keys, calculate the chord progression
    # I - VI7 - ii - V7
    key_semitones = KEYS[key]
    
    # Find the VI chord (dominant 7th)
    vi_semitones = (key_semitones + 9) % 12  # 9 semitones up from tonic
    vi_key = None
    for k, semitones in KEYS.items():
        if semitones == vi_semitones:
            vi_key = k
            break
    
    # Find the ii chord (minor)
    ii_semitones = (key_semitones + 2) % 12  # 2 semitones up from tonic
    ii_key = None
    for k, semitones in KEYS.items():
        if semitones == ii_semitones:
            ii_key = k
            break
    
    # Find the V chord (dominant 7th)
    v_semitones = (key_semitones + 7) % 12  # 7 semitones up from tonic
    v_key = None
    for k, semitones in KEYS.items():
        if semitones == v_semitones:
            v_key = k
            break
    
    if vi_key and ii_key and v_key:
        return f"{key} {vi_key}7 {ii_key}m {v_key}7"
    return f"in the key of {key}"

def get_rhythm_changes_56_chord_progression(key):
    """Return the chord progression for Rhythm Changes bars 5-6 in the given key"""
    # Special cases with exact accidentals
    if key == "Gb" or key == "F#":
        return "F#7 - B7 Cdim"
    elif key == "B":
        return "B7 - E7 Fdim"
    
    # For other keys, calculate the chord progression
    # I7 - IV7 #IVdim
    key_semitones = KEYS[key]
    
    # Find the IV chord (dominant 7th)
    iv_semitones = (key_semitones + 5) % 12  # 5 semitones up from tonic (perfect fourth)
    iv_key = None
    for k, semitones in KEYS.items():
        if semitones == iv_semitones:
            iv_key = k
            break
    
    # Find the #IV (diminished)
    sharp_iv_semitones = (key_semitones + 6) % 12  # 6 semitones up from tonic (tritone)
    sharp_iv_key = None
    for k, semitones in KEYS.items():
        if semitones == sharp_iv_semitones:
            sharp_iv_key = k
            break
    
    if iv_key and sharp_iv_key:
        return f"{key}7 - {iv_key}7 {sharp_iv_key}dim"
    return f"in the key of {key}"

def get_ii7_to_v7_chord_progression(key):
    """Return the chord progression for ii7 to V7 in the given key"""
    # Special cases with exact accidentals
    if key == "Gb" or key == "F#":
        return "Ab7 - Db7 -"
    elif key == "B":
        return "C#7 - F#7 -"
    
    # For other keys, calculate the chord progression
    # ii7 - V7
    key_semitones = KEYS[key]
    
    # Find the ii chord (dominant 7th)
    ii_semitones = (key_semitones + 2) % 12  # 2 semitones up from tonic
    ii_key = None
    for k, semitones in KEYS.items():
        if semitones == ii_semitones:
            ii_key = k
            break
    
    # Find the V chord (dominant 7th)
    v_semitones = (key_semitones + 7) % 12  # 7 semitones up from tonic
    v_key = None
    for k, semitones in KEYS.items():
        if semitones == v_semitones:
            v_key = k
            break
    
    if ii_key and v_key:
        return f"{ii_key}7 - {v_key}7 -"
    return f"in the key of {key}"

def draw_button(screen, text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    
    # Start with the default font size
    font_size = 36
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    
    # If the text is too wide for the button, reduce the font size
    while text_rect.width > width - 20 and font_size > 16:  # Keep minimum font size at 16
        font_size -= 2
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
    
    # Center the text on the button
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text_surface, text_rect)
    
    return pygame.Rect(x, y, width, height)

def draw_return_arrow(screen):
    x, y = 950, 550
    width, height = 40, 40
    color = (200, 200, 200)
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.line(screen, (0, 0, 0), (x + 30, y + 10), (x + 10, y + 20), 2)
    pygame.draw.line(screen, (0, 0, 0), (x + 10, y + 20), (x + 30, y + 30), 2)
    pygame.draw.line(screen, (0, 0, 0), (x + 30, y + 10), (x + 30, y + 30), 2)
    return pygame.Rect(x, y, width, height)

def draw_footer_text(screen):
    font = pygame.font.Font(None, 24)
    text1 = font.render("Made by tsy", True, (0, 0, 0))
    text2 = font.render("Contact: tungsyauy@gmail.com", True, (0, 0, 0))
    screen.blit(text1, (10, 550))
    screen.blit(text2, (10, 570))

def map_random_key_for_display(phrase_type, generated_key):
    """
    Map the randomly generated key to the correct key for display purposes.
    For Major 25: Display a perfect fifth lower (7 semitones lower)
    For Minor 25: Display a minor third lower (3 semitones lower)
    """
    # Handle None case
    if generated_key is None:
        return generated_key
        
    # For Major 25 patterns - display a perfect fifth lower
    if phrase_type in ["short_25_major", "long_25_major"]:
        # Calculate the key a perfect fifth lower (7 semitones)
        if generated_key in KEYS:
            key_semitones = KEYS[generated_key]
            target_semitones = (key_semitones - 7) % 12  # Perfect fifth lower
            for k, semitones in KEYS.items():
                if semitones == target_semitones:
                    return k
        return generated_key
    
    # For Minor 25 patterns - display a minor third lower
    elif phrase_type in ["short_25_minor", "long_25_minor"]:
        # For minor keys, remove the 'm' suffix if present
        base_key = generated_key
        if isinstance(generated_key, str) and generated_key.endswith('m'):
            base_key = generated_key[:-1]
        
        # Calculate the key a minor third lower (3 semitones)
        if base_key in KEYS:
            key_semitones = KEYS[base_key]
            target_semitones = (key_semitones - 3) % 12  # Minor third lower
            for k, semitones in KEYS.items():
                if semitones == target_semitones:
                    return k
        return base_key
    
    return generated_key

def run_phrase_generator(screen, phrase_type, temp_files, key=None, use_random_cycling=False):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Initialize cyclers
    if phrase_type in ["short_25_minor", "long_25_minor"]:
        left_cycler = Cycler(minor_B_cells)
        right_cycler = Cycler(minor_C_cells)
    elif phrase_type == "turnaround":
        left_cycler = Cycler(turnaround_cells_1)
        right_cycler = Cycler(MAJOR_RESOLUTION_CELLS)
    elif phrase_type == "rhythm_changes_56":
        left_cycler = Cycler(CELLS)
        right_cycler = Cycler(DFB)
    elif phrase_type == "ii7_to_v7":
        left_cycler = Cycler(CELLS_up2)
        right_cycler = Cycler(CELLS_down5)
    elif phrase_type in ["major", "long_major"]:
        left_cycler = Cycler(MAJOR_CELLS)
        right_cycler = Cycler(MAJOR_CELLS)
    elif phrase_type in ["7sus4", "long_7sus4", "7sus4_minor", "7sus4_dominant", "7sus4_half_dim", "7sus4_altered", 
                         "long_7sus4_minor", "long_7sus4_dominant", "long_7sus4_half_dim", "long_7sus4_altered"]:
        left_cycler = Cycler(CELLS)
        right_cycler = Cycler(CELLS)
    else:
        cell_set = CELLS2 if phrase_type in ["short_25_major", "long_25_major"] else CELLS
        left_cycler = Cycler(cell_set)
        right_cycler = Cycler(MAJOR_RESOLUTION_CELLS if phrase_type in ["short_25_major", "long_25_major"] else cell_set)

    # Initialize resolution cycler
    if phrase_type == "long_25_minor":
        resolution_cycler = Cycler(minor_C_cells)
    elif phrase_type in ["short_25_major", "long_25_major", "turnaround"]:
        resolution_cycler = Cycler(MAJOR_RESOLUTION_CELLS)
    elif phrase_type == "rhythm_changes_56":
        resolution_cycler = Cycler(DFB)
    elif phrase_type == "ii7_to_v7":
        resolution_cycler = Cycler(CELLS_down5)
    elif phrase_type in ["long_major", "long_7sus4", "long_7sus4_minor", "long_7sus4_dominant", "long_7sus4_half_dim", "long_7sus4_altered"]:
        resolution_cycler = Cycler(MAJOR_CELLS if phrase_type == "long_major" else CELLS)
    else:
        resolution_cycler = None

    # Initialize key cycler
    key_cycler = Cycler(list(KEYS.keys()))

    # Set expected phrase lengths
    expected_lengths = {
        "7sus4": 9,
        "7sus4_minor": 9,
        "7sus4_dominant": 9,
        "7sus4_half_dim": 9,
        "7sus4_altered": 9,
        "major": 9,
        "short_25_major": 9,
        "long_25_major": 17,
        "short_25_minor": 9,
        "long_25_minor": 17,
        "turnaround": 17,
        "rhythm_changes_56": 17,
        "ii7_to_v7": 17,
        "long_major": 17,
        "long_7sus4": 17,
        "long_7sus4_minor": 17,
        "long_7sus4_dominant": 17,
        "long_7sus4_half_dim": 17,
        "long_7sus4_altered": 17
    }

    # Define pitch range (F3 to E5)
    F3_PITCH = 5 + (2 * 12)
    E5_PITCH = 4 + (6 * 12)

    def is_phrase_in_range(phrase):
        for note in phrase:
            pitch_class, octave = note_to_pitch(note)
            absolute_pitch = pitch_class + (octave * 12)
            if absolute_pitch < F3_PITCH or absolute_pitch > E5_PITCH:
                return False
        return True

    # Initial phrase generation
    selected_key = key
    if selected_key:
        # For chord-specific 7sus4 phrases, find the correct generation key
        if phrase_type.startswith("7sus4_") or phrase_type.startswith("long_7sus4_"):
            # Extract chord type from phrase type
            if phrase_type.startswith("long_7sus4_"):
                chord_type = phrase_type.replace("long_7sus4_", "")
            else:
                chord_type = phrase_type.replace("7sus4_", "")
            effective_key = find_7sus4_generation_key(selected_key, chord_type)
        else:
            effective_key = get_dominant_or_relative_major_key(phrase_type, selected_key)
        key_cycler = Cycler([effective_key])
    key = key_cycler.next_item()
    while True:
        # Map new chord-specific phrase types to base types for generation
        base_phrase_type = phrase_type
        if phrase_type.startswith("7sus4_"):
            base_phrase_type = "7sus4"
        elif phrase_type.startswith("long_7sus4_"):
            base_phrase_type = "long_7sus4"
        
        transposed_phrase, generated_key, phrase_length = generate_phrase(
            left_cycler, 
            right_cycler if base_phrase_type not in ["long_25_major", "long_25_minor", "turnaround", "rhythm_changes_56", "ii7_to_v7", "long_major", "long_7sus4"] else resolution_cycler, 
            Cycler([key]), 
            base_phrase_type
        )
        if (phrase_length == expected_lengths[phrase_type] and 
            is_phrase_in_range(transposed_phrase)):
            break
        print(f"Generated phrase length {phrase_length} (expected {expected_lengths[phrase_type]}), "
              f"pitch range {'valid' if is_phrase_in_range(transposed_phrase) else 'out of F3-E5 range'}, regenerating with key {key}...")

    show_partial = True
    try:
        score_image_partial = generate_partial_score_png(transposed_phrase, phrase_length)
        score_image_full = generate_score_png(transposed_phrase)
        image_partial = pygame.image.load(score_image_partial)
        image_full = pygame.image.load(score_image_full)
        orig_width, orig_height = image_full.get_size()
        aspect_ratio = orig_width / orig_height
        target_width = 1000
        target_height = int(target_width / aspect_ratio)
        max_height = 560
        if target_height > max_height:
            target_height = max_height
            target_width = int(target_height * aspect_ratio)
        image_partial = pygame.transform.scale(image_partial, (target_width, target_height))
        image_full = pygame.transform.scale(image_full, (target_width, target_height))
        crop_factor = 0.85
        crop_height = int(target_height * crop_factor)
        image_partial = image_partial.subsurface((0, 0, target_width, crop_height))
        image_full = image_full.subsurface((0, 0, target_width, crop_height))
        new_height = crop_height
        new_width = target_width
        y_offset = (600 - new_height - 50) // 2 if (600 - new_height - 50) > 0 else 0
        x_offset = (1000 - new_width) // 2
        chord_map_key = phrase_type if phrase_type in KEY_CHORD_MAP else "major"
        if selected_key:
            if phrase_type in ["short_25_major", "long_25_major"]:
                display_text = get_major_25_chord_progression(selected_key)
            elif phrase_type in ["short_25_minor", "long_25_minor"]:
                display_text = get_minor_25_chord_progression(selected_key)
            elif phrase_type == "turnaround":
                display_text = get_turnaround_chord_progression(selected_key)
            elif phrase_type == "rhythm_changes_56":
                display_text = get_rhythm_changes_56_chord_progression(selected_key)
            elif phrase_type == "ii7_to_v7":
                display_text = get_ii7_to_v7_chord_progression(selected_key)
            elif phrase_type in ["long_major", "major"]:
                display_text = f"in the key of {selected_key}"
            elif phrase_type in ["long_7sus4", "7sus4"]:
                display_text = KEY_CHORD_MAP["7sus4"][selected_key]
            elif phrase_type in ["7sus4_minor", "long_7sus4_minor"]:
                display_text = KEY_CHORD_MAP["7sus4_minor"][selected_key]
            elif phrase_type in ["7sus4_dominant", "long_7sus4_dominant"]:
                display_text = KEY_CHORD_MAP["7sus4_dominant"][selected_key]
            elif phrase_type in ["7sus4_half_dim", "long_7sus4_half_dim"]:
                display_text = KEY_CHORD_MAP["7sus4_half_dim"][selected_key]
            elif phrase_type in ["7sus4_altered", "long_7sus4_altered"]:
                display_text = KEY_CHORD_MAP["7sus4_altered"][selected_key]
            else:
                display_text = KEY_CHORD_MAP[chord_map_key][selected_key]
        else:
            # For random mode, use the correct chord progressions with mapping
            if phrase_type in ["7sus4", "long_7sus4"]:
                display_text = KEY_CHORD_MAP["7sus4"][generated_key]
            elif phrase_type in ["7sus4_minor", "long_7sus4_minor"]:
                target_key = find_7sus4_target_key_for_display(generated_key, "minor")
                display_text = get_7sus4_chord_display(target_key, "minor")
            elif phrase_type in ["7sus4_dominant", "long_7sus4_dominant"]:
                target_key = find_7sus4_target_key_for_display(generated_key, "dominant")
                display_text = get_7sus4_chord_display(target_key, "dominant")
            elif phrase_type in ["7sus4_half_dim", "long_7sus4_half_dim"]:
                target_key = find_7sus4_target_key_for_display(generated_key, "half_dim")
                display_text = get_7sus4_chord_display(target_key, "half_dim")
            elif phrase_type in ["7sus4_altered", "long_7sus4_altered"]:
                target_key = find_7sus4_target_key_for_display(generated_key, "altered")
                display_text = get_7sus4_chord_display(target_key, "altered")
            elif phrase_type in ["short_25_major", "long_25_major"]:
                # Map the generated key to the correct display key
                display_key = map_random_key_for_display(phrase_type, generated_key)
                display_text = get_major_25_chord_progression(display_key)
            elif phrase_type in ["short_25_minor", "long_25_minor"]:
                # Map the generated key to the correct display key
                display_key = map_random_key_for_display(phrase_type, generated_key)
                display_text = get_minor_25_chord_progression(display_key)
            elif phrase_type == "turnaround":
                display_text = get_turnaround_chord_progression(generated_key)
            elif phrase_type == "rhythm_changes_56":
                display_text = get_rhythm_changes_56_chord_progression(generated_key)
            elif phrase_type == "ii7_to_v7":
                display_text = get_ii7_to_v7_chord_progression(generated_key)
            else:
                display_text = KEY_CHORD_MAP[chord_map_key][generated_key]
        key_text = font.render(display_text, True, (0, 0, 0))
        key_y_position = y_offset + new_height + 30
        key_rect = key_text.get_rect(center=(1000 // 2, key_y_position))
        print(f"Key text y-position: {key_y_position}")
        print(f"Generated phrase: {' '.join(transposed_phrase)}, Display key: {display_text}, Selected key: {selected_key}, Generated key: {generated_key}")
    except Exception as e:
        print(f"Error initializing score: {e}")
        cleanup_files(temp_files)
        return False, None

    toggle_button = pygame.Rect(400, key_y_position + 50, 200, 50)
    toggle_text = "Show Full Phrase"

    running = True
    while running:
        screen.fill((255, 255, 255))
        if show_partial:
            screen.blit(image_partial, (x_offset, y_offset))
        else:
            screen.blit(image_full, (x_offset, y_offset))
        screen.blit(key_text, key_rect)
        draw_footer_text(screen)
        draw_button(screen, toggle_text, toggle_button.x, toggle_button.y, toggle_button.width, toggle_button.height, (200, 200, 200), (0, 0, 0))
        return_button = draw_return_arrow(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                cleanup_files(temp_files)
                return False, None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                cleanup_files(temp_files)
                return True, phrase_type
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    cleanup_files(temp_files)
                    return True, phrase_type
                if toggle_button.collidepoint(event.pos):
                    if show_partial:
                        show_partial = False
                        toggle_text = "Generate Next Phrase"
                    else:
                        cleanup_files(temp_files)
                        # Handle random cycling for 7sus4 phrases
                        if use_random_cycling and (phrase_type.startswith("7sus4_") or phrase_type.startswith("long_7sus4_")):
                            # Get next random chord type and update phrase_type
                            current_chord_type = random_7sus4_cycler.get_next_chord_type()
                            if phrase_type.startswith("long_7sus4_"):
                                phrase_type = "long_" + current_chord_type
                            else:
                                phrase_type = current_chord_type
                        
                        # For chord-specific 7sus4 phrases, find the correct generation key
                        if selected_key and (phrase_type.startswith("7sus4_") or phrase_type.startswith("long_7sus4_")):
                            # Extract chord type from phrase type
                            if phrase_type.startswith("long_7sus4_"):
                                chord_type = phrase_type.replace("long_7sus4_", "")
                            else:
                                chord_type = phrase_type.replace("7sus4_", "")
                            effective_key = find_7sus4_generation_key(selected_key, chord_type)
                            key = effective_key
                        else:
                            key = key_cycler.next_item()
                        while True:
                            # Map new chord-specific phrase types to base types for generation
                            base_phrase_type = phrase_type
                            if phrase_type.startswith("7sus4_"):
                                base_phrase_type = "7sus4"
                            elif phrase_type.startswith("long_7sus4_"):
                                base_phrase_type = "long_7sus4"
                            
                            transposed_phrase, generated_key, phrase_length = generate_phrase(
                                left_cycler, 
                                right_cycler if base_phrase_type not in ["long_25_major", "long_25_minor", "turnaround", "rhythm_changes_56", "ii7_to_v7", "long_major", "long_7sus4"] else resolution_cycler, 
                                Cycler([key]), 
                                base_phrase_type
                            )
                            if (phrase_length == expected_lengths[phrase_type] and 
                                is_phrase_in_range(transposed_phrase)):
                                break
                            print(f"Generated phrase length {phrase_length} (expected {expected_lengths[phrase_type]}), "
                                  f"pitch range {'valid' if is_phrase_in_range(transposed_phrase) else 'out of F3-E5 range'}, regenerating with key {key}...")
                        try:
                            score_image_partial = generate_partial_score_png(transposed_phrase, phrase_length)
                            score_image_full = generate_score_png(transposed_phrase)
                            image_partial = pygame.image.load(score_image_partial)
                            image_full = pygame.image.load(score_image_full)
                            orig_width, orig_height = image_full.get_size()
                            aspect_ratio = orig_width / orig_height
                            target_width = 1000
                            target_height = int(target_width / aspect_ratio)
                            max_height = 560
                            if target_height > max_height:
                                target_height = max_height
                                target_width = int(target_height * aspect_ratio)
                            image_partial = pygame.transform.scale(image_partial, (target_width, target_height))
                            image_full = pygame.transform.scale(image_full, (target_width, target_height))
                            crop_factor = 0.85
                            crop_height = int(target_height * crop_factor)
                            image_partial = image_partial.subsurface((0, 0, target_width, crop_height))
                            image_full = image_full.subsurface((0, 0, target_width, crop_height))
                            new_height = crop_height
                            new_width = target_width
                            y_offset = (600 - new_height - 50) // 2 if (600 - new_height - 50) > 0 else 0
                            x_offset = (1000 - new_width) // 2
                            chord_map_key = phrase_type if phrase_type in KEY_CHORD_MAP else "major"
                            if selected_key:
                                if phrase_type in ["short_25_major", "long_25_major"]:
                                    display_text = get_major_25_chord_progression(selected_key)
                                elif phrase_type in ["short_25_minor", "long_25_minor"]:
                                    display_text = get_minor_25_chord_progression(selected_key)
                                elif phrase_type == "turnaround":
                                    display_text = get_turnaround_chord_progression(selected_key)
                                elif phrase_type == "rhythm_changes_56":
                                    display_text = get_rhythm_changes_56_chord_progression(selected_key)
                                elif phrase_type == "ii7_to_v7":
                                    display_text = get_ii7_to_v7_chord_progression(selected_key)
                                elif phrase_type in ["long_major", "major"]:
                                    display_text = f"in the key of {selected_key}"
                                elif phrase_type in ["long_7sus4", "7sus4"]:
                                    display_text = KEY_CHORD_MAP["7sus4"][selected_key]
                                elif phrase_type in ["7sus4_minor", "long_7sus4_minor"]:
                                    display_text = KEY_CHORD_MAP["7sus4_minor"][selected_key]
                                elif phrase_type in ["7sus4_dominant", "long_7sus4_dominant"]:
                                    display_text = KEY_CHORD_MAP["7sus4_dominant"][selected_key]
                                elif phrase_type in ["7sus4_half_dim", "long_7sus4_half_dim"]:
                                    display_text = KEY_CHORD_MAP["7sus4_half_dim"][selected_key]
                                elif phrase_type in ["7sus4_altered", "long_7sus4_altered"]:
                                    display_text = KEY_CHORD_MAP["7sus4_altered"][selected_key]
                                else:
                                    display_text = KEY_CHORD_MAP[chord_map_key][selected_key]
                            else:
                                # For random mode, use the correct chord progressions with mapping
                                if phrase_type in ["7sus4", "long_7sus4"]:
                                    display_text = KEY_CHORD_MAP["7sus4"][generated_key]
                                elif phrase_type in ["7sus4_minor", "long_7sus4_minor"]:
                                    target_key = find_7sus4_target_key_for_display(generated_key, "minor")
                                    display_text = get_7sus4_chord_display(target_key, "minor")
                                elif phrase_type in ["7sus4_dominant", "long_7sus4_dominant"]:
                                    target_key = find_7sus4_target_key_for_display(generated_key, "dominant")
                                    display_text = get_7sus4_chord_display(target_key, "dominant")
                                elif phrase_type in ["7sus4_half_dim", "long_7sus4_half_dim"]:
                                    target_key = find_7sus4_target_key_for_display(generated_key, "half_dim")
                                    display_text = get_7sus4_chord_display(target_key, "half_dim")
                                elif phrase_type in ["7sus4_altered", "long_7sus4_altered"]:
                                    target_key = find_7sus4_target_key_for_display(generated_key, "altered")
                                    display_text = get_7sus4_chord_display(target_key, "altered")
                                elif phrase_type in ["short_25_major", "long_25_major"]:
                                    # Map the generated key to the correct display key
                                    display_key = map_random_key_for_display(phrase_type, generated_key)
                                    display_text = get_major_25_chord_progression(display_key)
                                elif phrase_type in ["short_25_minor", "long_25_minor"]:
                                    # Map the generated key to the correct display key
                                    display_key = map_random_key_for_display(phrase_type, generated_key)
                                    display_text = get_minor_25_chord_progression(display_key)
                                elif phrase_type == "turnaround":
                                    display_text = get_turnaround_chord_progression(generated_key)
                                elif phrase_type == "rhythm_changes_56":
                                    display_text = get_rhythm_changes_56_chord_progression(generated_key)
                                elif phrase_type == "ii7_to_v7":
                                    display_text = get_ii7_to_v7_chord_progression(generated_key)
                                else:
                                    display_text = KEY_CHORD_MAP[chord_map_key][generated_key]
                            key_text = font.render(display_text, True, (0, 0, 0))
                            key_y_position = y_offset + new_height + 30
                            key_rect = key_text.get_rect(center=(1000 // 2, key_y_position))
                            print(f"Key text y-position: {key_y_position}")
                            print(f"Generated phrase: {' '.join(transposed_phrase)}, Display key: {display_text}, Selected key: {selected_key}, Generated key: {generated_key}")
                            show_partial = True
                            toggle_text = "Show Full Phrase"
                        except Exception as e:
                            print(f"Error generating new score: {e}")

        clock.tick(60)
    
    return False, None