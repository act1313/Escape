# import all of the packages it will need
import pygame
import os

pygame.font.init()

# all of the constants for the project
WIDTH, HEIGHT = 900, 500
FPS = 60
WHITE = (255, 255, 255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Library.jpg')), (WIDTH, HEIGHT))
LIVES_FONT = pygame.font.SysFont("comicsans", 25)
RIDDLE_FONT = pygame.font.SysFont("comicsans", 20)


def draw_window(lives):
    WIN.blit(BACKGROUND, (0, 0))
    # Rendering the font into displayable text
    riddle_text = RIDDLE_FONT.render("This is where the riddle will go so okay hello, chicken nuggets ", 1, WHITE)
    lives_text = LIVES_FONT.render(f"Lives: {lives}", 1, WHITE)
    # Making the text show on the screen
    WIN.blit(riddle_text, (WIDTH // 2 - riddle_text.get_width() // 2, 10))
    WIN.blit(lives_text, (WIDTH - 100, 10))

    pygame.display.update()


# the main game loop for all of the events
def main():
    run = True
    thelives = 3
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        # looping through a list of the different events
        for event in pygame.event.get():
            # the game is able to close when we hit the close button
            if event.type == pygame.QUIT:
                run = False

        draw_window(thelives)

    pygame.quit()


# makes sure it will open the main loop first
if __name__ == "__main__":
    main()
