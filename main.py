from gtts import gTTS

test_text = ("Learn from yesterday, live for today, hope for tomorrow. "
             "The important thing is not to stop questioning. - Einstein")
language = "en"

obj = gTTS(text=test_text, lang=language, slow=True)

obj.save("test_sound.mp3")
