"""
Gestore audio per il gioco Pac-Man
"""

import pygame
import os

class SoundManager:
    """Classe per gestire i suoni del gioco"""
    
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_playing = False
        self.sound_enabled = True
        
        # Carica i suoni se esistono
        self.load_sounds()
    
    def load_sounds(self):
        """Carica tutti i file audio"""
        sound_files = {
            'eat_pellet': 'eat_pellet.wav',
            'eat_power_pellet': 'eat_power_pellet.wav',
            'eat_ghost': 'eat_ghost.wav',
            'death': 'death.wav',
            'game_start': 'game_start.wav',
            'siren': 'siren.wav'
        }
        
        assets_path = os.path.join(os.path.dirname(__file__), '../../assets')
        
        for sound_name, filename in sound_files.items():
            sound_path = os.path.join(assets_path, filename)
            try:
                if os.path.exists(sound_path):
                    self.sounds[sound_name] = pygame.mixer.Sound(sound_path)
                else:
                    # Crea un suono placeholder (silenzioso)
                    self.sounds[sound_name] = self._create_placeholder_sound()
            except pygame.error:
                self.sounds[sound_name] = self._create_placeholder_sound()
    
    def _create_placeholder_sound(self):
        """Crea un suono placeholder silenzioso"""
        # Crea un buffer audio vuoto di breve durata
        import numpy as np
        sample_rate = 22050
        duration = 0.1  # 100ms
        frames = int(duration * sample_rate)
        arr = np.zeros((frames, 2), dtype=np.int16)
        
        # Converti in formato pygame
        sound = pygame.sndarray.make_sound(arr)
        return sound
    
    def play_sound(self, sound_name):
        """Riproduce un suono"""
        if not self.sound_enabled:
            return
            
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except pygame.error:
                pass  # Ignora errori audio
    
    def stop_all_sounds(self):
        """Ferma tutti i suoni"""
        pygame.mixer.stop()
    
    def set_volume(self, volume):
        """Imposta il volume generale (0.0 - 1.0)"""
        pygame.mixer.set_num_channels(8)
        for sound in self.sounds.values():
            sound.set_volume(volume)
    
    def toggle_sound(self):
        """Attiva/disattiva i suoni"""
        self.sound_enabled = not self.sound_enabled
        if not self.sound_enabled:
            self.stop_all_sounds()
    
    def play_background_music(self):
        """Riproduce la musica di sottofondo"""
        if not self.sound_enabled:
            return
            
        try:
            music_path = os.path.join(os.path.dirname(__file__), 
                                    '../../assets/background_music.mp3')
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(-1)  # Loop infinito
                self.music_playing = True
        except pygame.error:
            pass  # Ignora se non c'è il file musicale
    
    def stop_background_music(self):
        """Ferma la musica di sottofondo"""
        pygame.mixer.music.stop()
        self.music_playing = False