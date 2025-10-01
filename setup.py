#!/usr/bin/env python3
"""
Script di installazione per il progetto Pac-Man
"""

import subprocess
import sys
import os

def check_python_version():
    """Controlla che la versione di Python sia supportata"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Errore: È richiesto Python 3.7 o superiore")
        print(f"   Versione attuale: {version.major}.{version.minor}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor} supportato")
    return True

def install_dependencies():
    """Installa le dipendenze del progetto"""
    print("📦 Installazione delle dipendenze...")
    
    try:
        # Controlla se pygame è già installato
        import pygame
        print("✅ pygame già installato")
        return True
    except ImportError:
        pass
    
    try:
        # Installa pygame
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        print("✅ pygame installato con successo")
        return True
    except subprocess.CalledProcessError:
        print("❌ Errore nell'installazione di pygame")
        print("   Prova a eseguire manualmente: pip install pygame")
        return False

def verify_installation():
    """Verifica che l'installazione sia andata a buon fine"""
    print("🔍 Verifica dell'installazione...")
    
    try:
        # Esegui il test script
        result = subprocess.run([sys.executable, "test_game.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Verifica completata con successo")
            return True
        else:
            print("❌ Verifica fallita")
            print("Output del test:")
            print(result.stdout)
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Errore durante la verifica: {e}")
        return False

def main():
    """Funzione principale di installazione"""
    print("🟡 Installazione Pac-Man Game")
    print("=" * 40)
    
    # Controlla la versione di Python
    if not check_python_version():
        return 1
    
    # Installa le dipendenze
    if not install_dependencies():
        return 1
    
    # Verifica l'installazione
    if not verify_installation():
        print("\n⚠️ L'installazione potrebbe avere problemi.")
        print("   Prova comunque a eseguire: python main.py")
        return 1
    
    print("\n🎉 Installazione completata con successo!")
    print("🏃 Per avviare il gioco esegui: python main.py")
    print("\n🎮 Controlli del gioco:")
    print("   - Frecce o WASD: movimento")
    print("   - SPAZIO: pausa")
    print("   - ESC: uscita")
    print("   - R: restart (a fine partita)")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())