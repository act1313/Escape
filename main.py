# import all of the packages it will need
import pygame
import os
import time

pygame.font.init()

# all of the constants for the project
WIDTH, HEIGHT = 1800, 1000
FPS = 60
BLACK = (0, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")
GREEN = (0, 255, 55)

# all of the images for the project
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'house.jpg')), (WIDTH, HEIGHT))
RECYCLING_BIN = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bin.PNG')), (80, 140))
SINK = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sink.png')), (100, 150))
WHITE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'white.jpg')), (WIDTH, HEIGHT))
PLASTIC_BOTTLE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'plastic_bottle.png')), (90, 200))
REUSABLE_BOTTLE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'reusable_bottle.png')), (64, 200))
PLASTIC_STRAW = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'straw.png')), (200, 140))
CAR = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'car.png')), (200, 100))

# The fonts for the projects
LIVES_FONT = pygame.font.SysFont("comicsans", 25)
RIDDLE_FONT = pygame.font.SysFont("comicsans", 28)
EXPLAIN_FONT = pygame.font.SysFont("comicsans", 25)


def level_one():
    # TODO reconfigure the level to be bigger and reset the hitboxes
    def draw_items():
        # render the images to display
        WIN.blit(RECYCLING_BIN, (WIDTH - RECYCLING_BIN.get_width(), HEIGHT - RECYCLING_BIN.get_height()))
        WIN.blit(SINK, (640, 220))

    def window(correct_items):
        WIN.blit(BACKGROUND, (0, 0))
        # Rendering the font into displayable text
        riddle_text = RIDDLE_FONT.render("This family left for the day. Click the things that are", True, BLACK)
        riddle_second_half_text = RIDDLE_FONT.render(" incorrect and don't help climate change.", True, BLACK)
        lives_text = LIVES_FONT.render(f"Items left: {correct_items}", True, BLACK)

        # Making the text show on the screen
        WIN.blit(riddle_text, (WIDTH // 2 - riddle_text.get_width() // 2, 10))
        WIN.blit(riddle_second_half_text, (WIDTH // 2 - riddle_second_half_text.get_width() // 2, 50))
        WIN.blit(lives_text, (WIDTH - 125, 10))

        draw_items()

        # showing the images on the screen
        pygame.display.update()

    # the hit boxes for the areas
    bin_area = pygame.Rect(WIDTH - RECYCLING_BIN.get_width(), HEIGHT - RECYCLING_BIN.get_height(), 40, 70)
    sink_area = pygame.Rect(640, 220, 50, 75)
    light_one_area = pygame.Rect(375, 100, 190, 35)
    light_two_area = pygame.Rect(665, 105, 115, 35)
    light_three_area = pygame.Rect(475, 295, 375, 35)

    run = True
    items = 5
    # whether or not the item was clicked so we won't click it again and deduct from the items variable
    bin_clicked = True
    sink_clicked = True
    light_one_clicked = True
    light_two_clicked = True
    light_three_clicked = True

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        window(items)
        # looping through a list of the different events
        for event in pygame.event.get():
            # the game is able to close when we hit the close button
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Checking to see if all of the items have been clicked and reduce the amount of corrects items
                    if bin_area.collidepoint(event.pos) and bin_clicked:
                        bin_clicked = False
                        items -= 1
                        print("bin")

                    if sink_area.collidepoint(event.pos) and sink_clicked:
                        sink_clicked = False
                        items -= 1
                        print("sink")

                    if light_one_area.collidepoint(event.pos) and light_one_clicked:
                        light_one_clicked = False
                        items -= 1
                        print("light one")

                    if light_two_area.collidepoint(event.pos) and light_two_clicked:
                        light_two_clicked = False
                        items -= 1
                        print("light two")

                    if light_three_area.collidepoint(event.pos) and light_three_clicked:
                        light_three_clicked = False
                        items -= 1
                        print("light three")

        if items <= 0:
            level_one_explain()

    pygame.quit()


def level_one_explain():
    run = True
    while run:
        WIN.blit(WHITE, (0, 0))

        # Rendering all the text on the screen
        explanation = EXPLAIN_FONT.render("Good job on passing the first test.", True, BLACK)
        explanation_1 = EXPLAIN_FONT.render(
            "You successfully identified the lights on, the running water, and the recycling.", True, BLACK)
        explanation_2 = EXPLAIN_FONT.render(
            "Turning the lights off when not in use helps reduce carbon emissions and other greenhouse gases.", True,
            BLACK)
        explanation_3 = EXPLAIN_FONT.render(
            "Turning off running water when not in use can help save water and conserve energy.", True, BLACK)
        explanation_4 = EXPLAIN_FONT.render(
            "You shouldn't put recycling in the trash because stuff like that will take long to break down,", True,
            BLACK)
        explanation_5 = EXPLAIN_FONT.render("and recycling helps to reuse unused plastic and other things.", True,
                                            BLACK)
        next_level = EXPLAIN_FONT.render("Please press enter to go the next level...", True, BLACK)

        # Actually displaying the text to the screen
        WIN.blit(explanation, (WIDTH // 2 - explanation.get_width() // 2, 75))
        WIN.blit(explanation_1, (WIDTH // 2 - explanation_1.get_width() // 2, 125))
        WIN.blit(explanation_2, (WIDTH // 2 - explanation_2.get_width() // 2, 175))
        WIN.blit(explanation_3, (WIDTH // 2 - explanation_3.get_width() // 2, 225))
        WIN.blit(explanation_4, (WIDTH // 2 - explanation_4.get_width() // 2, 275))
        WIN.blit(explanation_5, (WIDTH // 2 - explanation_5.get_width() // 2, 325))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 375))

        pygame.display.update()

        # Looping through the different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_two_question_one()

    pygame.quit()


def level_two_question_one():
    # the hit boxes for the answers
    reusable_bottle_area = pygame.Rect(620, 250, 100, 100)
    plastic_bottle_area = pygame.Rect(205, 250, 100, 100)

    def window():
        WIN.blit(WHITE, (0, 0))

        question_font = pygame.font.SysFont("comicsans", 60)
        text_font = pygame.font.SysFont("comicsans", 30)
        lives_font = pygame.font.SysFont("comicsans", 40)

        question = question_font.render("Which is better to use?", True, BLACK)
        text = text_font.render("Reusable", True, BLACK)
        text_2 = text_font.render("Plastic", True, BLACK)
        lives_text = lives_font.render(f"Lives: {level_two_question_one.lives}", True, BLACK)

        pygame.draw.circle(WIN, GREEN, (670, 300), 100)
        WIN.blit(REUSABLE_BOTTLE, (650, 275))

        pygame.draw.circle(WIN, GREEN, (255, 300), 100)
        WIN.blit(PLASTIC_BOTTLE, (225, 275))

        WIN.blit(question, (WIDTH // 2 - question.get_width() // 2, 10))
        WIN.blit(text, (715 - text.get_width(), 225))
        WIN.blit(text_2, (285 - text_2.get_width(), 225))
        WIN.blit(lives_text, (WIDTH - 125, 10))

        pygame.display.update()

    # whether or not the item was clicked so we won't click it again and deduct lives and increment level again
    bottle_clickable = True
    level_two_question_one.lives = 3
    run = True
    while run:
        window()
        # Looping through the different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # checking to see if we clicked the button
                    if reusable_bottle_area.collidepoint(event.pos) and bottle_clickable:
                        bottle_clickable = False
                        level_two_question_two()

                    if plastic_bottle_area.collidepoint(event.pos) and bottle_clickable:
                        bottle_clickable = False
                        level_two_question_one.lives -= 1
                        level_two_question_two()

    pygame.quit()


def level_two_question_two():
    plastic_straw_area = pygame.Rect(620, 250, 100, 100)
    paper_straw_area = pygame.Rect(205, 250, 100, 100)

    def window():
        WIN.blit(WHITE, (0, 0))

        question_font = pygame.font.SysFont("comicsans", 50)
        text_font = pygame.font.SysFont("comicsans", 30)
        lives_font = pygame.font.SysFont("comicsans", 40)

        question = question_font.render("Which type of straw is better to use?", True, BLACK)
        text_2 = text_font.render("Plastic", True, BLACK)
        text = text_font.render("Paper", True, BLACK)
        lives_text = lives_font.render(f"Lives: {level_two_question_one.lives}", True, BLACK)

        # drawing the straw and circle
        pygame.draw.circle(WIN, GREEN, (670, 300), 100)
        WIN.blit(PLASTIC_STRAW, (630, 275))

        pygame.draw.circle(WIN, GREEN, (255, 300), 100)
        WIN.blit(PLASTIC_STRAW, (205, 275))

        WIN.blit(question, (WIDTH // 2 - question.get_width() // 2, 10))
        WIN.blit(text, (285 - text_2.get_width(), 225))
        WIN.blit(text_2, (700 - text.get_width(), 225))
        WIN.blit(lives_text, (WIDTH - 125, 10))

        pygame.display.update()

    run = True
    straw_clickable = True
    while run:
        window()
        straw_clicked = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if plastic_straw_area.collidepoint(event.pos) and straw_clickable:
                        straw_clickable = False
                        level_two_question_one.lives -= 1
                        level_two_question_three()

                    if paper_straw_area.collidepoint(event.pos) and straw_clickable:
                        straw_clickable = False
                        level_two_question_three()

    pygame.quit()


def level_two_question_three():
    normal_car_area = pygame.Rect(620, 250, 100, 100)
    electric_car_area = pygame.Rect(205, 250, 100, 100)

    def window():
        WIN.blit(WHITE, (0, 0))

        question_font = pygame.font.SysFont("comicsans", 37)
        text_font = pygame.font.SysFont("comicsans", 27)
        lives_font = pygame.font.SysFont("comicsans", 40)

        question = question_font.render("Which type of car is better for the environment?", True, BLACK)
        text_2 = text_font.render("Electric Car", True, BLACK)
        text = text_font.render("Gas Fueled Car", True, BLACK)
        lives_text = lives_font.render(f"Lives: {level_two_question_one.lives}", True, BLACK)

        # drawing the straw and circle
        pygame.draw.circle(WIN, GREEN, (670, 300), 100)
        WIN.blit(CAR, (630, 275))

        pygame.draw.circle(WIN, GREEN, (255, 300), 100)
        WIN.blit(CAR, (205, 275))

        WIN.blit(question, (WIDTH // 2 - question.get_width() // 2, 10))
        WIN.blit(text, (290 - text_2.get_width(), 225))
        WIN.blit(text_2, (760 - text.get_width(), 225))
        WIN.blit(lives_text, (WIDTH - 125, 10))

        pygame.display.update()

    car_clickable = True
    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if normal_car_area.collidepoint(event.pos) and car_clickable:
                        car_clickable = False
                        level_two_explain()

                    if electric_car_area.collidepoint(event.pos) and car_clickable:
                        car_clickable = False
                        level_two_question_one.lives -= 1
                        if level_two_question_one.lives <= 0:
                            game_over()
                        elif level_two_question_one.lives < 0:
                            level_two_explain()

    pygame.quit()


def level_two_explain():
    run = True
    while run:
        WIN.blit(WHITE, (0, 0))

        # Rendering all the text on the screen
        explanation = EXPLAIN_FONT.render("Good job on passing the second test.", True, BLACK)
        explanation_1 = EXPLAIN_FONT.render(
            "You successfully answered which option was better for the environment", True, BLACK)
        explanation_2 = EXPLAIN_FONT.render(
            "Using a reusable water bottle over a plastic one helps reduce plastic which then leads to the ocean", True,
            BLACK)
        explanation_3 = EXPLAIN_FONT.render(
            "Using a paper straw over a plastic straw also helps reduce plastic", True, BLACK)
        explanation_4 = EXPLAIN_FONT.render(
            "Using an electric car over a normal car helps reduce about 4.6 metric tons of CO2 per year for each car",
            True,
            BLACK)
        next_level = EXPLAIN_FONT.render("Please press enter to go the next level...", True, BLACK)

        # Actually displaying the text to the screen
        WIN.blit(explanation, (WIDTH // 2 - explanation.get_width() // 2, 75))
        WIN.blit(explanation_1, (WIDTH // 2 - explanation_1.get_width() // 2, 125))
        WIN.blit(explanation_2, (WIDTH // 2 - explanation_2.get_width() // 2, 175))
        WIN.blit(explanation_3, (WIDTH // 2 - explanation_3.get_width() // 2, 225))
        WIN.blit(explanation_4, (WIDTH // 2 - explanation_4.get_width() // 2, 275))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 325))

        pygame.display.update()

        # Looping through the different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three()

    pygame.quit()


def level_three():
    print("all good")


def game_over():
    print("game over")


def main():
    level_one()


# makes sure it will open the main loop first
if __name__ == "__main__":
    main()
