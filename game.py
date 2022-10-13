from tkinter.tix import IMAGE
import pygame
from pygame import *
from sound import *
from draw import *
from fighter import *

# Define assets path
IMAGES="assets/image/"

class GameManager:
    # Initialize startup
    def __init__(self, mode, left, right):
        # Create game screen
        pygame.display.set_caption("League of Fighters")
        self.screen = pygame.display.set_mode()
        self.x, self.y = self.screen.get_size()
        # Load Spritesheets
        yasuo_attack1 = pygame.image.load(IMAGES + "yasuo/Attack1.png").convert_alpha()
        yasuo_attack2 = pygame.image.load(IMAGES + "yasuo/Attack2.png").convert_alpha()
        yasuo_attack3 = pygame.image.load(IMAGES + "yasuo/Attack3.png").convert_alpha()
        yasuo_death = pygame.image.load(IMAGES + "yasuo/Death.png").convert_alpha()
        yasuo_guard = pygame.image.load(IMAGES + "yasuo/Guard.png").convert_alpha()
        yasuo_hit = pygame.image.load(IMAGES + "yasuo/Hit.png").convert_alpha()
        yasuo_idle = pygame.image.load(IMAGES + "yasuo/Idle.png").convert_alpha()
        yasuo_jump = pygame.image.load(IMAGES + "yasuo/Jump.png").convert_alpha()
        yasuo_run = pygame.image.load(IMAGES + "yasuo/Run.png").convert_alpha()
        self.yasuo = [yasuo_attack1, yasuo_attack2, yasuo_attack3, yasuo_death, yasuo_guard, yasuo_hit, yasuo_idle, yasuo_jump, yasuo_run]
        self.yasuo_steps = [6,7,4,5,1,1,3,1,7]
        darius_attack1 = pygame.image.load(IMAGES + "darius/Attack1.png").convert_alpha()
        darius_attack2 = pygame.image.load(IMAGES + "darius/Attack2.png").convert_alpha()
        darius_attack3 = pygame.image.load(IMAGES + "darius/Attack3.png").convert_alpha()
        darius_death = pygame.image.load(IMAGES + "darius/Death.png").convert_alpha()
        darius_guard = pygame.image.load(IMAGES + "darius/Guard.png").convert_alpha()
        darius_hit = pygame.image.load(IMAGES + "darius/Hit.png").convert_alpha()
        darius_idle = pygame.image.load(IMAGES + "darius/Idle.png").convert_alpha()
        darius_jump = pygame.image.load(IMAGES + "darius/Jump.png").convert_alpha()
        darius_run = pygame.image.load(IMAGES + "darius/Run.png").convert_alpha()
        self.darius = [darius_attack1, darius_attack2, darius_attack3, darius_death, darius_guard, darius_hit, darius_idle, darius_jump, darius_run]
        self.darius_steps = [6,4,4,5,1,1,3,1,7]
        pantheon_attack1 = pygame.image.load(IMAGES + "yasuo/Attack1.png").convert_alpha()
        pantheon_attack2 = pygame.image.load(IMAGES + "yasuo/Attack2.png").convert_alpha()
        pantheon_attack3 = pygame.image.load(IMAGES + "yasuo/Attack3.png").convert_alpha()
        pantheon_death = pygame.image.load(IMAGES + "yasuo/Death.png").convert_alpha()
        pantheon_guard = pygame.image.load(IMAGES + "yasuo/Guard.png").convert_alpha()
        pantheon_hit = pygame.image.load(IMAGES + "yasuo/Hit.png").convert_alpha()
        pantheon_idle = pygame.image.load(IMAGES + "yasuo/Idle.png").convert_alpha()
        pantheon_jump = pygame.image.load(IMAGES + "yasuo/Jump.png").convert_alpha()
        pantheon_run = pygame.image.load(IMAGES + "yasuo/Run.png").convert_alpha()
        self.pantheon = [pantheon_attack1, pantheon_attack2, pantheon_attack3, pantheon_death, pantheon_guard, pantheon_hit, pantheon_idle, pantheon_jump, pantheon_run]
        self.pantheon_steps = [6,7,4,5,1,1,3,1,7]
        leesin_attack1 = pygame.image.load(IMAGES + "leesin/Attack1.png").convert_alpha()
        leesin_attack2 = pygame.image.load(IMAGES + "leesin/Attack2.png").convert_alpha()
        leesin_attack3 = pygame.image.load(IMAGES + "leesin/Attack3.png").convert_alpha()
        leesin_death = pygame.image.load(IMAGES + "leesin/Death.png").convert_alpha()
        leesin_guard = pygame.image.load(IMAGES + "leesin/Guard.png").convert_alpha()
        leesin_hit = pygame.image.load(IMAGES + "leesin/Hit.png").convert_alpha()    
        leesin_idle = pygame.image.load(IMAGES + "leesin/Idle.png").convert_alpha()
        leesin_jump = pygame.image.load(IMAGES + "leesin/Jump.png").convert_alpha()
        leesin_run = pygame.image.load(IMAGES + "leesin/Run.png").convert_alpha()
        self.leesin = [leesin_attack1, leesin_attack2, leesin_attack3, leesin_death, leesin_guard, leesin_hit, leesin_idle, leesin_jump, leesin_run]
        self.leesin_steps = [6,5,4,5,1,1,3,1,7]
        self.champions = [self.yasuo, self.leesin, self.darius, self.pantheon]
        # Create fighters
        self.mode = mode
        self.leftFighter = Fighter(self.screen, self.x*0.2, self.y*0.55, self.x, self.y, self.champions[left], self.yasuo_steps, 0)
        self.rightFighter = Fighter(self.screen, self.x*0.7, self.y*0.55, self.x, self.y, self.champions[right], self.yasuo_steps, self.mode)
        # Create score
        self.leftScore = 0
        self.rightScore = 0
        self.gameOver = False
        self.gameOverTime = 0
        
    # Game loop
    def start(self, mapChoice, left, right):
        # Create font
        count_font = pygame.font.Font(IMAGES + "font.ttf", 120)
        score_font = pygame.font.Font(IMAGES + "font.ttf", 45)
        # Initialize variables
        run = True
        clock = 0
        intro_count = 3
        timer_count = 60
        last_count_update = pygame.time.get_ticks()
        if mapChoice == 0: img = IMAGES + "map/bilgewater.jpg"
        if mapChoice == 1: img = IMAGES + "map/city2.jpg"
        if mapChoice == 2: img = IMAGES + "map/demacia1.jpg"
        if mapChoice == 3: img = IMAGES + "map/demacia2.jpg"
        if mapChoice == 4: img = IMAGES + "map/ionia1.jpg"
        if mapChoice == 5: img = IMAGES + "map/ionia2.jpg"
        if mapChoice == 6: img = IMAGES + "map/noxus.jpg"
        if mapChoice == 7: img = IMAGES + "map/shadow.jpg"
        if mapChoice == 8: img = IMAGES + "map/void1.jpg"
        if mapChoice == 9: img = IMAGES + "map/zaun.jpg"

        # Main loop
        while run:
            clock += pygame.time.Clock().tick(60) / 1000
            drawBg(self.screen, img, self.x, self.y)
            drawHp(self.screen, self.leftFighter, self.rightFighter, self.x, self.y)
            drawText(self.screen,"P1: " + str(self.leftScore), score_font, (220, 20, 60), self.x*0.05, self.y*0.1)
            drawText(self.screen,"P2: " + str(self.rightScore), score_font, (220, 20, 60), self.x*0.65, self.y*0.1)

            if intro_count <= -1:
                self.leftFighter.move(True, self.x, self.y, self.rightFighter)
                self.rightFighter.move(False, self.x, self.y, self.leftFighter)
            else:
                if (intro_count >= 1): drawText(self.screen, str(intro_count), count_font, (220, 20, 60), self.x/2, self.y/3)
                else: drawText(self.screen, "FIGHT", count_font, (220, 20, 60), self.x/2-120, self.y/3)
                if (pygame.time.get_ticks() - last_count_update) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()

            self.leftFighter.update()
            self.rightFighter.update()

            self.leftFighter.draw(True)
            self.rightFighter.draw(False)

            if self.gameOver == False:
                if self.leftFighter.health <= 0:
                    self.rightScore += 1
                    self.gameOver = True
                    self.gameOverTime = pygame.time.get_ticks()
                if self.rightFighter.health <= 0:
                    self.leftScore += 1
                    self.gameOver = True
                    self.gameOverTime = pygame.time.get_ticks()
            else:
                if self.leftFighter.health <= 0:
                    drawText(self.screen, "PLAYER 2 WIN", count_font, (220, 20, 60), self.x/2-300, self.y/3)
                if self.rightFighter.health <= 0:
                    drawText(self.screen, "PLAYER 1 WIN", count_font, (220, 20, 60), self.x/2-300, self.y/3)
                if pygame.time.get_ticks() - self.gameOverTime > 2000:
                    self.gameOver = False
                    self.leftFighter = Fighter(self.screen, self.x*0.2, self.y*0.55, self.x, self.y, self.champions[left], self.yasuo_steps, 0)
                    self.rightFighter = Fighter(self.screen, self.x*0.7, self.y*0.55, self.x, self.y, self.champions[right], self.yasuo_steps, self.mode)
                    
                
            # Event handler
            for event in pygame.event.get():
                # Allow exit
                if event.type == pygame.QUIT:
                    run = False
                # Mouse click
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    run = False
            # Update display
            pygame.display.update()