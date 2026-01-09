# import sys
# import pygame  # type: ignore
# from settings import Settings
# from ship import Ship

# class AlienInvasion:
#     """   """
#     def __init__(self):
#         pygame.init()
#         self.settings=Settings()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width,self.settings.screen_height)
#         )
        
#         # self.screen = pygame.display.set_mode((1200,800))
#         pygame.display.set_caption("Alien Invasion")
        
#         self.ship=Ship(self)
        
#         # self.bg_color = (230,230,230)
#         self.screen.fill(self.settings.bg_color)
#         self.ship.blitme()
        
#     def run_game(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.OUIT:
#                     sys.exit()
                    
#             self.screen.fill(self.bg_color)
                    
#             pygame.display.flip()
            
            
# if __name__=='__main__':
#     ai=AlienInvasion()
#     ai.run_game()


import sys
import pygame  # type: ignore
from settings import Settings
from ship import Ship

class AlienInvasion:
    """O'yin asosiy klassi – invaziya o'yini."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()  # Katta harf emas, lekin Python case-sensitive
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """O'yin asosiy tsikli."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Tuzatildi: OUIT → QUIT
                    pygame.quit()  # Qo'shildi: toza yopish
                    sys.exit()
            
            # Ekran tozalash va chizish
            self.screen.fill(self.settings.bg_color)  # Tuzatildi: self.bg_color → self.settings.bg_color
            self.ship.blitme()  # Qo'shildi: har kadrda ship chizish
            
            pygame.display.flip()  # Ekran yangilash

if __name__ == '__main__':  # Kichik harf, to'g'ri
    ai = AlienInvasion()
    ai.run_game()