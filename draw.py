import pygame

# Draw background
def drawBg(screen, img, x, y):
    img = pygame.image.load(img).convert_alpha()
    img = pygame.transform.scale(img, (x, y))
    screen.blit(img, (0,0))

def drawHp(screen, left, right, x, y):
    pygame.draw.rect(screen, (0, 0, 0), (x*0.05-5, y*0.05-5, x*0.3+10, y*0.05+10)) # outline
    pygame.draw.rect(screen, (255, 0, 0), (x*0.05, y*0.05, x*0.3, y*0.05))
    pygame.draw.rect(screen, (255, 255, 0), (x*0.05, y*0.05, x*0.3*left.health/100, y*0.05))
    
    pygame.draw.rect(screen, (0, 0, 0), (x*0.65-5, y*0.05-5, x*0.3+10, y*0.05+10))
    pygame.draw.rect(screen, (255, 0, 0), (x*0.65, y*0.05, x*0.3, y*0.05))
    pygame.draw.rect(screen, (255, 255, 0), (x*0.65, y*0.05, x*0.3*right.health/100, y*0.05))

def drawText(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))