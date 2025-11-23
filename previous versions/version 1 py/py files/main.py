import pygame
from ui import get_welcome_screen, get_mode_selection, get_key_selection, get_phrase_type, get_length_selection, get_7sus4_chord_type_selection
from phrase_generator_ui import run_phrase_generator
from score_generator import cleanup_files
from random_cycler import random_7sus4_cycler

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Musical Staff Generator")
    temp_files = ["score.ly", "score.png", "score_partial.ly", "score_partial.png"]

    while True:
        action = get_welcome_screen(screen)
        if action is None:
            break
        elif action == "proceed":
            while True:
                mode = get_mode_selection(screen)
                if mode is None:
                    break
                if mode == "back_to_welcome":
                    break  # Return to welcome screen
                selected_key = None
                continue_loop = True  # Initialize continue_loop
                if mode == "random":
                    while True:
                        phrase_type = get_phrase_type(screen, mode)
                        if phrase_type is None:
                            break
                        if phrase_type == "back_to_mode":
                            break
                        if phrase_type == "7sus4_select":
                            # Handle 7sus4 chord type selection first
                            while True:
                                chord_type_selection = get_7sus4_chord_type_selection(screen, mode)
                                if chord_type_selection is None:
                                    break
                                if chord_type_selection == "back_to_phrase_type":
                                    break
                                
                                # Handle random chord type selection
                                if chord_type_selection == "7sus4_random":
                                    # For random chord type, get length selection first
                                    while True:
                                        length_selection = get_length_selection(screen, "Random", mode, None)
                                        if length_selection is None:
                                            break
                                        if length_selection == "back_to_phrase_type":
                                            break
                                        # Random cycling through chord types
                                        while True:
                                            # Get a random chord type for each phrase
                                            current_chord_type = random_7sus4_cycler.get_next_chord_type()
                                            # Create composite phrase type
                                            if length_selection == "7sus4":
                                                final_phrase_type = current_chord_type
                                            elif length_selection == "long_7sus4":
                                                final_phrase_type = "long_" + current_chord_type
                                            else:
                                                final_phrase_type = length_selection
                                            continue_loop, next_screen = run_phrase_generator(screen, final_phrase_type, temp_files, use_random_cycling=True)
                                            if not continue_loop:
                                                break
                                            # If phrase generator returns True, break out of random cycling to go back to length selection
                                            if next_screen:
                                                break
                                        if not continue_loop:
                                            break
                                    if length_selection is None or not continue_loop:
                                        break
                                else:
                                    # Normal chord type selection
                                    # Then get length selection
                                    while True:
                                        # Map chord type to display name
                                        chord_type_display = {
                                            "7sus4_minor": "Minor",
                                            "7sus4_dominant": "Dominant", 
                                            "7sus4_half_dim": "ø7",
                                            "7sus4_altered": "Altered"
                                        }.get(chord_type_selection, "7sus4")
                                        length_selection = get_length_selection(screen, chord_type_display, mode, None)
                                        if length_selection is None:
                                            break
                                        if length_selection == "back_to_phrase_type":
                                            break
                                        # Create composite phrase type
                                        if length_selection == "7sus4":
                                            final_phrase_type = chord_type_selection
                                        elif length_selection == "long_7sus4":
                                            final_phrase_type = "long_" + chord_type_selection
                                        else:
                                            final_phrase_type = length_selection
                                        continue_loop, next_screen = run_phrase_generator(screen, final_phrase_type, temp_files)
                                        if not continue_loop:
                                            break
                                        # If phrase generator returns True, go back to length selection
                                        if next_screen:
                                            continue
                                    if length_selection is None or not continue_loop:
                                        break
                                    # If we broke out of length selection, go back to chord type selection
                            if chord_type_selection is None or not continue_loop:
                                break
                            # If we broke out of chord type selection, continue to next phrase type
                        elif phrase_type in ["major_25_select", "minor_25_select", "major_select"]:
                            phrase_category = {
                                "major_25_select": "Major 25",
                                "minor_25_select": "Minor 25",
                                "major_select": "Major"
                            }[phrase_type]
                            length_selection = get_length_selection(screen, phrase_category, mode, None)
                            if length_selection is None:
                                break
                            if length_selection == "back_to_phrase_type":
                                continue
                            continue_loop, next_screen = run_phrase_generator(screen, length_selection, temp_files)
                            if not continue_loop:
                                break
                            if next_screen:
                                continue
                        else:
                            continue_loop, next_screen = run_phrase_generator(screen, phrase_type, temp_files)
                            if not continue_loop:
                                break
                            if next_screen:
                                continue
                elif mode == "designate":
                    while True:
                        selected_key = get_key_selection(screen)
                        if selected_key is None:
                            break
                        if selected_key == "back_to_mode":
                            break
                        while True:
                            phrase_type = get_phrase_type(screen, mode, selected_key)
                            if phrase_type is None:
                                break
                            if phrase_type == "back_to_key":
                                break
                            if phrase_type == "7sus4_select":
                                # Handle 7sus4 chord type selection first
                                while True:
                                    chord_type_selection = get_7sus4_chord_type_selection(screen, mode, selected_key)
                                    if chord_type_selection is None:
                                        break
                                    if chord_type_selection == "back_to_phrase_type":
                                        break
                                    
                                    # Handle random chord type selection
                                    if chord_type_selection == "7sus4_random":
                                        # For random chord type, get length selection first
                                        while True:
                                            length_selection = get_length_selection(screen, "Random", mode, selected_key)
                                            if length_selection is None:
                                                break
                                            if length_selection == "back_to_phrase_type":
                                                break
                                            # Random cycling through chord types
                                            while True:
                                                # Get a random chord type for each phrase
                                                current_chord_type = random_7sus4_cycler.get_next_chord_type()
                                                # Create composite phrase type
                                                if length_selection == "7sus4":
                                                    final_phrase_type = current_chord_type
                                                elif length_selection == "long_7sus4":
                                                    final_phrase_type = "long_" + current_chord_type
                                                else:
                                                    final_phrase_type = length_selection
                                                continue_loop, next_screen = run_phrase_generator(screen, final_phrase_type, temp_files, key=selected_key, use_random_cycling=True)
                                                if not continue_loop:
                                                    break
                                                # If phrase generator returns True, break out of random cycling to go back to length selection
                                                if next_screen:
                                                    break
                                            if not continue_loop:
                                                break
                                        if length_selection is None:
                                            break
                                    else:
                                        # Normal chord type selection
                                        # Then get length selection
                                        while True:
                                            # Map chord type to display name
                                            chord_type_display = {
                                                "7sus4_minor": "Minor",
                                                "7sus4_dominant": "Dominant", 
                                                "7sus4_half_dim": "ø7",
                                                "7sus4_altered": "Altered"
                                            }.get(chord_type_selection, "7sus4")
                                            length_selection = get_length_selection(screen, chord_type_display, mode, selected_key)
                                            if length_selection is None:
                                                break
                                            if length_selection == "back_to_phrase_type":
                                                break
                                            # Create composite phrase type
                                            if length_selection == "7sus4":
                                                final_phrase_type = chord_type_selection
                                            elif length_selection == "long_7sus4":
                                                final_phrase_type = "long_" + chord_type_selection
                                            else:
                                                final_phrase_type = length_selection
                                            continue_loop, next_screen = run_phrase_generator(screen, final_phrase_type, temp_files, key=selected_key)
                                            if not continue_loop:
                                                break
                                            # If phrase generator returns True, go back to length selection
                                            if next_screen:
                                                continue
                                        if length_selection is None:
                                            break
                                        # If we broke out of length selection, go back to chord type selection
                                if chord_type_selection is None:
                                    break
                                # If we broke out of chord type selection, continue to next phrase type
                            elif phrase_type in ["major_25_select", "minor_25_select", "major_select"]:
                                phrase_category = {
                                    "major_25_select": "Major 25",
                                    "minor_25_select": "Minor 25",
                                    "major_select": "Major"
                                }[phrase_type]
                                length_selection = get_length_selection(screen, phrase_category, mode, selected_key)
                                if length_selection is None:
                                    break
                                if length_selection == "back_to_phrase_type":
                                    continue
                                continue_loop, next_screen = run_phrase_generator(screen, length_selection, temp_files, key=selected_key)
                                if not continue_loop:
                                    break
                                if next_screen:
                                    continue
                            else:
                                continue_loop, next_screen = run_phrase_generator(screen, phrase_type, temp_files, key=selected_key)
                                if not continue_loop:
                                    break
                                if next_screen:
                                    continue
                        if phrase_type is None or not continue_loop:
                            break
                if mode is None:
                    break

    pygame.quit()
    cleanup_files(temp_files)
    print("Program closed.")

if __name__ == "__main__":
    main()