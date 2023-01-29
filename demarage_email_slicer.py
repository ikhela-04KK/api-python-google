
from tkinter.ttk import Progressbar
import tkinter
from tkinter import ttk
from PIL import Image , ImageTk
import time
import sign_up as su


# jmise en place de trois module et reliéés pour permettre le bon fonctionnement des widgets.

# je n'est pas encore ajouter la base de donnée je sais aussi que cette tache sera très difficile s

# plus de module interconnectés plus de donnée à faire circuler 
# mais je sais que je vais arriver 
# je dois bien utilisé cette particularité , c'est vrai que c'est un seul proje mais j'ai l'occasion de mettre tout mon savoir d=la dedans ,  je rappelle nous ne sommes pas pressés , nous avançons pas à pas 

class demarage(tkinter.Tk):
    
    width=720
    height=510
    def __init__(self):
        super().__init__()
        self.title("Ikhela")
        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        self.x_coordinate = (self.width_screen/2) - (self.width/2)
        self.y_coordinate = (self.height_screen/2)-(self.height/2)
        self.geometry("%dx%d+%d+%d"%(self.width,self.height,self.x_coordinate,self.y_coordinate))
        self.overrideredirect(1)
        
        #pour lees commandes avec les touches 
        self.bind("<Enter>",self.bar)
        
        
        # background de l'élément et le style 
        self.config(background="#363c54")
    
    
        #*creation du frame centrer dans la fenêtre
        self.center_frame = tkinter.Frame(self,bg="#363c54")
        self.center_frame.pack(expand="yes")
    
    
        #*text dans le label center
         
        ## titre
        self.c_titrelabel=tkinter.Label(self.center_frame, text="Ikhela", font=("Fauna One", 26),fg="#f0f0f0",bg="#363c54")
        self.c_titrelabel.pack()
    
        ## sous-titre
        self.c_stitrelabel=tkinter.Label(self.center_frame, text="Appuyer sur la touche Entrer", font=("Cambria",10),fg="#f0f0f0",bg="#363c54")
        self.c_stitrelabel.pack(pady=15)
    
        ## entry_center
        self.c_titrelabel = tkinter.Entry(self.center_frame,font=("Cambira",20),bd=0,fg="#f0f0f0",bg="#363c54",justify="center")
        self.c_titrelabel.pack(pady=15)
    
    
        #*creation du powerby
        self.w_produc_title=tkinter.Label(self,text="Powered by Ikhela & Co",font=("Fauna One",7),bg="#363c54",fg="#ffffff")
        self.w_produc_title.place(x=15,y=450)
    
    
        #*faire une bar de progression
        self.styles=ttk.Style()
        self.styles.theme_use('clam')# voir comment changer le theme en un theme plus convenanles 
        self.styles.configure("red.horizontal.TProgressbar",foreground='red',background="#363c54")
        self.progress=Progressbar(self.center_frame,style="red.Horizontal.TProgressbar",orient="horizontal",length=200,mode='indeterminate')
        self.progress.pack(pady=10)
        
    # methode pour faire la bar de progression     
    def bar(self,event):
        for r, _ in enumerate(range(186)):
            self.progress['value'] = r
            self.update_idletasks()
            time.sleep(0.03)
        self.destroy()
        
        # importation  du module sign_up qui permet d'acceder directement au lecteur de menu 
        
        open_s = su.sign_ups()
        open_s.mainloop()

if __name__=="__main__":
    app = demarage()     
    app.mainloop()



