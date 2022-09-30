# basic shell of a pygame program
# will modify to show some basic elements of the 'game'
#
# https://realpython.com/pygame-a-primer/

# Simple pygame program

# Import and initialize the pygame library
import pygame

def game(environment):

    pygame.init()

    # name the window
    pygame.display.set_caption('Gathering Simulator')

    # Set up the drawing window
    screen = pygame.display.set_mode([1600, 800])
    # 0-399 = info/buttons/tbd
    # 400-1199 = map display
    # 1200-1599 = minimap

    # left, top, width, height
    info = (0, 0, 400, 800)
    map = (400, 0, 800, 800)
    mini = (1200, 0, 400, 800)

    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render(str(environment.state()), True, (0,255,0), (0,0,255))
    textRect = text.get_rect()
    textRect.center = (400 // 2, 200 // 2)

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with (mostly) darkness
        screen.fill((20,20,20))

        # try and show the text
        text = font.render(str(environment.state()), True, (0, 255, 0), (0, 0, 255))
        screen.blit(text, textRect)


        # info section
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(info), 2)


        # map section
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(map), 2)


        # minimap section
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(mini), 2)

        # circle: surface, color, center, radius, width
        center_y = mini[2]//2  # circle center location (y) based on width of section
        center_x = mini[0] + center_y  # circle center (x) is starting point plus half width
        pygame.draw.circle(screen, (0, 0, 255), (center_x, center_y), center_y - 10)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()