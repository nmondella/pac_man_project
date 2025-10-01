"""
Modulo per la gestione delle collisioni nel gioco Pac-Man
"""

import pygame
from config.settings import CELL_SIZE

class CollisionManager:
    """Classe per gestire le collisioni nel gioco"""
    
    @staticmethod
    def check_collision(rect1, rect2):
        """Controlla se due rettangoli si sovrappongono"""
        return rect1.colliderect(rect2)
    
    @staticmethod
    def check_circle_collision(pos1, radius1, pos2, radius2):
        """Controlla la collisione tra due cerchi"""
        dx = pos1[0] - pos2[0]
        dy = pos1[1] - pos2[1]
        distance = (dx * dx + dy * dy) ** 0.5
        return distance < (radius1 + radius2)
    
    @staticmethod
    def get_grid_position(pixel_x, pixel_y):
        """Converte coordinate pixel in coordinate griglia"""
        return pixel_x // CELL_SIZE, pixel_y // CELL_SIZE
    
    @staticmethod
    def get_pixel_position(grid_x, grid_y):
        """Converte coordinate griglia in coordinate pixel"""
        return grid_x * CELL_SIZE, grid_y * CELL_SIZE
    
    @staticmethod
    def is_position_valid(x, y, maze):
        """Controlla se una posizione è valida nel labirinto"""
        grid_x, grid_y = CollisionManager.get_grid_position(x, y)
        
        if grid_y < 0 or grid_y >= len(maze):
            return False
        if grid_x < 0 or grid_x >= len(maze[0]):
            return False
            
        return maze[grid_y][grid_x] != '#'
    
    @staticmethod
    def get_nearest_valid_position(x, y, maze):
        """Trova la posizione valida più vicina"""
        grid_x, grid_y = CollisionManager.get_grid_position(x, y)
        
        # Se la posizione è già valida, restituiscila
        if CollisionManager.is_position_valid(x, y, maze):
            return x, y
        
        # Cerca nelle posizioni adiacenti
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                new_x = (grid_x + dx) * CELL_SIZE
                new_y = (grid_y + dy) * CELL_SIZE
                
                if CollisionManager.is_position_valid(new_x, new_y, maze):
                    return new_x, new_y
        
        # Se non trova nulla, restituisci la posizione originale
        return x, y