class MusicInstrument:
    def __init__(self, text):
        self.text = text
        print(text)

    def piano(self):
        print("piano")

    def set_sound(self, type1):
        self.type1 = type1

    def get_sound(self):
        return self.type1


mi = MusicInstrument("Tim")
si = MusicInstrument("John")
#si.piano()
si.set_sound("mahogony")
print(si.get_sound())

mi.set_sound("doet")
print(mi.get_sound())
