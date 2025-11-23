import pygame
from ui import get_mode_selection, get_key_selection, get_phrase_type
from phrase_generator_ui import run_phrase_generator
from score_generator import cleanup_files

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Musical Staff Generator")
    temp_files = ["score.ly", "score.png", "score_partial.ly", "score_partial.png"]

    while True:
        mode = get_mode_selection(screen)
        if mode is None:
            break
        selected_key = None
        if mode == "random":
            while True:
                phrase_type = get_phrase_type(screen, mode)
                if phrase_type is None:
                    break
                if phrase_type == "back_to_mode":
                    break
                continue_loop, next_screen = run_phrase_generator(screen, phrase_type, temp_files)
                if not continue_loop:
                    break
                if next_screen:  # Back to phrase type selection
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
                    continue_loop, next_screen = run_phrase_generator(screen, phrase_type, temp_files, key=selected_key)
                    if not continue_loop:
                        break
                    if next_screen:  # Back to phrase type selection
                        continue
                if phrase_type is None or not continue_loop:
                    break

    pygame.quit()
    cleanup_files(temp_files)
    print("Program closed.")

if __name__ == "__main__":
    main()