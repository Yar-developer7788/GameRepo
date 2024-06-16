import tkinter
from tkinter import *
import random
import time
win = Tk()
win.geometry("500x500")
win.title("Don`t press me")
clicks = 0
hp = 100
frazes = ["ahahahah", "DON`t", "NOOOOOOOOOO", "AHAHAHAHAHAH", "Hmm...", "Umm..."]
frazes_txt = ["Don`t press th button!", "Noooo", "Can you hear me?!", "STOOOP", "NO!", "I will delete your system!!!!!!!!!!!!"]
colors = ["red","orange","blue","yellow","green"]
size = ["1280x720", "700x700", "500x500", "1920x1080","100x100"]
def bitva(btnnn,texxxxxt):
	global clicks
	if clicks < 100:
		clicks += 1
		win.update()
		btnnn['text'] = frazes[random.randint(0,5)]
		texxxxxt['text'] = frazes_txt[random.randint(0,5)]
		btnnn['bg'] = colors[random.randint(0,4)]
		btnnn['fg'] = colors[random.randint(0,4)]
		win['background'] = colors[random.randint(0,4)]
		win.geometry(size[random.randint(0,4)])
		win.title(f"{clicks}/100")
		win.update()
	else:
		btnnn.destroy()
		texxxxxt['text'] = "you killed me..."
		time.sleep(10)
		# os.system("shutdown")
		# os.system("shutdown /s /t 0")
		for _ in range(100):
			win.update()		
			win.geometry(size[random.randint(0,4)])
			time.sleep(0.01)
			win.update()
		win.destroy()
	win.update()
def unlock(btn, btnn):
	btn['state'] = "normal"
	btnn.destroy()
def click(bt):
	global clicks
	clicks+=1
	print(clicks)
	match clicks:
		case 1:
			bt['text'] = "NOOOOO"
		case 2:
			bt['text'] = "D"
		case 3:
			bt['text'] = "DO"
		case 4:
			bt['text'] = "DON`"
		case 5:
			bt['text'] = "DON`T"
		case 6:
			bt['text'] = "DON`T P"
		case 7:
			bt['text'] = "DON`T PR"
		case 8:
			bt['text'] = "DON`T PRE"
		case 9:
			bt['text'] = "DON`T PRES"
		case 10:
			bt['text'] = "DON`T PRESS"
		case 11:
			bt['text'] = "DON`T PRESS "
		case 12:
			bt['text'] = "DON`T PRESS M"
		case 13:
			bt['text'] = "DON`T PRESS ME"
		case 14:
			bt['text'] = "ahahahahah"
			bt['state'] = "disabled"
			btn2 = Button(text="Unlock", command=lambda: unlock(bt,btn2))
			btn2.pack()
		case 15:
			tex['fg'] = "red"
			bt['text'] = "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
			bt['command'] = lambda: bitva(btn1,tex)
			win.update()
tex = Label(text="hello from anaconda!")
tex.pack()
btn1 = Button(text="Don`t cick me!", command=lambda: click(btn1))
btn1.pack()
win.mainloop()