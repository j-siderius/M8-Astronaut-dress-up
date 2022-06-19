"""
This class will handle the audio coming from python
"""

from pydub import AudioSegment
from pydub.playback import play


class Sound:

    def __init__(self):
        "Insert stuff"

    def audioSetup(self):
        """
        This function will setup the audio
        """

    def mixer(self):
        """
        This function will handle the sounds and when they should be played
        """
        song = AudioSegment.from_wav("Hybrid Trap 2.wav")
        print('playing sound using  pydub')
        play(song)
