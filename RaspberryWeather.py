import requests
import pprint
import json
import locale
from datetime import datetime
import weather
import time as t
import pyttsx3
import math
import pygame
import io

engine= pyttsx3.init()
engine.setProperty('volume',1)
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)     
engine.setProperty('voice', 'turkish+m1')


try:
    to_unicode = unicode
except NameError:
    to_unicode = str

#Read JSON file
try:
    with open('data.json') as data_file:
        data = json.load(data_file)
except Exception as error:
    print('json datası okunamadı!')

# Define data
today=datetime.now()
#print(today.hour)
#print(int(data['data']['date']))
#print(abs(today.hour - int(data['data']['date'])) )
if(abs(today.hour - int(data['data']['date']) ) > 5 ) :
        url = 'https://api.openweathermap.org/data/2.5/forecast?q=istanbul&appid=ec28b0f637ce212e97efe5b7dd1ea74c&units=metric'
        res =requests.get(url)
        data = res.json()

        data1 = {
                    'date': datetime.now().hour
        }
        datanew = {'data':data1,'forecast':data}
        # Write JSON file
        with io.open('data.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(datanew,
            indent=4, sort_keys=True,
            separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))


def func1():
       
       today = datetime.now()
       temp=0
       hum=''
       status=''

       tomorrow_weather = datetime(today.year,today.month,today.day+1,12)
       if(today.month  in  [3 , 5 , 7 , 8 , 10]):
           if (today.day == 31) :
               tomorrow_weather = datetime(today.year,today.month+1,1,12)
           
               
       elif(today.month in [4 , 6 , 9 , 11] ):
           if(today.day == 30):
               tomorrow_weather = datetime(today.year,today.month+1,1,12)
               
       elif(today.month == 2):
            if(today.day == 29):
               tomorrow_weather = datetime(today.year,today.month+1,1,12)
               
       elif(today.month == 12 and today.day == 31):
          tomorrow_weather = datetime(today.year+1,1,1,12)
       
          
       tarih = datetime.strftime(today, '%A')
       
       if tarih == "Tuesday" and today.hour == 16 and today.minute == 0 :
           pygame.mixer.init()
           pygame.mixer.music.load("bereket.mp3")
           pygame.mixer.music.play()
           while pygame.mixer.music.get_busy() == True:
              continue
           
       elif tarih == "Wednesday" and today.hour == 14 and today.minute == 8 :
           pygame.mixer.init()
           pygame.mixer.music.load("preprodlartestehazirmi.mp3")
           pygame.mixer.music.play()
           while pygame.mixer.music.get_busy() == True:
              continue
           
           
       if today.hour == 9 and today.minute == 4 :
           pygame.mixer.init()
           pygame.mixer.music.load("gunaydin.mp3")
           pygame.mixer.music.play()
           while pygame.mixer.music.get_busy() == True:
              continue
           
       if today.hour == 12 and today.minute == 22 :
           pygame.mixer.init()
           pygame.mixer.music.load("afiyetolsunmillet.mp3")
           pygame.mixer.music.play()
           while pygame.mixer.music.get_busy() == True:
              continue
           
       if today.hour == 17 and today.minute == 52 :
           pygame.mixer.init()
           pygame.mixer.music.load("hayirliaksamlar.mp3")
           pygame.mixer.music.play()
           while pygame.mixer.music.get_busy() == True:
             continue
           
           

           for val in data['forecast']['list']:
             weather_date = datetime.strptime(val['dt_txt'],'%Y-%m-%d %H:%M:%S')
             if(weather_date == tomorrow_weather):
                 temp = int(val['main']['temp'])
                 hum =  int(val['main']['humidity'])
                 status = str(val['weather'][0]['main'])    
           if (temp <= 0 ):
             pygame.mixer.init()
             pygame.mixer.music.load("kar.mp3")
             pygame.mixer.music.play()
             while pygame.mixer.music.get_busy() == True:
               continue
             
           elif ( 0 < temp and temp <= 10):
              pygame.mixer.init()
              pygame.mixer.music.load("yarinhavasoguk.mp3")
              pygame.mixer.music.play()
              while pygame.mixer.music.get_busy() == True:
                 continue
              
           elif ( 10 < temp and temp <= 15):
              pygame.mixer.init()
              pygame.mixer.music.load("birazcikserin.mp3")
              pygame.mixer.music.play()
              while pygame.mixer.music.get_busy() == True:
                 continue
              
           elif ( 15 < temp and temp <= 19):
               pygame.mixer.init()
               pygame.mixer.music.load("yarinhava.mp3")
               pygame.mixer.music.play()
               while pygame.mixer.music.get_busy() == True:
                     continue
               engine.say(temp)
               engine.runAndWait()
               pygame.mixer.init()
               pygame.mixer.music.load("derece.mp3")
               pygame.mixer.music.play()
               while pygame.mixer.music.get_busy() == True:
                     continue
               
           elif ( 19 < temp and temp <= 25):
               pygame.mixer.init()
               pygame.mixer.music.load("havagüzel.mp3")
               pygame.mixer.music.play()
               while pygame.mixer.music.get_busy() == True:
                  continue
               
           elif ( 25 < temp and temp <= 35):
               pygame.mixer.init()
               pygame.mixer.music.load("acikrenk.mp3")
               pygame.mixer.music.play()
               while pygame.mixer.music.get_busy() == True:
                   continue
               
           elif ( 35 < temp ):
                pygame.mixer.init()
                pygame.mixer.music.load("basinagünes.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                   continue
                
           if ( 60 < hum):
              pygame.mixer.init()
              pygame.mixer.music.load("yükseknem.mp3")
              pygame.mixer.music.play()
              while pygame.mixer.music.get_busy() == True:
                 continue
              
           if (status == "Rain") :
              pygame.mixer.init()
              pygame.mixer.music.load("yagmur.mp3")
              pygame.mixer.music.play()
              while pygame.mixer.music.get_busy() == True:
                 continue
              

func1()       


