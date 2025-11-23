# ui.py
import pygame

def draw_button(screen, text, x, y, width, height, color, text_color):
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
    # Draw a simple left arrow using lines
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

def get_mode_selection(screen):
    """Display initial screen to choose between Random and Designate modes"""
    font = pygame.font.Font(None, 48)
    title = font.render("Choose Mode", True, (0, 0, 0))
    title_rect = title.get_rect(center=(500, 100))
    
    button_random = pygame.Rect(250, 300, 200, 50)
    button_designate = pygame.Rect(550, 300, 200, 50)
    return_button = draw_return_arrow(screen)  # Return button
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "Random", 250, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Designate", 550, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)  # Add footer text
        draw_return_arrow(screen)  # Redraw return button to ensure visibility
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
                    return None  # Return to exit program (no previous page)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return None  # Same as return button

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
    
    return_button = draw_return_arrow(screen)  # Return button
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        for key, rect in key_buttons.items():
            draw_button(screen, key, rect.x, rect.y, rect.width, rect.height, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)  # Add footer text
        draw_return_arrow(screen)  # Redraw return button
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
    
    button_7sus4 = pygame.Rect(100, 200, 200, 50)
    button_major = pygame.Rect(400, 200, 200, 50)
    button_short_25_major = pygame.Rect(700, 200, 200, 50)
    button_long_25_major = pygame.Rect(100, 300, 200, 50)
    button_short_25_minor = pygame.Rect(400, 300, 200, 50)
    button_long_25_minor = pygame.Rect(700, 300, 200, 50)
    button_turnaround = pygame.Rect(100, 400, 200, 50)
    button_rhythm_changes_56 = pygame.Rect(400, 400, 200, 50)
    button_ii7_to_v7 = pygame.Rect(700, 400, 200, 50)
    return_button = draw_return_arrow(screen)  # Return button
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        draw_button(screen, "7sus4", 100, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Major", 400, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Short 25 Major", 700, 200, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Long 25 Major", 100, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Short 25 Minor", 400, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Long 25 Minor", 700, 300, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Turnaround", 100, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "Rhythm Changes 5-6", 400, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_button(screen, "II7 to V7", 700, 400, 200, 50, (200, 200, 200), (0, 0, 0))
        draw_footer_text(screen)  # Add footer text
        draw_return_arrow(screen)  # Redraw return button
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return "back_to_key" if mode == "designate" else "back_to_mode"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_7sus4.collidepoint(event.pos):
                    return "7sus4"
                elif button_major.collidepoint(event.pos):
                    return "major"
                elif button_short_25_major.collidepoint(event.pos):
                    return "short_25_major"
                elif button_long_25_major.collidepoint(event.pos):
                    return "long_25_major"
                elif button_short_25_minor.collidepoint(event.pos):
                    return "short_25_minor"
                elif button_long_25_minor.collidepoint(event.pos):
                    return "long_25_minor"
                elif button_turnaround.collidepoint(event.pos):
                    return "turnaround"
                elif button_rhythm_changes_56.collidepoint(event.pos):
                    return "rhythm_changes_56"
                elif button_ii7_to_v7.collidepoint(event.pos):
                    return "ii7_to_v7"
                elif return_button.collidepoint(event.pos):
                    return "back_to_key" if mode == "designate" else "back_to_mode"