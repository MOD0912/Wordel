import customtkinter as ctk
from PIL import Image, ImageTk
import pyautogui

ctk.deactivate_automatic_dpi_awareness()
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class Start_picture(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="white")        
        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        self.attributes("-fullscreen", True)
        self.attributes("-transparent", "white")

        self.after(2000, self.destroy)
        self.widget()
    
    def widget(self):
        self.image = ctk.CTkImage(Image.open('images/Wordel.png'), size=(500, 500))
        self.image_label = ctk.CTkLabel(self, image=self.image, text=" ", width=500, height=500)
        self.image_label.grid(row=1, column=1)




class GUI(ctk.CTk): 
    def __init__(self):
        super().__init__()
        self.title("Wordel")
        print(self.size())
        self.resizable(0, 0)
        self.iconbitmap('images/Wordel.ico')
        self.after(2000, self.deiconify)
        self.labels = []
        self.place_buttons()
        self.num = 0
        self.win = False
        
    def start_picture(self):
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.image = ctk.CTkImage(Image.open('images/Wordel.png'), size=(self.width, self.height))
        self.image_label = ctk.CTkLabel(self, image=self.image, text=" ", width=self.height, height=self.width)
        self.image_label.grid(row=0, column=0, columnspan=5, rowspan=6)
        self.after(2000, self.image_label.destroy)
        screen_width, screen_height = pyautogui.size()
        print(screen_width, screen_height)
        #self.geometry(f"{self.width}x{self.height}+{int(screen_width/2 - self.width/2)}+{int(screen_height/2 - self.height/2)}")
        
    def place_buttons(self):
        self.nol = 5                                                #number of letters
        row = 0
        grd_row = (0, 1, 2, 3, 4, 5)
        grd_col = ()
        for i in range(self.nol):
            grd_col += (i,)
        self.grid_rowconfigure(grd_row, weight = 1)
        self.grid_columnconfigure(grd_col, weight = 1)
        self.random_word()

        for i in range(5):                                  
            for i in range(self.nol):
                col = i%self.nol
                print(col)
                label = ctk.CTkLabel(self, text=" ", fg_color="white", corner_radius=10, width=100, height=100)
                label.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                self.labels.append(label)
            row += 1
        self.entry = ctk.CTkEntry(self, corner_radius=10, placeholder_text="Enter a word")
        self.entry.grid(row=row, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        self.entry.bind("<Return>", self.check_word)
        self.after(70, self.start_picture)
    
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
        
            
     
if __name__ == "__main__":
    start_picture = Start_picture()
    start_picture.update()
    app = GUI()
    app.mainloop()