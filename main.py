from tkinter import*
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init() # creating instance of Engine class

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

#get_close_matches(word,possibilities,n,cutoff)

#close_match=get_close_matches('appel',['ape','apple','app','ap','peach','puppy'])
#print(close_match)


# FUNCTIONALITY
def search():
    data=json.load(open('data.json'))
    word=enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        print(meaning)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n\n')
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno("confirm",f'Did you mean {close_match} instead?')
        if res==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)

            meaning=data[close_match]

            textarea.delete(1.0,END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Errr','The word doesnt exist,Please double check.')
            enterwordEntry.delete(0,END)
            textarea.delete(1.0,END)

    else:
        messagebox.showinfo('Information','The word doesnt exist.')
        enterwordEntry.delete(0,END)
        textarea.delete(1.0,END)

def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0,END)

def iexit():
    res=messagebox.askyesno('Confirm','Do you want to exit?')
    if res==True:
        root.destroy()

    else:
        pass


def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()






# GUI
root=Tk()

root.geometry('1000x626+100+30')

root.title('Talking Dictionary created be ME')

root.resizable(False,False)

bgImage = PhotoImage(file='dbg1.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

enterwordLabel=Label(root,text='Enter Word',font=('castellar',30,'bold'),foreground='red')
enterwordLabel.place(x=550,y=20)

enterwordEntry=Entry(root,font=('ariel',23,'bold'),justify=CENTER,bd=7,relief=GROOVE)
enterwordEntry.place(x=490,y=80)

searchImage=PhotoImage(file='search.png')
searchButton=Button(root,image=searchImage,bd=0,cursor='hand2',
                    command=search)
searchButton.place(x=540,y=140)

micImage=PhotoImage(file='mic.png')
micButton=Button(root,image=micImage,bd=0,cursor='hand2',command=wordaudio)
micButton.place(x=710,y=140)

meaningLabel=Label(root,text='Meaning',font=('castellar',30,'bold'),foreground='red')
meaningLabel.place(x=580,y=220)

textarea=Text(root,width=34,height=10,font=('arial',12,'bold'),bd=8,relief=GROOVE)
textarea.place(x=510,y=290)

audioImage=PhotoImage(file='microphone.png')
audioButton=Button(root,image=audioImage,bd=0,cursor='hand2',command=meaningaudio)
audioButton.place(x=550,y=510)

clearImage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearImage,bd=0,cursor='hand2',command=clear)
clearButton.place(x=630,y=510)

exitImage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitImage,bd=0,cursor='hand2',command=iexit)
exitButton.place(x=720,y=510)

def enter_function(event):
    searchButton.invoke()
root.bind('<Return>',enter_function)

root.mainloop() # every line of code above this
