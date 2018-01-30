# Computer Programming 1
# Unit 11 - Graphics
#
# A stormy day


# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

#Images
guinea = pygame.image.load('guinea.png')
hay = pygame.image.load('hay.png')
bedding = pygame.image.load('bedding.png')
hay2 = pygame.image.load('hay2.png')

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BROWN = (84, 43, 5)


def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    screen.blit(guinea, (x, y))

def draw_raindrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, BROWN, rect)

''' Make clouds '''
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)

''' Make rain '''
num_drops = 700
rain = []

for i in range(num_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    drop = [x, y, r, r, stop]
    rain.append(drop)

# Lightning stuff
lightning_prob = 300 # (higher is less frequent)
lightning_timer = 0

# Sound Effects
#pygame.mixer.music.load("sounds/rain.ogg")
#thunder = pygame.mixer.Sound("sounds/thunder.ogg")

# Game loop
#pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    ''' move clouds '''
    for c in far_clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    ''' move rain '''
    for r in rain:
        r[0] -= 1
        r[1] += 4

        if r[1] > r[4]:
            r[0] = random.randrange(0, 1000)
            r[1] = random.randrange(-100, 0)

    ''' flash lighting '''
    if random.randrange(0, 300) == 0:
        lightning_timer = 5
        #thunder.play()
    else:
        lightning_timer -= 1
    
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.blit(hay2, (0, 0))
    else:
        screen.blit(hay, (0, 0))

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    screen.blit(bedding,[0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' clouds '''
    for c in far_clouds:
        draw_cloud(c, NOT_QUITE_DARK_GRAY)

    ''' rain ''' 
    for r in rain:
        draw_raindrop(r)

    ''' clouds '''
    for c in near_clouds:
        draw_cloud(c, DARK_GRAY)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
