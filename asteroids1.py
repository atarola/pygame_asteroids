#!/usr/bin/env python

import math

import pygame
from pygame.locals import *


class World(object):
    """ contains all of our game state """

    RENDER_OPTIONS = HWSURFACE | DOUBLEBUF | RESIZABLE
    BLACK = (0, 0, 0)

    def __init__(self, size, player):
        # setting up the screen
        self.size = size
        self.surface = pygame.display.set_mode(size, self.RENDER_OPTIONS)
        self.surface.fill(self.BLACK)

        # adding a sprite group
        self.sprites = pygame.sprite.RenderUpdates()
        self.sprites.add(player)

    def render(self):
        """ render the sprites to the window """
        updatedRects = self.sprites.draw(self.surface)
        pygame.display.update(updatedRects)

    def set_size(self, new_size):
        """ set the window size """
        self.size = new_size
        self.surface = pygame.display.set_mode(new_size, self.RENDER_OPTIONS)


class Player(pygame.sprite.Sprite):
    """ represents the player """

    def __init__(self, position):
        super(Player, self).__init__()
        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        self.rect.center = position


def main():
    """ runs our application """

    # setup pygame
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Asteroids 0.1")

    # store our game state
    player = Player((400, 300))
    world = World((800, 600), player)

    # use the clock to throttle the fps to something reasonable
    clock = pygame.time.Clock()

    # main loop
    running = True
    while running:
        events = pygame.event.get()

        # handle our events
        for event in events:
            if event.type == QUIT:
                running = False
                break

            if event.type == VIDEORESIZE:
                world.set_size(event.dict['size'])

        world.render()
        pygame.display.flip()
        clock.tick(40)


if __name__ == "__main__":
    main()
