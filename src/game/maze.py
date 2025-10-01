import pygame
from config.settings import *
from config.maze import MAZE_LAYOUT

class Maze:
    """Classe per gestire il labirinto e i pellet"""
    
    def __init__(self):
        self.layout = [list(row) for row in MAZE_LAYOUT]
        self.original_layout = [list(row) for row in MAZE_LAYOUT]
        self.pellets_eaten = 0
        self.total_pellets = self._count_pellets()
        
    def _count_pellets(self):
        """Conta il numero totale di pellet nel labirinto"""
        count = 0
        for row in self.layout:
            for cell in row:
                if cell == PELLET or cell == POWER_PELLET:
                    count += 1
        return count
    
    def get_cell(self, x, y):
        """Restituisce il contenuto di una cella del labirinto"""
        if 0 <= y < len(self.layout) and 0 <= x < len(self.layout[y]):
            return self.layout[y][x]
        return WALL
    
    def set_cell(self, x, y, value):
        """Imposta il contenuto di una cella del labirinto"""
        if 0 <= y < len(self.layout) and 0 <= x < len(self.layout[y]):
            self.layout[y][x] = value
    
    def eat_pellet(self, x, y):
        """Rimuove un pellet dalla posizione specificata"""
        cell = self.get_cell(x, y)
        if cell == PELLET or cell == POWER_PELLET:
            self.set_cell(x, y, EMPTY)
            self.pellets_eaten += 1
            return cell
        return None
    
    def is_level_complete(self):
        """Controlla se tutti i pellet sono stati mangiati"""
        return self.pellets_eaten >= self.total_pellets
    
    def reset(self):
        """Resetta il labirinto allo stato originale"""
        self.layout = [list(row) for row in self.original_layout]
        self.pellets_eaten = 0
    
    def get_pacman_start_position(self):
        """Trova la posizione iniziale di Pac-Man"""
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == PACMAN_START:
                    return x, y
        return 18, 18  # Posizione di default
    
    def get_ghost_start_positions(self):
        """Trova le posizioni iniziali dei fantasmi"""
        positions = []
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == GHOST_START:
                    positions.append((x, y))
        
        # Se non ci sono abbastanza posizioni, usa quelle di default
        while len(positions) < 4:
            positions.extend([(15, 11), (16, 11), (17, 11), (18, 11)])
        
        return positions[:4]
    
    def draw(self, screen):
        """Disegna il labirinto"""
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                pixel_x = x * CELL_SIZE
                pixel_y = y * CELL_SIZE
                
                if cell == WALL:
                    # Disegna il muro
                    pygame.draw.rect(screen, BLUE, 
                                   (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE))
                elif cell == PELLET:
                    # Disegna il pellet piccolo
                    center_x = pixel_x + CELL_SIZE // 2
                    center_y = pixel_y + CELL_SIZE // 2
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), 2)
                elif cell == POWER_PELLET:
                    # Disegna il power pellet grande
                    center_x = pixel_x + CELL_SIZE // 2
                    center_y = pixel_y + CELL_SIZE // 2
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), 6)
    
    def check_pellet_collision(self, entity_rect):
        """Controlla se un'entità è in collisione con un pellet"""
        # Calcola le coordinate della griglia per l'entità
        left = entity_rect.left // CELL_SIZE
        right = entity_rect.right // CELL_SIZE
        top = entity_rect.top // CELL_SIZE
        bottom = entity_rect.bottom // CELL_SIZE
        
        pellets_found = []
        
        # Controlla tutte le celle che l'entità occupa
        for y in range(max(0, top), min(len(self.layout), bottom + 1)):
            for x in range(max(0, left), min(len(self.layout[0]), right + 1)):
                cell = self.get_cell(x, y)
                if cell == PELLET or cell == POWER_PELLET:
                    pellets_found.append((x, y, cell))
        
        return pellets_found