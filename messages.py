import pygame

class messages:
    
    def draw(self, message, apple_count, screen, width, height):
        font = pygame.font.Font(None, 50)
        text = font.render(message + " Apple Count: " + str(apple_count), True, (255,0,0))
        screen.blit(text, [width//2-150, height//2])
        pygame.display.flip()