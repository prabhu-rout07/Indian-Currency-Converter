from tkinter import *
from tkinter import ttk

converter = Tk()
converter.geometry("630x400")
converter.title(" Indian_Currency_Converter")
converter.config(background="pink")

OPTIONS ={ "Austrillian Dollar" : 0.022,
          "Brazilian Real": 0.069,
          "Bulgerian lev":0.02512,
           "Euro":0.012,
           "Hong Kong Dollar": 0.10,
           "Japanese Yen": 1.41,
           "Saudi Riyal" : 0.049,
            "Nepalese Rupee":1.58,
           "Kuwaiti Dinar":0.0041,
           "Ru1ssian Ruble":1.03,
          "British Pound":0.01103,
          "Pakisthani Rupee":2.18,
          "US Dollar": 0.013,
          "Chinese Yuan" :0.093,
          "Bangladeshi Taka":1.12,
           "Singapore Dollar": 0.019,
          "Sri Lankan Rupee":2.49,
          "Swiss Franc": 0.013

    }

def ok():
    price = rupees.get()
    ans = variable.get()
    DICT = OPTIONS.get (ans,None)
    converted = float(DICT) * float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"CURRENCY CONVERTED \nINTO >>> ", INSERT,ans,INSERT,"\nAMOUNT IS : ", INSERT,converted)
    
appName = Label(converter, text="INDIAN CURRENCY CONVERTER", font =("impact",25,"bold","underline"), fg ="dark red", bg="pink")
appName.place(x=120, y=0)

result = Text(converter, height=5,width=50, font =("cooper",15,"bold","italic"), fg ="dark green", bd=5, bg="yellow")
result.place(x=30,y=50)


india = Label(converter, text="Indian Rupees: ",font =("",18,"bold"), fg ="red", bg="pink")
india.place(x=0, y=200)

rupees = Entry(converter, font =("calibri",20),bg="orange")
rupees.place(x=200,y=200)

choice = Label(converter, text="Choice ",font =("arial",18,"bold"), fg ="blue", bg="pink")
choice.place(x=0,y=250)

variable = StringVar(converter)
variable.set(None)
option = OptionMenu(converter, variable,*OPTIONS)
option.place(x=200,y=250, width=200, height=50)

button = Button(converter, text="CONVERT", font=("arial",20,), fg="red", bg="light blue", command=ok)
button.place(x=200, y=300)
converter.mainloop()
