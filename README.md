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
- XQuartz: http://xquartz.macosforge.org/landing

Now, In a terminal, run this:

    export CC='/usr/bin/gcc'
    export CFLAGS='-isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk -I/opt/X11/include -arch i386 -arch x86_64'
    export LDFLAGS='-arch i386 -arch x86_64'
    export ARCHFLAGS='-arch i386 -arch x86_64'

    brew update
    brew install mercurial sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi
    pip install hg+http://bitbucket.org/pygame/pygame

To verify your install, run:

    python -c 'import pygame'

If there is no output, you're good to go.

## Step 1: Window and main loop.

### Pygame Init

When we first want to run pygame, we need to let SDL setup it's environment.  
This must be done before we do anything else with pygame.

    pygame.init()

Depending on the submodule, you may need to init them too:

    pygame.font.init()

### Windows and Surfaces

In pygame, most of the graphics interactions we'll deal with will be against
pygame `Surface` instances.  The main window and any images we add will be
represented to us as `Surface` instances.

    # image here will be a surface
    image = pygame.image.load('assets/ship.png')

The biggest thing you will do with surfaces is called a `blit`.  An easy way to
think of it is like stamping one image onto another.  This can also be done for
part of the source image, to allow for efficient spritesheets.

To create a Window in pygame, you will call `pygame.display.set_mode`, which
will return you a surface representing the contents of the window.

    # will return a pygame.Surface object
    surface = pygame.display.set_mode((800, 600))

Pygame, by default, double-buffers all of it's graphics input.  There are
actually two surfaces representing the screen under the covers, and pygame will
show one, while allowing you to update the other.  This is done so that the
screen doesn't flicker while executing drawing commands.  

Once your window surface is ready to be presented to the user, a simple
`pygame.display.flip()` will flip the buffer and shown surface, displaying your
updates.

### Events and an Event Loop

The window manager will feed your application information about what is going on
with it via events.  Keypresses, mousemovements, window resizing, and closing are
all given to you via this method.  Unless you pump out all of the events in the
queue, the window manager will consider your application non-responsive, and show
the beach-ball of death, or equivalent.

To grab all of the events that currently exist in the queue:

    # returns a list of pygame.events.Event objects
    events = pygame.event.get()

    for event in events:
        ...

All we need to do now is to loop over the events and handle them appropriately.

If you want to add your own events to the queue, it's pretty easy to do:

    # event data to pass in the queue
    event = pygame.event.Event(USEREVENT, {foo: bar})
    pygame.event.post(event)

### The Clock

The clock object allows us to throttle a loop to a certain fps by sleeping
based on the last time the clock was `tick()`d.  Doing this to our main loop
(discussed below) is important for both saving cpu cycles from the computer
(and battery life) and allowing us to have a sane view of the simulation for
timings and such.

    clock = pygame.time.clock()

    while True:
        print "foo"
        clock.tick(30) # throttle the loop to 30 fps

### Sprites & Sprite Groups

Sprites are a convienent wrapper around both a surface, and a `pygame.Rect`
object.  They implement a `.draw(<pygame.Surface>)` method that will blit the
sprite's surface onto the surface provided to it.  

Sprite Groups are containers for sprites, that will either `.draw()` or
`update()` the sprites contained within in one shot.

## Step 2: Getting the player to move.

### Quick Vector Introduction

### Cleanup Event Handling

### Player Facings

### Moving the Sprites

## Step 3: Asteroids and Bullets

### Adding Bullets

### Adding Asteroids

### Collision Detection

## Step 4: Scene Management

### Creating a Scene System

### Adding a New Game Scene

### Adding a Game Over Scene
