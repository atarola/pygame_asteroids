#!/usr/bin/env python

import math

import pygame
from pygame.locals import *


class World(object):
    """ contains all of our game state """

    RENDER_OPTIONS = HWSURFACE | DOUBLEBUF | RESIZABLE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, size, player):
        # setting up the screen
        self.size = size
        self.surface = pygame.display.set_mode(size, self.RENDER_OPTIONS)
        self.surface.fill(self.BLACK)

        # adding a sprite group
        self.sprites = pygame.sprite.RenderUpdates()
        self.sprites.add(player)

    def update(self):
        self.sprites.update()

    def render(self):
        """ render the sprites to the window """
        def clear_callback(surface, rect):
            surface.fill(self.BLACK, rect)

        self.sprites.clear(self.surface, clear_callback)
        updatedRects = self.sprites.draw(self.surface)
        pygame.display.update(updatedRects)

    def set_size(self, new_size):
        """ set the window size """
        self.size = new_size
        self.surface = pygame.display.set_mode(new_size, self.RENDER_OPTIONS)


class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnatude(self):
        """ return the magnatude (aka: distance) this vector represents """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        """ return a unit vector """
        return self / self.magnatude()

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        return Vector(x, y)

    def __div__(self, n):
        x = self.x / n
        y = self.y / n
        return Vector(x, y)

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def to_position(self):
        return (self.x, self.y)

    def to_radians(self):
        radians = math.atan2(self.x, self.y)
        return (radians, self.magnatude())

    def to_degrees(self):
        radians, magnatude = self.to_radians()
        return (math.degrees(radians), magnatude)

    @classmethod
    def from_position(self, position):
        return Vector(position[0], position[1])

    @classmethod
    def from_radians(self, radians, magnatude=1):
        return Vector(math.sin(radians), math.cos(radians)) * magnatude

    @classmethod
    def from_degrees(self, degrees, magnatude=1):
        return Vector.from_radians(math.radians(degrees), magnatude)


class Player(pygame.sprite.Sprite):
    """ represents the player """

    def __init__(self, position):
        super(Player, self).__init__()
        self.orig_image = pygame.image.load('assets/ship.png')

        # setup pygames rendering
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.rect.center = position

        # handle our motion
        self.motion = Vector(0, 0)
        self.facing = Vector.from_degrees(90)
        self.forward = False
        self.backward = False

    def update(self):
        # if we are thrusting, add the vector of our facing to the motion
        if self.forward:
            self.motion = self.motion - self.facing

        if self.backward:
            self.motion = self.motion + self.facing

        # modify the ships position by it's motion
        current = Vector.from_position(self.rect.center) + self.motion

        # rotate our sprite to match our direction, and put it in the right place
        degrees, _ = self.facing.to_degrees()
        self.image = pygame.transform.rotate(self.orig_image, degrees)
        self.rect = self.image.get_rect()
        self.rect.center = current.to_position()

    def turn_left(self):
        degrees, _ = self.facing.to_degrees()
        degrees = (degrees + 10) % 360
        self.facing = Vector.from_degrees(degrees)

    def turn_right(self):
        degrees, _ = self.facing.to_degrees()
        degrees = (degrees - 10) % 360
        self.facing = Vector.from_degrees(degrees)


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

            if (event.type == KEYDOWN) and (event.key == K_UP):
                player.forward = True

            if (event.type == KEYDOWN) and (event.key == K_DOWN):
                player.backward = True

            if event.type == KEYUP:
                if event.key in (K_UP, K_DOWN):
                    player.forward = False
                    player.backward = False

                if event.key == K_LEFT:
                    player.turn_left()

                if event.key == K_RIGHT:
                    player.turn_right()

        world.update()
        world.render()
        pygame.display.flip()
        clock.tick(40)


if __name__ == "__main__":
    main()
