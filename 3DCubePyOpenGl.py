import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (800, 600)
pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)
pygame.display.set_caption('Random 3D Cube')

# Define the cube's vertices
vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

# Define the cube's edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Main rendering loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Rotate the cube randomly
    glRotatef(random.uniform(0, 1), 1, 0, 0)
    glRotatef(random.uniform(0, 1), 0, 1, 0)
    glRotatef(random.uniform(0, 1), 0, 0, 1)

    # Draw the cube
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)
