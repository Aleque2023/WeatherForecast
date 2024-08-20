from tkinter import *
import requests
from bs4 import *

window = Tk()

window.geometry("400x300")

icon = PhotoImage(file="weatherLogo.png")
window.iconphoto(True, icon)
window.title("Current Weather for any US City")
    
def clear():
    entryCity.delete(0, END)
    entryState.delete(0, END)
    labelEnd.destroy()
    subBtn['state'] = NORMAL

def getWeather():
        city = entryCity.get()
        state = entryState.get()
        global labelEnd
        if (city == "" or state == ""):
            end="Nothing was entered in a textbox"
            labelEnd = Label(window)
            labelEnd.grid(row=3, column=0, columnspan=2)
            labelEnd.config(text=end)
            subBtn['state'] = DISABLED
        else:    
            r = requests.get("https://www.travelmath.com/cities/" + city + ", " + state)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                for txt1 in soup.find_all("p")[4]:
                    lat = txt1.next_sibling
                    lat = lat.strip()
                    break

                for txt2 in soup.find_all("p")[5]:
                    long = txt2.next_sibling
                    long = long.strip()
                    break
                
                url2 = "https://forecast.weather.gov/MapClick.php?lat=" + lat + "&lon=" + long
                r2 = requests.get(url2)
                soup2 = BeautifulSoup(r2.text, "html.parser")
                final = soup2.find("p", class_= "myforecast-current-lrg").text
                end = "The current temperature in " + city + ", " + state + " is: " + final
                subBtn['state'] = DISABLED
            except:
                end = "The City, or State was incorrect."
                subBtn['state'] = DISABLED
            labelEnd = Label(window)
            labelEnd.grid(row=3, column=0, columnspan=2)
            labelEnd.config(text=end)
            
def caps(event):
    v.set(v.get().upper())

def title(event):
    w.set(w.get().title())

labelCity = Label(window, 
                  text="Enter City Name:", 
                  justify="left")
labelCity.grid(row=0, column=0)
w = StringVar()
entryCity = Entry(window, 
                  font=("times new roman", 10), 
                  textvariable=w)
entryCity.bind("<KeyRelease>", title)
entryCity.grid(row=0,column=1)

labelState = Label(window, 
                   text="Enter State Name:", 
                   justify="left")
labelState.grid(row=1, column=0)
v = StringVar()
entryState = Entry(window, 
                   font=("times new roman", 10), 
                   textvariable=v)
entryState.bind("<KeyRelease>", caps)
entryState.grid(row=1, column=1)

subBtn = Button(window, 
                command=getWeather, 
                text="submit", 
                width=15)
subBtn.grid(row=2,column=0)

clearBtn = Button(window, 
                  command=clear,
                  text="clear", 
                  width=15)
clearBtn.grid(row=2, column=1)

window.mainloop()