import pygame 

Base_image_path ='data/images/'

def load_image( path):
    img = pygame.image.load(Base_image_path + path).convert()
    img.set_colorkey((0,0,0))
    return img