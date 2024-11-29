import pygame


# Class player, the entity controlled by the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_height):
        super().__init__()
        self.li_images = ["Images\Player1.png", "Images\Player2.png", "Images\Player1.png", "Images\Player3.png"]
        for i in range(len(self.li_images)):
            self.li_images[i] = pygame.transform.scale(pygame.image.load(self.li_images[i]), (40, 100))
        self.state_im = 0
        self.image = self.li_images[self.state_im]
        self.rect = self.image.get_rect()
        self.rect.x = self.spawn_x = x
        self.rect.y = self.spawn_y = y
        self.speed = 5
        self.y_velocity = 0
        self.gravity = 0.5
        self.jump_strength = -12
        self.on_ground = False
        self.orientation = "E"
        self.last_dash = 0
        self.mini_dash = 0
        self.screen_height = screen_height
        self.time = pygame.time.get_ticks()

    def spawn(self):
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y

    def update(self):
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        if self.rect.y >= self.screen_height - self.rect.height:
            self.rect.y = self.screen_height - self.rect.height
            self.on_ground = True
            self.y_velocity = 0
        if pygame.time.get_ticks() - self.time > 150:
            self.time = pygame.time.get_ticks()
            self.state_im += 1
            if self.state_im == 4:
                self.state_im = 0
            self.image = self.li_images[self.state_im]



    def jump(self):
        if self.on_ground:
            self.y_velocity = self.jump_strength
            self.on_ground = False

    def dash(self):
        if pygame.time.get_ticks() - self.last_dash >= 1500:
            if self.orientation == "E":
                self.rect.x += 15
            elif self.orientation == "W":
                self.rect.x -= 15
            self.mini_dash += 1
            if self.mini_dash == 10:
                self.last_dash = pygame.time.get_ticks()
        else:
            self.mini_dash = 0
