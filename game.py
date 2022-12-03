# Christopher Juncker
# CS410RL
# game.py
#
# basic shell of a pygame program
# will modify to show some basic elements of the 'game'
#
# https://realpython.com/pygame-a-primer/

# Simple pygame program

# Import and initialize the pygame library
import pygame
import math

def game(environment, lock):

    pygame.init()
    clock = pygame.time.Clock()

    # name the window
    pygame.display.set_caption('Gathering Simulator')

    # Set up the drawing window
    screen = pygame.display.set_mode([1600, 800])

    # display division:
    # 0-399 = info/buttons/tbd
    # 400-1199 = map display
    # 1200-1599 = minimap
    #
    # left, top, width, height
    info = (0, 0, 400, 800)
    map = (400, 0, 800, 800)
    mini = (1200, 0, 400, 800)

    font = pygame.font.Font('freesansbold.ttf', 16)

    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(30)  # maximum frames per second

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with (mostly) darkness
        screen.fill((20,20,20))



        # INFO SECTION
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(info), 2)

        lock.acquire()
        state = environment.state()
        lock.release()
        # what is a loop? i keep hearing about them
        text0 = font.render(str(state[0]), True, (0, 255, 0), (0, 0, 255))
        text1 = font.render(str(state[1]), True, (0, 255, 0), (0, 0, 255))
        text2 = font.render(str(state[2]), True, (0, 255, 0), (0, 0, 255))
        text0_rect = pygame.Rect(10,10,400,40)
        text1_rect = pygame.Rect(10,60,400,40)
        text2_rect = pygame.Rect(10,110,400,40)
        screen.blit(text0, text0_rect)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)


        # MAP SECTION
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(map), 2)

        lock.acquire()
        # convert map dimensions to game dimensions (800x800
        x_factor = 800 / environment.x
        y_factor = 800 / environment.y

        # plot node location
        # subtract 800 from y-coordinate because y-coordinates are reversed (0 on top not bottom)
        pygame.draw.circle(screen, (0, 255, 0), (400 + environment.node[0] * x_factor,
                                                 800 - environment.node[1] * y_factor), 5)


        # plot agent location
        pygame.draw.circle(screen, (255, 0, 0), (400 + environment.agent[0] * x_factor,
                                                 800 - environment.agent[1] * y_factor), 5)
        lock.release()




        # MINIMAP SECTION
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(mini), 2)

        # circle: surface, color, center, radius, width
        center_y = mini[2]//2  # circle center location (y) based on width of section
        center_x = mini[0] + center_y  # circle center (x) is starting point plus half width
        radius = center_y - 10  # give a few pixels of extra room around the circle
        pygame.draw.circle(screen, (0, 0, 255), (center_x, center_y), radius)

        pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), 7)

        # convert the proximity to a position on the minimap
        if state[2] == 0:
            proximity = radius
        else:
            proximity = radius * state[2]  # state[2] proximity is already normalized to range 0,1

        # calculate node location relative to center of circle
        rel_x = proximity * math.cos(math.radians(state[1]))
        rel_y = proximity * math.sin(math.radians(state[1]))
        # and draw a little circle for the node
        # subtract rel_y because again coordinates are reversed in the visual system
        pygame.draw.circle(screen, (0, 255, 0), (center_x + rel_x, center_y - rel_y), 7)


        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
