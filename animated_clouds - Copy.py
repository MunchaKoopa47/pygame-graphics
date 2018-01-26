# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (32, 58, 29)
GRAY = (48, 48, 48)
BLUE = (12, 32, 66)
YELLOW = (255, 255, 175)
DARKBLUE = (0, 12, 33)

# Make clouds
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GRAY, [x + 20, y + 20, 60, 40])

# Make rain
num_rain = 100
rain = []
for n in range(num_rain):
    x = random.randrange(-10, 810)
    y = random.randrange(-50, 700)
    loc = [x, y]
    rain.append(loc)
    
def draw_rain(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.rect(screen, BLUE, [x, y, 5, 10])
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] += 2

        if c[0] > 900:
           c[0] = random.randrange(-1600, 0)
           c[1] = random.randrange(-50, 200)

    for r in rain:
        r[0] += 3
        r[1] += 10

        if r[1] > 620:
           r[0] = random.randrange(-1, 801)
           r[1] = random.randrange(-10, 0)
             
    # Drawing code
    ''' sky '''
    screen.fill(DARKBLUE)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, GRAY, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, GRAY, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, GRAY, [0, 410], [800, 410], 5)

    ''' rain '''
    for r in rain:
        draw_rain(r)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
