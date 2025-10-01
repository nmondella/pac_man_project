#!/usr/bin/env python3
"""
Test script per verificare che tutti i componenti del gioco siano funzionanti
"""

import sys
import os

# Aggiungi il percorso del progetto al Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def test_imports():
    """Test che tutti i moduli possano essere importati correttamente"""
    print("🧪 Test degli import...")
    
    try:
        # Test import configurazione
        from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
        from config.maze import MAZE_LAYOUT
        print("✅ Configurazione importata correttamente")
        
        # Test import entità
        from src.entities.entity import Entity
        from src.entities.pacman import PacMan
        from src.entities.ghost import Ghost
        print("✅ Entità importate correttamente")
        
        # Test import gioco
        from src.game.maze import Maze
        from src.game.game import PacManGame
        print("✅ Logica di gioco importata correttamente")
        
        # Test import utilità
        from src.utils.collision import CollisionManager
        from src.utils.sound import SoundManager
        print("✅ Utilità importate correttamente")
        
        return True
        
    except ImportError as e:
        print(f"❌ Errore nell'importazione: {e}")
        return False

def test_pygame():
    """Test che pygame sia installato e funzionante"""
    print("\n🎮 Test di pygame...")
    
    try:
        import pygame
        pygame.init()
        print("✅ pygame installato e inizializzato correttamente")
        
        # Test creazione superficie
        screen = pygame.display.set_mode((100, 100))
        print("✅ Superficie di test creata correttamente")
        
        pygame.quit()
        return True
        
    except ImportError:
        print("❌ pygame non è installato. Esegui: pip install pygame")
        return False
    except Exception as e:
        print(f"❌ Errore con pygame: {e}")
        return False

def test_game_components():
    """Test che i componenti del gioco possano essere istanziati"""
    print("\n🎯 Test dei componenti del gioco...")
    
    try:
        from src.game.maze import Maze
        from src.entities.pacman import PacMan
        from src.entities.ghost import Ghost
        
        # Test creazione labirinto
        maze = Maze()
        print("✅ Labirinto creato correttamente")
        
        # Test posizioni iniziali
        pacman_pos = maze.get_pacman_start_position()
        ghost_positions = maze.get_ghost_start_positions()
        print(f"✅ Posizione Pac-Man: {pacman_pos}")
        print(f"✅ Posizioni fantasmi: {ghost_positions[:2]}...")
        
        # Test creazione entità
        pacman = PacMan(pacman_pos[0] * 20, pacman_pos[1] * 20)
        ghost = Ghost(ghost_positions[0][0] * 20, ghost_positions[0][1] * 20, 'blinky')
        print("✅ Entità create correttamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Errore nella creazione dei componenti: {e}")
        return False

def test_game_creation():
    """Test che il gioco principale possa essere creato"""
    print("\n🕹️ Test creazione gioco...")
    
    try:
        from src.game.game import PacManGame
        
        # Crea il gioco senza avviarlo
        game = PacManGame()
        print("✅ Gioco principale creato correttamente")
        
        # Test che le entità siano state inizializzate
        assert game.pacman is not None, "Pac-Man non inizializzato"
        assert len(game.ghosts) > 0, "Fantasmi non inizializzati"
        assert game.maze is not None, "Labirinto non inizializzato"
        print("✅ Tutte le entità sono state inizializzate")
        
        # Pulisci pygame
        import pygame
        pygame.quit()
        
        return True
        
    except Exception as e:
        print(f"❌ Errore nella creazione del gioco: {e}")
        return False

def main():
    """Esegue tutti i test"""
    print("🚀 Avvio test del progetto Pac-Man...\n")
    
    tests = [
        test_imports,
        test_pygame,
        test_game_components,
        test_game_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            break  # Ferma i test se uno fallisce
    
    print(f"\n📊 Risultati: {passed}/{total} test passati")
    
    if passed == total:
        print("🎉 Tutti i test sono passati! Il gioco dovrebbe funzionare correttamente.")
        print("🏃 Esegui 'python main.py' per avviare il gioco.")
    else:
        print("⚠️ Alcuni test sono falliti. Controlla gli errori sopra.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())