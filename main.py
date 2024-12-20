import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import json

ctk.deactivate_automatic_dpi_awareness()
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green







class GUI(ctk.CTk): 
    def __init__(self):
        super().__init__()
        self.title("Wordel")
        self.resizable(0, 0)
        self.iconbitmap('images/Wordel.ico')

        self.game_frame = ctk.CTkFrame(self, corner_radius=10, bg_color="#2c2f33")

        self.start_page_frame = ctk.CTkFrame(self, corner_radius=10, bg_color="#2c2f33")
        self.difficulty = ctk.CTkTabview(self.start_page_frame, corner_radius=10, bg_color="#2c2f33", height=400, width=400, command=self.change_tree)
        

    
        self.easy = self.difficulty.add("Easy")
        self.normal = self.difficulty.add("Normal")
        self.hard = self.difficulty.add("Hard")
        


        self.tree = ttk.Treeview(self.easy)
        self.dic = { 
            0: self.easy,
            1: self.normal, 
            2:self.hard
        }

        self.start_page_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.start_page_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.start_page()        
        self.after(000, self.deiconify)
        self.labels = []
        self.num = 0
        self.win = False
        self.time = None

    def change_tree(self):
        self.tree.grid_forget()
        master = self.dic[self.difficulty.index(self.difficulty.get())]
        print(master, self.difficulty.index(self.difficulty.get()))
        self.tree = ttk.Treeview(master=master)
        self.tree_config()
        self.tree.grid()

    def start_page(self):
        self.start_page_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.difficulty.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.game_frame.grid_forget()
       
        self.tree_config()

    def tree_config(self):
        difficulty = self.difficulty.get().lower()
        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                    background="#2a2d2e",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#343638",
                    bordercolor="#343638",
                    borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                    background="#565b5e",
                    foreground="white",
                    relief="flat")
        style.map("Treeview.Heading",
                background=[('active', '#3484F0')])
        
        self.tree['columns'] = ('Name', 'Time')
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Name", anchor=tk.W)
        self.tree.column("Time", anchor=tk.CENTER)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Time", text="Time[s]", anchor=tk.CENTER)
        print(difficulty)
        with open(f"I_am_invisible/{difficulty}.json", "r") as json_file:   
            data = json.load(json_file)
        print(data)
        for i in data:
            self.tree.insert(parent='', index='end', iid=0, text='', values=(i, data[i]))
        self.tree.grid(sticky="nsew", padx=5, pady=5) 

        
    def place_buttons(self):
        self.nol = 5                                                #number of letters
        row = 0
        grd_row = (0, 1, 2, 3, 4, 5)
        grd_col = ()
        for i in range(self.nol):
            grd_col += (i,)
        self.random_word()

        for i in range(5):                                  
            for i in range(self.nol):
                col = i%self.nol
                print(col)
                label = ctk.CTkLabel(self.game_frame, text=" ", fg_color="white", corner_radius=10, width=100, height=100)
                label.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                self.labels.append(label)
            row += 1
        self.entry = ctk.CTkEntry(self.game_frame, corner_radius=10, placeholder_text="Enter a word")
        self.entry.grid(row=row, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        self.entry.bind("<Return>", self.check_word)
    
    def check_word(self, event):
        word = self.entry.get()
        if len(word) != self.nol or self.win:
            return
        wrong = 0
        for i in range(self.nol):
            if word[i] != self.word[i]:
                color = "#777b7e"
                wrong += 1
            if word[i]  in self.word:
                color = "#c8b356" 
                wrong += 1 
            if word[i] == self.word[i]:
                color = "#6aa963"
            
            self.labels[self.num].configure(fg_color=color, text=word[i], font=("Arial", 50), text_color="black")
            self.num+=1
        if wrong == 0:
            self.win = True
              
        self.entry.delete(0, "end")

    
    def random_word(self):
        self.word = "hello"



class Start_picture(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")        
        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        self.attributes("-fullscreen", True)
        self.attributes("-transparent", "white")
        self.after(2000, self.destroy)
        self.after(200, self.widget)
    
    def widget(self):
        self.image_label = ctk.CTkLabel(self, image=ctk.CTkImage(Image.open('images/Wordel.png'), size=(500, 500)), text=" ", width=500, height=500)
        self.image_label.grid(row=1, column=1)
            
     
if __name__ == "__main__":
    app = GUI()
    start_picture = Start_picture()
    start_picture.mainloop()
