from getch import getch
import csv
import os
def show_status():
    cr = ["\033[0m","\033[7m"]
    lx = [status["1"],status["2"],status["q"],status["w"],status["a"],status["s"],status["z"],status["x"]]
    allcode = "12qwaszx"
    excode = ""
    nochar = 1
    print(" _____________\n|             |")
    print("| ",end='')
    print(cr[status["1"]]+"< 1 >"+cr[0],end=' ')
    print(cr[status["2"]]+"< 2 >"+cr[0],end=' ')
    print("|\n|             |\n| ",end='')
    print(cr[status["q"]]+"< Q >"+cr[0],end=' ')
    print(cr[status["w"]]+"< W >"+cr[0],end=' ')
    print("|\n|             |\n| ",end='')
    print(cr[status["a"]]+"< A >"+cr[0],end=' ')
    print(cr[status["s"]]+"< S >"+cr[0],end=' ')
    print("|\n|             |\n| ",end='')
    print(cr[status["z"]]+"< Z >"+cr[0],end=' ')
    print(cr[status["x"]]+"< X >"+cr[0],end=' ')
    print("|\n|_____________|")
    f = open("mrd.csv","r")
    for i in range(len(allcode)):
        if lx[i] == 1:
            excode += allcode[i]
    nochar = 1
    for line in csv.DictReader(f):
        if excode == line["excode"]:
            print("-> "+line["char"])
            nochar = 0
            break
    if nochar == 1:
        print("\033[7;31mNOCHAR\033[0m")
    return line["char"]
    
    
kuan,gao = os.get_terminal_size()
status = {"1":0,
          "2":0,
          "q":0,
          "w":0,
          "a":0,
          "s":0,
          "z":0,
          "x":0}
text = ""
ex = 1
while ex == 1:
    key = getch()
    fxj = {"65":"上","66":"下","67":"右","68":"左"}
    if key in status:
        if status[key] == 0:
            status[key] = 1
        else:
            status[key] = 0
    elif ord(key) == 10:
        text += show_status()
    elif ord(key) == 127:
        text = text[0:-1]
    elif key == "n":
        text += "\n"
    elif ord(key) == 32:
        text += chr(10240)
    elif ord(key) == 24:
        ex = 0
    show_status()
    print(text,end='')
    print("\033[7m \033[0m")
    nd = 0
    for i in text:
        if i == "\n":
            nd += 1

    for i in range((gao-13)-(nd)):
        print()
