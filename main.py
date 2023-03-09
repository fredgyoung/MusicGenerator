import random


def get_chord():
    major_chords = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minor_chords = ['Am', 'Bm', 'Cm', 'Dm', 'Em', 'Fm', 'Gm']
    rand = random.randint(0, 6)
    return major_chords[rand]


def get_pitch():
    pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    rand = random.randint(0, 11)
    return pitches[rand]


def get_duration():
    durations = [4, 8, 16]
    rand = random.randint(0, 2)
    return durations[rand]


def create_measure():
    chord = get_chord()
    pitch = get_pitch()
    duration = get_duration()
    print(pitch, end = " ")


if __name__ == '__main__':

    for i in range(32):
        create_measure()
