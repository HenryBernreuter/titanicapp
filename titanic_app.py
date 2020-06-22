import math
import pandas as pd
import numpy as np
import itertools
import csv
from tkinter import *
import tkinter as tk

#GUI
# creating an instance for Tk
root = tk.Tk()
root.geometry('300x300')
# Window Title
root.title("Final Project")
# Title
l1 = tk.Label(root, text='Would you have survived?', font = 'Helvetica 18', fg = "red")
l1.pack()
#Enter your age
l2 = tk.Label(root,text='Enter your age:',fg = "black")
l2.place(x= 25, y =55)
t1 = tk.Text(root, height = 1, width = 30)
t1.place(x=25,y=85)

# Male or female
l3 = tk.Label(root, text='Enter 1 for male and 0 for female: ')
l3.place(x=25, y=110)
t2 = tk.Text(root, height = 1, width = 30)
t2.place(x=25,y=135)

#First class
l4 = tk.Label(root, text='Enter 1 for 1st Class, 2 for 2nd, 3 for 3rd')
l4.place(x=25, y=155)
t3 =tk.Text(root, height = 1, width = 30)
t3.place(x=25,y=175)


# Label : Result
res = tk.Label(root, text = " ")
res.place(x=27, y=220)
res2 = tk.Label(root, text = " ")
res2.place(x=27, y=240)
# defining survive function
def survive():
    GUIlistd = []
    GUIlists = []
    a = int(t1.get("1.0", 'end-1c'))
    b = int(t2.get("1.0", 'end-1c'))
    c = int(t3.get("1.0", 'end-1c'))

    if 0 < a >= 16:
        GUIlists.append(pof16s)
        GUIlistd.append(pof16d)
    elif 17 < a >= 26:
        GUIlists.append(pof26s)
        GUIlistd.append(pof26d)
    elif 27 < a >= 36:
        GUIlists.append(pof36s)
        GUIlistd.append(pof36d)
    elif 37 < a >= 62:
        GUIlists.append(pof62s)
        GUIlistd.append(pof62d)
    if b == 1:
        GUIlists.append(pofmales)
        GUIlistd.append(pofmaled)
    elif b == 0:
        GUIlists.append(poffemales)
        GUIlistd.append(poffemaled)
    if c == 1:
        GUIlists.append(pof1sts)
        GUIlistd.append(pof1std)
    elif c == 2:
        GUIlists.append(pof2nds)
        GUIlistd.append(pof2ndd)
    elif c == 3:
        GUIlists.append(pof3rds)
        GUIlistd.append(pof3rdd)
    if sum(GUIlists) > 1:
        res.config(text= "You Lived")

    else:
        res.config(text= "You Died")

    print("Lived",sum(GUIlists))
    print("DEad",sum(GUIlistd))
    print(GUIlists)
    print(GUIlistd)

survive = tk.Button(root, text = "Did I survive?", command = survive, height=1, width=15)
survive.place(x=100, y=200)




qbutton = Button(root, text = "Quit", command = root.quit,height=1, width=5 )
qbutton.place(x=120,y=250)

#Import data

url = 'https://raw.githubusercontent.com/HenryBernreuter/kaggleData/master/train_titanic.csv'
df = pd.read_csv(url, error_bad_lines=False)


df['Agelt17'] = np.where(df['Age'] <= 16, 1, 0)
df['Age1726'] = [1 if x > 16 and x <= 26 else 0 for x in df['Age']]
df['Age2736'] = [1 if x > 26 and x <= 36 else 0 for x in df['Age']]
df['Age3762'] = [1 if x > 36 and x <= 62 else 0 for x in df['Age']]
df['Agegt62'] = [1 if x > 62 else 0 for x in df['Age']]


#####Survival prob#####
n_surv1 = df["Survived"][df["Survived"] == 1].count()
print("The probability of  survival is  ", round(n_surv1), "%")
n_surv0 = df["Survived"][df["Survived"] == 0].count()
print("The probability of death is  ", round(n_surv0), "%")
tot_surv = df["Survived"].count()
print("The total survival probability is",tot_surv, "%")


#####This is the probability of survival#####
p_surv1 = n_surv1 / tot_surv
print("The probability of survival",round(p_surv1,2)*100,"%")

#####This is the probability of death#####
p_surv0 = n_surv0 / tot_surv
print("The probability of death",round(p_surv0,2)*100,"%")

#####P(Pclass|Survived)#####



#####Probability of survival for Class 1#####

cl1sur1 = df["Survived"][df["Survived"]==1] & df["Pclass"][df["Pclass"]==1].count()
cl1sur1 = df[(df.Survived == 1) & (df.Pclass == 1)].count()
p_cl1sur1 = cl1sur1 / n_surv1
print("The Proability of Survival for the 1st class",round(p_cl1sur1.Pclass,2)*100,"%")



#####Probability of death for class 1#####
cl1sur0 = df[(df.Survived == 0) & (df.Pclass == 1)].count()
p_cl1sur0 = cl1sur0 / n_surv0
print("The Probability of Death of 1st Class",round(p_cl1sur0.Pclass,2)*100, "%")


#####Probability of survival for Class 2#####
cl2sur1 = df[(df.Survived == 1) & (df.Pclass == 2)].count()
p_cl2sur1 = cl2sur1 / n_surv1
print("The Probability of survival for 2nd Class",round(p_cl2sur1.Pclass,2)*100 ,"%")


#####Probability of death for class 2#####
cl2sur0 = df[(df.Survived == 0) & (df.Pclass == 2)].count()
p_cl2sur0 = cl2sur0 / n_surv0
print("The Probability of death for the 2nd class",round(p_cl2sur0.Pclass,2)*100,"%")


#####Probability of survival for Class 3#####

cl3sur1 = df[(df.Survived == 1) & (df.Pclass == 3)].count()
p_cl3sur1 = cl3sur1 / n_surv1
print("The Probability of survival for the 3nd class",round(p_cl3sur1.Pclass,2)*100,"%")



#####Probability of death for class 3#####

cl3sur0 = df[(df.Survived == 0) & (df.Pclass == 3)].count()
p_cl3sur0 = cl3sur0 / n_surv0
print("The Probability of death for the 3nd class",round(p_cl3sur0.Pclass,2)*100,"%")



#####P(Sex|Survived)#####


#####Probability of Male survived#####

MaleSurv1 = df[(df.Survived == 1) & (df.Sex == "male")].count()
p_MaleSurv1 = MaleSurv1 / n_surv1
print("The Probability of survival for males's",round(p_MaleSurv1.Sex,2)*100,"%")



#####Probability of Male death#####

MaleSurv0 = df[(df.Survived == 0) & (df.Sex == "male")].count()
p_MaleSurv0 = MaleSurv0 / n_surv0
print("The Probability of death for males's",round(p_MaleSurv0.Sex,2)*100,"%")



#####Probability of Female survived#####
FmaleSurv1 = df[(df.Survived == 1) & (df.Sex == "female")].count()
p_FmaleSurv1 = FmaleSurv1 / n_surv1
print(p_FmaleSurv1.Sex)


#####Probability of Female death#####

FmaleSurv0 = df[(df.Survived == 0) & (df.Sex == "female")].count()
p_FmaleSurv0 = FmaleSurv0 / n_surv0
print(p_FmaleSurv0.Sex)


#####P(Age|Survived)#####


#####Probability of <17 survived#####

lt17surv1 = df[(df.Survived == 1) & (df.Agelt17 == 1)].count()
p_lt17surv1 = lt17surv1 / n_surv1
print(p_lt17surv1.Agelt17)


#####Probability of <17 death#####

lt17surv0 = df[(df.Survived == 0) & (df.Agelt17 == 1)].count()
p_lt17surv0 = lt17surv0 / n_surv0
print(p_lt17surv0.Agelt17)


#####Probability of 17-26 survive#####

A1726surv1 = df[(df.Survived == 1) & (df.Age1726 == 1)].count()
p_A1726surv1 = A1726surv1 / n_surv1
print(p_A1726surv1.Age1726)


#####Probability of 17-26 death#####

A1726surv0 = df[(df.Survived == 0) & (df.Age1726 == 1)].count()
p_A1726surv0 = A1726surv0 / n_surv0
print(p_A1726surv0.Age1726)


#####Probability of 27-36 survive#####

A2736surv1 = df[(df.Survived == 1) & (df.Age2736 == 1)].count()
p_A2736surv1 = A2736surv1 / n_surv1
print(p_A2736surv1.Age2736)


#####Probability of 27-36 death#####

A2736surv0 = df[(df.Survived == 0) & (df.Age2736 == 1)].count()
p_A2736surv0 = A2736surv0 / n_surv0
print(p_A2736surv0.Age2736)


#####Probability of 37-62 survive#####

A3762surv1 = df[(df.Survived == 1) & (df.Age3762 == 1)].count()
p_A3762surv1 = A3762surv1 / n_surv1
print(p_A3762surv1.Age3762)


#####Probability of 37-62 death#####

A3762surv0 = df[(df.Survived == 0) & (df.Age3762 == 1)].count()
p_A3762surv0 = A3762surv0 / n_surv0
print(p_A3762surv0.Age3762)


#####Probability of >62 survive#####

Agt62surv1 = df[(df.Survived == 1) & (df.Agegt62 == 1)].count()
p_Agt62surv1 = Agt62surv1 / n_surv1
print(p_Agt62surv1.Agegt62)


#####Probability of >62 death#####

Agt62surv0 = df[(df.Survived == 0) & (df.Agegt62 == 1)].count()
p_Agt62surv0 = Agt62surv0 / n_surv0
print(p_Agt62surv0.Agegt62)

GUIlists = []
#proability of survial
pof16s = p_lt17surv1.Agelt17
pof26s = p_A1726surv1.Age1726
pof36s = p_A3762surv1.Age3762
pof62s = p_Agt62surv1.Agegt62
pofmales = p_MaleSurv1.Sex
poffemales = p_FmaleSurv1.Sex
pof1sts = p_cl1sur1.Pclass
pof2nds = p_cl2sur1.Pclass
pof3rds = p_cl3sur1.Pclass
#proability of death
GUIlistd = []
pof16d = p_lt17surv0.Agelt17
pof26d = p_A1726surv0.Age1726
pof36d = p_A3762surv0.Age3762
pof62d = p_Agt62surv0.Agegt62
pofmaled = p_MaleSurv0.Sex
poffemaled = p_FmaleSurv0.Sex
pof1std = p_cl1sur0.Pclass
pof2ndd = p_cl2sur0.Pclass
pof3rdd = p_cl3sur0.Pclass

#Opening the window
root.mainloop()