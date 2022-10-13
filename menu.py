import pygame
import random
from pygame import *
from game import GameManager
from sound import *
from draw import *
from fighter import *

# Define assets path
IMAGES="assets/image/"
SOUNDS="assets/sound/"

class MenuManager:
    # Initialize startup
    def __init__(self):
        # Create game screen
        pygame.display.set_caption("League of Fighters")
        self.screen = pygame.display.set_mode()
        self.x, self.y = self.screen.get_size()
        # Create sound
        self.sound = SoundManager()
        # Create menu screens
        self.loadingScreen = []
        loadDemacia = []
        loadFreljord = []
        loadNoxus = []
        loadPiltover = []
        loadTargon = []

        for x in range(25):
            loadDemacia.append(pygame.image.load(IMAGES + "menu/demacia/Layer_" + str(x) + "1.png"))
            loadFreljord.append(pygame.image.load(IMAGES + "menu/freljord/Layer_" + str(x) + "1.png"))
            loadNoxus.append(pygame.image.load(IMAGES + "menu/noxus/Layer_" + str(x) + "1.png"))
            loadTargon.append(pygame.image.load(IMAGES + "menu/targon/Layer_" + str(x) + "1.png"))
        for x in range(4):
            loadPiltover.append(pygame.image.load(IMAGES + "menu/piltover/Layer_" + str(x) + "1.png"))

        self.loadingScreen.append(loadDemacia)
        self.loadingScreen.append(loadFreljord)
        self.loadingScreen.append(loadNoxus)
        self.loadingScreen.append(loadTargon)
        self.loadingScreen.append(loadPiltover)
        # Random a screen
        self.randomMap = random.randint(0, 4)
        self.state = 0
        # Define buttons
        self.buttonTitle = pygame.image.load(IMAGES + "menu/title.png")
        self.buttonTitle = pygame.transform.scale(self.buttonTitle, (int(self.x*0.5), int(self.y*0.5)))
        self.buttonCredit = pygame.image.load(IMAGES + "menu/credit.png")
        self.buttonCredit = pygame.transform.scale(self.buttonCredit, (int(self.x*0.1), int(self.y*0.1)))
        self.buttonName = pygame.image.load(IMAGES + "menu/name.png")
        self.buttonName = pygame.transform.scale(self.buttonName, (int(self.x*0.2), int(self.y*0.2)))
        self.buttonPlay = pygame.image.load(IMAGES + "menu/start.png")
        self.buttonPlay = pygame.transform.scale(self.buttonPlay, (int(self.x*0.1), int(self.y*0.1)))
        self.buttonPvE = pygame.image.load(IMAGES + "menu/pve.png")
        self.buttonPvE = pygame.transform.scale(self.buttonPvE, (int(self.x*0.1), int(self.y*0.1)))
        self.buttonPvP = pygame.image.load(IMAGES + "menu/pvp.png")
        self.buttonPvP = pygame.transform.scale(self.buttonPvP, (int(self.x*0.1), int(self.y*0.1)))
        self.buttonSelectChampion = pygame.image.load(IMAGES + "menu/selectchampion.png")
        self.buttonSelectChampion = pygame.transform.scale(self.buttonSelectChampion, (int(self.x*0.3), int(self.y*0.3)))
        self.buttonSelectMap = pygame.image.load(IMAGES + "menu/selectmap.png")
        self.buttonSelectMap = pygame.transform.scale(self.buttonSelectMap, (int(self.x*0.2), int(self.y*0.2)))
        self.buttonSelectMode = pygame.image.load(IMAGES + "menu/selectmode.png")
        self.buttonSelectMode = pygame.transform.scale(self.buttonSelectMode, (int(self.x*0.2), int(self.y*0.2)))
        self.buttonTag = pygame.image.load(IMAGES + "menu/tag.png")
        self.buttonTag = pygame.transform.scale(self.buttonTag, (int(self.x*0.1), int(self.y*0.1)))
        # Define maps
        self.map1 = pygame.image.load(IMAGES + "map/bilgewater.jpg")
        self.map1 = pygame.transform.scale(self.map1, (int(self.x*0.16), int(self.y*0.2)))
        self.map2 = pygame.image.load(IMAGES + "map/city2.jpg")
        self.map2 = pygame.transform.scale(self.map2, (int(self.x*0.16), int(self.y*0.2)))
        self.map3 = pygame.image.load(IMAGES + "map/demacia1.jpg")
        self.map3 = pygame.transform.scale(self.map3, (int(self.x*0.16), int(self.y*0.2)))
        self.map4 = pygame.image.load(IMAGES + "map/demacia2.jpg")
        self.map4 = pygame.transform.scale(self.map4, (int(self.x*0.16), int(self.y*0.2)))
        self.map5 = pygame.image.load(IMAGES + "map/ionia1.jpg")
        self.map5 = pygame.transform.scale(self.map5, (int(self.x*0.16), int(self.y*0.2)))
        self.map6 = pygame.image.load(IMAGES + "map/ionia2.jpg")
        self.map6 = pygame.transform.scale(self.map6, (int(self.x*0.16), int(self.y*0.2)))
        self.map7 = pygame.image.load(IMAGES + "map/noxus.jpg")
        self.map7 = pygame.transform.scale(self.map7, (int(self.x*0.16), int(self.y*0.2)))
        self.map8 = pygame.image.load(IMAGES + "map/shadow.jpg")
        self.map8 = pygame.transform.scale(self.map8, (int(self.x*0.16), int(self.y*0.2)))
        self.map9 = pygame.image.load(IMAGES + "map/void1.jpg")
        self.map9 = pygame.transform.scale(self.map9, (int(self.x*0.16), int(self.y*0.2)))
        self.map10 = pygame.image.load(IMAGES + "map/zaun.jpg")
        self.map10 = pygame.transform.scale(self.map10, (int(self.x*0.16), int(self.y*0.2)))
        # Define champions
        self.yasuo = pygame.image.load(IMAGES + "menu/yasuo.png")
        self.yasuo = pygame.transform.scale(self.yasuo, (int(self.y*0.2), int(self.y*0.2)))
        self.leesin = pygame.image.load(IMAGES + "menu/leesin.png")
        self.leesin = pygame.transform.scale(self.leesin, (int(self.y*0.2), int(self.y*0.2)))
        self.darius = pygame.image.load(IMAGES + "menu/darius.png")
        self.darius = pygame.transform.scale(self.darius, (int(self.y*0.2), int(self.y*0.2)))
        self.pantheon = pygame.image.load(IMAGES + "menu/pantheon.png")
        self.pantheon = pygame.transform.scale(self.pantheon, (int(self.y*0.2), int(self.y*0.2)))
        self.ticked = pygame.image.load(IMAGES + "menu/ticked.png")
        self.ticked = pygame.transform.scale(self.ticked, (int(self.y*0.05), int(self.y*0.05)))

    # Run screen loop
    def MenuLoop(self, skin):
        self.state += 0.1
        if self.state >= len(skin):
            self.state = 0
        self.map = skin[int(self.state)]
        self.map = pygame.transform.scale(self.map, (self.x, self.y))
        self.screen.blit(self.map, (0,0))

    # Mouse click check 
    def click(self, mouse, pos, w, h):
        xMouse = mouse[0]
        yMouse = mouse[1]
        xPos = pos[0]
        yPos = pos[1]
        if (xMouse > xPos) and (xMouse < xPos + w) and (yMouse > yPos) and (yMouse < yPos + h):
            return True
        else:
            return False
    
    # Print default buttons
    def default(self):
        self.screen.blit(self.buttonPlay, (self.x*0.45,self.y*0.5))
        self.screen.blit(self.buttonCredit, (self.x*0.45,self.y*0.65))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.view = -1
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.click(mouse.get_pos(), [self.x*0.45,self.y*0.53], self.x*0.1, self.y*0.05):
                    self.view = 2
                if self.click(mouse.get_pos(), [self.x*0.45,self.y*0.68], self.x*0.1, self.y*0.04):
                    self.view = 1
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.view = -1
    
    # Print credit
    def name(self):
        self.screen.blit(self.buttonName, (self.x*0.4,self.y*0.5))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.view = 0

    def selectMode(self):
        self.screen.blit(self.buttonSelectMode, (self.x*0.4,self.y*0.35))
        self.screen.blit(self.buttonPvP, (self.x*0.45,self.y*0.5))
        self.screen.blit(self.buttonPvE, (self.x*0.45,self.y*0.65))
        #self.screen.blit(self.buttonTag, (self.x*0.45,self.y*0.8))
        self.mode = -1
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.click(mouse.get_pos(), [self.x*0.47,self.y*0.52], self.x*0.08, self.y*0.08):
                    self.view = 3
                    self.mode = 0
                if self.click(mouse.get_pos(), [self.x*0.47,self.y*0.67], self.x*0.08, self.y*0.08):
                    self.view = 3
                    self.mode = 1
                # if self.click(mouse.get_pos(), [self.x*0.47,self.y*0.82], self.x*0.08, self.y*0.08):
                #     self.view = 3
                #     self.mode = 2
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.view = 0

    def selectMap(self):
        self.screen.blit(self.buttonSelectMap, (self.x*0.4,self.y*0.35))
        self.screen.blit(self.map1, (self.x*0.1,self.y*0.5))
        self.screen.blit(self.map2, (self.x*0.26,self.y*0.5))
        self.screen.blit(self.map3, (self.x*0.42,self.y*0.5))
        self.screen.blit(self.map4, (self.x*0.58,self.y*0.5))
        self.screen.blit(self.map5, (self.x*0.74,self.y*0.5))
        self.screen.blit(self.map6, (self.x*0.1,self.y*0.7))
        self.screen.blit(self.map7, (self.x*0.26,self.y*0.7))
        self.screen.blit(self.map8, (self.x*0.42,self.y*0.7))
        self.screen.blit(self.map9, (self.x*0.58,self.y*0.7))
        self.screen.blit(self.map10, (self.x*0.74,self.y*0.7))
        self.mapChoice = -1
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.click(mouse.get_pos(), [self.x*0.1,self.y*0.5], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 0
                if self.click(mouse.get_pos(), [self.x*0.26,self.y*0.5], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 1
                if self.click(mouse.get_pos(), [self.x*0.42,self.y*0.5], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 2
                if self.click(mouse.get_pos(), [self.x*0.58,self.y*0.5], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 3
                if self.click(mouse.get_pos(), [self.x*0.74,self.y*0.5], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 4
                if self.click(mouse.get_pos(), [self.x*0.1,self.y*0.7], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 5
                if self.click(mouse.get_pos(), [self.x*0.26,self.y*0.7], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 6
                if self.click(mouse.get_pos(), [self.x*0.42,self.y*0.7], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 7
                if self.click(mouse.get_pos(), [self.x*0.58,self.y*0.7], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 8
                if self.click(mouse.get_pos(), [self.x*0.74,self.y*0.7], self.x*0.16, self.y*0.2):
                    self.view = 4
                    self.mapChoice = 9
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.view = 2

    def selectChampion(self):
        self.screen.blit(self.buttonSelectChampion, (self.x*0.35,self.y*0.3))
        self.screen.blit(self.yasuo, (self.x*0.5-self.y*0.2,self.y*0.55))
        self.screen.blit(self.leesin, (self.x*0.5,self.y*0.55))
        self.screen.blit(self.darius, (self.x*0.5-self.y*0.2,self.y*0.75))
        #self.screen.blit(self.pantheon, (self.x*0.5,self.y*0.75))
        self.left = -1
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.click(mouse.get_pos(), [self.x*0.5-self.y*0.2,self.y*0.55], self.y*0.2, self.y*0.2):
                    self.left = 0
                    self.view = 5
                if self.click(mouse.get_pos(), [self.x*0.5,self.y*0.55], self.y*0.2, self.y*0.2):
                    self.left = 1
                    self.view = 5
                if self.click(mouse.get_pos(), [self.x*0.5-self.y*0.2,self.y*0.75], self.y*0.2, self.y*0.2):
                    self.left = 2
                    self.view = 5
                # if self.click(mouse.get_pos(), [self.x*0.5,self.y*0.75], self.y*0.2, self.y*0.2):
                #     self.left = 3   
                #     self.view = 5
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                self.view = 3

    # Pick second champ
    def selectChampion2(self):
        self.screen.blit(self.buttonSelectChampion, (self.x*0.35,self.y*0.3))
        self.screen.blit(self.yasuo, (self.x*0.5-self.y*0.2,self.y*0.55))
        self.screen.blit(self.leesin, (self.x*0.5,self.y*0.55))
        self.screen.blit(self.darius, (self.x*0.5-self.y*0.2,self.y*0.75))
        #self.screen.blit(self.pantheon, (self.x*0.5,self.y*0.75))
        self.right = -1
        if (self.left == 0): self.screen.blit(self.ticked, (self.x*0.5-self.y*0.2,self.y*0.55))
        if (self.left == 1): self.screen.blit(self.ticked, (self.x*0.5,self.y*0.55))
        if (self.left == 2): self.screen.blit(self.ticked, (self.x*0.5-self.y*0.2,self.y*0.75))
        if (self.left == 3): self.screen.blit(self.ticked, (self.x*0.5,self.y*0.75))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.click(mouse.get_pos(), [self.x*0.5-self.y*0.2,self.y*0.55], self.y*0.2, self.y*0.2):
                        self.right = 0
                    if self.click(mouse.get_pos(), [self.x*0.5,self.y*0.55], self.y*0.2, self.y*0.2):
                        self.right = 1
                    if self.click(mouse.get_pos(), [self.x*0.5-self.y*0.2,self.y*0.75], self.y*0.2, self.y*0.2):
                        self.right = 2
                    #if self.click(mouse.get_pos(), [self.x*0.5,self.y*0.75], self.y*0.2, self.y*0.2):
                        #self.right = 3
                    self.view = 0     
                    game = GameManager(self.mode, self.left, self.right)
                    game.start(self.mapChoice, self.left, self.right)              
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                    self.view = 4

    # Game loop
    def start(self):
        # Initialize variables
        self.run = True
        self.view = 0
        self.mode = -1
        self.mapChoice = -1
        self.left = -1
        self.right = -1
        pygame.mixer.music.load(SOUNDS + "theme.wav")
        mixer.music.play(-1)
        mixer.music.set_volume(0.06)

        # Main loop
        while self.run:
            # Menu gif
            self.MenuLoop(self.loadingScreen[self.randomMap])
            self.screen.blit(self.buttonTitle, (self.x*0.25,0))      
            if self.view == 0: self.default()
            if self.view == 1: self.name()
            if self.view == 2: self.selectMode()
            if self.view == 3: self.selectMap()
            if self.view == 4: self.selectChampion()
            if self.view == 5: self.selectChampion2()
            if self.view == -1: self.run = False
            pygame.display.update()