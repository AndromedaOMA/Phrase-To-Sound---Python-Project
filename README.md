<h1 align="center">Hi 👋, here we have the Phrase To Sound project</h1>
<h3 align="center">Developed this platform in the fifth semester of the faculty.</h3>

---

<h3 align="left">Here we have the requirement:</h3>

(EN) The purpose of the application is to be able to convert a sentence into an mp3 file, which will store
spoken recording of the sentence. For this, two scripts will be created.
  
  - Script 1 : 2 directories will be given as input parameters: one containing several
  text files, and one where the mp3 files will be stored. The first directory given at the entrance will
  run recursively. The files will contain one sentence per line. Each sentence will be
  converted to mp3 file and stored in the output directory.
  
  - Script 2 : To create a minimal graphical interface, in which one can enter a
  sentence. Pressing a Play button will convert the sentence to sound and play it.
  Use a text2speech library for this.
  
(RO) Scopul aplicației este să poată converti o propoziție într-un fișier mp3, care va stoca
înregistrarea rostită a propoziției. Pentru asta, vor fi create două scripturi.
  
  - Script 1 : Se vor da ca și parametri de intrare 2 directoare: unul în care se află mai multe
  fișiere text, și unul în care se vor stoca fișierele mp3. Primul director dat la intrare se va
  parcurge recursiv. Fișierele vor conține câte o propoziție pe linie.Fiecare propoziție va fi
  convertită în fișier mp3 și stocat în directorul de output.
  
  - Script 2 : Să se creeze o interfață grafică minimală, în care să se poată introduce o
  propoziție. Apăsând un buton de Play, se va converti propoziția în sunet și se va reda.
  Utilizati o librarie text2speech pentru acest lucru.
  
---

<h3 align="left">Installation:</h3>

1. Clone the current repositoy! Now you have the project avalable on your local server!</br>
 Type command: ```git clone git@github.com:AndromedaOMA/Phrase-To-Sound---Python-Project```
2. Opent the cmd terminal and navigate to the directory where the project is cloned </br>
3. Run the Python cmd line in order to run the project: </br>
 Type command: ```python main.py ./text_samples ./text_converted_to_audio```
4. Have fun!


# How does it work?

- The GUI is divided into three main components, a list of mp3 files, a text border and a button.
- The list of mp3 files represents all text-to-audio conversions of the text files in the directory entered at the first argument on the Python command line. You can select one of these and you will automatically hear the pronunciation of the text files.
- The text border and the button have a common role: Enter any text you want then press the button to give you the audio pronunciation of what you typed!
  </br>
  </br>
<img src="https://github.com/user-attachments/assets/96ee3009-2acc-4b1b-b329-ac1dbff0638a" width="600" height="600"></img>

---

<h3 align="left">Structure:</h3>

 - The structure of the project is simple: 
     I. In the file main.py we will call the two scripts that build the foundation of the project: converter.py and gui.py
     II. converter.py focuses on working with files and converting them from text files to mp3 files. The gTTS library will be used
     III. gui.py focuses on building the GUI and rendering the desired output. The gTTS, tkinter and playsound libraries will be used
    
<h3 align="left">The logic behind the code:</h3>

 - The entire project was written using the Pyhon programming language and gTTS libraries for text-to-audio conversion, tkinter to generate the GUI and playsound to play the voice based on the chosen/written audio file.
 
---

- ⚡ Fun fact **This is my first project made using Python language!**
