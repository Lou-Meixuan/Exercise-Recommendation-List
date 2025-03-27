import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.text_surf = font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surf, self.text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exercise Recommendation")
font = pygame.font.SysFont(None, 40)

button_color = (0, 128, 255)
text_color = (255, 255, 255)
button_rect = pygame.Rect(300, 250, 200, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check click button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("")
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()

