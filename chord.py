

class Chord:

    def __init__(self):
        self.root = None


class Note:

    def __init__(self):
        self.pitch = None
        self.duration = None


keys = ['C', 'CD', 'D', 'DE', 'E', 'F', 'FG', 'G', 'GA', 'A', 'AB', 'B', 'C']

major_chords = {
    'C': ['C', 'E', 'G'],
    'D': ['D', 'F#', 'A'],
    'E': ['E', 'G#', 'B'],
    'F#': ['F#', 'A#', 'C#'],
    'Ab': ['Ab', 'C', 'Eb'],
    'Bb': ['Bb', 'D', 'F'],
    'C#': ['C#', 'E#', 'G#'],
    'Eb': ['Eb', 'G', 'Bb'],
    'F': ['F', 'A', 'C'],
    'G': ['G', 'B', 'D'],
    'A': ['A', 'C#', 'E'],
    'B': ['B', 'D#', 'F#']
}

minor_chords = {
    'Cm': ['C', 'Eb', 'G'],
    'Dm': ['D', 'F', 'A'],
    'Em': ['E', 'G', 'B'],
    'F#': ['F#', 'A', 'C#'],
    'Ab': ['Ab', 'B', 'Eb'],
    'Bb': ['Bb', 'Db', 'F'],
    'C#': ['C#', 'E', 'G#'],
    'Eb': ['Eb', 'Gb', 'Bb'],
    'Fm': ['F', 'Ab', 'C'],
    'Gm': ['G', 'Bb', 'D'],
    'Am': ['A', 'C', 'E'],
    'Bm': ['B', 'D', 'F#'],
}
