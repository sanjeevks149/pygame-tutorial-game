import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ninja master")

        self.window = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

        self.image = pygame.image.load("data\images\clouds\cloud_1.png")

        self.pos = [90,50]

        self.movement = [False,False]

    def run(self):
        while True:
            self.window.blit(self.image, self.pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key ==  pygame.K_DOWN:
                        self.movement[1] = False
            pygame.display.update()
            self.clock.tick(60)

Game().run()