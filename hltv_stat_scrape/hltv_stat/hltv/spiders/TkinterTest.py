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

data_frame = Frame(main_frame)
data_frame.grid()

team1_title = StringVar()
Label(data_frame, textvariable=team1_title).grid(row=0, column=0, pady=10, padx=50)
team1_title.set("Team 1 Stats:")

Label(data_frame, text="Head to Head Stats:").grid(row=0, column=1, pady=10, padx=50)

team2_title = StringVar()
Label(data_frame, textvariable=team2_title).grid(row=0, column=2, pady=10, padx=50)
team2_title.set("Team 2 Stats:")

team1_record = StringVar()
Label(data_frame, textvariable=team1_record).grid(row=1, column=0, padx=50)
team1_record.set("0-0-0")

h2h_record = StringVar()
Label(data_frame, textvariable=h2h_record).grid(row=1, column=1, padx=50)
h2h_record.set("0-0-0")

team2_record = StringVar()
Label(data_frame, textvariable=team2_record).grid(row=1, column=2, padx=50)
team2_record.set("0-0-0")

team1_listbox_frame = Frame(data_frame)
team1_listbox_frame.grid(row=2, column=0, padx=50)

team1_scrollbar = Scrollbar(team1_listbox_frame)
team1_scrollbar.pack(side=RIGHT, fill=Y)

team1_listbox = Listbox(team1_listbox_frame ,yscrollcommand=team1_scrollbar.set)
team1_listbox.pack()

team1_scrollbar.config(command=team1_listbox.yview)

h2h_listbox_frame = Frame(data_frame)
h2h_listbox_frame.grid(row=2, column=1, padx=50)

h2h_scrollbar = Scrollbar(h2h_listbox_frame)
h2h_scrollbar.pack(side=RIGHT, fill=Y)

h2h_listbox = Listbox(h2h_listbox_frame ,yscrollcommand=h2h_scrollbar.set)
h2h_listbox.pack()

h2h_scrollbar.config(command=h2h_listbox.yview)

team2_listbox_frame = Frame(data_frame)
team2_listbox_frame.grid(row=2, column=2, padx=50)

team2_scrollbar = Scrollbar(team2_listbox_frame)
team2_scrollbar.pack(side=RIGHT, fill=Y)

team2_listbox = Listbox(team2_listbox_frame ,yscrollcommand=team2_scrollbar.set)
team2_listbox.pack()

team2_scrollbar.config(command=team2_listbox.yview)

main_frame.pack()

root.mainloop()