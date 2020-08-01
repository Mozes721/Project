from tkinter import *
from tkinter.ttk import *
import Tkinter_projects as bck


def main():


    root = Tk()
    root.title("Age Calculator...")
    root.geometry("250x200")

    #setting up the image
    Style().configure("TFrame", background="#333")

    #Info text
    t1 = Label(root, text="Calculate your age now!")
    t1.grid(row = 0, column = 1, sticky = W, pady = 2)

    # this will create a label widget
    l1 = Label(root, text = "Name")
    l2 = Label(root, text = "Year")
    l3 = Label(root, text = "Month")
    l4 = Label(root, text = "Day")



    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row = 1, column = 0, sticky = W, pady = 2)
    l2.grid(row = 2, column = 0, sticky = W, pady = 2)
    l3.grid(row = 3, column = 0, sticky = W, pady = 2)
    l4.grid(row = 4, column = 0, sticky = W, pady = 2)

    #Entry widgets
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e4 = Entry(root)

    #arrange the widgets
    e1.grid(row = 1, column = 1, sticky = W, pady = 2)
    e2.grid(row = 2, column = 1, sticky = W, pady = 2)
    e3.grid(row = 3, column = 1, sticky = W, pady = 2)
    e4.grid(row = 4, column = 1, sticky = W, pady = 2)

    def open_window():
        sub = Tk()
        sub.title('Your age is')
        sub.geometry('150x100')
        l5 =Label(sub, command=bck.calculate_age(e2.get(), e3.get(), e4.get()), text='Hy ' + e1.get() + ' you are ')
        l5.grid(row=0, column=0, sticky = W, pady = 2)



    #Button
    B = Button(root, text="Calculate Age", command=open_window)
    B.grid(row = 5, column = 1)

    root.mainloop()

if __name__ == '__main__':
    main()
