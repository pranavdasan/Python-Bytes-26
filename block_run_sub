import pygame

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game variables
fps = 60
clock = pygame.time.Clock()
gravity = 10/fps

# Player variables
player_size = 30
player_x = 50
player_y = SCREEN_HEIGHT - player_size - 20
player_velocity_y = 0
player_color = (255, 0, 0)

# Ground variables
ground_height = 20
ground_y = SCREEN_HEIGHT - ground_height
ground_color = (0, 255, 0)

# Obstacles variabels
obstacle_width = 20
obstacle_height = 30
obstacle_x = SCREEN_WIDTH # Spawn off screen
obstacle_speed = 2


# Game loop
running = True

while running:
  # Clear screen/make it white
  screen.fill((255, 255, 255))
  
  # Check events
  for event in pygame.event.get():
      # Check if event is a quit event
      if event.type == pygame.QUIT:
        running = False
  
  # Find keys being pressed
  keys = pygame.key.get_pressed()
  
  if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and (player_y + player_size == ground_y):
    player_velocity_y = -6

  player_velocity_y += gravity # Apply gravity
  
  # Check ground collision
  if player_y + player_size > ground_y:
    player_velocity_y = 0
    player_y = ground_y - player_size # Set player on ground
    
  #Check if above ground
  if player_y + player_size <= ground_y:
    player_y += player_velocity_y   # Update player position
  
  obstacle_x -= obstacle_speed # Update obstacle position
  
  # Reset obstalce when it goes off screen
  if obstacle_x + obstacle_width < 0:
    obstacle_x = SCREEN_WIDTH
  
  # Create player
  player = pygame.Rect(player_x, player_y, player_size, player_size)
  
  
  # Create ground
  ground = pygame.Rect(0, ground_y, SCREEN_WIDTH, ground_height)
  
  # Create obstacle
  obstacle = pygame.Rect(obstacle_x, ground_y-obstacle_height, obstacle_width, obstacle_height)
  
  # Detect obstacle collision
  if player.colliderect(obstacle):
    running = False # Game over
  
  
  # Draw player
  pygame.draw.rect(screen, player_color, player)
  
  # Draw ground
  pygame.draw.rect(screen, ground_color, ground)
  
  # Draw obstacle
  pygame.draw.rect(screen, (0, 0, 255), obstacle)
  
  # Refresh screen
  pygame.display.update()
  clock.tick(fps) # Sets fps

pygame.quit()
  
  
  
