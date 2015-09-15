#!/usr/bin/env python

import sys
import sdl2
import sdl2.ext

# setup our window
sdl2.ext.init()
window = sdl2.ext.Window("Asteroids!", size=(800, 600))
window.show()

# main loop
running = True
while running:

    # if there are any events, process them
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

    sdl2.SDL_Delay(10)
