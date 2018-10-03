import pygame
from settings import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        """Set up our player"""
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = vec(WIDTH/2, HEIGHT - 20)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = self.rect.center

        self.timer = 0
        self.rTimes = 1

        self.leftButton = pygame.K_LEFT
        self.rightButton = pygame.K_RIGHT
        self.killTime = 10

    def jump(self):
        """Jump only when on the ground"""
        #Check if player is grounded
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            if not self.kill():
                self.vel.y = PLAYER_JUMP_VEL

    def input(self):
        keys = pygame.key.get_pressed()

        self.acc = vec(0, PLAYER_GRAV)  # Setting Player Gravity

        if keys[self.leftButton]:
            # Move Left
            self.acc.x = -PLAYER_ACC

        if keys[self.rightButton]:
            # Move Right
            self.acc.x = PLAYER_ACC



    def update(self, dt):
        """Update the player"""
        self.acc = vec(0, PLAYER_GRAV) #Setting Player Gravity

        self.input()
        self.kill()
        self.timer_inc(dt)


        #Apply Physics
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #Set Position
        self.rect.midbottom = self.pos

        if self.rect.left - 10 > WIDTH:
            self.pos.x = 0
        if self.rect.right + 10 < 0:
            self.pos.x = WIDTH


    def kill(self):
        """kill the player if they move for too long"""
        if self.timer > self.killTime:
            self.image.fill(RED)
            self.acc = vec(0, PLAYER_GRAV)
            return True
        return False

    def timer_inc(self, dt):
        """increase timer"""
        if self.vel.x > 1:
            self.timer += 1 * dt
        if self.vel.x < -1:
            self.timer += 1 * dt