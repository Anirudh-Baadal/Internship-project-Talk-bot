![image](https://user-images.githubusercontent.com/93869586/169685482-52f4ec3a-278d-4b10-bd7e-0be0244581e4.png)

Requiered packages:

1.	Pyttsx3:  converts text input to audio format.

2.	Speechrecognition:To convert input from the user which is in audio format into to text format.

3.	Chatterbot:  It responds the user back with the data processed.

4.	Pyaudio: This handles audio in python.


Implementation:

Input from the user is taken in audio format and this is converted to text format using a package called speechrecognition then then data in text format is fed as input to a package named chatterbot which gives out the response in text format which is converted to audio format then using pyttsx3 package. Then again the program waits for the input from user which is converted to text format via speechrecogniton package and in this manner the process loops until the user says BYE which stops the program execution by bringing it out of the loop.

Conclusion:
Using some some of the easy to install packages like pyttsx3 and speechrecognition  etc, a good working talk bot can be implemented from the comfort of our home.

Errors/problems faced:

Pyaudio : ‘pip install pyaudio’ ths command was unable to install the package to solve this issue the commands below was uselfull
‘pip install pipwin’ & ‘pipwin install PyAudio’
as it installed the package successfully.

Unable to recognize the input from user:  the environment where the program is being ran must a free from heavy noise as the program gets confused between actual input and noise some of the feasible solution include turning off any device near the microphone of the pc in which the program is being ran which creates disturbance via sound.

References:

1.	https://www.codegrepper.com/code-examples/python/pipwin+install+pyaudio+for+python+3.9

2.  https://chatterbot.readthedocs.io/en/stable/tutorial.html
