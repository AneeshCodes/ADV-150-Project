# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:39:58 2022

@author: anees
"""

from tkinter import *
import random

root = Tk()
root.title("1D List Part 2")
root.geometry("400x400")

countryEntry = Entry(root)
capitalEntry = Entry(root)

displayCountry = Label(root)
displayCapital = Label(root)

random = Label(root)

countryList = []
capitalList = []

def display():
    country1 = countryEntry.get()
    capital1 = capitalEntry.get()
    
    countryList.append(country1)
    capitalList.append(capital1)
    
    displayCountry["text"] = str(countryList)
    displayCapital["text"] = str(capitalList)
    
def displayRand():
    countryLength = len(countryList)
    countryIndex = random.randint(0,countryLength-1)
    
    capitalLength = len(capitalList)
    capitalIndex = random.randint(0,capitalLength-1)
    
    country2 = countryList(countryIndex)
    capital2 = capitalList(capitalIndex)
    
    random["text"] = "Location: " + str(capital2) + ", " + str(country2)

display = Button(root, text="Display the Country and Capital", command=display)
randomlyDisplay = Button(root, text="Randomly Display the Country and Capital", command=displayRand)
countryEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
capitalEntry.place(relx=0.5,rely=0.3, anchor=CENTER)
display.place(relx=0.5, rely=0.4, anchor=CENTER)
displayCountry.place(relx=0.5, rely=0.5, anchor=CENTER)
displayCapital.place(relx=0.5,rely=0.6,anchor=CENTER)
randomlyDisplay.place(relx=0.5,rely=0.7,anchor=CENTER)
random.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()