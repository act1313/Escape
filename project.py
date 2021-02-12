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
RECYCLING_BIN = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bin.PNG')), (40, 70))
SINK = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sink.png')), (50, 75))
LIVES_FONT = pygame.font.SysFont("comicsans", 25)
RIDDLE_FONT = pygame.font.SysFont("comicsans", 27)


# the main game loop for all of the events
def main():

    binArea = pygame.Rect(WIDTH - RECYCLING_BIN.get_width(), HEIGHT - RECYCLING_BIN.get_height(), 40, 70)
    sinkArea = pygame.Rect(640, 220, 50, 75)
    lightoneArea = pygame.Rect(375, 100, 190, 35)
    lighttwoArea = pygame.Rect(665, 105, 115, 35)
    lightthreeArea = pygame.Rect(475, 295, 375, 35)

    def draw_items():
        # render the images to display
        WIN.blit(RECYCLING_BIN, (WIDTH - RECYCLING_BIN.get_width(), HEIGHT - RECYCLING_BIN.get_height()))
        WIN.blit(SINK, (640, 220))


    def window():
        WIN.blit(BACKGROUND, (0, 0))
        # Rendering the font into displayable text
        riddle_text = RIDDLE_FONT.render("Click the things that are wrong and that don't help global warming.", 1, BLACK)
        lives_text = LIVES_FONT.render(f"Items left: {items}", 1, BLACK)

        # Making the text show on the screen
        WIN.blit(riddle_text, (WIDTH // 2 - riddle_text.get_width() // 2, 10))
        WIN.blit(lives_text, (WIDTH - 125, 10))

        draw_items()

        # showing the images on the screen
        pygame.display.update()


    run = True
    items = 5

    bin_clicked = True
    sink_clicked = True
    light_one_clicked = True
    light_two_clicked = True
    light_three_clicked = True

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        window()
        # looping through a list of the different events
        for event in pygame.event.get():
            # the game is able to close when we hit the close button
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if binArea.collidepoint(event.pos) and bin_clicked == True:
                        bin_clicked = False
                        items -= 1
                        print("bin")

                    if sinkArea.collidepoint(event.pos) and sink_clicked == True:
                        sink_clicked = False
                        items -= 1
                        print("sink")

                    if lightoneArea.collidepoint(event.pos) and light_one_clicked == True:
                        light_one_clicked = False
                        items -= 1
                        print("light one")

                    if lighttwoArea.collidepoint(event.pos) and light_two_clicked == True:
                        light_two_clicked = False
                        items -= 1
                        print("light two")

                    if lightthreeArea.collidepoint(event.pos) and light_three_clicked == True:
                        light_three_clicked = False
                        items -= 1
                        print("light three")

    pygame.quit()


# makes sure it will open the main loop first
if __name__ == "__main__":
    main()
