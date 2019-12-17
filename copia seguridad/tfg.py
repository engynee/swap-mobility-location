import os,collections

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
    lat=[]
    longi=[]
   
    """for i in coordenadesInicials.items():
        for j in i[1]: #accedeixo a cada tupla individualment
            lat.append(j[0]) #guardem cada valos de lat i long
            longi.append(j[1])"""
    for i in range(len(coordenadesInicials.items())-1): #de cada parella de longitud i latitud de cada fitxer busquem les repetides
	for j in coordenadesInicials.values()[i]:
		for k in coordenadesInicials.values()[i+1]:
		 if j[0] == k[0]:
                     lat.append(j[0])
            
    for i in range(len(coordenadesInicials.items())-1):
	for j in coordenadesInicials.values()[i]:
	    for k in coordenadesInicials.values()[i+1]:
                if j[1] == k[1]:
                    longi.append(j[1])
            
    for i,y in collections.Counter(lat).items(): #recorrem totes les lats i contem les latituds repetides amb un valor de lambda = 4
        if (y>0):
            latRepetides.append(i) #s'afegeixen en cas d'existir, a un array

    for i,y in collections.Counter(longi).items(): #contem les longituds repetides amb un valor de lambda = 4
        if (y>0):
            longiRepetides.append(i)
    return latRepetides, longiRepetides

def IdLatitudsRepetides(latRepetides):
    IdLat=[]
    for j in latRepetides: #per cada una de les lats repes
        count=0
        for k in range(len(coordenadesInicials.values())): #per a la llargada del vector de totes les latituds,longituds inicials
            l=0
            while (l<len(coordenadesInicials.values()[k])): #anem recorrent cada tupla de lat,long inicial fins arribar a la ultima
                if (coordenadesInicials.values()[count][l][0] == j): #accedim a totes les tuples de cada key, dins totes les tuples amb el parametre count accedim als keys de 1 en 1
                    #dins cada key tenim un conjunt de tuples, amb el parametre l accedim a cada tupla de key en el que estiguem individualment i amb el [0] indiquem el primer de la tupla (la latitud)
                    IdLat.append(tuple((coordenadesInicials.keys()[count],j)))#com estem dins la condicio de haver trobat una latitud igual a la del array que teniem guardat, afegim una tupla que ens digui 
                    l=l+1 #el key i la latitud per cada lat repe que trobi
                else:
                    pass
                    l=l+1 #seguent tupla del mateix key
            count=count+1 #seguent key
    IdLat = list(set(IdLat)) #treiem els repes i ho posem en forma de llista
    return IdLat

def IdLongitudsRepetides(longiRepetides): #lo mateix amb longitud [1]
    IdLongi=[]
    for j in longiRepetides:
        count=0
        for k in range(len(coordenadesInicials.values())):
            l=0
            while (l<len(coordenadesInicials.values()[k])):
                if (coordenadesInicials.values()[count][l][1] == j):
                    IdLongi.append(tuple((coordenadesInicials.keys()[count],j)))
                l=l+1
            count=count+1
    IdLongi = list(set(IdLongi))
    return IdLongi

def swapLatLocalitzacions(idLatRepetides):
    idFet=0
    id2Fet=0
    mida=0
    swap=[]
    swap2=[]
    while (mida < len(idLatRepetides)-1):
        trobat = False
        trobat2= False
        temp = []
        temp2=[]
        if idLatRepetides[mida][0] in coordenadesInicials:
            count = 0
            for x in coordenadesInicials[idLatRepetides[mida][0]]:
                if x[0] == idLatRepetides[mida][1]:
                    trobat2 = True
                    idFet = count+1
                    if not temp:
                        temp = coordenadesInicials[idLatRepetides[mida][0]][count+1:]
                    else:
                        temp.append(coordenadesInicials[idLatRepetides[mida][0]][count+1:])
                else:
                    pass
                count = count+1
    	else:
            pass
        coun = 0
	if trobat2 == True:
            for i in range(1,len(idLatRepetides)-mida):
                if idLatRepetides[mida+i][0] in coordenadesInicials:
                    trobat=True
                    count3 = 0
                    if trobat and coun <1:
                        for x in coordenadesInicials[idLatRepetides[mida+i][0]]:
                            if x[0] == idLatRepetides[mida+i][1] and coun<1:
                                coun = coun+1
                                id2Fet = count3+1
                                if not temp2:
                                    temp2 = coordenadesInicials[idLatRepetides[mida+i][0]][count3+1:]
                                else:
                                    temp2.append(coordenadesInicials[idLatRepetides[mida+i][0]][count3+1:])
                                coordenadesInicials[idLatRepetides[mida][0]][idFet:] = temp2
                                coordenadesInicials[idLatRepetides[mida+i][0]][id2Fet:] = temp
			    count3 = count3+1
    		    else: pass
		else:
                    pass

	mida= mida+1
	#print temp2
    return coordenadesInicials
""" def f(a):
			idFet=0
			id2Fet=0
			mida=0
			swap=[]
			swap2=[]
			while (mida < len(trobar)-1):
				print 'comenco'
				trobat = False
				trobat2= False
				temp = []
				temp2=[]
				if trobar[mida][0] in a:
					trobat2 = True
					print 'entro1'
					print trobar[mida]
					count = 0
					for x in a[trobar[mida][0]]:
						if x[0] == trobar[mida][1]:
							print 'entro 2'
							print a[trobar[mida][0]]
							idFet = count+1
							temp.append(a[trobar[mida][0]][count+1:])
						else: pass
						count = count+1
						#print temp
				else:
					trobat2 = False
				coun = 0
				if trobat2 == True:
					for i in range(1,len(trobar)-mida):
						print trobar[mida+i]
						if trobar[mida+i][0] in a:
							print 'soc coun'
							print coun
							trobat=True
							count3 = 0
							if trobat and coun <1:
								for x in a[trobar[mida+i][0]]:
									if x[0] == trobar[mida+i][1]:
										#trobat = True
										coun = coun+1
										print 'entro 3'
										id2Fet = count3+1
										temp2.append(a[trobar[mida+i][0]][count3+1:])
										print a[trobar[mida+i][0]]
										print 'trobat!!!'
										print temp,temp2
										a[trobar[mida][0]][idFet:] = temp2
										a[trobar[mida+i][0]][id2Fet:] = temp
									#trobat = False
									count3 = count3+1
							else: pass
						else:
							pass

				mida= mida+1"""

def swapLongiLocalitzacions(idLongiRepetides):
    idFet=0
    id2Fet=0
    mida=0
    swap=[]
    swap2=[]
    while (mida < len(idLongiRepetides)-1):
        trobat = False
        trobat2= False
        temp = []
        temp2=[]
        
        if idLongiRepetides[mida][0] in coordenadesInicials:
            count = 0
            for x in coordenadesInicials[idLongiRepetides[mida][0]]:
                if x[1] == idLongiRepetides[mida][1] and trobat2 == False:
                    trobat2 = True
                    idFet = count+1
                    if not temp:
                        temp = coordenadesInicials[idLongiRepetides[mida][0]][count+1:]
                    else:
                        temp.append(coordenadesInicials[idLongiRepetides[mida][0]][count+1:])
                else:
                    pass
                count = count+1
    	else:
            pass
        coun = 0
        
	if trobat2 == True:
            
            for i in range(1,len(idLongiRepetides)-mida):
                if idLongiRepetides[mida+i][0] in coordenadesInicials:
                    trobat=True
                    count3 = 0
                    if trobat and coun <1:
                        for x in coordenadesInicials[idLongiRepetides[mida+i][0]]:
                            if x[1] == idLongiRepetides[mida+i][1] and coun<1:
                                coun = coun+1
                                id2Fet = count3+1
                                if not temp2:
                                    temp2 = coordenadesInicials[idLongiRepetides[mida+i][0]][count3+1:]
                                else:
                                    temp2.append(coordenadesInicials[idLongiRepetides[mida+i][0]][count3+1:])
                                coordenadesInicials[idLongiRepetides[mida][0]][idFet:] = temp2
                                coordenadesInicials[idLongiRepetides[mida+i][0]][id2Fet:] = temp
                            else: pass
			    count3 = count3+1
			    
    		    else: pass
		else:
                    pass
        mida= mida+1
    
    return coordenadesInicials
    
                
"""def neteja(coordenadesInicials):
    result = []
    for i in coordenadesInicials.items():
        llarg = 0
        while (llarg < len(coordenadesInicials.items())):
            for x in i:
                if '[[' or ', [[' or ']]' or ', []' or ']] ,' or ', [(' or')],(' or '[]' in str(x):
                    s=str(x)
                    s=s.replace('[]','()')
                    s=s.replace('[[','')
                    s=s.replace(']]',']')
                    s=s.replace('[]','')
                    s=s.replace(', [[',',')
                    s=s.replace(')]] ,','],')
                    s=s.replace(', [(',',(')
                    s=s.replace(')],( ,','),(')
                result.append(s)
            llarg = llarg +1
    res_dct = {result[i]: result[i + 1] for i in range(0, len(result), 2)}
    res_dct = '\n'.join(res_dct)
    dict2=coordenadesInicials.copy()
    
    return res_dct"""


def generarNousFitxers(coordenadesFinals):
    for i in coordenadesFinals:
        f = open('C:/Users/SatecSistemas/Desktop/programillas/tfg/coordenadesFinals/' + i +".txt",'a')
        f.write(str(coordenadesFinals[i]))
        
if __name__ == "__main__":
    latRepetides=[]
    longiRepetides=[]
    idLongiRepetides=[]
    idLatRepetides=[]
    coordenadesInicials = {}
    coordenadesFinals = {}
    for (roots,dir,files) in os.walk('C:/Users/SatecSistemas/Desktop/programillas/tfg/coordenades'): #si eso ya cambio la ruta
        coordenadesInicials = llegirCoordenades(roots,files)#ja tinc totes les coordenades guardades a coordenadesUsuaris, compta ara les que estan repetides
    latRepetides, longiRepetides = interseccions(coordenadesInicials)

    idLatRepetides = IdLatitudsRepetides(latRepetides)
    idLongiRepetides = IdLongitudsRepetides(longiRepetides)
    swapLatLocalitzacions(idLatRepetides)
    coordenadesFinals = swapLongiLocalitzacions(idLongiRepetides)
    #coordenadesFinals = neteja(coordenadesInicials)
    generarNousFitxers(coordenadesFinals)
    
    
