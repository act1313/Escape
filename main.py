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
HOME = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'home.jpg')), (850, 850))
RECYCLING_BIN = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bin.PNG')), (80, 140))
SINK = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sink.png')), (100, 150))
WHITE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'white.jpg')), (WIDTH, HEIGHT))
LIGHT_SWITCH = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'light_switch.jpg')), (30, 35))
PLASTIC_BOTTLE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'plastic_bottle.png')), (90, 200))
REUSABLE_BOTTLE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'reusable_bottle.png')), (64, 200))
PLASTIC_STRAW = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'straw.png')), (200, 140))
CAR = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'car.png')), (200, 100))

# The fonts for the projects
LIVES_FONT = pygame.font.SysFont("comicsans", 50)
RIDDLE_FONT = pygame.font.SysFont("comicsans", 56)
EXPLAIN_FONT = pygame.font.SysFont("comicsans", 50)


def level_one():
    def draw_items():
        # render the images to display
        WIN.blit(RECYCLING_BIN, (WIDTH - RECYCLING_BIN.get_width(), HEIGHT - RECYCLING_BIN.get_height()))
        WIN.blit(SINK, (1280, 440))
        WIN.blit(LIGHT_SWITCH, (465, 400))
        WIN.blit(LIGHT_SWITCH, (550, 775))

    def window():
        WIN.blit(BACKGROUND, (0, 0))
        # Rendering the font into displayable text
        riddle_text = RIDDLE_FONT.render("This family left for the day. Click the things that are", True, BLACK)
        riddle_second_half_text = RIDDLE_FONT.render(" incorrect and don't help climate change.", True, BLACK)
        lives_text = LIVES_FONT.render(f"Items left: {items}", True, BLACK)

        # Making the text show on the screen
        WIN.blit(riddle_text, (WIDTH // 2 - riddle_text.get_width() // 2, 10))
        WIN.blit(riddle_second_half_text, (WIDTH // 2 - riddle_second_half_text.get_width() // 2, 50))
        WIN.blit(lives_text, (WIDTH - 250, 10))

        draw_items()

        # showing the images on the screen
        pygame.display.update()

    # the hit boxes for the areas
    bin_area = pygame.Rect(WIDTH - RECYCLING_BIN.get_width(), HEIGHT - RECYCLING_BIN.get_height(), 80, 140)
    sink_area = pygame.Rect(1280, 440, 100, 150)
    light_switch_one_area = pygame.Rect(465, 400, 30, 35)
    light_switch_two_area = pygame.Rect(550, 775, 30, 35)

    run = True
    items = 4
    # whether or not the item was clicked so we won't click it again and deduct from the items variable
    bin_clicked = True
    sink_clicked = True
    light_switch_one_clicked = True
    light_switch_two_clicked = True

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
                    # Checking to see if all of the items have been clicked and reduce the amount of corrects items
                    if bin_area.collidepoint(event.pos) and bin_clicked:
                        bin_clicked = False
                        items -= 1
                        print("bin")

                    if sink_area.collidepoint(event.pos) and sink_clicked:
                        sink_clicked = False
                        items -= 1
                        print("sink")

                    if light_switch_one_area.collidepoint(event.pos) and light_switch_one_clicked:
                        light_switch_one_clicked = False
                        items -= 1
                        print("light switch one")

                    if light_switch_two_area.collidepoint(event.pos) and light_switch_two_clicked:
                        light_switch_two_clicked = False
                        items -= 1
                        print("light switch two")

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
        WIN.blit(explanation, (WIDTH // 2 - explanation.get_width() // 2, 150))
        WIN.blit(explanation_1, (WIDTH // 2 - explanation_1.get_width() // 2, 250))
        WIN.blit(explanation_2, (WIDTH // 2 - explanation_2.get_width() // 2, 350))
        WIN.blit(explanation_3, (WIDTH // 2 - explanation_3.get_width() // 2, 450))
        WIN.blit(explanation_4, (WIDTH // 2 - explanation_4.get_width() // 2, 550))
        WIN.blit(explanation_5, (WIDTH // 2 - explanation_5.get_width() // 2, 650))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 751))

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
    reusable_bottle_area = pygame.Rect(1240, 500, 200, 200)
    plastic_bottle_area = pygame.Rect(410, 500, 200, 200)

    def window():
        WIN.blit(WHITE, (0, 0))

        # loading in the fonts for the text
        question_font = pygame.font.SysFont("comicsans", 120)
        text_font = pygame.font.SysFont("comicsans", 60)
        lives_font = pygame.font.SysFont("comicsans", 60)

        # rendering the text
        question = question_font.render("Which is better to use?", True, BLACK)
        text = text_font.render("Reusable", True, BLACK)
        text_2 = text_font.render("Plastic", True, BLACK)
        lives_text = lives_font.render(f"Lives: {level_two_question_one.lives}", True, BLACK)

        # drawing the circle and the water bottles
        pygame.draw.circle(WIN, GREEN, (1340, 600), 200)
        WIN.blit(REUSABLE_BOTTLE, (1300, 500))

        pygame.draw.circle(WIN, GREEN, (510, 600), 200)
        WIN.blit(PLASTIC_BOTTLE, (450, 500))

        # displaying the text
        WIN.blit(question, (WIDTH // 2 - question.get_width() // 2, 20))
        WIN.blit(text, (1430 - text.get_width(), 450))
        WIN.blit(text_2, (570 - text_2.get_width(), 450))
        WIN.blit(lives_text, (WIDTH - 250, 10))

        # updating the screen
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
    plastic_straw_area = pygame.Rect(1240, 500, 200, 200)
    paper_straw_area = pygame.Rect(410, 500, 200, 200)

    def window():
        WIN.blit(WHITE, (0, 0))

        question_font = pygame.font.SysFont("comicsans", 100)
        text_font = pygame.font.SysFont("comicsans", 60)
        lives_font = pygame.font.SysFont("comicsans", 80)

        question = question_font.render("Which type of straw is better to use?", True, BLACK)
        text_2 = text_font.render("Plastic", True, BLACK)
        text = text_font.render("Paper", True, BLACK)
        lives_text = lives_font.render(f"Lives: {level_two_question_one.lives}", True, BLACK)

        # drawing the straw and circle
        pygame.draw.circle(WIN, GREEN, (1340, 600), 200)
        WIN.blit(PLASTIC_STRAW, (1260, 550))

        pygame.draw.circle(WIN, GREEN, (510, 600), 200)
        WIN.blit(PLASTIC_STRAW, (410, 550))

        WIN.blit(question, (WIDTH // 2 - question.get_width() // 2, 20))
        WIN.blit(text, (570 - text_2.get_width(), 450))
        WIN.blit(text_2, (1400 - text.get_width(), 450))
        WIN.blit(lives_text, (WIDTH - 250, 20))

        pygame.display.update()

    run = True
    straw_clickable = True
    while run:
        window()
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
    normal_car_area = pygame.Rect(1240, 500, 200, 200)
    electric_car_area = pygame.Rect(410, 500, 200, 200)

    def window():
        WIN.blit(WHITE, (0, 0))

        question_font = pygame.font.SysFont("comicsans", 75)
        text_font = pygame.font.SysFont("comicsans", 55)
        lives_font = pygame.font.SysFont("comicsans", 80)

        question = question_font.render("Which type of car is better for the environment?", True, BLACK)
        text_2 = text_font.render("Electric Car", True, BLACK)
        text = text_font.render("Gas Fueled Car", True, BLACK)
        lives_text = lives_font.render(f"Lives: {level_two_question_one.lives}", True, BLACK)

        # drawing the straw and circle
        pygame.draw.circle(WIN, GREEN, (1340, 600), 200)
        WIN.blit(CAR, (1260, 550))

        pygame.draw.circle(WIN, GREEN, (510, 600), 200)
        WIN.blit(CAR, (410, 550))

        WIN.blit(question, (WIDTH // 2 - question.get_width() // 2, 20))
        WIN.blit(text, (580 - text_2.get_width(), 450))
        WIN.blit(text_2, (1520 - text.get_width(), 450))
        WIN.blit(lives_text, (WIDTH - 250, 20))

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
        WIN.blit(explanation, (WIDTH // 2 - explanation.get_width() // 2, 150))
        WIN.blit(explanation_1, (WIDTH // 2 - explanation_1.get_width() // 2, 250))
        WIN.blit(explanation_2, (WIDTH // 2 - explanation_2.get_width() // 2, 350))
        WIN.blit(explanation_3, (WIDTH // 2 - explanation_3.get_width() // 2, 450))
        WIN.blit(explanation_4, (WIDTH // 2 - explanation_4.get_width() // 2, 550))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 650))

        pygame.display.update()

        # Looping through the different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three_starting_explain()

    pygame.quit()


def level_three_starting_explain():
    def window():
        font = pygame.font.SysFont("comicsans", 50)

        text = font.render(
            "For the final level, you will be answering questions about different types of renewable energy.", True,
            BLACK)
        text_2 = font.render("Renewable energy, or clean energy, is energy that comes from natural sources", True,
                             BLACK)
        text_2b = font.render("or processes that are constantly replenished.", True, BLACK)
        text_3 = font.render("Press enter to go to the first question.", True, BLACK)

        WIN.blit(WHITE, (0, 0))

        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 350))
        WIN.blit(text_2, (WIDTH // 2 - text_2.get_width() // 2, 450))
        WIN.blit(text_2b, (WIDTH // 2 - text_2b.get_width() // 2, 550))
        WIN.blit(text_3, (WIDTH // 2 - text_3.get_width() // 2, 650))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three_question_one()

    pygame.quit()


def level_three_question_one():
    def window():
        riddle_font = pygame.font.SysFont("comicsans", 40)
        font = pygame.font.SysFont("comicsans", 50)

        riddle = riddle_font.render(
            "What type of on energy is used on many houses today that is the most abundant energy source in the world?",
            True, BLACK)
        riddle_2 = riddle_font.render("(Hint: Click one through four to answer.)", True, BLACK)

        solar = font.render("1) Solar Energy", True, BLACK)
        wind = font.render("2) Wind Energy", True, BLACK)
        hydro = font.render("3) Hydro Energy", True, BLACK)
        geothermal = font.render("4) Geothermal Energy", True, BLACK)

        WIN.blit(WHITE, (0, 0))
        WIN.blit(HOME, (WIDTH // 2 - HOME.get_width() // 2, 200))

        WIN.blit(riddle, (WIDTH // 2 - riddle.get_width() // 2, 20))
        WIN.blit(riddle_2, (WIDTH // 2 - riddle_2.get_width() // 2, 70))

        WIN.blit(solar, (50, 750))
        WIN.blit(wind, (500, 750))
        WIN.blit(hydro, (950, 750))
        WIN.blit(geothermal, (1400, 750))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level_three_question_one_explain()
                if event.key == pygame.K_2:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_3:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_4:
                    print("Incorrect! Please try again.")

    pygame.quit()


def level_three_question_one_explain():
    def window():
        font = pygame.font.SysFont("comicsans", 50)

        text = font.render("Solar energy, if you didn't already know, is energy from the sun.", True, BLACK)
        text_1 = font.render("Solar energy is also the most abundant source of energy because today there are", True,
                             BLACK)
        text_2 = font.render("89 petawatts(one petawatt is one quadrillion watts)", True, BLACK)
        text_3 = font.render("of potential solar energy production available on earth.", True, BLACK)
        next_level = font.render("Press enter to go to the next question...", True, BLACK)

        WIN.blit(WHITE, (0, 0))

        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 350))
        WIN.blit(text_1, (WIDTH // 2 - text_1.get_width() // 2, 425))
        WIN.blit(text_2, (WIDTH // 2 - text_2.get_width() // 2, 500))
        WIN.blit(text_3, (WIDTH // 2 - text_3.get_width() // 2, 575))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 650))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three_question_two()

    pygame.quit()


def level_three_question_two():
    def window():
        riddle_font = pygame.font.SysFont("comicsans", 40)
        font = pygame.font.SysFont("comicsans", 50)

        riddle = riddle_font.render(
            "What type of on energy is used to as 74% of Washtingon's power (the state) and is commonly acquired with a dam?",
            True, BLACK)
        riddle_2 = riddle_font.render("(Hint: Click one through four to answer.)", True, BLACK)

        solar = font.render("1) Solar Energy", True, BLACK)
        wind = font.render("2) Wind Energy", True, BLACK)
        hydro = font.render("3) Hydro Energy", True, BLACK)
        geothermal = font.render("4) Geothermal Energy", True, BLACK)

        WIN.blit(WHITE, (0, 0))
        WIN.blit(HOME, (WIDTH // 2 - HOME.get_width() // 2, 200))

        WIN.blit(riddle, (WIDTH // 2 - riddle.get_width() // 2, 20))
        WIN.blit(riddle_2, (WIDTH // 2 - riddle_2.get_width() // 2, 70))

        WIN.blit(solar, (50, 750))
        WIN.blit(wind, (500, 750))
        WIN.blit(hydro, (950, 750))
        WIN.blit(geothermal, (1400, 750))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_2:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_3:
                    level_three_question_two_explain()
                if event.key == pygame.K_4:
                    print("Incorrect! Please try again.")

    pygame.quit()


def level_three_question_two_explain():
    def window():
        font = pygame.font.SysFont("comicsans", 50)

        text = font.render("Hydro power, if you didn't already know, is energy generated from flowing water", True,
                           BLACK)
        text_1 = font.render("Hydro power is also one of the most inexpensive sources of energy.", True,
                             BLACK)
        text_2 = font.render("It is also one of the more widely used power source because", True, BLACK)
        text_3 = font.render("it is used for electricity in all of the states except (Delaware and Mississippi).", True,
                             BLACK)
        next_level = font.render("Press enter to go to the next question...", True, BLACK)

        WIN.blit(WHITE, (0, 0))

        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 350))
        WIN.blit(text_1, (WIDTH // 2 - text_1.get_width() // 2, 425))
        WIN.blit(text_2, (WIDTH // 2 - text_2.get_width() // 2, 500))
        WIN.blit(text_3, (WIDTH // 2 - text_3.get_width() // 2, 575))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 650))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three_question_three()

    pygame.quit()


def level_three_question_three():
    def window():
        riddle_font = pygame.font.SysFont("comicsans", 40)
        font = pygame.font.SysFont("comicsans", 50)

        riddle = riddle_font.render(
            "What type of energy is harnessed in large scale farms and produces no greenhouse gases?",
            True, BLACK)
        riddle_2 = riddle_font.render("(Hint: Click one through four to answer.)", True, BLACK)

        solar = font.render("1) Solar Energy", True, BLACK)
        wind = font.render("2) Wind Energy", True, BLACK)
        hydro = font.render("3) Hydro Energy", True, BLACK)
        geothermal = font.render("4) Geothermal Energy", True, BLACK)

        WIN.blit(WHITE, (0, 0))
        WIN.blit(HOME, (WIDTH // 2 - HOME.get_width() // 2, 200))

        WIN.blit(riddle, (WIDTH // 2 - riddle.get_width() // 2, 20))
        WIN.blit(riddle_2, (WIDTH // 2 - riddle_2.get_width() // 2, 70))

        WIN.blit(solar, (50, 750))
        WIN.blit(wind, (500, 750))
        WIN.blit(hydro, (950, 750))
        WIN.blit(geothermal, (1400, 750))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_2:
                    level_three_question_three_explain()
                if event.key == pygame.K_3:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_4:
                    print("Incorrect! Please try again.")

    pygame.quit()


def level_three_question_three_explain():
    def window():
        font = pygame.font.SysFont("comicsans", 49)

        text = font.render("Wind power, if you didn't already know, is energy harnessed from the wind in the form of wind turbines.", True, BLACK)
        text_1 = font.render("Wind turbines do no requires fuel and do not emit any pollutants or gases, but", True, BLACK)
        text_2 = font.render("resources are used and small amounts of pollutants are produced during the creation of turbines.", True, BLACK)
        text_3 = font.render("One manufacturer of turbines found that they save on average 93,000 tons of CO2 over a coal power plant.", True, BLACK)
        next_level = font.render("Press enter to go to the next question...", True, BLACK)

        WIN.blit(WHITE, (0, 0))

        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 350))
        WIN.blit(text_1, (WIDTH // 2 - text_1.get_width() // 2, 425))
        WIN.blit(text_2, (WIDTH // 2 - text_2.get_width() // 2, 500))
        WIN.blit(text_3, (WIDTH // 2 - text_3.get_width() // 2, 575))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 650))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three_question_four()

    pygame.quit()


def level_three_question_four():
    def window():
        riddle_font = pygame.font.SysFont("comicsans", 40)
        font = pygame.font.SysFont("comicsans", 50)

        riddle = riddle_font.render(
            "What type of on energy is used on many houses today that is the most abundant energy source in the world?",
            True, BLACK)
        riddle_2 = riddle_font.render("(Hint: Click one through four to answer.)", True, BLACK)

        solar = font.render("1) Solar Energy", True, BLACK)
        wind = font.render("2) Wind Energy", True, BLACK)
        hydro = font.render("3) Hydro Energy", True, BLACK)
        geothermal = font.render("4) Geothermal Energy", True, BLACK)

        WIN.blit(WHITE, (0, 0))
        WIN.blit(HOME, (WIDTH // 2 - HOME.get_width() // 2, 200))

        WIN.blit(riddle, (WIDTH // 2 - riddle.get_width() // 2, 20))
        WIN.blit(riddle_2, (WIDTH // 2 - riddle_2.get_width() // 2, 70))

        WIN.blit(solar, (50, 750))
        WIN.blit(wind, (500, 750))
        WIN.blit(hydro, (950, 750))
        WIN.blit(geothermal, (1400, 750))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level_three_question_four_explain()
                if event.key == pygame.K_2:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_3:
                    print("Incorrect! Please try again.")
                if event.key == pygame.K_4:
                    print("Incorrect! Please try again.")

    pygame.quit()


def level_three_question_four_explain():
    def window():
        font = pygame.font.SysFont("comicsans", 50)

        text = font.render("Solar energy, if you didn't already know, is energy from the sun.", True, BLACK)
        text_1 = font.render("Solar energy is also the most abundant source of energy because today there are", True,
                             BLACK)
        text_2 = font.render("89 petawatts(one petawatt is one quadrillion watts)", True, BLACK)
        text_3 = font.render("of potential solar energy production available on earth.", True, BLACK)
        next_level = font.render("Press enter to go to the next question...", True, BLACK)

        WIN.blit(WHITE, (0, 0))

        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 350))
        WIN.blit(text_1, (WIDTH // 2 - text_1.get_width() // 2, 425))
        WIN.blit(text_2, (WIDTH // 2 - text_2.get_width() // 2, 500))
        WIN.blit(text_3, (WIDTH // 2 - text_3.get_width() // 2, 575))
        WIN.blit(next_level, (WIDTH // 2 - next_level.get_width() // 2, 650))

        pygame.display.update()

    run = True
    while run:
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_three_question_two()

    pygame.quit()


def end_game():
    def window():
        WIN.blit(WHITE, (0, 0))
        pygame.display.update()

    run = False
    while run:
        window()
        for event in pygame.event.get():
            if pygame.event == pygame.QUIT:
                run = False

    pygame.quit()


def game_over():
    restart = False
    run = True
    while run:
        if not restart:
            restart = True
            font = pygame.font.SysFont("comicsans", 250)
            WIN.blit(WHITE, (0, 0))

            text = font.render("Game Over!", True, BLACK)
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 500))

            pygame.display.update()
        elif restart:
            time.sleep(3.14)
            level_two_question_one()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def main():
    level_one()


# makes sure it will open the main loop first
if __name__ == "__main__":
    main()
