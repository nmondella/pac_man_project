# 🟡 Pac-Man Game in Python

Un classico gioco Pac-Man implementato in Python utilizzando pygame, con una struttura modulare e organizzata.

## 📁 Struttura del Progetto

```
pac_man_project/
├── main.py                 # File principale per avviare il gioco
├── requirements.txt        # Dipendenze del progetto
├── README.md              # Documentazione
├── config/                # Configurazioni del gioco
│   ├── __init__.py
│   ├── settings.py        # Impostazioni generali
│   └── maze.py           # Layout del labirinto
├── src/                   # Codice sorgente
│   ├── __init__.py
│   ├── entities/          # Entità del gioco
│   │   ├── __init__.py
│   │   ├── entity.py      # Classe base per le entità
│   │   ├── pacman.py      # Classe Pac-Man
│   │   └── ghost.py       # Classe Fantasmi
│   ├── game/              # Logica di gioco
│   │   ├── __init__.py
│   │   ├── game.py        # Classe principale del gioco
│   │   └── maze.py        # Gestione del labirinto
│   └── utils/             # Utilità
│       ├── __init__.py
│       ├── collision.py   # Gestione collisioni
│       └── sound.py       # Gestione audio
└── assets/                # Risorse (per futuri suoni/immagini)
```

## 🎮 Caratteristiche

- **Pac-Man animato** con apertura e chiusura della bocca
- **4 Fantasmi colorati** con AI basilare (inseguimento e fuga)
- **Sistema di punteggi** con pellet normali e power pellet
- **Modalità spaventato** per i fantasmi quando Pac-Man mangia power pellet
- **Gestione vite** e game over
- **Interfaccia utente** con punteggio, vite e pellet rimanenti
- **Sistema di pausa** e restart
- **Tunnels laterali** per il teletrasporto
- **Struttura modulare** facilmente estendibile

## 🕹️ Controlli

- **Frecce direzionali** o **WASD**: Muovi Pac-Man
- **SPAZIO**: Metti in pausa/riprendi il gioco
- **R**: Ricomincia il gioco (quando finisce)
- **ESC**: Esci dal gioco

## 🚀 Installazione e Avvio

### Prerequisiti
- Python 3.7 o superiore
- pip (gestore pacchetti Python)

### Installazione

1. **Clona o scarica il progetto**
2. **Naviga nella cartella del progetto**:
   ```bash
   cd pac_man_project
   ```

3. **Crea un ambiente virtuale** (raccomandato):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Su macOS/Linux
   # oppure su Windows: venv\Scripts\activate
   ```

4. **Installa le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Oppure installa pygame direttamente:
   ```bash
   pip install pygame
   ```

### Avvio del Gioco

**Con ambiente virtuale attivo:**
```bash
source venv/bin/activate  # Attiva l'ambiente virtuale
python main.py
```

**Oppure metodo rapido:**
```bash
# Esegui tutto in un comando
source venv/bin/activate && python main.py
```

## 🎯 Obiettivo del Gioco

- Mangia tutti i pellet nel labirinto per vincere
- Evita i fantasmi o mangiali quando sono spaventati (blu)
- Mangia i power pellet (grandi) per spaventare i fantasmi temporaneamente
- Non farti catturare dai fantasmi o perderai una vita
- Il gioco finisce quando perdi tutte e 3 le vite

## ⚙️ Configurazione

Il gioco può essere personalizzato modificando i file in `config/`:

- **`settings.py`**: Dimensioni schermo, velocità, colori, punteggi
- **`maze.py`**: Layout del labirinto

## 🔧 Estensioni Possibili

Il progetto è strutturato per essere facilmente estendibile:

- **Livelli multipli**: Aggiungi nuovi layout di labirinto
- **Power-up aggiuntivi**: Implementa nuovi tipi di pellet
- **AI migliorata**: Migliora il comportamento dei fantasmi
- **Effetti sonori**: Aggiungi file audio nella cartella `assets/`
- **Grafica migliorata**: Sostituisci le forme geometriche con sprite
- **Sistema di salvataggio**: Salva punteggi e progressi
- **Modalità multiplayer**: Aggiungi un secondo giocatore

## 🐛 Risoluzione Problemi

### Errore "pygame not found"
```bash
pip install pygame
```

### Il gioco è troppo veloce/lento
Modifica il valore `FPS` in `config/settings.py`

### Problemi con i controlli
Assicurati che la finestra del gioco sia attiva e in primo piano

## 📝 Licenza

Questo progetto è stato creato a scopo educativo e di intrattenimento.

## 👨‍💻 Autore

Progetto Pac-Man - Ottobre 2025

---

Buon divertimento! 🟡👻👻👻👻