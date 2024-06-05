
# import wikipedia

# from tkinter import *


# def wiki(text):

#     t = wikipedia.summary(text)

#     Fact = t
#     root = Tk()
#     root.geometry("600x600")
#     T = Text(root, height = 30, width = 30)

#     l = Label(root, text = "result of the query")
#     l.config(font =("Courier", 14))

#     b2 = Button(root, text = "Exit", command = root.destroy)

#     l.pack()
#     T.pack()

#     b2.pack()

#     T.insert(END, Fact)

#     mainloop()



import wikipedia
from tkinter import *

def wiki(text):
    try:
        t = wikipedia.summary(text)
    except wikipedia.exceptions.DisambiguationError as e:
        t = "DisambiguationError: The term you entered may refer to multiple topics:\n" + "\n".join(e.options)
    except wikipedia.exceptions.PageError:
        t = "PageError: The page does not exist."
    except Exception as e:
        t = f"An error occurred: {e}"

    Fact = t
    root = Tk()
    root.geometry("600x600")
    T = Text(root, height = 30, width = 70)
    
    l = Label(root, text = "Result of the query")
    l.config(font = ("Courier", 14))

    b2 = Button(root, text = "Exit", command = root.destroy)

    l.pack()
    T.pack()
    b2.pack()

    T.insert(END, Fact)

    mainloop()

# Example usage
wiki("elections")
