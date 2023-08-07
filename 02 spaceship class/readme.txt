DOCUMENTATION

MAIN.PY
------------
In this file the class GAME controls the display, the quit button and ipdates the sprites,
that are the collection of the squares that formes the ship.
Initialize pygame,
calls ship_init()


Classes: Game [methods; quit update_display update ]
Functions: None
Attributes: [clock, frame]



SHIP.PY
----------
THis classe creates the ship, made of 4 surfaces istances of this class,
defined in the ship_init() function

Classes: Ship [methods: update colorvariation pulsar]
Functions: ship_init()
Attributes: [ sprites, screen]