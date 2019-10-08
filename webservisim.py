from google_speech import Speech
from flask import Flask, jsonify , flash, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import pygame
import threading
import logging
import os

YUKLEME_KLASORU = ''
UZANTILAR = set(['mp3'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = YUKLEME_KLASORU
app.secret_key = "Flask_Dosya_Yukleme_Ornegi"

def uzanti_kontrol(dosyaname):
   return '.' in dosyaname and \
   dosyaname.rsplit('.', 1)[1].lower() in UZANTILAR


playlist = [
    {
        'team':'prodify',
        'options you can play':'avengers.mp3 ,daily.mp3, pavyon.mp3 , games.mp3 ,izmirmarsi.mp3, team.mp3, withme.mp3, skyfall.mp3, supermario.mp3 , geceler.mp3 ,sehrimintadi.mp3 ,ironman.mp3 ,animals.mp3' 
        
    },
    {
        'team':'runway',
        'options you can play':'avengers.mp3 , games.mp3 ,pavyon.mp3,izmirmarsi.mp3, team.mp3, withme.mp3, skyfall.mp3, supermario.mp3 , gs.mp3'
    
    },
    {
        'team':'hayatagaci',
        'options you can play':'avengers.mp3 ,pavyon.mp3 , gs.mp3, games.mp3 ,izmirmarsi.mp3, geceler.mp3 ,sehrimintadi.mp3 , team.mp3, withme.mp3, skyfall.mp3, supermario.mp3 ,blackwidow.mp3'
    },
    {
        'team':'gevendeler',
        'options you can play':'avengers.mp3 ,pavyon.mp3 , games.mp3 ,izmirmarsi.mp3, team.mp3, withme.mp3, skyfall.mp3, supermario.mp3 ,animals.mp3 '
    
    },
    {
        'team':'lascrum',
        'options you can play':'avengers.mp3 , pavyon.mp3 , games.mp3 ,izmirmarsi.mp3, team.mp3, withme.mp3, skyfall.mp3, supermario.mp3 , bellaciao.mp3'
    }
]

def sayIt(speechText):
    lang = "tr"
    speech = Speech(speechText, lang)
    sox_effects = ("vol", "2.5")
    speech.play(sox_effects)
    

@app.route('/konustur/<string:param>')
def index(param):
    sayIt(param)
    return jsonify(param), 200


def soundIt(dosyaadi):
        
        pygame.mixer.init()
        pygame.mixer.music.load(dosyaadi)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
              continue

@app.route('/duyuru/<string:parametre>', methods=['GET'])
def index9(parametre):
    pygame.mixer.init()
    pygame.mixer.music.load("anons.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
            continue
    sayIt(parametre)
    return jsonify(parametre), 200
   
@app.route('/cal/b2b', methods=['GET'])
def index10():
    pygame.mixer.init()
    pygame.mixer.music.load("b2b.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
            continue
    return jsonify(parametre), 200   
   

@app.route('/playlist/<string:team_name>/<string:dosya>', methods=['GET'])
def index5(team_name ,dosya):
    x = threading.Thread(target=soundIt, args=(dosya,))
    x.start()
    dirpath = os.getcwd()
    #soundIt(dosya)
    #return jsonify({'directory': dirpath}),200
    return render_template('listen.html')   

@app.route('/playlist/<string:team_name>/', methods=['GET'])
def index4(team_name):
    sound = [sound for sound in playlist if sound['team'] == team_name]
    return jsonify(sound), 200
    if len(sound) == 0:
        return jsonify({'sound': 'Not found'}),404
   # return jsonify({'sound': sound})  


@app.route("/")
def hello():
      return render_template('index.html')


# Form ile dosya yükleme sayfası
@app.route('/dosyayukleme')
def dosyayukleme():
   return render_template("dosyayukleme.html")


# Form ile dosya yükleme sayfası - Sonuç
@app.route('/dosyayukleme/<string:dosya>')
def dosyayuklemesonuc(dosya):
   return render_template("dosyayukleme.html", dosya=dosya)

# Form ile dosya yükleme işlemi
@app.route('/dosyayukle', methods=['POST'])
def dosyayukle():
	
   if request.method == 'POST':
      
		# formdan dosya gelip gelmediğini kontrol edelim
      if 'dosya' not in request.files:
         flash('Dosya seçilmedi')
         return redirect('dosyayukleme')         
							
		# kullanıcı dosya seçmemiş ve tarayıcı boş isim göndermiş mi
      dosya = request.files['dosya']					
      if dosya.filename == '':
         flash('Dosya seçilmedi')
         return redirect('dosyayukleme')

		# gelen dosyayı güvenlik önlemlerinden geçir
      if dosya and uzanti_kontrol(dosya.filename):
         dosyaadi = secure_filename(dosya.filename)
         dosya.save(os.path.join(app.config['UPLOAD_FOLDER'], dosyaadi))
         #return redirect(url_for('dosyayukleme',dosya=dosyaadi))
         return redirect('dosyayukleme/' + dosyaadi)
      else:
         flash('İzin verilmeyen dosya uzantısı')
         return redirect('dosyayukleme')
							
   else:
      abort(401)        

if __name__ == "__main__":
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run(port=8455,host='0.0.0.0')
