#!/usr/bin/env python3
"""
Quick test per verificare che il gioco si avvii correttamente
"""

import sys
import os
import time

# Aggiungi il percorso del progetto al Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def main():
    """Test rapido del gioco"""
    try:
        print("🟡 Test avvio Pac-Man...")
        
        from src.game.game import PacManGame
        import pygame
        
        # Crea il gioco
        game = PacManGame()
        print("✅ Gioco creato con successo")
        
        # Simula alcuni frame
        for i in range(10):
            game.update()
            game.draw()
            game.clock.tick(60)
            
            # Simula eventi di uscita dopo alcuni frame
            if i > 5:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                if not game.handle_events():
                    break
        
        print("✅ Test completato con successo!")
        print("🎮 Il gioco è pronto per essere utilizzato!")
        
        pygame.quit()
        return 0
        
    except Exception as e:
        print(f"❌ Errore durante il test: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())