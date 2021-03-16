
import pyttsx3

robot_brain = input("Nhap : ")
robot_mouth = pyttsx3.init()
robot_mouth.say(f" oh {robot_brain},nice to meet you kakaka")
robot_mouth.runAndWait()