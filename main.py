import pygame
from pygame.locals import *
from OpenGL.GL import *


def draw_line():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # Red color

    glVertex2f(-0.5, 0.0)  # Start of the line
    glVertex2f(0.5, 0.0)  # End of the line

    glEnd()

    pygame.display.flip()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_line()


if __name__ == "__main__":
    main()
