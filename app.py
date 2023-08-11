import pygame
import time
import random

pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Define snake characteristics
BLOCK_SIZE = 20
SNAKE_SPEED = 5

# Create the game display
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Define the Snake function
def snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, GREEN, [block[0], block[1], block_size, block_size])

# Define the game loop
def game_loop():
    game_exit = False
    game_over = False

    # Initial snake position
    lead_x = SCREEN_WIDTH / 2
    lead_y = SCREEN_HEIGHT / 2

    # Initial snake movement
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Generate random food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    clock = pygame.time.Clock()

    while not game_exit:
        while game_over:
            game_display.fill(BLACK)
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over", True, RED)
            game_display.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(BLACK)

        # Draw the food
        pygame.draw.rect(game_display, BLUE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Snake mechanics
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        snake(BLOCK_SIZE, snake_list)

        pygame.display.update()

        # Check if the snake ate the food
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()