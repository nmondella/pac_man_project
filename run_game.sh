#!/bin/bash
# Script di avvio semplificato per Pac-Man Game

echo "🟡 Avvio Pac-Man Game..."

# Controlla se l'ambiente virtuale esiste
if [ ! -d "venv" ]; then
    echo "📦 Creazione ambiente virtuale..."
    python3 -m venv venv
    
    echo "📦 Installazione dipendenze..."
    source venv/bin/activate
    pip install pygame
else
    echo "✅ Ambiente virtuale trovato"
fi

# Attiva l'ambiente virtuale e avvia il gioco
echo "🚀 Avvio del gioco..."
source venv/bin/activate && python main.py