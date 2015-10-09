# Pygame asteroids

This repo contains a set of steps to go from 0 to asteroids in simple steps.

- Create a pygame screen that can be closed.
- Add a player to the screen.
- Get the player to move.
- Asteroids & Bullets
- Scoring and Text

## Step 0: Install Pygame

### Windows

Download the package from: http://www.pygame.org/download.shtml

### Linux

Fetch from your package manager

### OSX

First, install Homebrew and XQuartz:

- Homebrew: http://brew.sh/
- XQuartz: http://xquartz.macosforge.org/landing

Now, In a terminal, run this:

    export CC='/usr/bin/gcc'
    export CFLAGS='-isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk -I/opt/X11/include -arch i386 -arch x86_64'
    export LDFLAGS='-arch i386 -arch x86_64'
    export ARCHFLAGS='-arch i386 -arch x86_64'

    brew install mercurial sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi
    pip install hg+http://bitbucket.org/pygame/pygame

To verify your install, run:

    python -c 'import pygame'

If there is no output, you're good to go.

## Step 1: Window and main loop.

Windows, surfaces, events, and clocks. Resizing the screen.

## Step 2: Add a player to the screen.

Pygame sprite groups and sprites.

## Step 3: Getting the player to move.

Newtonian Physics and vectors!

## Step 4: Asteroids and Bullets

Sprites, Collision Detection, and such.
