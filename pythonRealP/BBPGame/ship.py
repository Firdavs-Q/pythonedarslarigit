# import pygame # type: ignore

# class Ship:
#     def __init__(self,ai_game):
#         self.screen = ai_game.screen
#         self.screen_rect = ai_game.screen.get_rect()
        
        
#         self.image = pygame.image.load('./images/ship.bmp')
#         self.rect = self.image.get_rect()
        
#         self.rect.midbottom = self.screen_rect.midbottom
        
#     def blitme(self):
#         self.screen.blit(self.image,self.rect)
        
import pygame  # type: ignore

class Ship:
    """Kema (ship) klassi."""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Haqiqiy image:
        self.image = pygame.image.load('./images/s.bmp')
        # Test uchun oddiy surface (oq to'rtburchak, 60x40)
        # self.image = pygame.Surface((60, 40))
        # self.image.fill((255, 255, 255))  # Oq rang
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)