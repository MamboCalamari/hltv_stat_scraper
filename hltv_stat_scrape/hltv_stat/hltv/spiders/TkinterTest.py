from Tkinter import *

#TODO: Documentation, Listeners for Scrape button (begin scrape, change team_title's)

class TkinterTest:

    def __init__(self):
        self.root = Tk()
        self.configure_root()
        self.main_frame = Frame(self.root)

        self.top_frame = Frame(self.main_frame)
        self.top_frame.grid()
        Label(self.top_frame, text="Team 1:").grid(row=0)
        self.team1_entry = Entry(self.top_frame)
        self.team1_entry.grid(row=0, column=1)
        Label(self.top_frame).grid(row=0, column=3, padx=100)
        Label(self.top_frame, text="Team 2:").grid(row=0, column=4)
        self.team2_entry = Entry(self.top_frame)
        self.team2_entry.grid(row=0, column=5, sticky=E)
        self.main_frame.pack()

        self.map_frame = Frame(self.main_frame)
        self.map_frame.grid()
        self._all = BooleanVar()
        self.dust2 = BooleanVar()
        self.mirage = BooleanVar()
        self.cache = BooleanVar()
        self.train = BooleanVar()
        self.cobblestone = BooleanVar()
        self.overpass = BooleanVar()
        self.nuke = BooleanVar()
        self.non_all = (self.dust2, self.mirage, self.cache, self.train, self.cobblestone, self.overpass, self.nuke)
        self.configure_map_frame()
        self.main_frame.pack()

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid()
        self.scrape_button = Button(self.button_frame, text="Scrape")
        self.scrape_button.grid(row=0, column=0)
        self.main_frame.pack()

        self.data_frame = Frame(self.main_frame)
        self.data_frame.grid()
        self.team1_title = StringVar()
        self.team2_title = StringVar()
        self.team1_record = StringVar()
        self.team2_record = StringVar()
        self.h2h_record = StringVar()
        self.configure_data_frame()

        self.team1_listbox_frame = Frame(self.data_frame)
        self.team1_listbox_frame.grid(row=2, column=0, padx=50)
        self.team1_scrollbar = Scrollbar(self.team1_listbox_frame)
        self.team1_scrollbar.pack(side=RIGHT, fill=Y)
        self.team1_listbox = Listbox(self.team1_listbox_frame ,yscrollcommand=self.team1_scrollbar.set, width=30)
        self.team1_listbox.pack()
        self.team1_scrollbar.config(command=self.team1_listbox.yview)

        self.h2h_listbox_frame = Frame(self.data_frame)
        self.h2h_listbox_frame.grid(row=2, column=1, padx=50)
        self.h2h_scrollbar = Scrollbar(self.h2h_listbox_frame)
        self.h2h_scrollbar.pack(side=RIGHT, fill=Y)
        self.h2h_listbox = Listbox(self.h2h_listbox_frame, yscrollcommand=self.h2h_scrollbar.set, width=30)
        self.h2h_listbox.pack()
        self.h2h_scrollbar.config(command=self.h2h_listbox.yview)

        self.team2_listbox_frame = Frame(self.data_frame)
        self.team2_listbox_frame.grid(row=2, column=2, padx=50)
        self.team2_scrollbar = Scrollbar(self.team2_listbox_frame)
        self.team2_scrollbar.pack(side=RIGHT, fill=Y)
        self.team2_listbox = Listbox(self.team2_listbox_frame, yscrollcommand=self.team2_scrollbar.set, width=30)
        self.team2_listbox.pack()
        self.team2_scrollbar.config(command=self.team2_listbox.yview)

        self.main_frame.pack()

        self.root.mainloop()

    def configure_root(self):
        self.root.resizable(width=False, height=False)

    def configure_map_frame(self):
        Label(self.map_frame, text="Map(s):").grid(row=0, column=0)

        all_check = Checkbutton(self.map_frame, text="All", variable=self._all, command=self.all_listener)
        all_check.grid(row=0, column=1)
        dust2_check = Checkbutton(self.map_frame, text="Dust II", variable=self.dust2, command=self.non_all_listener)
        dust2_check.grid(row=0, column=2)
        mirage_check = Checkbutton(self.map_frame, text="Mirage", variable=self.mirage, command=self.non_all_listener)
        mirage_check.grid(row=0, column=3)
        cache_check = Checkbutton(self.map_frame, text="Cache", variable=self.cache, command=self.non_all_listener)
        cache_check.grid(row=0, column=4)
        train_check = Checkbutton(self.map_frame, text="Train", variable=self.train, command=self.non_all_listener)
        train_check.grid(row=0, column=5)
        cobblestone_check = Checkbutton(self.map_frame, text="Cobblestone", variable=self.cobblestone, command=self.non_all_listener)
        cobblestone_check.grid(row=0, column=6)
        overpass_check = Checkbutton(self.map_frame, text="Overpass", variable=self.overpass, command=self.non_all_listener)
        overpass_check.grid(row=0, column=7)
        nuke_check = Checkbutton(self.map_frame, text="Nuke", variable=self.nuke, command=self.non_all_listener)
        nuke_check.grid(row=0, column=8)

    def configure_data_frame(self):
        Label(self.data_frame, textvariable=self.team1_title).grid(row=0, column=0, pady=10, padx=50)
        self.team1_title.set("Team 1 Stats:")

        Label(self.data_frame, text="Head to Head Stats:").grid(row=0, column=1, pady=10, padx=50)

        Label(self.data_frame, textvariable=self.team2_title).grid(row=0, column=2, pady=10, padx=50)
        self.team2_title.set("Team 2 Stats:")

        Label(self.data_frame, textvariable=self.team1_record).grid(row=1, column=0, padx=50)
        self.team1_record.set("0-0-0")

        Label(self.data_frame, textvariable=self.h2h_record).grid(row=1, column=1, padx=50)
        self.h2h_record.set("0-0-0")

        Label(self.data_frame, textvariable=self.team2_record).grid(row=1, column=2, padx=50)
        self.team2_record.set("0-0-0")

    def all_listener(self):
        if self._all.get():
            for var in self.non_all:
                var.set(FALSE)

    def non_all_listener(self):
        for var in self.non_all:
            if var:
                self._all.set(FALSE)
                return

tk1 = TkinterTest()