# game options / settings
TITLE = "Jumpy!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 20

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 15
MOD_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0
GAME_SCREEN_SOUND_VOLUME = 0.1
GAME_MUSIC_SOUND_VOLUME = 0.5
GAME_SOUND_VOLUME = 0.2

# starting platforms
PLATFORM_LIST = [
    (0, HEIGHT - 60),
    (WIDTH / 2 - 50, HEIGHT * 3 / 4),
    (125, HEIGHT - 350),
    (350, 200),
    (175, 100)
]

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 255)
BGCOLOR = LIGHTBLUE