import pygame
import random

class Fighter():
    def __init__(self, map, x, y, w, h, sheet, steps, isAI):
        self.size = 162
        self.rect = pygame.Rect((x, y, w*0.1, h*0.35))
        self.gravity = 0
        self.canJump = True
        self.action = 6 # 0-2: attack, 3: death, 4: guard, 5: hit, 6:idle, 7: jump, 8: run
        self.skill = 0
        self.frame_index = 0
        self.attacking = False
        self.health = 100
        self.attack_cooldown = 0
        self.flip = False
        self.running = False
        self.hit = False
        self.guarding = False
        self.guard_cooldown = 0
        self.push = False
        self.update_time = pygame.time.get_ticks()
        self.guard_timer = 0
        # For AI
        self.AI = isAI
        # Define animations
        self.animation_list = []
        for y, animation in enumerate(steps):
            temp_list = []
            for x in range(animation):
                temp = sheet[y].subsurface(x * self.size, 0, self.size, self.size)
                temp_list.append(pygame.transform.scale(temp, (self.size * 4, self.size * 4)))
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.map = map

    def move(self, isLeft, width, height, target):
        SPEED = width*0.02
        GRAVITY = height*0.075
        dx = dy = 0
        self.running = False
        self.skill = 0
        self.guarding = False
        key = pygame.key.get_pressed()

        if self.attacking == False and self.health > 0:
            # Control
            if isLeft:
                # if key[pygame.K_q]:
                #     temp = self.AI
                #     self.AI = target.AI
                #     target.AI = temp
                if key[pygame.K_a]: 
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]: 
                    dx = SPEED
                    self.running = True
                if key[pygame.K_s]: 
                    self.guarding = True
                    self.guard_timer = pygame.time.get_ticks()
                if key[pygame.K_w] and self.canJump: 
                    self.gravity = -GRAVITY
                    self.canJump = False
                if key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_f]: 
                    self.frame_index = 0
                    self.attack(target)
                    if key[pygame.K_r]: 
                        self.skill = 1
                    elif key[pygame.K_t]:
                        self.skill = 2
                    else: 
                        self.skill = 3       
                    
            # Right control
            else:
                # if key[pygame.K_u]:
                #     temp = self.AI
                #     self.AI = target.AI
                #     target.AI = temp
                if key[pygame.K_j]: 
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_l]: 
                    dx = SPEED
                    self.running = True
                if key[pygame.K_k]: 
                    self.guarding = True
                    self.guard_timer = pygame.time.get_ticks()
                if key[pygame.K_i] and self.canJump: 
                    self.gravity = -GRAVITY
                    self.canJump = False
                if key[pygame.K_p] or key[pygame.K_LEFTBRACKET] or key[pygame.K_SEMICOLON]: 
                    self.frame_index = 0
                    self.attack(target)
                    if key[pygame.K_p]: 
                        self.skill = 1
                    elif key[pygame.K_LEFTBRACKET]:
                        self.skill = 2
                    else: 
                        self.skill = 3  
            
            # AI Control
            if self.AI == 1:
                randomMoves = 0
                attack_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width * self.flip, self.rect.y, 2*self.rect.width, 2*self.rect.height)
                if attack_rect.colliderect(target.rect):
                    randomMoves = random.randint(31,70)
                else:
                    if self.flip:
                        randomMoves = random.randint(0,20)
                    else:
                        randomMoves = random.randint(16,30)
                if target.health <= 0: randomMoves = 17
                if randomMoves >= 0 and randomMoves < 16:
                    dx = -SPEED
                    self.running = True
                elif randomMoves > 15 and randomMoves < 21 and self.canJump:
                    self.gravity = -GRAVITY
                    self.canJump = False
                elif randomMoves > 20 and randomMoves < 31:
                    dx = SPEED
                    self.running = True
                elif randomMoves > 30 and randomMoves < 41 and self.guard_cooldown <= 0:
                    self.guarding = True
                    self.guard_timer = pygame.time.get_ticks()
                else:
                    self.frame_index = 0
                    self.attack(target)
                    if randomMoves > 40 and randomMoves < 51:
                        self.skill = 1
                    elif randomMoves > 50 and randomMoves < 61:
                        self.skill = 2
                    elif randomMoves > 61 and randomMoves < 71:
                        self.skill = 3
        # Gravity
        self.gravity += 5
        dy += self.gravity

        # Screen lock
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > width:
            dx = width - self.rect.right
        if self.rect.top + dy < 0:
            dy = -self.rect.top
        if self.rect.bottom + dy > height*0.9:
            dy = height*0.9 - self.rect.bottom
            self.canJump = True

        self.rect.x += dx
        self.rect.y += dy
        
        if pygame.time.get_ticks() -  self.guard_timer > 2000:
            self.guard_timer = 5000
            self.guarding = False
        if self.guarding == False and self.guard_timer > 0:
            self.guard_timer -= 1000
        if self.attack_cooldown == 0:
            self.push = False
        if self.push == True:
            if self.flip:
                self.rect.x += SPEED * (0.7 - 0.35 * self.canJump)
            else:
                self.rect.x -= SPEED * (0.7 - 0.35 * self.canJump)
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.guard_cooldown > 0:
            self.guard_cooldown -= 1
        # Flip lock
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else: 
            self.flip = True

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.update_action(3)
        elif self.hit:
            self.update_action(5)
        elif self.guarding:
            self.update_action(4)
        elif self.attacking:
            if self.skill == 1:
                self.update_action(0)
            elif self.skill == 2:
                self.update_action(1)
            elif self.skill == 3:
                self.update_action(2)
        elif self.canJump == False:
            self.update_action(7)
        elif self.running: 
            self.update_action(8)
        else: 
            self.update_action(6)

        cooldown = 40
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.health <= 0:
                self.frame_index = len(self.animation_list[3]) - 1
            else:
                self.frame_index = 0
                if self.attacking:
                    self.attacking = False  
                    self.attack_cooldown = 20
                if self.hit:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 20
                    self.push = True

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attack_rect = pygame.Rect(self.rect.centerx - 2 * self.rect.width * self.flip, self.rect.y, 2*self.rect.width, 2*self.rect.height)
            if attack_rect.colliderect(target.rect) and target.guarding == False:
                target.health -= 10   
                target.hit = True      
            elif attack_rect.colliderect(target.rect) and target.guarding == True:
                target.push = True
                self.attack_cooldown = 10
                target.guarding = False
                target.guard_cooldown = 30

    def draw(self, isLeft):
        img = pygame.transform.flip(self.image, self.flip, False)
        self.map.blit(img, (self.rect.x - 248 , self.rect.y - 120))
        