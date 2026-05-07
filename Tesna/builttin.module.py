import os

from gtts import gTTS

g=gTTS(text="നമസ്കാരം, സുഖമാണോ",lang="ml")
g.save("sample.mp3")

os.system("start sample.mp3")