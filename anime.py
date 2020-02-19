import webbrowser
import msvcrt as m
import re
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
    
def guardarFichero(web):
    f=open('fichero.txt', 'w')
    f.write(web)
def avanzar():
    web = abrirFichero()
    web2= web.split('/')
    inicio='01'
    final=16
    web3=web2[7].split('.')
    """while(web3[0] != "tomo"):
        if web3[0] < '09':
            sec=int(web3[0])
            sec+=1
            secf = str(sec)
            web="http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/0"+secf+".html"
            final +=1
        else:
            sec=int(web3[0])
            sec+=1
            secf = str(sec)

            web="http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+secf+".html"
            final +=1"""
    if (int(web3[0]) >= final):
        print "es el ultimo cap, reiniciamo"# si es ultim capitol poso a 0 les pagines del manga amb INICIO i passo de capitol amb PROXIMO
        proximo0 = int(web2[6])
        proximo0 +=1
        proximo = str(proximo0)
        webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+inicio+".html", new = 1, autoraise=True) #obro el nou capitol
        webfn = "http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+inicio+".html" #el guardo
        guardarFichero(webfn)
    else:
        # si no era la ultima pagina del manga, nomes sumo 1 a la pagina pero no passa res perque continui llegint el manga i guardo
        #aquesta direccio NO SE SI ESTA MOLT BE AQUESTA PART JAJA
        print "no es el ultimo"
        proximo = web2[6]
        siguiente0=web3[0]

        if (siguiente0 <'09'):
            siguiente0 = int(web3[0])
            siguiente0 += 1
            siguiente = str(siguiente0)
            webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/0"+siguiente+".html", new = 1, autoraise=True)
            webfn = "http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/0"+siguiente+".html"
            guardarFichero(webfn)
            print webfn
        else:
            siguiente0 = int(web3[0])
            siguiente0 += 1
            siguiente = str(siguiente0)
            webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+siguiente+".html", new = 1, autoraise=True)
            webfn = "http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+siguiente+".html"
            guardarFichero(webfn)

def retroceder():
    web=abrirFichero()
    final=0
    web2= web.split('/')
    final=15
    inicio='01'
    web3=web2[7].split('.')

    if (int(web3[0]) <= int(inicio)): # si es el primer retrocedeixo de capitol
        proximo0 = int(web2[6])
        proximo0 -= 1
        proximo = str(proximo0)
        webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+inicio+".html", new = 1, autoraise=True)
        webfn = "http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+inicio+".html"
        guardarFichero(webfn)
    else:
        proximo = web2[6]
        anterior0=web3[0]
        if (anterior0 <='10'):
            anterior0 = int(web3[0])
            anterior0 -= 1
            anterior = str(anterior0)
            webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/0"+anterior+".html", new = 1, autoraise=True)
            webfn = "http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/0"+anterior+".html"
        else:
            anterior0 = int(web3[0])
            anterior0 -= 1
            anterior = str(anterior0)
            webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+anterior+".html", new = 1, autoraise=True)
            webfn = "http://www.onepiecemangayanime.com/mangaonline/manga/tomo084/"+proximo+"/"+anterior+".html"
        guardarFichero(webfn)
    
def key(event):
                             
    if (event.keysym != 'Right' or event.keysym != 'Left' or event.char != 'f' or event.char != 'g'):
        root.bind_all('<Key>', key)
        if event.keysym == 'Right':
            avanzar()
            
        if event.keysym == 'Left':
            retroceder()
            # normal number and letter characters
        elif event.char == 'f':
            # charcters like []/.,><#$ also Return and ctrl/key
            raise SystemExit
        elif event.char == 'g':
            nuevoGuardar()
#def animeContinua():

def animeEscull():
    webbrowser.open("http://www.onepiecemangayanime.com/mangaonline/manga.php", new=0, autoraise= True)

    """print "por que tomo, capitulo y pagina quieres empezar?"
    tomo=raw_input() # pedimos una pagina
    tomo2 = str(tomo) # la ponemos como '085' porque sino no lo acepta
    capitulo = raw_input()
    capitulo2 = str(capitulo)
    pagina=raw_input()
    pagina2 = str(pagina)
    tecla=input #lo declaramos como input
    web2= web.split('/')
    web3 = web2[7].split('.')
    web4=web2
    tomof = re.split('(\d+)',web4[5]) #separamos el tomo085 en tomo y 085
    tomoFinal = tomof[1].replace(tomof[1],tomo2) #pillamos la parte del 085 y la reemplazamos
    web = web.replace(web2[5], "tomo" + tomoFinal)#reemplazamos el tomo + la palabra tomo porque lo pide la url
    print web
    web = web.replace(web2[6], capitulo)
    print web
    web= web.replace(web3[0], pagina)
    print web
    guardarFichero(web)
    webbrowser.open(abrirFichero(), new=1, autoraise=True)"""

    
def abrirFichero ():
    f=open('fichero.txt', 'r')
    print "almenos esto si que va"
    return f.read()
def nuevoGuardar():
    web=abrirFichero()
    guardarFichero(web)
    
        
if __name__ == "__main__":
    fora = input
    tecla=input
    print "vols continuar per on l'ultim cop?"
    resposta=raw_input()
    if (resposta=='s'):
        webbrowser.open(abrirFichero(), new = 0, autoraise=True)
        root = tk.Tk()
        print( "Press a key (Escape key to exit):" )
        root.bind_all('<Key>', key)
        root.mainloop()
    elif (resposta == 'n'):# si la respuesta es n entendemos que no
        animeEscull()
        print "abrimos la nueva"#elegiremos la nueva pagina etc
        root = tk.Tk()
        print( "Press a key (Escape key to exit):" )
        root.bind_all('<Key>', key)
        root.mainloop()
        
            

    
    

    
	
    
