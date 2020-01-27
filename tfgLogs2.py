import os,collections
import logging

def llegirCoordenades(roots,files):
    coordenadesInicials = {}
    linees = ()
    for i in files:#inicialitzem el diccionari de localitzacions amb els ids i totes les coordenades buides
        i = i.split('.') #volem obtindre el nom del fitxer per inicialitzar el diccionari amb el id
        index = i[0]
        coordenadesInicials.update({index:[]})
        
    for j in files: #donem valor a cada ID del diccionari
        f=open(roots +'/'+ j, 'r') #obrim fitxers de un en un
        j = j.split('.')
        index=j[0]
        linees=f.readlines() #guardem el conjunt de linees del fitxer que tractem
        for l in linees:
            linees = l.split(',')
            tuples = (linees[2],linees[3]) #guardem les COORDENADES de cada linea del fitxer pertinent
            coordenadesInicials[index].append(tuples) #anem creant un diccionari amb un id i totes les trajectories tal que: {1:[(lat,long),(lat,long)],2:...}
        f.close()
    return coordenadesInicials

def interseccions(coordenadesInicials):
    interseccions=[]
    interRepetides=[]

    for i in range(len(coordenadesInicials.items())-1): #de cada parella de longitud i latitud de cada fitxer busquem les repetides
	for j in coordenadesInicials.values()[i]:
	    for k in coordenadesInicials.values()[i+1]:
                if j == k:
                    interseccions.append(j)
            
    for i,y in collections.Counter(interseccions).items(): #recorrem totes les lats i contem les latituds repetides amb un valor de lambda = 4
        if (y>0):
            interRepetides.append(i) #s'afegeixen en cas d'existir, a un array

    return interRepetides

def IdPosicionsRepetides(posRepetides):
    idPos=[]
    for j in posRepetides: #per cada una de les posicions repes
        count=0
        for k in range(len(coordenadesInicials.values())): #per a la llargada del vector de totes les latituds,longituds inicials
            l=0
            while (l<len(coordenadesInicials.values()[k])): #anem recorrent cada tupla de lat,long inicial fins arribar a la ultima
                if (coordenadesInicials.values()[count][l] == j): #accedim a totes les tuples de cada key, dins totes les tuples amb el parametre count accedim als keys de 1 en 1
                    #dins cada key tenim un conjunt de tuples, amb el parametre l accedim a cada tupla de key en el que estiguem individualment 
                    idPos.append(tuple((coordenadesInicials.keys()[count],j)))#com estem dins la condicio de haver trobat una tupla igual a la del array que teniem guardat, afegim una tupla que ens digui 
                    l=l+1 #el key i la tupla per cada repe que trobi
                else:
                    pass
                    l=l+1 #seguent tupla del mateix key
            count=count+1 #seguent key
    idPos = list(set(idPos)) #treiem els repes i ho posem en forma de llista
    return idPos


def swapLocalitzacions(idPosRepetides): #canviarem les trajectories a partir de la seguent que trobem que sigui igual
    idFet=0
    z=0
    id2Fet=0
    mida=0
    swap=[]
    swap2=[]
    LOG_FILENAME = 'logFile.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    while (mida < len(idPosRepetides)-1):#anirem recorrent totes les latituds que hem trobat que es repeteixen menys la ultima
        trobat = False
        trobat2= False
        temp = []
        temp2=[]
        count2=0
        if idPosRepetides[mida][0] in coordenadesInicials: #nomes per entrar si o si a aquest bucle
            count = 0
            for x in coordenadesInicials[idPosRepetides[mida][0]]:#recorrem totes les trajectories que tenim i busquem la que tingui un id = al que tenim guardat
                if x == idPosRepetides[mida][1] and count2<1:#quan el trobem
                    trobat2 = True
                    count2=count2+1
                    idFet = count+1
                    if not temp: 
                        temp = coordenadesInicials[idPosRepetides[mida][0]][count+1:]#afegim el conjunt de trajectories a partir del de despres a un array buit
                    else:
                        temp.append(coordenadesInicials[idPosRepetides[mida][0]][count+1:])
                else:
                    pass
                count = count+1
    	else:
            pass
        coun = 0
	if trobat2 == True: #fem el mateix que abans, pero comprovem del conjunt de ids que tenim els de despres del que hem trobat a dalt
            for i in range(1,len(idPosRepetides)-mida):
                if idPosRepetides[mida+i][0] in coordenadesInicials and idPosRepetides[mida+i][1] == idPosRepetides[mida][1]:
                    trobat=True
                    count3 = 0
                    if trobat and coun <1:
                        for x in coordenadesInicials[idPosRepetides[mida+i][0]]:
                            if x == idPosRepetides[mida+i][1] and coun<1:
                                print x
                                coun = coun+1
                                z=z+1
                                id2Fet = count3+1
                                if not temp2:
                                    temp2 = coordenadesInicials[idPosRepetides[mida+i][0]][count3+1:]
                                else:
                                    temp2.append(coordenadesInicials[idPosRepetides[mida+i][0]][count3+1:])
                                logging.debug('canvi numero' + ' '+str(z)+' ' +'del ID:'+' ' + str(idPosRepetides[mida][0])+' ' + 'a partir de'+' ' + str(coordenadesInicials[idPosRepetides[mida][0]][idFet-1]))
                                logging.debug('-----------------')
                                logging.debug('canvi del ID'+' ' + str(idPosRepetides[mida+i][0])+' ' + 'a partir de'+' ' + str(coordenadesInicials[idPosRepetides[mida+i][0]][count3]))
                                logging.debug('----------------------------------')
                                coordenadesInicials[idPosRepetides[mida][0]][idFet:] = temp2 #aqui finalment fem el swap. del vector que hem trobat a dalt que coincidia amb el id emmagatzemat, a partir de la localitzacio trobada, el seguent li posem l'array que hem afegir del id seguent
                                coordenadesInicials[idPosRepetides[mida+i][0]][id2Fet:] = temp#li posem el array que teniem guardat del id anterior
                                
			    count3 = count3+1
    		    else: pass
		else:
                    pass

	mida= mida+1
    return coordenadesInicials



def generarNousFitxers(coordenadesFinals):
    for i in coordenadesFinals:
        f = open('C:/Users/SatecSistemas/Desktop/programillas/tfg/coordenadesFinals/' + i +".txt",'a')
        f.write(str(coordenadesFinals[i]))
        
if __name__ == "__main__":
    
      
    PosicionsRepetides=[]
    idPosRepetides=[]
    coordenadesInicials = {}
    coordenadesFinals = {}
    for (roots,dir,files) in os.walk('C:/Users/SatecSistemas/Desktop/programillas/tfg/coordenades'): #si eso ya cambio la ruta
        coordenadesInicials = llegirCoordenades(roots,files)#ja tinc totes les coordenades guardades a coordenadesUsuaris, compta ara les que estan repetides
    PosRepetides = interseccions(coordenadesInicials)

    idPosRepetides = IdPosicionsRepetides(PosRepetides)#obtenim els ids de les latituds repetides
    #idLongiRepetides = IdLongitudsRepetides(longiRepetides)#obtenim els ids de les longituds repetides
    coordenadesFinals = swapLocalitzacions(idPosRepetides)#intercanviem les localitzacions de les latituds repetides
    generarNousFitxers(coordenadesFinals)#creem els fitxers amb les noves localitzacions
    
