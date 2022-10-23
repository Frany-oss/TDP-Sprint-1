from pygame.math import Vector2
import sys, pygame, time

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

a = Vector2(200, -100)
b = Vector2(200, 100)
c = a - b # or Vector2(0, -200)
alpha = a.angle_to(b)

points = list(map(Vector2, [(100, 100), (200, 100), (300, 100), (400, 100), (500, 100)]))
target = Vector2(550, 400)

rel_points = []
angles = []

for i in range(1, len(points)):
    rel_points.append(points[i] - points[i-1])
    angles.append(0)

def solve_invers_kinematics(i, endpoint, target):
    if i < len(points) - 2:
        endpoint = solve_invers_kinematics(i+1, endpoint, target)
    current_point = points[i]

    angle = (endpoint - current_point).angle_to(target - current_point)
    angles[i] += angle

    return current_point + (endpoint - current_point).rotate(angle)


def render():
    black = 0, 0, 0
    white = 255, 255, 255

    screen.fill(white)

    for i in range(1, len(points)):
        prev = points[i - 1]
        cur = points[i]
        pygame.draw.aaline(screen, black, prev, cur)

    for point in points:
        pygame.draw.circle(screen, black, (int(point[0]), int(point[1])), 5)
    pygame.draw.circle(screen, black, (int(target[0]), int(target[1])), 10)

    pygame.display.flip()

while True:
    time.sleep(0.0666) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    solve_invers_kinematics(0, points[-1], target)


    angle = 0
    for i in range(1, len(points)):
        angle += angles[i - 1]
        points[i] = points[i - 1] + rel_points[i - 1].rotate(angle)

    render()
    pygame.time.wait(int(1000/60))


