# from kivy.app import App
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):
#         return Label(text="Hello Android!")

# MyApp().run()

import pygame
import sys

# Standard initialization
pygame.init()

# 1. DYNAMIC RESOLUTION: Use (0,0) and FULLSCREEN to get the phone's actual resolution
# This prevents stretching or aspect ratio issues.
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Hello Android")

# 2. SAFE FONT LOADING: Default fonts (None) can sometimes fail on specific Android builds.
# We render the text once to use in the loop.
try:
    font = pygame.font.SysFont("sans-serif", 64)
except:
    font = pygame.font.Font(None, 64)

text = font.render("Hello Android!", True, (255, 255, 255))
text_rect = text.get_rect(center=(info.current_w // 2, info.current_h // 2))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 3. TOUCH INPUT: Android touch events map to FINGERDOWN
        if event.type == pygame.FINGERDOWN:
            print("Screen touched!")

    screen.fill((20, 20, 40))  # A nice dark blue
    screen.blit(text, text_rect)
    pygame.display.flip()
    
    clock.tick(60)
