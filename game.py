# Game Imports
import pygame
import input
import dialogue
import subprocess
from player import Player 
from npc import Npc
from sprite import sprites

# LLM Imports
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

pygame.init()

# Setup
pygame.display.set_caption("NPC PLYGRND")
screen = pygame.display.set_mode((600, 600))
running = True

player = Player("images/player.png", 285, 250)
npc1 = Npc("images/npc_male1.png", 140, 130)
npc1_hitbox = pygame.Rect(npc1.x, npc1.y, 32, 64)

# Dialogue State
show_dialogue = False
dialogue_text = ""

# Dialogue Typing
base_font = pygame.font.Font(None,24)
user_Text = ''

# Color Booleans for Game Mechanics
red = False
blue = False
green = False
yellow = False

# Dialogue Box Code
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

# OLLAMA LLM CODE
template = """

Here is the conversation history: {context}

Question: {question}

"""
with open("npc1.txt", "r", encoding="utf-8") as file:
    originalText = file.read()
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Game Loop
while running:

    with open("npc1.txt", "r", encoding="utf-8") as file:
        gameContext = file.read()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # For Movement
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
            if show_dialogue:                

                if event.key == pygame.K_ESCAPE:
                    show_dialogue = False
                    user_Text = ''
                else:
                    if event.key == pygame.K_BACKSPACE:
                        user_Text = user_Text[:-1]
                    elif event.key == pygame.K_RETURN:
                        print("You: ", user_Text)
                        result = chain.invoke({"context": gameContext, "question": user_Text})
                        print("Bot: ", result)
                        gameContext += f"\nUser: {user_Text}\nAI: {result}"
                    else:
                        user_Text += event.unicode
                    
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if npc1_hitbox.collidepoint(event.pos):
                print("NPC Clicked!")
                show_dialogue = True
                try:
                    # Run dialogue.py and capture output
                    dialogue_text = subprocess.check_output(["python", "dialogue.py"], text=True).strip()
                except Exception as e:
                    dialogue_text = "Error loading dialogue!"

    # Update Code
    player.update()

    # Draw Code
    screen.fill((0, 0, 0))  # Clear screen

    # Draw quadrants
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 300, 300))    # Red (Top Left)
    pygame.draw.rect(screen, (0, 0, 255), (300, 0, 300, 300))  # Blue (Top Right)
    pygame.draw.rect(screen, (0, 255, 0), (0, 300, 300, 300))  # Green (Bottom Left)
    pygame.draw.rect(screen, (255, 255, 0), (300, 300, 300, 300))  # Yellow (Bottom Right)



    if player.inRed():
        if red is False:
            # Open NPC1 Character Text File for writing(Lebron James)
            with open("npc1.txt", "a") as file:
                file.write("\nI scored 2 points")
            red = True
            yellow = False
            blue = False
            green = False
        
    if player.inBlue():
        if blue is False:
            with open("npc1.txt", "a") as file:
                file.write("\nYou scored 2 points")
            blue = True
            red = False
            yellow = False
            green = False

    if player.inGreen():
        if green is False:
            with open("npc1.txt", "a") as file:
                file.write("\nI scored 3 points")
            green = True
            red = False
            blue = False
            yellow = False

    if player.inYellow():
        if yellow is False:
            with open("npc1.txt", "a") as file:
                file.write("\nYou Scored 3 Points")            
            yellow = True
            red = False
            blue = False
            green = False
    
    # Draw sprites
    for s in sprites:
        s.draw(screen)
    
        # Draw Dialogue Box if active
    if show_dialogue:        
        draw_dialogue_box(screen, dialogue_text)

    text_surface = base_font.render(user_Text,True,(255,255,255))
    screen.blit(text_surface, (10,560)) 

    pygame.display.flip()
    pygame.time.delay(17)

pygame.quit()
with open("npc1.txt", "w") as profile:
    profile.write(originalText)


