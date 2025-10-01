#!/usr/bin/env python3
"""
Pac-Man Game
Un classico gioco Pac-Man implementato in Python con pygame.

Controlli:
- Frecce direzionali o WASD per muovere Pac-Man
- SPAZIO per mettere in pausa
- ESC per uscire
- R per ricominciare (quando game over o vittoria)

Autore: Progetto Pac-Man
Data: Ottobre 2025
"""

import sys
import os

# Aggiungi il percorso del progetto al Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

try:
    from src.game.game import PacManGame
except ImportError as e:
    print(f"Errore nell'importazione: {e}")
    print("Assicurati che pygame sia installato: pip install pygame")
    sys.exit(1)

def main():
    """Funzione principale per avviare il gioco"""
    try:
        print("Avvio del gioco Pac-Man...")
        print("Controlli:")
        print("- Frecce direzionali o WASD per muoverti")
        print("- SPAZIO per mettere in pausa")
        print("- ESC per uscire")
        print("- R per ricominciare quando finisce il gioco")
        print("\nBuon divertimento!")
        
        game = PacManGame()
        game.run()
        
    except KeyboardInterrupt:
        print("\nGioco interrotto dall'utente.")
    except Exception as e:
        print(f"Errore durante l'esecuzione del gioco: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()