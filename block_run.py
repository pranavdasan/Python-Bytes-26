import pygame
import math
import random
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Game Variables
fps = 60
player_size = 30
player_x = 50
player_y = SCREEN_HEIGHT - player_size - 20
player_velocity_y = 0
gravity = 10/fps
score = 0

# Obstacle Variables
obstacle_width = 30
obstacle_height = 30
obstacle_x = SCREEN_WIDTH # Spawn the obstacle off screen
obstacle_speed = 2 
obstacle_type = "SINGLE"
possible_types = ["SINGLE", "DOUBLE", "TALL"]

# Ground variables
ground_height = 20
ground_y = SCREEN_HEIGHT - ground_height

# Load font
font = pygame.font.Font(None, 36)

# Game loop
running = True

# Initialize clock
clock = pygame.time.Clock()

while running:
    # Clear screen
    screen.fill((255, 255, 255))
 
    # Check events
    for event in pygame.event.get():
       # Check if event is a quit event
       if event.type == pygame.QUIT:
           running = False

    # Find keys being pressed
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and player_y+player_size == ground_y:
        player_velocity_y = -6
    
    player_velocity_y += gravity

    # Collisions
    if player_y + player_size > ground_y:
        player_velocity_y = 0
        player_y = ground_y - player_size

    # Update player posistion
    if player_y + player_size <= ground_y:
        player_y += player_velocity_y
    
    # Update obstacle speed
    obstacle_speed = -3 + 20 / (1+math.e ** (-0.1 * (score - 10)))


    # Update obstacle posistion
    obstacle_x -= obstacle_speed

    # Reset obstacle when it goes off screen
    if obstacle_x + obstacle_width < 0:
        obstacle_x = SCREEN_WIDTH # Puts it back to right of screen
        score += 1 # Update score
        obstacle_type = random.choices(possible_types, weights=[0.5, 0.3, 0.2], k=1)[0]
        

    # Create obstacle hitbox, different type, different hitbox
    if obstacle_type == "SINGLE":
        obstacle = pygame.Rect(obstacle_x, ground_y - obstacle_height, obstacle_width, obstacle_height)
    elif obstacle_type == "DOUBLE":
        obstacle = pygame.Rect(obstacle_x-obstacle_width, ground_y - obstacle_height, 2*obstacle_width, obstacle_height*2)
    elif obstacle_type == "TALL":
        obstacle = pygame.Rect(obstacle_x, ground_y - 2*obstacle_height, obstacle_width, 2*obstacle_height)

    # Create player hitbox
    player = pygame.Rect(player_x, player_y, player_size, player_size)

    # Detect obstacle collision
    if player.colliderect(obstacle):
        running = False # Game over
 
    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Draw obstacle(s)
    if obstacle_type == "SINGLE":
        pygame.draw.polygon(screen, (0, 0, 255), [
            (obstacle_x, ground_y),
            (obstacle_x + obstacle_width/2,  ground_y - obstacle_height), 
            (obstacle_x + obstacle_width, ground_y)])
    elif obstacle_type == "DOUBLE":
        pygame.draw.polygon(screen, (0, 0, 255), [
          (obstacle_x, ground_y),
          (obstacle_x + obstacle_width / 2, ground_y - obstacle_height),
          (obstacle_x + obstacle_width, ground_y)
        ])
        
        pygame.draw.polygon(screen, (0, 0, 255), [
          (obstacle_x-obstacle_width, ground_y),
          (obstacle_x + obstacle_width / 2 - obstacle_width, ground_y - obstacle_height),
          (obstacle_x, ground_y)
        ])
    elif obstacle_type == "TALL":
        pygame.draw.polygon(screen, (0, 0, 255), [
            (obstacle_x, ground_y),
            (obstacle_x + obstacle_width/2,  ground_y - 2*obstacle_height), 
            (obstacle_x + obstacle_width, ground_y)])

    # Draw ground
    pygame.draw.rect(screen, (0, 255, 0), (0, ground_y, SCREEN_WIDTH, ground_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))

    # Refresh Screen
    pygame.display.update()
    clock.tick(fps) # Set FPS

pygame.quit()

