# main.py
import pygame
from data import CELLS, MAJOR_CELLS, MAJOR_RESOLUTION_CELLS, KEYS, KEY_CHORD_MAP
from music_utils import Cycler, note_to_pitch
from phrase_generator import generate_phrase
from score_generator import generate_score_png, generate_partial_score_png, cleanup_files

def draw_button(screen, text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)

def get_phrase_type(screen):
    font = pygame.font.Font(None, 48)
    title = font.render("Choose Phrase Type", True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_7sus4 = pygame.Rect(250, 200, 200, 50)
    button_major = pygame.Rect(550, 200, 200, 50)
    button_short_25 = pygame.Rect(250, 300, 200, 50)
    button_long_25 = pygame.Rect(550, 300, 200, 50)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "7sus4", 250, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Major", 550, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Short 25 Major", 250, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Long 25 Major", 550, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_7sus4.collidepoint(event.pos):
                    return "7sus4"
                elif button_major.collidepoint(event.pos):
                    return "major"
                elif button_short_25.collidepoint(event.pos):
                    return "short_25_major"
                elif button_long_25.collidepoint(event.pos):
                    return "long_25_major"

def run_phrase_generator(screen, phrase_type, temp_files):
    clock = pygame.time.Clock()
    
    # Font for displaying key
    font = pygame.font.Font(None, 36)

    # Initialize cyclers based on phrase type
    cell_set = MAJOR_CELLS if phrase_type == "major" else CELLS
    resolution_cycler = Cycler(MAJOR_RESOLUTION_CELLS) if phrase_type in ["short_25_major", "long_25_major"] else None
    left_cycler = Cycler(cell_set)
    right_cycler = Cycler(MAJOR_RESOLUTION_CELLS if phrase_type == "short_25_major" else cell_set)
    key_cycler = Cycler(list(KEYS.keys()))

    # Define expected phrase lengths
    expected_lengths = {
        "7sus4": 9,  # 5 (left) + 4 (right) - 1 (overlap)
        "major": 9,  # 5 (left) + 4 (right) - 1 (overlap)
        "short_25_major": 9,  # 5 (left) + 4 (resolution) - 1 (overlap)
        "long_25_major": 17  # 5 (resolution) + 4 + 4 + 4 (three preceding cells) - 3 (overlaps)
    }

    # Define pitch range (F3 to E5)
    F3_PITCH = 5 + (3 * 12)  # F3 = 5 semitones + 36 (3 octaves) = 41
    E5_PITCH = 4 + (5 * 12)  # E5 = 4 semitones + 60 (5 octaves) = 64

    def is_phrase_in_range(phrase):
        for note in phrase:
            pitch_class, octave = note_to_pitch(note)
            absolute_pitch = pitch_class + (octave * 12)
            if absolute_pitch < F3_PITCH or absolute_pitch > E5_PITCH:
                return False
        return True

    # Initial phrase generation with length and pitch range validation
    key = key_cycler.next_item()  # Get initial key
    while True:
        transposed_phrase, generated_key, phrase_length = generate_phrase(left_cycler, right_cycler if phrase_type != "long_25_major" else resolution_cycler, Cycler([key]), phrase_type)
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
        # Debugging: Print original dimensions and aspect ratio
        aspect_ratio = orig_width / orig_height
        print(f"Original dimensions: width={orig_width}, height={orig_height}, aspect_ratio={aspect_ratio}")
        # Scale to fit the screen width
        target_width = 1000  # Fit the screen width
        target_height = int(target_width / aspect_ratio)  # Height based on aspect ratio
        max_height = 560  # Maximum height before cropping
        if target_height > max_height:
            target_height = max_height
            target_width = int(target_height * aspect_ratio)
        # Scale the images
        image_partial = pygame.transform.scale(image_partial, (target_width, target_height))
        image_full = pygame.transform.scale(image_full, (target_width, target_height))
        # Crop the bottom portion to remove the LilyPond footer
        crop_factor = 0.85
        crop_height = int(target_height * crop_factor)
        image_partial = image_partial.subsurface((0, 0, target_width, crop_height))
        image_full = image_full.subsurface((0, 0, target_width, crop_height))
        new_height = crop_height  # Update new_height after cropping
        new_width = target_width
        # Center the staff vertically and horizontally
        y_offset = (600 - new_height - 50) // 2 if (600 - new_height - 50) > 0 else 0
        x_offset = (1000 - new_width) // 2  # Center horizontally
        print(f"Staff: new_width={new_width}, new_height={new_height}, x_offset={x_offset}, y_offset={y_offset}")
        # Render initial key text using chord mapping
        chord_map_key = phrase_type if phrase_type in KEY_CHORD_MAP else "major"
        key_text = font.render(KEY_CHORD_MAP[chord_map_key][key], True, (0, 0, 0))  # Black text
        key_y_position = y_offset + new_height + 30  # Position below the staff
        key_rect = key_text.get_rect(center=(1000 // 2, key_y_position))
        print(f"Key text y-position: {key_y_position}")
    except Exception as e:
        print(f"Error initializing score: {e}")
        cleanup_files(temp_files)
        return False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                cleanup_files(temp_files)
                return True  # Return to selection screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_partial:
                    # Switch to full phrase on first click
                    show_partial = False
                else:
                    # Generate new phrase and show partial on second click
                    cleanup_files(temp_files)
                    key = key_cycler.next_item()  # Advance key only when generating a new valid phrase
                    while True:
                        transposed_phrase, generated_key, phrase_length = generate_phrase(left_cycler, right_cycler if phrase_type != "long_25_major" else resolution_cycler, Cycler([key]), phrase_type)
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
                        # Debugging: Print original dimensions and aspect ratio
                        aspect_ratio = orig_width / orig_height
                        print(f"Original dimensions: width={orig_width}, height={orig_height}, aspect_ratio={aspect_ratio}")
                        # Scale to fit the screen width
                        target_width = 1000  # Fit the screen width
                        target_height = int(target_width / aspect_ratio)  # Height based on aspect ratio
                        max_height = 560  # Maximum height before cropping
                        if target_height > max_height:
                            target_height = max_height
                            target_width = int(target_height * aspect_ratio)
                        # Scale the images
                        image_partial = pygame.transform.scale(image_partial, (target_width, target_height))
                        image_full = pygame.transform.scale(image_full, (target_width, target_height))
                        # Crop the bottom portion to remove the LilyPond footer
                        crop_factor = 0.85
                        crop_height = int(target_height * crop_factor)
                        image_partial = image_partial.subsurface((0, 0, target_width, crop_height))
                        image_full = image_full.subsurface((0, 0, target_width, crop_height))
                        new_height = crop_height  # Update new_height after cropping
                        new_width = target_width
                        # Center the staff vertically and horizontally
                        y_offset = (600 - new_height - 50) // 2 if (600 - new_height - 50) > 0 else 0
                        x_offset = (1000 - new_width) // 2  # Center horizontally
                        print(f"Staff: new_width={new_width}, new_height={new_height}, x_offset={x_offset}, y_offset={y_offset}")
                        chord_map_key = phrase_type if phrase_type in KEY_CHORD_MAP else "major"
                        key_text = font.render(KEY_CHORD_MAP[chord_map_key][key], True, (0, 0, 0))  # Update key text
                        key_y_position = y_offset + new_height + 30  # Position below the staff
                        key_rect = key_text.get_rect(center=(1000 // 2, key_y_position))
                        print(f"Key text y-position: {key_y_position}")
                        show_partial = True
                        print(f"Key: {KEY_CHORD_MAP[chord_map_key][key]}, Phrase: {' '.join(transposed_phrase)}")
                    except Exception as e:
                        print(f"Error generating new score: {e}")

        screen.fill((255, 255, 255))
        # Display either partial or full phrase based on state
        if show_partial:
            screen.blit(image_partial, (x_offset, y_offset))
        else:
            screen.blit(image_full, (x_offset, y_offset))
        # Display key text below the staff
        screen.blit(key_text, key_rect)
        pygame.display.flip()
        clock.tick(60)
    
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Musical Staff Generator")
    temp_files = ["score.ly", "score.png", "score_partial.ly", "score_partial.png"]

    while True:
        phrase_type = get_phrase_type(screen)
        if phrase_type is None:
            break
        if not run_phrase_generator(screen, phrase_type, temp_files):
            break

    pygame.quit()
    cleanup_files(temp_files)
    print("Program closed.")

if __name__ == "__main__":
    main()