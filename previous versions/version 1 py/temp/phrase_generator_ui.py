import pygame
from data import CELLS, MAJOR_CELLS, MAJOR_RESOLUTION_CELLS, KEYS, KEY_CHORD_MAP, minor_B_cells, minor_C_cells, minor_C_cells_down2, turnaround_cells_1, DFB, CELLS_up5, CELLS_up2, CELLS_down5
from music_utils import Cycler, note_to_pitch
from phrase_generator import generate_phrase
from score_generator import generate_score_png, generate_partial_score_png, cleanup_files
from constants import KEYS

def get_dominant_or_relative_major_key(phrase_type, tonic_key):
    """Map the tonic key to the dominant (for major 25) or relative major (for minor 25), or use tonic key directly."""
    if tonic_key not in KEYS:
        raise KeyError(f"Invalid tonic key: {tonic_key}")
    key_semitones = KEYS[tonic_key]
    if phrase_type in ["short_25_major", "long_25_major"]:  # Dominant for major 25
        dominant_semitones = (key_semitones + 7) % 12
        for key, semitones in KEYS.items():
            if semitones == dominant_semitones:
                return key
    elif phrase_type in ["short_25_minor", "long_25_minor"]:  # Relative major for minor 25
        relative_major_semitones = (key_semitones + 3) % 12
        for key, semitones in KEYS.items():
            if semitones == relative_major_semitones:
                return key
    return tonic_key  # Use tonic key directly for turnaround and other types

def draw_button(screen, text, x, y, width, height, color, text_color):
    """Draw a button and return its rectangle"""
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)

def draw_return_arrow(screen):
    """Draw a return arrow button in the bottom-right corner"""
    x, y = 950, 550  # Bottom-right corner
    width, height = 40, 40
    color = (200, 200, 200)  # Light gray
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.line(screen, (0, 0, 0), (x + 30, y + 10), (x + 10, y + 20), 2)  # Left diagonal
    pygame.draw.line(screen, (0, 0, 0), (x + 10, y + 20), (x + 30, y + 30), 2)  # Right diagonal
    pygame.draw.line(screen, (0, 0, 0), (x + 30, y + 10), (x + 30, y + 30), 2)  # Vertical line
    return pygame.Rect(x, y, width, height)

def draw_footer_text(screen):
    """Draw footer text on every page"""
    font = pygame.font.Font(None, 24)  # Smaller font size
    text1 = font.render("Made by tsy", True, (0, 0, 0))
    text2 = font.render("Contact: tungsyauy@gmail.com", True, (0, 0, 0))
    screen.blit(text1, (10, 550))  # Position at bottom-left
    screen.blit(text2, (10, 570))

def run_phrase_generator(screen, phrase_type, temp_files, key=None):
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
    else:
        cell_set = MAJOR_CELLS if phrase_type == "major" else CELLS
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
    else:
        resolution_cycler = None

    # Initialize key cycler
    key_cycler = Cycler(list(KEYS.keys()))

    # Set expected phrase lengths
    expected_lengths = {
        "7sus4": 9,
        "major": 9,
        "short_25_major": 9,
        "long_25_major": 17,
        "short_25_minor": 9,
        "long_25_minor": 17,
        "turnaround": 17,
        "rhythm_changes_56": 17,
        "ii7_to_v7": 17
    }

    # Define pitch range (F3 to E5)
    F3_PITCH = 5 + (2 * 12)  # F3 = 5 semitones + 24 (2 octaves) = 29
    E5_PITCH = 4 + (6 * 12)  # E5 = 4 semitones + 72 (6 octaves) = 76

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
        effective_key = get_dominant_or_relative_major_key(phrase_type, selected_key)
        key_cycler = Cycler([effective_key])
    key = key_cycler.next_item()
    while True:
        transposed_phrase, generated_key, phrase_length = generate_phrase(
            left_cycler, 
            right_cycler if phrase_type not in ["long_25_major", "long_25_minor", "turnaround", "rhythm_changes_56", "ii7_to_v7"] else resolution_cycler, 
            Cycler([key]), 
            phrase_type
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
                display_text = f"in the key of {selected_key}"
            elif phrase_type in ["short_25_minor", "long_25_minor"]:
                display_text = f"in the key of {selected_key}m"
            elif phrase_type == "turnaround":
                display_text = f"in the key of {selected_key}"
            else:
                display_text = KEY_CHORD_MAP[chord_map_key][selected_key]
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

    # Define toggle button
    toggle_button = pygame.Rect(400, key_y_position + 50, 200, 50)  # Centered below key text
    toggle_text = "Show Full Phrase"

    running = True
    while running:
        screen.fill((255, 255, 255))
        if show_partial:
            screen.blit(image_partial, (x_offset, y_offset))
        else:
            screen.blit(image_full, (x_offset, y_offset))
        screen.blit(key_text, key_rect)
        draw_footer_text(screen)  # Add footer text
        draw_button(screen, toggle_text, toggle_button.x, toggle_button.y, toggle_button.width, toggle_button.height, (200, 200, 200), (0, 0, 0))
        return_button = draw_return_arrow(screen)  # Draw return button
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
                        key = key_cycler.next_item()
                        while True:
                            transposed_phrase, generated_key, phrase_length = generate_phrase(
                                left_cycler, 
                                right_cycler if phrase_type not in ["long_25_major", "long_25_minor", "turnaround", "rhythm_changes_56", "ii7_to_v7"] else resolution_cycler, 
                                Cycler([key]), 
                                phrase_type
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
                                    display_text = f"in the key of {selected_key}"
                                elif phrase_type in ["short_25_minor", "long_25_minor"]:
                                    display_text = f"in the key of {selected_key}m"
                                elif phrase_type == "turnaround":
                                    display_text = f"in the key of {selected_key}"
                                else:
                                    display_text = KEY_CHORD_MAP[chord_map_key][selected_key]
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