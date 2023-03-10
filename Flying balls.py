import pygame, sys, math, random

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1200, 800
COLORS = ['lightblue', 'aqua', 'white', 'royalblue', 'pink', 'lightsalmon', 'lightcyan', 'springgreen', 'lemonchiffon' ]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
dots = []
timer = 0

def bubbles(x, y):
    random_colors = [random.choice(COLORS) for _ in range(3)]
    for _ in range(25):
        dots.append({'x': x, 'y': y,
                     'x_change': random.uniform(-1, 1),
                     'y_change': random.uniform(-1, 1),
                     'size': random.randint(1, 9),
                     "speed_x": random.uniform(0.2, 0.5),
                     "speed_y": random.uniform(0.2, 0.5),
                     'color': random.choice(random_colors),
                     'tail': [],
                     'life_time': 1
                     })

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x, position_y = pygame.mouse.get_pos()
            bubbles(position_x, position_y)

    if timer % 150 == 0 and len(dots) < 500:
        random_position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        bubbles(*random_position)

    for dot in dots:
        if dot['life_time'] % int(150 - (dot['speed_x'] + dot['speed_y']) * 100) == 0:
            if len(dot['tail']) > 5:
                del dot['tail'][0]
            dot['tail'].append((dot['x'], dot['y']))
        dot['x'] += dot['x_change'] * dot['speed_x']
        dot['y'] += dot['y_change'] * dot['speed_y'] + (dot['life_time'] / 2000) * dot['size'] / 5
        pygame.draw.circle(screen, dot['color'], (dot['x'], dot['y']), dot['size'], dot['size'] // 2)
        for closeness, tail_elem in enumerate(dot['tail'][::-1]):
            pygame.draw.circle(screen, dot['color'], tail_elem, dot['size'] - closeness, math.floor(dot['size'] // 2))
        dot['life_time'] += 1

    dots = [x for x in dots if x['y'] < (HEIGHT + 500)]
    pygame.display.flip()
    timer += 1
    clock.tick(120)

