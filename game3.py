import pygame
import random

# Inicialización
pygame.init()
WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10
BLOCK_SIZE = WIDTH // COLS
FPS = 60

COLORS = [
    (255, 85, 85),   # Rojo
    (100, 200, 115), # Verde
    (120, 108, 245), # Azul
    (255, 140, 50),  # Naranja
    (50, 220, 220),  # Cyan
    (255, 255, 85),  # Amarillo
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Collapse 💥")
clock = pygame.time.Clock()

grid = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]
particles = []

class ExplosionParticle:
    def __init__(self, x, y, color):
        self.x = x * BLOCK_SIZE + BLOCK_SIZE // 2
        self.y = y * BLOCK_SIZE + BLOCK_SIZE // 2
        self.radius = 2
        self.color = color
        self.life = 30
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.radius += 0.5
        self.life -= 1

    def draw(self, surface):
        if self.life > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            color = grid[y][x] if grid[y][x] else (30, 30, 30)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

def get_connected(x, y, color, visited):
    if x < 0 or x >= COLS or y < 0 or y >= ROWS:
        return []
    if (y, x) in visited or grid[y][x] != color:
        return []
    visited.add((y, x))
    group = [(y, x)]
    group += get_connected(x+1, y, color, visited)
    group += get_connected(x-1, y, color, visited)
    group += get_connected(x, y+1, color, visited)
    group += get_connected(x, y-1, color, visited)
    return group

def eliminate_group(group):
    for y, x in group:
        color = grid[y][x]
        grid[y][x] = None
        for _ in range(6):
            particles.append(ExplosionParticle(x, y, color))

def apply_gravity():
    for x in range(COLS):
        stack = [grid[y][x] for y in range(ROWS) if grid[y][x]]
        missing = ROWS - len(stack)
        new_blocks = [random.choice(COLORS) for _ in range(missing)]
        stack = new_blocks + stack
        for y in range(ROWS):
            grid[y][x] = stack[y]

def main():
    running = True
    while running:
        screen.fill((10, 10, 30))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x = mx // BLOCK_SIZE
                y = my // BLOCK_SIZE
                if grid[y][x]:
                    color = grid[y][x]
                    group = get_connected(x, y, color, set())
                    if len(group) >= 3:
                        eliminate_group(group)
                        apply_gravity()

        draw_grid()

        for p in particles[:]:
            p.update()
            p.draw(screen)
            if p.life <= 0:
                particles.remove(p)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()