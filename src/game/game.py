import pygame
import sys
from config.settings import *
from src.game.maze import Maze
from src.entities.pacman import PacMan
from src.entities.ghost import Ghost

class PacManGame:
    """Classe principale del gioco Pac-Man"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pac-Man")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        # Inizializza il gioco
        self.maze = Maze()
        self.init_entities()
        
        # Stato del gioco
        self.game_over = False
        self.game_won = False
        self.paused = False
        
    def init_entities(self):
        """Inizializza Pac-Man e i fantasmi"""
        # Inizializza Pac-Man
        pacman_x, pacman_y = self.maze.get_pacman_start_position()
        self.pacman = PacMan(pacman_x * CELL_SIZE, pacman_y * CELL_SIZE)
        
        # Inizializza i fantasmi
        ghost_positions = self.maze.get_ghost_start_positions()
        ghost_types = ['blinky', 'pinky', 'inky', 'clyde']
        
        self.ghosts = []
        for i, (ghost_x, ghost_y) in enumerate(ghost_positions):
            ghost_type = ghost_types[i] if i < len(ghost_types) else 'blinky'
            ghost = Ghost(ghost_x * CELL_SIZE, ghost_y * CELL_SIZE, ghost_type)
            self.ghosts.append(ghost)
    
    def handle_events(self):
        """Gestisce gli eventi di input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and (self.game_over or self.game_won):
                    self.reset_game()
        
        # Gestione del movimento di Pac-Man
        if not self.paused and not self.game_over and not self.game_won:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.pacman.set_next_direction(UP)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.pacman.set_next_direction(DOWN)
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.pacman.set_next_direction(LEFT)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.pacman.set_next_direction(RIGHT)
        
        return True
    
    def update(self):
        """Aggiorna la logica del gioco"""
        if self.paused or self.game_over or self.game_won:
            return
        
        # Aggiorna Pac-Man
        self.pacman.update(self.maze.layout)
        
        # Controlla collisioni con i pellet
        pacman_rect = self.pacman.get_rect()
        pellets = self.maze.check_pellet_collision(pacman_rect)
        
        for pellet_x, pellet_y, pellet_type in pellets:
            power_pellet = self.pacman.eat_pellet(pellet_type)
            self.maze.eat_pellet(pellet_x, pellet_y)
            
            # Se è un power pellet, spaventa i fantasmi
            if power_pellet:
                for ghost in self.ghosts:
                    ghost.set_scared_mode()
        
        # Aggiorna i fantasmi
        pacman_center = self.pacman.get_center()
        for ghost in self.ghosts:
            ghost.update(self.maze.layout, pacman_center)
        
        # Controlla collisioni con i fantasmi
        self.check_ghost_collisions()
        
        # Controlla se il livello è completato
        if self.maze.is_level_complete():
            self.game_won = True
    
    def check_ghost_collisions(self):
        """Controlla le collisioni tra Pac-Man e i fantasmi"""
        pacman_rect = self.pacman.get_rect()
        
        for ghost in self.ghosts:
            ghost_rect = ghost.get_rect()
            
            # Controlla se c'è una collisione
            if pacman_rect.colliderect(ghost_rect):
                if ghost.scared:
                    # Pac-Man mangia il fantasma
                    self.pacman.eat_ghost()
                    ghost.reset_position()
                else:
                    # Pac-Man viene catturato
                    game_over = self.pacman.lose_life()
                    if game_over:
                        self.game_over = True
                    else:
                        # Resetta le posizioni
                        self.reset_positions()
    
    def reset_positions(self):
        """Resetta le posizioni di Pac-Man e dei fantasmi"""
        pacman_x, pacman_y = self.maze.get_pacman_start_position()
        self.pacman.reset_position(pacman_x, pacman_y)
        
        for ghost in self.ghosts:
            ghost.reset_position()
    
    def reset_game(self):
        """Resetta completamente il gioco"""
        self.maze.reset()
        self.init_entities()
        self.game_over = False
        self.game_won = False
        self.paused = False
    
    def draw(self):
        """Disegna tutti gli elementi del gioco"""
        # Pulisci lo schermo
        self.screen.fill(BLACK)
        
        # Disegna il labirinto
        self.maze.draw(self.screen)
        
        # Disegna Pac-Man
        self.pacman.draw(self.screen)
        
        # Disegna i fantasmi
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        
        # Disegna l'interfaccia utente
        self.draw_ui()
        
        # Disegna messaggi di stato
        if self.paused:
            self.draw_text("PAUSA - Premi SPAZIO per continuare", 
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
        elif self.game_over:
            self.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, RED)
            self.draw_text("Premi R per ricominciare", 
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
        elif self.game_won:
            self.draw_text("HAI VINTO!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, GREEN)
            self.draw_text("Premi R per ricominciare", 
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Disegna l'interfaccia utente"""
        # Punteggio
        score_text = f"Punteggio: {self.pacman.score}"
        self.draw_text(score_text, 10, 10, WHITE, align_center=False)
        
        # Vite
        lives_text = f"Vite: {self.pacman.lives}"
        self.draw_text(lives_text, 10, 40, WHITE, align_center=False)
        
        # Pellet rimanenti
        remaining = self.maze.total_pellets - self.maze.pellets_eaten
        pellets_text = f"Pellet: {remaining}"
        self.draw_text(pellets_text, 10, 70, WHITE, align_center=False)
        
        # Controlli
        controls_text = "Usa FRECCE o WASD per muoverti, SPAZIO per pausa, ESC per uscire"
        text_width = self.font.size(controls_text)[0]
        self.draw_text(controls_text, SCREEN_WIDTH - text_width - 10, 
                      SCREEN_HEIGHT - 30, WHITE, align_center=False)
    
    def draw_text(self, text, x, y, color, align_center=True):
        """Disegna del testo sullo schermo"""
        text_surface = self.font.render(text, True, color)
        if align_center:
            text_rect = text_surface.get_rect(center=(x, y))
            self.screen.blit(text_surface, text_rect)
        else:
            self.screen.blit(text_surface, (x, y))
    
    def run(self):
        """Loop principale del gioco"""
        running = True
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()