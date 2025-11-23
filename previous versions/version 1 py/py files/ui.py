# ui.py
import pygame

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

def get_welcome_screen(screen):
    """Display welcome screen with 'Enter' and 'Exit' buttons"""
    font = pygame.font.Font(None, 60)  # Larger font for title
    title = font.render("Bebop Practice Program", True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_enter = pygame.Rect(400, 300, 200, 50)
    button_exit = pygame.Rect(400, 400, 200, 50)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "Enter", 400, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Exit", 400, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_enter.collidepoint(event.pos):
                    return "proceed"
                elif button_exit.collidepoint(event.pos):
                    return None

def get_mode_selection(screen):
    """Display screen to choose between Random and Designate modes"""
    font = pygame.font.Font(None, 48)
    title = font.render("Choose Mode", True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_random = pygame.Rect(400, 300, 200, 50)
    button_designate = pygame.Rect(400, 400, 200, 50)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "Random", 400, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Designate", 400, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)
        return_button = draw_return_arrow(screen)  # Draw return arrow and get its rect
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_random.collidepoint(event.pos):
                    return "random"
                elif button_designate.collidepoint(event.pos):
                    return "designate"
                elif return_button.collidepoint(event.pos):
                    return "back_to_welcome"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return "back_to_welcome"

def get_key_selection(screen):
    """Display key selection screen with 12 key buttons"""
    font = pygame.font.Font(None, 48)
    title = font.render("Choose Key", True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    key_buttons = {}
    keys = ["C", "F", "Bb", "Eb", "Ab", "Db", "F#", "B", "E", "A", "D", "G"]
    for i, key in enumerate(keys):
        x = 200 + (i % 3) * 200
        y = 200 + (i // 3) * 100
        key_buttons[key] = pygame.Rect(x, y, 150, 50)
    
    return_button = draw_return_arrow(screen)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        for key, rect in key_buttons.items():
            draw_button(screen, key, rect.x, rect.y, rect.width, rect.height, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)
        draw_return_arrow(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return "back_to_mode"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for key, rect in key_buttons.items():
                    if rect.collidepoint(event.pos):
                        return key
                if return_button.collidepoint(event.pos):
                    return "back_to_mode"

def get_phrase_type(screen, mode, selected_key=None):
    font = pygame.font.Font(None, 48)
    title_text = f"Key of {selected_key}: Choose Phrase Type" if selected_key else "Choose Phrase Type"
    title = font.render(title_text, True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_7sus4 = pygame.Rect(250, 200, 200, 50)
    button_major = pygame.Rect(550, 200, 200, 50)
    button_major_25 = pygame.Rect(250, 300, 200, 50)
    button_minor_25 = pygame.Rect(550, 300, 200, 50)
    button_turnaround = pygame.Rect(250, 400, 200, 50)
    button_rhythm_changes_56 = pygame.Rect(550, 400, 200, 50)
    button_ii7_to_v7 = pygame.Rect(400, 500, 200, 50)
    return_button = draw_return_arrow(screen)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "7sus4", 250, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Major", 550, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Major 25", 250, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Minor 25", 550, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Turnaround", 250, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Rhythm Changes 5-6", 550, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "II7 to V7", 400, 500, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)
        draw_return_arrow(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return "back_to_key" if mode == "designate" else "back_to_mode"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_7sus4.collidepoint(event.pos):
                    return "7sus4_select"
                elif button_major.collidepoint(event.pos):
                    return "major_select"
                elif button_major_25.collidepoint(event.pos):
                    return "major_25_select"
                elif button_minor_25.collidepoint(event.pos):
                    return "minor_25_select"
                elif button_turnaround.collidepoint(event.pos):
                    return "turnaround"
                elif button_rhythm_changes_56.collidepoint(event.pos):
                    return "rhythm_changes_56"
                elif button_ii7_to_v7.collidepoint(event.pos):
                    return "ii7_to_v7"
                elif return_button.collidepoint(event.pos):
                    return "back_to_key" if mode == "designate" else "back_to_mode"

def get_length_selection(screen, phrase_category, mode, selected_key=None):
    """Display length selection screen for Major, Major 25, or Minor 25"""
    font = pygame.font.Font(None, 48)
    title_text = f"Key of {selected_key}: {phrase_category}" if selected_key else f"Choose {phrase_category} Length"
    title = font.render(title_text, True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_short = pygame.Rect(400, 300, 200, 50)
    button_long = pygame.Rect(400, 400, 200, 50)
    return_button = draw_return_arrow(screen)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "Short", 400, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Long", 400, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)
        draw_return_arrow(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return "back_to_phrase_type"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_short.collidepoint(event.pos):
                    if phrase_category == "Major 25":
                        return "short_25_major"
                    elif phrase_category == "Minor 25":
                        return "short_25_minor"
                    elif phrase_category == "Major":
                        return "major"
                    elif phrase_category == "7sus4":
                        return "7sus4"
                    elif phrase_category in ["Minor", "Dominant", "ø7", "Altered", "Random"]:
                        return "7sus4"  # All 7sus4 chord types use short 7sus4 base
                elif button_long.collidepoint(event.pos):
                    if phrase_category == "Major 25":
                        return "long_25_major"
                    elif phrase_category == "Minor 25":
                        return "long_25_minor"
                    elif phrase_category == "Major":
                        return "long_major"
                    elif phrase_category == "7sus4":
                        return "long_7sus4"
                    elif phrase_category in ["Minor", "Dominant", "ø7", "Altered", "Random"]:
                        return "long_7sus4"  # All 7sus4 chord types use long 7sus4 base
                elif return_button.collidepoint(event.pos):
                    return "back_to_phrase_type"

def get_7sus4_chord_type_selection(screen, mode, selected_key=None):
    """Get the chord type selection for 7sus4 phrases"""
    font = pygame.font.Font(None, 48)
    title_text = f"Key of {selected_key}: Choose 7sus4 Chord Type" if selected_key else "Choose 7sus4 Chord Type"
    title = font.render(title_text, True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_minor = pygame.Rect(250, 200, 150, 50)
    button_dominant = pygame.Rect(425, 200, 150, 50)
    button_half_dim = pygame.Rect(600, 200, 150, 50)
    button_altered = pygame.Rect(338, 300, 150, 50)
    button_random = pygame.Rect(513, 300, 150, 50)
    return_button = draw_return_arrow(screen)
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "Minor", 250, 200, 150, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Dominant", 425, 200, 150, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "ø7", 600, 200, 150, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Altered", 338, 300, 150, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Random", 513, 300, 150, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)
        draw_return_arrow(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return "back_to_phrase_type"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_minor.collidepoint(event.pos):
                    return "7sus4_minor"
                elif button_dominant.collidepoint(event.pos):
                    return "7sus4_dominant"
                elif button_half_dim.collidepoint(event.pos):
                    return "7sus4_half_dim"
                elif button_altered.collidepoint(event.pos):
                    return "7sus4_altered"
                elif button_random.collidepoint(event.pos):
                    return "7sus4_random"
                elif return_button.collidepoint(event.pos):
                    return "back_to_phrase_type"