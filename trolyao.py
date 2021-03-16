
#from datetime import date,datetime
import datetime
import pyttsx3
import speech_recognition
import webbrowser 
robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()


def speak(robot_brain):

	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
def Time():
	time = datetime.datetime.now().strftime("%I:%M:%p")
	speak(time)
def welcome():
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour < 12:
		speak("Good morning sir")
	elif hour <= 18 and hour >= 12:
		speak("Good afternoon sir")
	else:
		speak("Good everning sir")
	
	

def do_the_command():
	#robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		robot_ear.pause_threshold = 3
		audio = robot_ear.listen(mic)

	try:
		voice = robot_ear.recognize_google(audio,language='en')
		print("Boss: "+ voice)
	except:
		voice = ""
	return voice	


if __name__ == '__main__':
	welcome()
	speak("What do you want me to do, sir ?")
	while True:
		
		voice  = do_the_command().lower()
		if "google" in voice:
			speak("What you want to search sir ?")
			search = do_the_command().lower()
			url = f"https://www.google.com/search?q={search}"
			webbrowser.get().open(url)
			speak(f"Here are your {search} on google ")
			speak("what next you want me to do ?")
			
		elif "youtube" in voice:
			speak("What you want to search sir ?")
			search = do_the_command().lower()
			url = f"https://www.youtube.com/search?q={search}"
			webbrowser.get().open(url)
			speak(f"Here are your {search} on youtube ")
			speak("what next you want me to do ?")

		elif "time" in voice:
			Time()
			speak("what next you want me to do ?")
		elif "quit" in voice:
			speak("have a good day sir , see you next time")
			break

	

		





		






