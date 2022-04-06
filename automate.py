from tkinter import *
import tkinter as tk
from time import sleep
import pyautogui
import keyboard
import pyperclip
from tkinter import scrolledtext

global key

script = []

window = Tk()
menubar = tk.Menu(window)
salutations = tk.Menu(menubar,tearoff= 0)

menubar.add_cascade(label="Help", menu=salutations)

window.config(menu=menubar)

window.title("Auto Friend") # title bar
window.configure(background="beige")

window.geometry("1000x600") # resized window

#lbl1 = Label(window, text="        ", font=("Arial Bold", 30)) # text in program
#lbl1.configure(background="white") # Making the text colour fit
#lbl1.grid(row=1,column=1) 

liste = scrolledtext.ScrolledText(window, 
                                    wrap = tk.WORD, 
                                    width = 40, 
                                    height = 18, 
                                    font = ("Calibri",
                                            10))
liste.see("end")
liste.place(x=550,y=10)


def helper():
    window2 = Tk()
    window2.configure(background="beige")
    window2.title("Help")
    window2.geometry("600x500")
    lbl1 = Label(window2, text="Special Keyboard Commands", font=("Calibri", 10))
    lbl1.configure(background="beige")
    lbl1.place(x=30, y=40) 
    text_area = scrolledtext.ScrolledText(window2, 
                                      wrap = tk.WORD, 
                                      width = 50, 
                                      height = 20, 
                                      font = ("calibri",
                                              10))
  
    text_area.grid(column = 0, pady = 10, padx = 10)
    
    text_area.insert(tk.INSERT,

    "Auto Friend (Auto Mate?) V.0.2\n\n" + 
                     "There's several available options to build your automation script.\n\n" +
                    "Pause - Enter the number of seconds you'd like to program to pause for.\n\n" +
                    "Key Press - Enter the SINGLE key to press. Special options such as tab can be found in the help/keyboard commands section\n\n" +
                    "Mouse Move - Enter the X and Y coordinates that you would like the mouse to move to - Selecting show mouse coordinates should help you pinpoint this.\n\n" +
                    "Mouse Click - Enter the amount of times you would like the mouse to left click.\n\n" +
                    "The Hotkeys should be self explanatory, you can add a the function you'd like to use into your script.\n\n"+
                    "Pause before start - Enter the number of seconds you'd like to pause the script before it starts running, to give you time to open the relevant programs\n\n" +
                    "Repeat - Allows you to loop the script as many times as needed\n\n" +
                    "Run Script - Begins the running of the script\n\n" +
                    "Can you save your script? - Kind of. You can edit the script text and copy paste your old script, or remove amend as needed. Keep it in the same format though!\n" +
                    "A new command has to go on a new line\n\n" +
                    "Why does it look like a child made this on windows 95? - If you can do better go ahead. \n\n" +
                    "If you like this or wish for additional features, feel free to let me know at iwhync@gmail.com")

    text_area.configure(state ='disabled')
    
def keyboard():
    window2 = Tk()
    window2.configure(background="beige")
    window2.title("Special Keyboard Commands")
    window2.geometry("650x600")
    lbl1 = Label(window2, text="Special Keyboard Commands", font=("Calibri", 10))
    lbl1.configure(background="white")
    lbl1.place(x=30, y=40) 
    text_area = scrolledtext.ScrolledText(window2, 
                                      wrap = tk.WORD, 
                                      width = 62, 
                                      height = 30, 
                                      font = ("Calibri",
                                              10))
  
    text_area.grid(column = 0, pady = 10, padx = 10)
    
    text_area.insert(tk.INSERT,

    "ENTER IN THE KEY BOX \n\naccept, add, alt, altleft, altright, apps, backspace, browserback, browserfavorites, browserforward," +
     "browserhome, browserrefresh, browsersearch, browserstop, capslock, clear, convert, ctrl, ctrlleft, ctrlright, decimal, del, delete,"+
     "divide, down, end, enter, esc, escape, execute, f1, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f2, f20, f21, f22, f23, f24, f3,"+
     "f4, f5, f6, f7, f8, f9, final, fn, hanguel, hangul, hanja, help, home, insert, junja, kana, kanji, launchapp1, launchapp2, launchmail,"+
     "launchmediaselect, left, modechange, multiply, nexttrack, nonconvert, num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, numlock,"+
      "pagedown, pageup, pause, pgdn, pgup, playpause, prevtrack, print, printscreen, prntscrn, prtsc, prtscr, return, right, scrolllock, select,"+
      "separator, shift, shiftleft, shiftright, sleep, space, stop, subtract, tab, up, volumedown, volumemute, volumeup," + 
      "win, winleft, winright, yen, command, option, optionleft, optionright")


    text_area.configure(state ='disabled')

salutations.add_command(label="Help", command=helper)  
salutations.add_command(label="Keyboard Commands", command=keyboard)

lblblank = Label(window, text="   ", font=("Calibri", 10), justify= LEFT)
lblblank.configure(background="beige")
lblblank.grid(row=1,column=1)

lblhotkeys = Label(window, text="Hotkeys:", font=("Calibri", 10), justify= LEFT)
lblhotkeys.configure(background="beige")
lblhotkeys.grid(row=2,column=1)

lblblank = Label(window, text="   ", font=("Calibri", 10), justify= LEFT)
lblblank.configure(background="beige")
lblblank.grid(row=3,column=1)

lblkey = Label(window, text="Key Press:", font=("Calibri", 10), justify= LEFT)
lblkey.configure(background="beige")
lblkey.grid(row=5,column=1)

lblsleep = Label(window, text="Pause:", font=("Calibri", 10))
lblsleep.configure(background="beige")
lblsleep.grid(row=4,column=1)
lblsleep = Label(window, text="  Seconds", font=("Calibri", 8))
lblsleep.configure(background="beige")
lblsleep.grid(row=4,column=3)

x3 = Entry(window,width=5,bd =5)
x3.grid(row= 4 ,column=2)

x1 = Entry(window,width=5,bd =5)
x1.grid(row=5,column=2)
x1.focus_set()


lblmouse = Label(window, text=" Mouse Move:", font=("Calibri", 10))
lblmouse.configure(background="beige")
lblmouse.grid(row=6,column=1)
lblmousex = Label(window, text="x=", font=("Calibri", 12))
lblmousex.configure(background="beige")
lblmousex.grid(row=6,column=2)
lblmousey = Label(window, text="y=      ", font=("Calibri", 12))
lblmousey.configure(background="beige")
lblmousey.grid(row=6,column=4)

x4 = Entry(window,width=5,bd =5)
x4.grid(row= 6 ,column=3)
x5 = Entry(window,width=5,bd =5)
x5.grid(row= 6 ,column=5)

lblmouseclick = Label(window, text=" Mouse Click: ", font=("Calibri", 10))
lblmouseclick.configure(background="beige")
lblmouseclick.grid(row=7,column=1)
lblmouseclick = Label(window, text="times", font=("Calibri", 8))
lblmouseclick.configure(background="beige")
lblmouseclick.grid(row=7,column=3)

x6 = Entry(window,width=5,bd =5)
x6.grid(row=7 ,column=2)

lblpause = Label(window, text="Pause before start: ", font=("Calibri", 10))
lblpause.configure(background="beige")
lblpause.place(x=500,y=460)

x8 = Entry(window,width=5,bd =5)
x8.place(x=670,y=460)


lblrepeat = Label(window, text="Repeat: ", font=("Calibri", 10))
lblrepeat.configure(background="beige")
lblrepeat.place(x=780,y=460)

x7 = Entry(window,width=5,bd =5)
x7.place(x=860,y=460)

def mouse():
    
    x = ""

    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.title("Mouse") # title bar
    root.configure(background="white")
    root.geometry("320x90")
    label = Label(root, text=x, font=("Arial Bold", 10))
    label.configure(background="white")
    label.place(x=10, y=10)
    str_var = tk.StringVar(value="Default")


    while True:
        x = pyautogui.position()
        x = str(x)
        x = x.replace("Point"," ").replace("(","").replace(")"," ").replace(",","")
        label = Label(root, text=x, font=("Arial Bold", 20))
        label.configure(background="white")
        label.place(x=10, y=10)
        root.update()
        label.destroy()

    root.mainloop()


def copy():
    liste.insert(tk.INSERT,"Copy"+"\n")

btncopy = Button(window, text="Copy", bg="light blue", fg="black",command = copy)
btncopy.grid(row=2,column=4)

def paste():
    liste.insert(tk.INSERT,"Paste"+"\n")

btnpaste = Button(window, text="Paste", bg="light blue", fg="black",command = paste)
btnpaste.grid(row=2,column=5)

    
def select_all():
    liste.insert(tk.INSERT,"Select All"+"\n")
    
btnselectall = Button(window, text="Select All", bg="light blue", fg="black",command = select_all)
btnselectall.grid(row=2,column=2)

def alt_tab():
    liste.insert(tk.INSERT,"Alt+Tab"+"\n")
    
btnselectall = Button(window, text="Alt+Tab", bg="light blue", fg="black",command = alt_tab)
btnselectall.grid(row=2,column=3)
    
def delete_last_line():
    liste.delete("end-1l","end")
    
btndeletelast = Button(window, text="Delete last line", bg="light blue", fg="black",command = delete_last_line)
btndeletelast.place(x=20,y=450)

def clear_all():
    liste.delete("1.0","end")
    
btnclear = Button(window, text="Clear All", bg="light blue", fg="black",command = clear_all)
btnclear.place(x=20,y=400)

def go(event):
    
    if x3.get() != "":
        liste.insert(tk.INSERT,"Pause: "+x3.get()+"\n")
        x3.delete(0,"end")
    if x1.get() != "":
        liste.insert(tk.INSERT,"Press: "+x1.get()+"\n")
        x1.delete(0,"end")
    if x4.get() != "" and x5.get() != "":
        liste.insert(tk.INSERT,"Mouse Move: "+"X= " + x4.get() + " Y= " + x5.get() +"\n")
        x4.delete(0,"end")
        x5.delete(0,"end")
    if x6.get() != "":
        liste.insert(tk.INSERT,"Mouse Click: "+x6.get()+"\n")
        x6.delete(0,"end")
    liste.yview(END)

def run():
    x = liste.get('1.0', 'end-1c') 
    x = x.splitlines()
    repeat = 1
    paws = 0
    
    if x8.get() !="":
        paws = int(x8.get())
        sleep(paws)
    
    if x7.get() != "":
        repeat = int(x7.get())
        
    while repeat > 0:
        for _ in range(len(x)):
            if "Pause: " in str(x[_]):
                com = str(x[_]).replace("Pause: ","")
                sleep(int(com))
            if "Press: " in str(x[_]):
                com = str(x[_]).replace("Press: ","")
                pyautogui.press(com)
            if "Mouse Move: " in str(x[_]):
                com = str(x[_]).replace("Mouse Move: ","").replace("X= ","").replace("Y= ","")
                com = com.split(" ")
                pyautogui.moveTo(int(com[0]), int(com[1]), 1)
            if "Mouse Click: " in str(x[_]):
                com = str(x[_]).replace("Mouse Click: ","")
                for _ in range(int(com)):
                    sleep(0.1)
                    pyautogui.click()
            if "Copy" in str(x[_]):
                com = str(x[_]).replace("Copy","")
                sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
            if "Paste" in str(x[_]):
                com = str(x[_]).replace("Paste","")
                sleep(0.1)
                pyautogui.hotkey('ctrl', 'v')
            if "Select All" in str(x[_]):
                com = str(x[_]).replace("Select All","")
                sleep(0.1)
                pyautogui.hotkey('ctrl', 'a')
            if "Alt+Tab" in str(x[_]):
                com = str(x[_]).replace("Alt+Tab","")
                sleep(0.3)
                pyautogui.hotkey('alt', 'tab')
                sleep(0.3)
        repeat -= 1
            
btnrun = Button(window, text="Run Script", bg="light green", fg="black",command = run)
btnrun.place(x=860,y=520)

btnmoose = Button(window, text="Show Mouse Coordinates", bg="pink", fg="black",command = mouse)
btnmoose.place(x=300,y=270)

window.bind('<Return>', go)

mainloop()

window.mainloop()
