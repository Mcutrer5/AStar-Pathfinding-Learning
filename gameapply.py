import pygame
import random
import heapq

WIDTH = 500
HEIGHT = 500
GRID_SIZE = 100
OBSTACLE_PROBABILITY = 0.2
BLOCK_SIZE = 50
GRID_SIZE = 10
NUM_OBSTACLES = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)



class Node:
    def __init__(self, x, y, cost, parent):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def generate_map():
    map = []
    for i in range(GRID_SIZE):
        map.append([])
        for j in range(GRID_SIZE):
            if random.random() < OBSTACLE_PROBABILITY:
                map[i].append(1)
            else:
                map[i].append(0)
    return map

def get_neighbors(x, y, map):
    neighbors = []
    # The and here is to make sure we don't go out of bounds or hit an obstacle
    if x > 0 and map[x - 1][y] == 0:
        neighbors.append((x - 1, y))
    if x < GRID_SIZE - 1 and map[x + 1][y] == 0:
        neighbors.append((x + 1, y))
    if y > 0 and map[x][y - 1] == 0:
        neighbors.append((x, y - 1))
    if y < GRID_SIZE - 1 and map[x][y + 1] == 0:
        neighbors.append((x, y + 1))
    return neighbors

def neighbors(node, map):
    x, y = node
    results = []
    if x > 0 and map[x - 1][y] != 1:
        results.append((x - 1, y))
    if x < GRID_SIZE - 1 and map[x + 1][y] != 1:
        results.append((x + 1, y))
    if y > 0 and map[x][y - 1] != 1:
        results.append((x, y - 1))
    if y < GRID_SIZE - 1 and map[x][y + 1] != 1:
        results.append((x, y + 1))
    return results

def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(start, goal, map):
    heap = []
    heapq.heappush(heap, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while heap:
        current = heapq.heappop(heap)[1]

        if current == goal:
            print("Found path: ", current)
            break

        for next_node in neighbors(current, map):
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                print("Adding to heap: ", next_node, " with cost: ", new_cost)
                priority = new_cost + heuristic(goal, next_node)
                heapq.heappush(heap, (priority, next_node))
                came_from[next_node] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def draw_grid(screen, map, start, goal, came_from, path):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if map[x][y] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
                
            pygame.draw.rect(screen, BLACK, rect, 1)

    for node in came_from:
        x, y = node
        if came_from[node] is not None:
            x2, y2 = came_from[node]
            if (x2, y2) in path and (x, y) in path:
                pygame.draw.line(screen, PURPLE, (x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2),
                                 (x2 * BLOCK_SIZE + BLOCK_SIZE // 2, y2 * BLOCK_SIZE + BLOCK_SIZE // 2), 2)
            else:
                pygame.draw.line(screen, GREEN, (x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2),
                                 (x2 * BLOCK_SIZE + BLOCK_SIZE // 2, y2 * BLOCK_SIZE + BLOCK_SIZE // 2), 2)

    rect = pygame.Rect(start[0] * BLOCK_SIZE, start[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, BLUE, rect)
    rect = pygame.Rect(goal[0] * BLOCK_SIZE, goal[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, RED, rect)
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Generate a random map with obstacles
    map = generate_map()

    # Set start and goal nodes
    start = (0, 0)
    goal = (GRID_SIZE - 1, GRID_SIZE - 1)

    came_from, cost_so_far = a_star(start, goal, map)
    path = reconstruct_path(came_from, start, goal)
    print("Path: ", path)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        draw_grid(screen, map, start, goal, came_from, path)
        pygame.display.update()

if __name__ == "__main__":
    main()