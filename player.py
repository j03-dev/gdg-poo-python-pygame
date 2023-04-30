import pygame
# Mere
class ObjetAnimer:
    def __init__(self, x, y, v, assets):
        self._position_x = x
        self._position_y = y
        self._vitesse = v
        self._assets = assets
        self.current_image = 0

    def go_left(self):
        self._position_x -= self._vitesse

    def go_right(self):
        self._position_x += self._vitesse

    def s_afficher(self, screen):
        if self.current_image < len(self._assets):
            screen.blit(self._assets[int(self.current_image)], (self._position_x, self._position_y))
        else:
            self.current_image = 0

    def s_animer(self):
        self.current_image = (self.current_image + 0.1) % len(self._assets)

# Fille
class Player(ObjetAnimer):
    def __init__(self, x, y, v, assests):
        super().__init__(x, y, v, assests)
        self.assets_right = self._assets.copy()
        self.assets_left = list(map(self.flip, self._assets))

    def go_right(self):
        self._position_x += self._vitesse
        self._assets = self.assets_right 

    def go_left(self):
        self._position_x -= self._vitesse
        self._assets = self.assets_left 

    def flip(self, image):
        return pygame.transform.flip(image, True, False)