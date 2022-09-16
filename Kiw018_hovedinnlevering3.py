#Hoved 3 - Kiw018 - Halvor brunt

#oppretter bunkene // globale variabler
A=list()
B=list()
C=list()
D=list()
E=list()
F=list()
G=list()
H=list()
#dict med alle bunkene
alle_bunker = {
        'A':A, 'B':B, 'C':C, 'D':D,
        'E':E, 'F':F, 'G':G, 'H':H
        }

kjør = 1 #global kjøre variabel

def meny():
        print("""
---------------------------------------
1 - new game
2 - load game
3 - avslutt
---------------------------------------
""")
        choice = (input('Choose option:  '))
        if choice == '1':
                new_game()
                return True
        elif choice == '2':
                load()
                for bunke in [A,B,C,D,E,F,G,H]: #hvis en liste har noe i seg har loaden funket og spillet fortsetter
                        if len(bunke)>0:
                                return True
                        else:
                                svar = input('Spille et nytt spill? (j/n):   ') #mulighet til å spille nytt spill
                                if svar == 'j': new_game()
                                else: break
        elif choice == '3':
                avslutt()
        else:
                print('\nInvalid option, but whatever. New game.\n')
                new_game()
                return True

def new_game():
        #Oppretter et nytt spill med nye bunker
        import random

        korttall = ['7','8','9','10','J','Q','K','A'] #kort verdiene - for å kunne iterere igjennom dem
        kortstokk = list() #overordnet liste for alle kortene

        for tall in korttall: #setter tall + symbol i listen
                kortstokk.append( '\u2660'+tall) #spar
                kortstokk.append('\u2666'+tall) #ruter
                kortstokk.append('\u2663'+tall) #kløver
                kortstokk.append('\u2665'+tall) #hjerter

        for bunke in [A,B,C,D,E,F,G,H]: #Setter kortene inn i bunkene tilfeldig 
            for n in range(0,4): #4 kort
                kort = random.choice(kortstokk)
                bunke.append(kort)
                kortstokk.remove(kort) #fjerner trukket kort fra kortstokken for å unngå duplikater

def load():
        liste= []
        try:
                with open('Wish_Solitaire.txt', 'r', encoding = 'UTF-8') as innfil:
                        doc1 = innfil.readlines() #bruker readlines for å få linjene i en liste
                        for linje in doc1:
                                linje = linje.rstrip().split() #fjerner linjeskift, og gjør hvert kort om til et liste element 
                                liste.append(linje)
                        #print(liste) #test
                        for i in range(0,8): #itererer gjennom alle linjene og bunkene
                                for item in liste[i]:
                                        [A,B,C,D,E,F,G,H][i].append(item)
        except: print('Filen finnes ikke')

                                
                                
                        

def avslutt():
        global kjør
        kjør = 0
     
def lagre():
        #Lagrer kortene inn i en txt-fil
        with open('Wish_Solitaire.txt', 'w', encoding = 'UTF-8') as fil:
                for kort_liste in [A,B,C,D,E,F,G,H]:
                        #print(*kort_liste) #test
                        for kort in kort_liste:
                                fil.write(kort+' ')
                        fil.write('\n') #linje skift for hver bunke
        global kjør #avslutter loopen
        kjør = 0

def printBunker():
    #printer alle bunke-navnene, øverstekortet i bunkene, og antall kort i bunkene
    print()
    for bokstav in 'ABCDEFGH': #printer bunkenavn
        print('      '+bokstav, end = ' ')
    print('\n    ',end='')#linje skift + litt mellomrom
    for bunke in [A,B,C,D,E,F,G,H]: #printer ut øverste kortet i alle bunkene
        mellomrom = 1      #antall mellomrom mellom bunkene
        if len(bunke)!=0 and len(bunke[0])>2: mellomrom -=1 #hvis kortet er tallet 10..
        if len(bunke)<1: #hvis bunken er tom
                mellomrom +=1
                print('  [0]',' '*mellomrom,sep='', end = '') #Hvis bunken er tom
        else: print('[',bunke[0],']',' '*mellomrom,sep='', end = '')
    print()
    for bunke in [A,B,C,D,E,F,G,H]: #printer hvor mange kort som er i bunken
        print('      ' + str(len(bunke)), end = ' ')
    print()


def vinn_tap(): #Sjekker for vinn eller tap
        if sum([len(x) for x in [A,B,C,D,E,F,G,H]]) == 0: #Dersom alle kort_listene er tomme
                print('Gratulerer!','Du vant!',sep = '\n')
                return True    
        else: #Sjekker om det er mulige trekk / om det er to like kort ved listene i indeks[0]
                øverste_kort=[x[0][1:] for x in [A,B,C,D,E,F,G,H] if len(x)>0]
                if len(set(øverste_kort)) == len(øverste_kort):
                        print('Du tapte... ', 'Always look at the briiiiight side of life...',
                              '*optimistical out of tune whistling*', sep = '\n')
                        return True

   

def game():
    printBunker()
    if vinn_tap(): #sjekker om du taper eller vinner
        global kjør #hvis vinn_tap() returnerer True slutter den å kjøre loopen
        kjør = 0
        return # hopper ut av funksjonen
    
    print('Trykk <ENTER> for meny')
    user = input('Velg to bunker:  ').upper()
    if len(user)== 2 and user[0] in 'ABCDEFGH' and user[1] in 'ABCDEFGH': #henter bunkene igjennom en dictionary ('alle_bunker') med 0'te og 1'ste bokstavene fra inputet som keys 
        b1 = alle_bunker[user[0]]# bunke-valg 1  
        b2 = alle_bunker[user [1]]#bunke-valg 2
        if (len(b1)>0 and len(b2)>0) and b1[0][1:] == b2[0][1:] :   #sjekker om tallene/bokstavene på kortet er like
            b1.pop(0) #fjerner øverste kortene i bunkene
            b2.pop(0)
        else: print('Du valgte enten ugyldige bunker, \net feil antall bunker, \neller kort som ikke var like')
      
    elif user == '': #Hvis brukeren trykker <ENTER> og vil ha opp menyen
            print("""\nSkriv 'lagre' for å lagre tilstanden i en fil.
Skriv 'avslutt' for å avslutte spillet.
Eller alt annet for å fortsette spillet.
""")
            valg = input('Skriv valg:').lower()
            if valg == 'lagre': lagre()
            elif valg == 'avslutt' : avslutt()           
    else:
        print ('Ugyldig input')
        return
   


#Programkjøre loop
if meny(): #hvis bruker gjør valg 1 eller 2 vil loopen kjøre
        while kjør == 1:
                game()


