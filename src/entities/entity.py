import pygame
from config.settings import *

class Entity:
    """Classe base per tutte le entità del gioco (Pac-Man, fantasmi, ecc.)"""
    
    def __init__(self, x, y, color, size=CELL_SIZE):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.direction = (0, 0)
        self.speed = 1
        
    def get_grid_pos(self):
        """Restituisce la posizione nella griglia"""
        return int(self.x // CELL_SIZE), int(self.y // CELL_SIZE)
    
    def get_center(self):
        """Restituisce il centro dell'entità"""
        return self.x + self.size // 2, self.y + self.size // 2
    
    def set_position(self, grid_x, grid_y):
        """Imposta la posizione basata sulle coordinate della griglia"""
        self.x = grid_x * CELL_SIZE
        self.y = grid_y * CELL_SIZE
    
    def move(self, maze):
        """Muove l'entità nella direzione corrente"""
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed
        
        # Controlla se il movimento è valido
        if self.can_move_to(new_x, new_y, maze):
            self.x = new_x
            self.y = new_y
            
            # Gestione del tunnel (teletrasporto ai lati)
            if self.x < 0:
                self.x = SCREEN_WIDTH - self.size
            elif self.x >= SCREEN_WIDTH:
                self.x = 0
    
    def can_move_to(self, x, y, maze):
        """Controlla se l'entità può muoversi in una posizione specifica"""
        # Calcola le coordinate della griglia per tutti i punti dell'entità
        left = int(x // CELL_SIZE)
        right = int((x + self.size - 1) // CELL_SIZE)
        top = int(y // CELL_SIZE)
        bottom = int((y + self.size - 1) // CELL_SIZE)
        
        # Controlla i limiti dello schermo
        if y < 0 or y + self.size > SCREEN_HEIGHT:
            return False
            
        # Permetti il movimento orizzontale oltre i bordi (tunnel)
        if x < 0 or x + self.size > SCREEN_WIDTH:
            return True
            
        # Controlla se tutte le celle sono libere (non muri)
        try:
            return (maze[top][left] != WALL and 
                   maze[top][right] != WALL and 
                   maze[bottom][left] != WALL and 
                   maze[bottom][right] != WALL)
        except IndexError:
            return False
    
    def draw(self, screen):
        """Disegna l'entità sullo schermo"""
        pygame.draw.circle(screen, self.color, 
                         (int(self.x + self.size // 2), 
                          int(self.y + self.size // 2)), 
                         self.size // 2)
    
    def get_rect(self):
        """Restituisce il rettangolo dell'entità per il rilevamento delle collisioni"""
        return pygame.Rect(self.x, self.y, self.size, self.size)