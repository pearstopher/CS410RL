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
    screen = pygame.display.set_mode([1000, 800])

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

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.draw.rect(screen, (200,20,20), pygame.Rect(30, 30, 60, 60), 2)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()