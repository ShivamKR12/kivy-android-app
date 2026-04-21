# from kivy.app import App
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):
#         return Label(text="Hello Android!")

# MyApp().run()

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Hello Android")

font = pygame.font.Font(None, 60)
text = font.render("Hello Android!", True, (255, 255, 255))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, (100, 200))
    pygame.display.flip()
    clock.tick(60)
