import pygame 

pygame.init()

# Screen Size
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Ground variables
ground_height = 20
ground_y = SCREEN_HEIGHT - ground_height

# Game Variables
fps = 60
player_size = 30
player_x = 30
player_y = SCREEN_HEIGHT - player_size - ground_height
player_y_velocity = 0
gravity = 10/fps

# Obstacle variables
obstacle_width = 30
obstacle_height = 30
obstacle_x = SCREEN_WIDTH # Spawns obstacles off screen
obstacle_speed = 2



running = True

# Initialize clock
clock = pygame.time.Clock()

while running:
    # Clear screen
    screen.fill((255, 255, 255))

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Find keys being pressed
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_SPACE] or keys[pygame.K_w]):
        player_y_velocity = -6 

    # Apply gravity
    player_y_velocity += gravity

    # Move obstacle
    obstacle_x -= obstacle_speed
    
    # Make player hitbox
    player = pygame.Rect(player_x,player_y, player_size, player_size)

    # Make ground hitbox
    ground = pygame.Rect(0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height)

    # Make obstacle hitbox
    obstacle = pygame.Rect(obstacle_x, ground_y - obstacle_height, obstacle_width, obstacle_height)

    if player_y + player_size > ground_y:
        player_y_velocity = 0
        player_y = ground_y - player_size

    if player.colliderect(obstacle):
        running = False 

    player_y += player_y_velocity

   
    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), player)

    #Draw ground
    pygame.draw.rect(screen, (0, 255, 0), ground)

    # Draw obstacle
    pygame.draw.polygon(screen, (0, 0, 255), [
        (obstacle_x, ground_y),
        (obstacle_x+obstacle_width/2, ground_y - obstacle_height),
        (obstacle_x + obstacle_width, ground_y)
    ])

    pygame.display.update()
    clock.tick(fps) # Sets FPS


pygame.quit() # Quits pygame