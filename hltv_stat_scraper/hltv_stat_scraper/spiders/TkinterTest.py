from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.resizable(width=False, height=False)

main_frame = Frame(root)

top_frame = Frame(main_frame)
top_frame.grid()

Label(top_frame, text="Team 1:").grid(row=0)

team1_entry = Entry(top_frame)
team1_entry.grid(row=0, column=1)

Label(top_frame).grid(row=0, column=3, padx=100)
Label(top_frame, text="Team 2:").grid(row=0, column=4)

team2_entry = Entry(top_frame)
team2_entry.grid(row=0, column=5, sticky=E)

main_frame.pack()

map_frame = Frame(main_frame)
map_frame.grid()

Label(map_frame, text="Map(s):").grid(row=0, column=0)

_all = BooleanVar()
all_check = Checkbutton(map_frame, text="All", variable=all)
all_check.grid(row=0, column=1)

dust2 = BooleanVar()
dust2_check = Checkbutton(map_frame, text="Dust II", variable=all)
dust2_check.grid(row=0, column=2)

mirage = BooleanVar()
mirage_check = Checkbutton(map_frame, text="Mirage", variable=all)
mirage_check.grid(row=0, column=3)

cache = BooleanVar()
cache_check = Checkbutton(map_frame, text="Cache", variable=all)
cache_check.grid(row=0, column=4)

train = BooleanVar()
train_check = Checkbutton(map_frame, text="Train", variable=all)
train_check.grid(row=0, column=5)

cobblestone = BooleanVar()
cobblestone_check = Checkbutton(map_frame, text="Cobblestone", variable=all)
cobblestone_check.grid(row=0, column=6)

overpass = BooleanVar()
overpass_check = Checkbutton(map_frame, text="Overpass", variable=all)
overpass_check.grid(row=0, column=7)

nuke = BooleanVar()
nuke_check = Checkbutton(map_frame, text="Nuke", variable=all)
nuke_check.grid(row=0, column=8)

main_frame.pack()

button_frame = Frame(main_frame)
button_frame.grid()

scrape_button = Button(button_frame, text="Scrape")
scrape_button.grid(row=0, column=0)

main_frame.pack()

# test_frame = Frame(main_frame)
# test_frame.grid()
#
# test_image = PhotoImage()

main_frame.pack()

root.mainloop()