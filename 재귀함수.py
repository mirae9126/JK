from tkinter import N


def count(num) :
    if num >=1 :
        print(num, end = ' ')
        count(num-1)
    else :
        return
count(10)
count(20)
