#!/usr/bin/env python

import pygame
from pygame.locals import *


class Window(object):
    """ stash away our window """

    RENDER_OPTIONS = HWSURFACE | DOUBLEBUF | RESIZABLE
    BLACK = (0, 0, 0)

    def __init__(self, size):
        self.size = size
        self.surface = pygame.display.set_mode(size, self.RENDER_OPTIONS)
        self.surface.fill(self.BLACK)

    def set_size(self, new_size):
        self.size = new_size
        self.surface = pygame.display.set_mode(new_size, self.RENDER_OPTIONS)


def main():
    """ runs our application """

    # setup pygame
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Asteroids 0.1")

    # store our game state
    world = {
        "window": Window()
    }

    # use the clock to throttle the fps to something reasonable
    clock = pygame.time.Clock()

    # main loop
    running = True
    while running:
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                running = False
                break

            if event.type == VIDEORESIZE:
                world['window'].set_size(event.dict['size'])

        pygame.display.flip()
        clock.tick(40)


if __name__ == "__main__":
    main()
