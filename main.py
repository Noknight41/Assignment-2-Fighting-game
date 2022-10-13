from game import *
from menu import MenuManager

# Initialize game
if __name__ == "__main__":
    pygame.init()
    game = MenuManager()
    game.start()
    pygame.quit()