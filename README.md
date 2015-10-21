# Pygame asteroids

This repo contains a set of steps to go from 0 to asteroids in simple steps.

- Create a pygame screen that can be closed.
- Add a player to the screen.
- Get the player to move.
- Asteroids & Bullets
- Scoring and Text

## Step 0: Install Pygame

### Windows

Ensure you have the NON-64 bit version of python
Download the package from: http://www.pygame.org/download.shtml for the version of python that you have

### Linux

Fetch from your package manager

### OSX

First, install Homebrew and XQuartz:

- Ensure you have installed Xcode and it is up to date
- Homebrew: http://brew.sh/
  - After installation run `brew update`
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

### Pygame Init

### Windows and Surfaces

### Events and an Event Loop

### Sprites & Sprite Groups

## Step 3: Getting the player to move.

### Quick Vector Introduction

### Cleanup Event Handling

### Player Facings

### Moving the Sprites

## Step 4: Asteroids and Bullets

### Adding Asteroids

### Adding Bullets

### Collision Detection

## Step 5: Scene Management

### Creating a Scene System

### Adding a New Game Scene

### Adding a Game Over Scene
