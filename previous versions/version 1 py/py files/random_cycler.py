import random

class Random7sus4Cycler:
    """Manages cycling through 7sus4 chord types in shuffled rounds"""
    def __init__(self):
        self.chord_types = ["7sus4_minor", "7sus4_dominant", "7sus4_half_dim", "7sus4_altered"]
        self.current_round = []
        self.current_index = 0
        self.round_count = 0
        self._start_new_round()
    
    def _start_new_round(self):
        """Start a new round by shuffling the chord types"""
        self.current_round = self.chord_types.copy()
        random.shuffle(self.current_round)
        self.current_index = 0
        self.round_count += 1
        print(f"Starting round {self.round_count}: {[ct.replace('7sus4_', '') for ct in self.current_round]}")
    
    def get_next_chord_type(self):
        """Get the next chord type in the current round, reshuffling if needed"""
        # If we've used all chord types in this round, start a new round
        if self.current_index >= len(self.current_round):
            self._start_new_round()
        
        # Get the current chord type and advance the index
        chord_type = self.current_round[self.current_index]
        self.current_index += 1
        chord_name = chord_type.replace('7sus4_', '')
        print(f"Generated chord type: {chord_name} (position {self.current_index} of round {self.round_count})")
        return chord_type

# Global instance for the random cycler
random_7sus4_cycler = Random7sus4Cycler() 