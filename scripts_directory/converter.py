from gtts import gTTS
import os


class Converter:
    def __init__(self, text_samples_directory, audio_samples_directory):
        self.text_samples_directory = text_samples_directory
        self.audio_samples_directory = audio_samples_directory
        self.text_samples = []

    def extract_text(self):
        for root, directories, files in os.walk(self.text_samples_directory):
            for fileName in files:
                full_filename = os.path.join(root, fileName)
                print(full_filename)
                if fileName.endswith('.txt'):
                    with open(full_filename, 'r', encoding='utf-8') as file:
                        for line in file:
                            line = line.strip()
                            self.text_samples.append(line)
                            print(line)

    def converter(self, flag=True, quote=None):
        if flag:
            text_sample_list = self.text_samples
        else:
            text_sample_list = quote
        language = "en"
        index = 0
        for text_sample in text_sample_list:
            if text_sample.strip():
                obj = gTTS(text=text_sample, lang=language, slow=True)
                obj.save(f"./{self.audio_samples_directory}/audio_quote_{index}.mp3")
                index += 1
