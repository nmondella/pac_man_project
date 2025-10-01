import pygame
from src.entities.entity import Entity
from config.settings import *

class PacMan(Entity):
    """Classe per il personaggio Pac-Man"""
    
    def __init__(self, x, y):
        super().__init__(x, y, YELLOW, CELL_SIZE - 2)
        self.speed = PACMAN_SPEED
        self.next_direction = (0, 0)
        self.mouth_open = True
        self.mouth_timer = 0
        self.lives = 3
        self.score = 0
        
    def update(self, maze):
        """Aggiorna Pac-Man"""
        # Prova a cambiare direzione se possibile
        if self.next_direction != (0, 0):
            next_x = self.x + self.next_direction[0] * self.speed
            next_y = self.y + self.next_direction[1] * self.speed
            
            if self.can_move_to(next_x, next_y, maze):
                self.direction = self.next_direction
                self.next_direction = (0, 0)
        
        # Muovi Pac-Man
        self.move(maze)
        
        # Aggiorna l'animazione della bocca
        self.mouth_timer += 1
        if self.mouth_timer >= 10:  # Cambia ogni 10 frame
            self.mouth_open = not self.mouth_open
            self.mouth_timer = 0
    
    def set_next_direction(self, direction):
        """Imposta la prossima direzione desiderata"""
        self.next_direction = direction
    
    def eat_pellet(self, pellet_type):
        """Pac-Man mangia un pellet"""
        if pellet_type == PELLET:
            self.score += PELLET_SCORE
            return False  # Pellet normale
        elif pellet_type == POWER_PELLET:
            self.score += POWER_PELLET_SCORE
            return True   # Power pellet
    
    def eat_ghost(self):
        """Pac-Man mangia un fantasma"""
        self.score += GHOST_SCORE
    
    def lose_life(self):
        """Pac-Man perde una vita"""
        self.lives -= 1
        return self.lives <= 0  # Ritorna True se game over
    
    def reset_position(self, start_x, start_y):
        """Resetta la posizione di Pac-Man"""
        self.set_position(start_x, start_y)
        self.direction = (0, 0)
        self.next_direction = (0, 0)
    
    def draw(self, screen):
        """Disegna Pac-Man con animazione della bocca"""
        center_x = int(self.x + self.size // 2)
        center_y = int(self.y + self.size // 2)
        radius = self.size // 2
        
        if self.mouth_open:
            # Disegna Pac-Man con la bocca aperta
            start_angle = 0
            end_angle = 360
            
            # Determina l'angolo della bocca basato sulla direzione
            if self.direction == RIGHT:
                start_angle = 30
                end_angle = 330
            elif self.direction == LEFT:
                start_angle = 150
                end_angle = 210
            elif self.direction == UP:
                start_angle = 240
                end_angle = 300
            elif self.direction == DOWN:
                start_angle = 60
                end_angle = 120
            
            # Disegna l'arco
            if start_angle != 0:
                points = [(center_x, center_y)]
                for angle in range(int(start_angle), int(end_angle) + 1, 5):
                    x = center_x + radius * pygame.math.Vector2(1, 0).rotate(angle).x
                    y = center_y + radius * pygame.math.Vector2(1, 0).rotate(angle).y
                    points.append((x, y))
                points.append((center_x, center_y))
                
                if len(points) > 2:
                    pygame.draw.polygon(screen, self.color, points)
            else:
                pygame.draw.circle(screen, self.color, (center_x, center_y), radius)
        else:
            # Disegna Pac-Man con la bocca chiusa (cerchio completo)
            pygame.draw.circle(screen, self.color, (center_x, center_y), radius)
        
        # Disegna l'occhio
        eye_offset = radius // 3
        if self.direction == RIGHT:
            eye_x = center_x + eye_offset
            eye_y = center_y - eye_offset
        elif self.direction == LEFT:
            eye_x = center_x - eye_offset
            eye_y = center_y - eye_offset
        elif self.direction == UP:
            eye_x = center_x
            eye_y = center_y - eye_offset
        elif self.direction == DOWN:
            eye_x = center_x
            eye_y = center_y + eye_offset
        else:
            eye_x = center_x + eye_offset
            eye_y = center_y - eye_offset
            
        pygame.draw.circle(screen, BLACK, (int(eye_x), int(eye_y)), 2)