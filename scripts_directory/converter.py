from gtts import gTTS


class Converter:
    def __init__(self, txt):
        self.test_text = txt

    def test_method(self):
        txt = self.test_text
        # test_text = ("Learn from yesterday, live for today, hope for tomorrow. "
        #              "The important thing is not to stop questioning. - Einstein")
        language = "en"
        obj = gTTS(text=txt, lang=language, slow=True)
        obj.save("test_sound.mp3")
