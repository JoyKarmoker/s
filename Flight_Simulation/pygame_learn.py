# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

pos = [(700, 400), (725, 450), (750, 500), (775, 475), (200, 200), (900, 400), (775, 475)]
index = 0
length = len(pos) - 1
print(length)
keys_pressed = 0
# bomber_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
bomber_pos = pygame.Vector2(pos[0][0], pos[0][1])
fighter_pos = pygame.Vector2(80, 100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys_pressed += 1
            if keys_pressed >= length:
                running = False
            index = index + 1
            print('index: ', index)
            print('Keys Pressed: ', keys_pressed)
            bomber_pos = pygame.Vector2(pos[index][0], pos[index][1])

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", bomber_pos, 40)
    pygame.draw.circle(screen, "green", fighter_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
