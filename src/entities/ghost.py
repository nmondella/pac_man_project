import pygame
import random
from src.entities.entity import Entity
from config.settings import *

class Ghost(Entity):
    """Classe per i fantasmi"""
    
    def __init__(self, x, y, ghost_type):
        color = GHOST_COLORS.get(ghost_type, RED)
        super().__init__(x, y, color, CELL_SIZE - 2)
        self.ghost_type = ghost_type
        self.speed = GHOST_SPEED
        self.scared = False
        self.scared_timer = 0
        self.original_color = color
        self.start_x = x
        self.start_y = y
        self.target = None
        self.last_direction = (0, 0)
        
    def update(self, maze, pacman_pos=None):
        """Aggiorna il fantasma"""
        # Aggiorna il timer della paura
        if self.scared:
            self.scared_timer -= 1
            if self.scared_timer <= 0:
                self.set_normal_mode()
        
        # Scegli una nuova direzione
        self.choose_direction(maze, pacman_pos)
        
        # Muovi il fantasma
        self.move(maze)
    
    def choose_direction(self, maze, pacman_pos=None):
        """Sceglie la direzione del fantasma"""
        grid_x, grid_y = self.get_grid_pos()
        possible_directions = []
        
        # Trova tutte le direzioni valide
        for direction in DIRECTIONS:
            new_x = self.x + direction[0] * self.speed
            new_y = self.y + direction[1] * self.speed
            
            # Non tornare indietro (a meno che non sia l'unica opzione)
            opposite_direction = (-self.last_direction[0], -self.last_direction[1])
            if direction == opposite_direction and len(possible_directions) > 0:
                continue
                
            if self.can_move_to(new_x, new_y, maze):
                possible_directions.append(direction)
        
        if possible_directions:
            if self.scared:
                # Se spaventato, muoviti casualmente lontano da Pac-Man
                if pacman_pos and random.random() < 0.7:  # 70% delle volte fuggi
                    self.direction = self._flee_from_pacman(possible_directions, pacman_pos)
                else:
                    self.direction = random.choice(possible_directions)
            else:
                # Comportamento normale: insegui Pac-Man
                if pacman_pos and random.random() < 0.8:  # 80% delle volte insegui
                    self.direction = self._chase_pacman(possible_directions, pacman_pos)
                else:
                    self.direction = random.choice(possible_directions)
            
            self.last_direction = self.direction
    
    def _chase_pacman(self, possible_directions, pacman_pos):
        """Sceglie la direzione migliore per inseguire Pac-Man"""
        best_direction = possible_directions[0]
        min_distance = float('inf')
        
        ghost_x, ghost_y = self.get_center()
        
        for direction in possible_directions:
            # Calcola dove sarebbe il fantasma dopo il movimento
            future_x = ghost_x + direction[0] * self.speed * 10
            future_y = ghost_y + direction[1] * self.speed * 10
            
            # Calcola la distanza da Pac-Man
            dx = future_x - pacman_pos[0]
            dy = future_y - pacman_pos[1]
            distance = dx * dx + dy * dy
            
            if distance < min_distance:
                min_distance = distance
                best_direction = direction
        
        return best_direction
    
    def _flee_from_pacman(self, possible_directions, pacman_pos):
        """Sceglie la direzione migliore per fuggire da Pac-Man"""
        best_direction = possible_directions[0]
        max_distance = 0
        
        ghost_x, ghost_y = self.get_center()
        
        for direction in possible_directions:
            # Calcola dove sarebbe il fantasma dopo il movimento
            future_x = ghost_x + direction[0] * self.speed * 10
            future_y = ghost_y + direction[1] * self.speed * 10
            
            # Calcola la distanza da Pac-Man
            dx = future_x - pacman_pos[0]
            dy = future_y - pacman_pos[1]
            distance = dx * dx + dy * dy
            
            if distance > max_distance:
                max_distance = distance
                best_direction = direction
        
        return best_direction
    
    def set_scared_mode(self):
        """Attiva la modalità spaventato"""
        self.scared = True
        self.scared_timer = SCARED_TIME // (1000 // FPS)  # Converti in frame
        self.color = BLUE
        self.speed = SCARED_GHOST_SPEED
    
    def set_normal_mode(self):
        """Disattiva la modalità spaventato"""
        self.scared = False
        self.scared_timer = 0
        self.color = self.original_color
        self.speed = GHOST_SPEED
    
    def reset_position(self):
        """Resetta la posizione del fantasma"""
        self.x = self.start_x
        self.y = self.start_y
        self.direction = (0, 0)
        self.last_direction = (0, 0)
        self.set_normal_mode()
    
    def draw(self, screen):
        """Disegna il fantasma"""
        center_x = int(self.x + self.size // 2)
        center_y = int(self.y + self.size // 2)
        radius = self.size // 2
        
        # Disegna il corpo del fantasma (cerchio nella parte superiore)
        pygame.draw.circle(screen, self.color, (center_x, center_y - 2), radius)
        
        # Disegna la parte inferiore del fantasma (rettangolo con ondulazioni)
        bottom_rect = pygame.Rect(self.x, center_y - 2, self.size, radius + 2)
        pygame.draw.rect(screen, self.color, bottom_rect)
        
        # Disegna le ondulazioni nella parte inferiore
        wave_width = self.size // 4
        for i in range(0, self.size, wave_width):
            wave_x = self.x + i
            wave_points = [
                (wave_x, self.y + self.size),
                (wave_x + wave_width // 2, self.y + self.size - 4),
                (wave_x + wave_width, self.y + self.size)
            ]
            if wave_x + wave_width <= self.x + self.size:
                pygame.draw.polygon(screen, self.color, wave_points)
        
        # Disegna gli occhi
        eye_size = 3
        left_eye_x = center_x - radius // 2
        right_eye_x = center_x + radius // 2
        eye_y = center_y - radius // 3
        
        pygame.draw.circle(screen, WHITE, (left_eye_x, eye_y), eye_size)
        pygame.draw.circle(screen, WHITE, (right_eye_x, eye_y), eye_size)
        
        # Pupille
        pupil_size = 1
        pygame.draw.circle(screen, BLACK, (left_eye_x, eye_y), pupil_size)
        pygame.draw.circle(screen, BLACK, (right_eye_x, eye_y), pupil_size)
        
        # Se spaventato, disegna un'espressione diversa
        if self.scared:
            # Bocca spaventata
            mouth_y = center_y + radius // 3
            pygame.draw.circle(screen, BLACK, (center_x, mouth_y), 2)