import pygame

# Ensure we're using pygame 2 or higher
print(f"Pygame version: {pygame.ver}")

# Create a valid vector and scale it
vector = pygame.Vector2(3, 4)  # A vector with magnitude 5
print(f"Original vector: {vector}, magnitude: {vector.length()}")

# Attempt to scale it
try:
    vector.scale_to_length(10)
    print(f"Scaled vector: {vector}, magnitude: {vector.length()}")
except Exception as e:
    print(f"Error scaling vector: {e}")