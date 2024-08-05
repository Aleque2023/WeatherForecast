import requests
from bs4 import *
import tkinter as tk

#a = 0
#while a < 1:

city = input("Enter a valid city: ")
if city.isalpha() == True:
    print
else:
    print("Please only enter valid characters.")
    
state = input("What state is the city in: ").upper()
if len(state) == 2 and state.isalpha() == True:
    print
else:
    print("Please only enter the abbreviated name of states.")
    
r = requests.get('https://www.travelmath.com/cities/' + city + ', ' + state)
print(r)
soup = BeautifulSoup(r.text, "html.parser")

end = "The current temperature in " + city + ", " + state + " is: "

for txt1 in soup.find_all("p")[4]:
    print(txt1.text, txt1.next_sibling)
    lat = txt1.next_sibling
    lat = lat.strip()
    break

for txt2 in soup.find_all("p")[5]:
    print(txt2.text, txt2.next_sibling)
    long = txt2.next_sibling
    long = long.strip()
    break

url2 = 'https://forecast.weather.gov/MapClick.php?lat=' + lat + '&lon=' + long
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.text, "html.parser")
final = soup2.find("p", class_= "myforecast-current-lrg").text

print(end + final)