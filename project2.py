# #Password Generator
# import tkinter as tk
# import random
# import string
# def generate():
#     length = int(entry.get())
#     chars = string.ascii_letters + string.digits
#     pwd = "".join(random.choice(chars) for _ in range(length))
#     label2.config(text=pwd)

# root = tk.Tk()
# root.title("Password Generator")

# tk.Label(root, text="Length:").pack()
# entry = tk.Entry(root)
# entry.pack()
# tk.Button(root, text="Generate", command=generate).pack()
# label2 = tk.Label(root, text="")
# label2.pack()
# root.mainloop()



## flip card
# import tkinter as tk
# cards = [("5+3=?", "8"), ("Capital of India?", "Delhi")]
# index = 0
# show_answer = False
# def flip():
#     global show_answer
#     show_answer = not show_answer
#     update_card()
# def next_card():
#     global index, show_answer
#     index = (index+1) % len(cards)
#     show_answer = False
#     update_card()
# def update_card():
#     q, a = cards[index]
#     label.config(text=a if show_answer else q)
# root = tk.Tk()
# root.title("Flashcards")
# label = tk.Label(root, text="", font=("Arial", 16))
# label.pack(pady=20)
# tk.Button(root, text="Flip", command=flip).pack()
# tk.Button(root, text="Next", command=next_card).pack()
# update_card()
# root.mainloop()