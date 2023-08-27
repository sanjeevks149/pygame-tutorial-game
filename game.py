import sys
import pygame
from scripts.entities import PhysicsEntities

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ninja master")

        self.window = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

        self.player = PhysicsEntities(self, 'player',(50,50),(8,15))

    def run(self):
        while True:
            self.window.fill((0,0,0))

            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key ==  pygame.K_DOWN:
                        self.movement[1] = False
            

            pygame.display.update()
            self.clock.tick(60)

Game().run()