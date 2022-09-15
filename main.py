import time
from plyer import notification
from tkinter import *
from PIL import Image, ImageTk 
import notification 

root =  Tk()
root.geometry("550x550")
root.title("Drink water Notification") 
root.resizable(False, False)  # disable resize 
 
# Main_frame

Main_frame = LabelFrame(root , padx = 100 , pady = 7 , borderwidth=3, relief= "raised") # inside padding 
Main_frame.grid( row = 0 , column = 1 , padx = 20, pady = 60) # outside pading 

# Here Lable 
lable_Display = Label(Main_frame , text = "Drinking water reminder" , font = ("Comic Sans MS" , 14 , "bold" ) , bg = "#C4C4C4" )
lable_Display.grid(row= 0,  column= 0 ,padx = 20 ,  pady = 10)

# Image 
Display_Image = ImageTk.PhotoImage(Image.open("image/drink.jpg"))
Default_Label = Label(Main_frame ,image = Display_Image)
Default_Label.grid(row = 1 , column = 0 , pady = 20)

# Entry Box
time_interver  =  Entry(Main_frame , width = 30 )
time_interver.insert(0, "Enter time:")
time_interver.grid(row = 2 ,column= 0 , padx=30)


# Notification funtion 

def Fun_notifi():
    t = int(time_interver.get())
    while True :
     notification.Notification()
     time.sleep(t)
     

# Button
button = Button(Main_frame , text = "SET" , bg = "#C4C4C4" , pady=16 , padx = 40 ,  borderwidth= 3, relief=SOLID, command = Fun_notifi )
button.grid(row = 3 ,column = 0 , pady = 10)


root.mainloop()    



   
           