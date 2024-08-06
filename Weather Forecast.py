import requests
from bs4 import *
import tkinter as tk

#a = 0
#while a < 1:
try:
    city = input("Enter a valid city: ").title()
    if city.isalpha() == True:
        print
    else:
        print("Please only enter valid characters.")
    
    state = input("What state is the city in: ").upper()
    if len(state) == 2 and state.isalpha() == True:
        print
    else:
        print("Please only enter the abbreviated name of states.")
except:
    print("User input was invalid...")
    
end = "The current temperature in " + city + ", " + state + " is: "
    
### This website allows me to grab the coordinates of the city the User inputs.
r = requests.get('https://www.travelmath.com/cities/' + city + ', ' + state)
soup = BeautifulSoup(r.text, "html.parser")

## I grab the latitude in this for loop.
for txt1 in soup.find_all("p")[4]:
    print(txt1.text, txt1.next_sibling)
    lat = txt1.next_sibling
    lat = lat.strip()
    break

## I grab the longitude in this for loop.
for txt2 in soup.find_all("p")[5]:
    print(txt2.text, txt2.next_sibling)
    long = txt2.next_sibling
    long = long.strip()
    break

### In this website I use the coordinates from the previous one to query the city.
url2 = 'https://forecast.weather.gov/MapClick.php?lat=' + lat + '&lon=' + long
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.text, "html.parser")
## In the line below, I grab the information on what the current temperature is of the city.
final = soup2.find("p", class_= "myforecast-current-lrg").text

## Output displays what the city, state, and the current temp.
print(end + final)