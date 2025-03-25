import pygame

dialogue_box_width = 600
dialogue_box_height = 100
padding_bottom = 50
font_size = 24
inputBoxColor = pygame.Color('black')
input_rect = pygame.Rect(0,550,600,50)

def draw_dialogue_box(screen, text):
    """Draws a dialogue box at the bottom of the screen with the given text."""
    font = pygame.font.Font(None, font_size)
    box_x = (screen.get_width() - dialogue_box_width) // 2
    box_y = screen.get_height() - dialogue_box_height - padding_bottom
    box_rect = pygame.Rect(box_x, box_y, dialogue_box_width, dialogue_box_height)

    # Draw the background of the dialogue box
    pygame.draw.rect(screen, (0, 0, 0), box_rect)  # Black background
    pygame.draw.rect(screen, (255, 255, 255), box_rect, 3)  # White border

    # Draw Input text
    pygame.draw.rect(screen, inputBoxColor, input_rect)

    # Render and draw the text
    text_surface = font.render(text, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=box_rect.center)
    screen.blit(text_surface, text_rect)

    