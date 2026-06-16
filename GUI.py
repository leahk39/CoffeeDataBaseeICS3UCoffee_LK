import pygame
import database

connection = database.connect()
database.create_tables(connection)

# initializing pygame
pygame.init()

# screen
screen = pygame.display.set_mode((600, 600))

# background image
background = pygame.image.load('background.png')

# title and icon
pygame.display.set_caption("Coffee Shop Database")
icon = pygame.image.load('coffeeIcon.png')
pygame.display.set_icon(icon)


# game loop
running = True
while running:

    # RGB - red, green, blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    # Draw white rectangle
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 400, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()