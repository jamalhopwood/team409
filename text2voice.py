import pyttsx3

class TextToVoice:
    def __init__(self, word):
        self.word = word

    def text2voice(self):
        engine = pyttsx3.init()

        """Rate"""
        rate = engine.getProperty('rate')
        #print("rate: ",rate)
        engine.setProperty('rate',rate+1)

        """Volumn"""
        volume = engine.getProperty('volume')
        #print(volume)
        engine.setProperty('volume',volume+1.25)

        """voice"""
        voices = engine.getProperty('voices')
        engine.setProperty('voices',voices[0].id)
        #engine.setProperty('voices',voices[1].id)

        engine.say(self.word)
        engine.runAndWait()

# t = TextToVoice()
# t.text2voice("hello everyone in WIT hackathon")
