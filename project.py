# import all of the packages it will need
import pygame
import os

pygame.font.init()

# all of the constants for the project
WIDTH, HEIGHT = 900, 500
FPS = 60
BLACK = (0, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'house.jpg')), (WIDTH, HEIGHT))
RECYCLING_BIN = pygame.image.load(os.path.join('assets', 'bin.PNG'))
LIVES_FONT = pygame.font.SysFont("comicsans", 25)
RIDDLE_FONT = pygame.font.SysFont("comicsans", 27)


def draw_window(items):
    WIN.blit(BACKGROUND, (0, 0))
    # Rendering the font into displayable text
    riddle_text = RIDDLE_FONT.render("Click the things that are wrong and that don't help global warming.", 1, BLACK)
    lives_text = LIVES_FONT.render(f"Items left: {items}", 1, BLACK)

    # Making the text show on the screen
    WIN.blit(riddle_text, (WIDTH // 2 - riddle_text.get_width() // 2, 10))
    WIN.blit(lives_text, (WIDTH - 125, 10))

    pygame.display.update()


# the main game loop for all of the events
def main():
    area = pygame.Rect(100, 150, 200, 124)
    run = True
    items = 3
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        # looping through a list of the different events
        for event in pygame.event.get():
            # the game is able to close when we hit the close button
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if area.collidepoint(event.pos):
                        print("clicked")
  
        draw_window(items)

    pygame.quit()


# makes sure it will open the main loop first
if __name__ == "__main__":
    main()
