# Configurazione del gioco Pac-Man

# Dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Dimensioni delle celle del labirinto
CELL_SIZE = 20
MAZE_WIDTH = SCREEN_WIDTH // CELL_SIZE
MAZE_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Colori (RGB)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 184, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 184, 82)
GREEN = (0, 255, 0)

# Colori dei fantasmi
GHOST_COLORS = {
    'blinky': RED,      # Rosso
    'pinky': PINK,      # Rosa
    'inky': CYAN,       # Ciano
    'clyde': ORANGE     # Arancione
}

# Velocità dei personaggi
PACMAN_SPEED = 2
GHOST_SPEED = 1.5
SCARED_GHOST_SPEED = 1

# Punteggi
PELLET_SCORE = 10
POWER_PELLET_SCORE = 50
GHOST_SCORE = 200

# Durata della modalità spaventato dei fantasmi (in millisecondi)
SCARED_TIME = 10000

# Direzioni
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

# Caratteri per il labirinto
WALL = '#'
PELLET = '.'
POWER_PELLET = 'o'
EMPTY = ' '
PACMAN_START = 'P'
GHOST_START = 'G'