import pygame
from player import ObjetAnimer, Player

LONGEUR = 700
LARGEUR = 700
titre = "POO partie 2"
COULEUR = (0, 0, 0) 

pygame.init()
pygame.display.set_caption(titre)
screen = pygame.display.set_mode((LONGEUR, LARGEUR))
running = True

list_assets = [pygame.image.load(f'player/run-{i}.png') for i in range(1, 9)]

objet_animer = Player(LONGEUR // 2, LARGEUR // 2, 1, list_assets)

while running:
    screen.fill(COULEUR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    objet_animer.s_afficher(screen)

    if keys[pygame.K_LEFT]:
        objet_animer.go_left()    
        objet_animer.s_animer()
    
    elif keys[pygame.K_RIGHT]:
        objet_animer.go_right()    
        objet_animer.s_animer()

    pygame.display.update()

pygame.quit()