import tkinter
from tkinter import *
from tkinter import font
import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
import webbrowser
Key='e0f879fdfa894478a9c4ec2428700641'
#command
def exeuc():
 samNumber=phonenumbers.parse(number)
 yourLocation=geocoder.description_for_number(samNumber,"en")
 #print(yourLocation)
 service_provider=phonenumbers.parse(number)
 car=carrier.name_for_number(service_provider,"en")
 from opencage.geocoder import OpenCageGeocode
 Geocoder=OpenCageGeocode(Key)
 query=str(yourLocation)
 results=Geocoder.geocode(query)
 #print(results)
 lat=results[0]['geometry']['lat']
 lng=results[0]['geometry']['lng']
 #print(lat,lng)
 myMap=folium.Map(location=[lat,lng],zoom_start=9)
 folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
 myMap.save('myLocation.html')
 #GUI FOR 2nd window with info
 def callback(url):
     webbrowser.open_new_tab(url)
 #newwin=tkinter.Tk()
 win.title('Information')
 win.geometry('300x300')
 btn.destroy()
 #Toplevel(newwin)
 Label(win,text='Information')
 var=StringVar()
 label=Label(win,textvariable=var,relief=FLAT)
 var.set("Country:"+str(yourLocation)+"\nService Provider:"+str(car)+"\nLatitude:"+str(lat)+"\nLongitude:"+str(lng))
 link=Label(win,text="Location",fg="blue",cursor='hand2')
 link.pack()
 link.bind("<Button-1>",lambda e:
 callback("myLocation.html"))
 label.pack()
 win.mainloop()
#GUI
win=tkinter.Tk()
win.title('ALERT')
win.geometry('300x300')
photobutn=PhotoImage(file='button.png')
btn=Button(win,text='ALERT',bd='5',bg='red',image=photobutn,command=exeuc)
btn.pack(side='top')
win.mainloop()
