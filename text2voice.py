import pyttsx3

def text2voice(word):
    engine = pyttsx3.init()

    """Rate"""
    rate = engine.getProperty('rate')
    print("rate: ",rate)
    engine.setProperty('rate',rate+1)

    """Volumn"""
    volume = engine.getProperty('volume')
    print(volume)
    engine.setProperty('volume',volume+1.25)

    """voice"""
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    #engine.setProperty('voices',voices[1].id)

    engine.say(word)
    engine.runAndWait()

text2voice("hello everyone in WIT hackathon")