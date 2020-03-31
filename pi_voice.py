from pydub import AudioSegment
from pydub.playback import play

def voice(random):
    sound = AudioSegment.from_mp3(random)
    out = play(sound)
