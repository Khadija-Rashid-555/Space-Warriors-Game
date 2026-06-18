import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Warriors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load Images
background_image = pygame.image.load(r"game background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

spaceship_image = pygame.image.load(r"spacecraft.png")
spaceship_image = pygame.transform.scale(spaceship_image, (200, 70))

asteroid_image = pygame.image.load(r"asteriood.png")
asteroid_image = pygame.transform.scale(asteroid_image, (110, 120))

# Font for text
font = pygame.font.SysFont("Arial", 36)

def start_screen():
    """Display the start screen and wait for the player to press any key."""
    while True:
        screen.fill(BLACK)
        title_text = font.render("SPACE WARRIORS", True, WHITE)
        ready_text = font.render("Are you ready?", True, WHITE)
        start_text = font.render("Press any key to start", True, RED)
        
        screen.blit(title_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(ready_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(start_text, (WIDTH // 2 - 150, HEIGHT // 2))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return  # Exit the start screen and begin the game

def draw_player(x, y):
    screen.blit(spaceship_image, (x, y))

def draw_obstacle(x, y):
    screen.blit(asteroid_image, (x, y))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def Game_Over(score):
    """Display the Game Over screen and handle restart or quit."""
    font = pygame.font.SysFont("Arial", 40)
    while True:
        screen.fill(BLACK)
        game_over_text = font.render("GAME OVER", True, RED)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return  # Restart game
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

# Main game loop
def main_game():
    # Player settings
    player_x = WIDTH // 2
    player_y = HEIGHT - 70
    player_speed = 7

    # Obstacle settings
    obstacle_x = random.randint(50, WIDTH - 50)
    obstacle_y = -50
    obstacle_speed = 7

    # Game variables
    score = 0
    running = True

    while running:
        screen.blit(background_image, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 200:
            player_x += player_speed

        # Move obstacle
        obstacle_y += obstacle_speed

        # Respawn obstacle
        if obstacle_y > HEIGHT:
            obstacle_y = -50
            obstacle_x = random.randint(50, WIDTH - 50)
            score += 1
            obstacle_speed += 0.5  # Increase difficulty

        # Draw player and obstacle
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Show score
        show_score(score)

        # Collision detection
        if (obstacle_x < player_x + 200 and obstacle_x + 110 > player_x and
            obstacle_y < player_y + 70 and obstacle_y + 120 > player_y):
            Game_Over(score)
            return  # Exit game loop to restart

        # Update the screen
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

# Run the game
start_screen()
while True:
    main_game()

