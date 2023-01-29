# mise en place d'un sign up 
import tkinter
from customtkinter import CTk, CTkLabel,CTkFrame,CTkEntry,CTkButton
import container as ct
# il faut que je pousses un peu vers le centrer la partie email et autre 
# creation de la fenêtre 

class sign_ups(tkinter.Tk):
     
    width = 720
    height = 510
    # fonts = ("Fauna One",15)
    couleur_principal = "#363c54"
    
    emails = "kankoffi36@gmail.com"
    passwords= "123456789"
    
    def __init__(self):
        super().__init__()
        
        self.title("sign up")
        self.resizable(False, False)
        self.width_screen = self.winfo_screenwidth() # donne la largeur de ton ecran
        self.height_screen = self.winfo_screenheight() # donne la hauteur de ton ecran 
        self.x_coordinate =  (self.width_screen/2)-(self.width/2)
        self.y_coordinate = (self.height_screen/2)-(self.height/2)
        self.geometry("%dx%d+%d+%d"%(self.width,self.height,self.x_coordinate,self.y_coordinate))
        self.config(bg="#fff")
        #self.overrideredirect(1)
        # permet de centrer l'écran 
        
        #*creation d'évènement pour le placeholder
        #*creation d'un label avec customtkinter
        #creation d'un label : ikhela, je l'es creer avec CTk pour faire des bord arrondies
        # ikhela = CTkLabel(self, text="Ikhela",corner_radius=50,fg_color=("#fff",self.couleur_principal),justify=LEFT,text_font=("Fauna     One",    15))
        # ikhela.place(x=15,y=10)
        
        # *creation du frame center 
        self.center_frame = tkinter.Frame(self,width="300",height="300",bg="#fff")
        self.center_frame.pack(expand="yes")
        
        
        #*creation du sign up avec les entrés et le placeholder
        #creation du email entry
        self.email_entry = CTkEntry(self.center_frame,width=220,height=60   ,placeholder_text="Email",    placeholder_text_color="#9898a7",fg_color="#fff",border_color=self.couleur_principal,justify="center",corner_radius=40,    text_color=self.couleur_principal)
        self.email_entry.pack(pady=25,padx=(195,0))
        
        #passeword entry
        self.password_entry = CTkEntry(self.center_frame,width=220,height=60   ,placeholder_text="Passeword",placeholder_text_color="#9898a7",fg_color="#fff",border_color=self.couleur_principal,
        justify="center",corner_radius=40,text_color=self.couleur_principal)
        self.password_entry.pack(pady=20, padx=(195,0))
        
        #powerby ikhela 
        self.power_label = CTkLabel(self,text="Powerby ikhela & co",fg_color="#fff", text_color=self.couleur_principal)
        self.power_label.place(x=15,y=462)
        
        #creation du boutton avec Ctk
        self.button_sg = CTkButton(self.center_frame, text="Sign Up",width=220,corner_radius=40,height=60 ,fg_color="#363c53",border_color="#fff",text_color="#e5e5e5",hover_color=("#253265","#31364c"), cursor="hand2", relief="sunken", command=self.function_1)
        self.button_sg.pack(pady=(60,0),padx=(195,0))
        
        
        #* deplacer l'image les champs de texte un peu vers la droite 
        #* creation d'un canvas 
        self.image = tkinter.PhotoImage(file="C:/Powershell full course/futur.png")
        self.canvas = tkinter.Canvas(self,width=310,height=510,background=self.couleur_principal,bd=0,highlightthickness=0,relief = "ridge")
        self.canvas.create_image(310,510,image=self.image)
        self.canvas.place(x=0,y=0)
        
    def function_1(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if (self.emails == email.strip()) and (self.passwords == password.strip()):
            self.destroy()
            
            # utilisation du module qui permet d'avoir accès au container principal
            ct.project()
            ct.mainloop()
        
            


if __name__ =="__main__":
    sign = sign_ups()
    sign.mainloop()
