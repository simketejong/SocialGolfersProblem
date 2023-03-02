import random

AantalPersonen = 16
AantalSpeelDagen = 4
##FlightsPerDag = 4
## MaximaleFlightGrote = 4
## MinimaleFlightGrote = 3
## TestRemain = AantalPersonen % MaximaleFlightGrote
## TestDevide = TestRemain / MinimaleFlightGrote
FlightVerdeling=[4,3,3,3,3] # testing

def AppendFlight():
    FlightIndeling.append({
        "flightnr" : 0,
        "Dag" : 0,
        "Flight" : 0,
        "Grote" : 0,
        "Personen" : []
    })
def AppendPersoon():
    Persoon.append({ 
        "nummer" : 0,
        "naam" : "",
        "hcp" : "",
        "email" : "",
        "met_wie_gespeeld" : [],
        "WelkeFlight" : [],
        "WelkeDag" : [],
        "WilNiet" : [],
        "buggy" : False,
        "dubbel" : []
})
def AppendDubbel():
    Dubbel.append({
        "flightnr" : 0,
        "Persoon" : ""
    })
def KanDeze(kandidaat, flightnr, grote):
    GeefTerug = True
    if kandidaat in FlightIndeling[flightnr]["Personen"]: # Deze zou al in flight zijn
        print("Moet niet kunnen ",kandidaat, flightnr)
        GeefTerug = False
    for controle in FlightIndeling[flightnr]["Personen"]: # Kijk of kandidaat ooit met een van de andere in flight heb gespeeld
        if kandidaat in Persoon[controle]["met_wie_gespeeld"]:
            GeefTerug = False
        if kandidaat in Persoon[controle]["WilNiet"]:
            GeefTerug = False
        if ((Persoon[controle]["buggy"]) & (grote == 4)):
            GeefTerug = False
    if GeefTerug: # muteer bij de andere spelers dat zij met kandidaat gespeeld hebben
        for AndereSpeler in FlightIndeling[flightnr]["Personen"]:
            Persoon[AndereSpeler]["met_wie_gespeeld"].append(kandidaat)
            Persoon[kandidaat]["met_wie_gespeeld"].append(AndereSpeler)
    return GeefTerug
def KandidaatMinsteDubbels():
    result=0
    DubbeleKandidaat = PersonenBeschikbaarVandaag.copy()
    tel = 0
    for check in PersonenBeschikbaarVandaag:
        DubbeleKandidaat[tel]=0
        for controle in FlightIndeling[flightnr]["Personen"]: # Kijk of kandidaat ooit met een van de andere in flight heb gespeeld
            if check in Persoon[controle]["met_wie_gespeeld"]:
                DubbeleKandidaat[tel] = DubbeleKandidaat[tel] + 1
            if check in Persoon[controle]["WilNiet"]:
                DubbeleKandidaat[tel] = AantalPersonen # dit kan zeker niet
        tel = tel + 1
    minste=min(DubbeleKandidaat)
    welke = 0
    for check in DubbeleKandidaat:
        if check == minste:
            result=welke
            welke=welke + 1
            break
    return result
                    
Creteria_0=False
Creteria_1=False
Pro = True
Buggies = False

TestRun=10000
Counter=0

LowestDubbel = 100
AmountLowestDubbel = 0
MaximumGespeeld = 0
MaxMax = 0
MinimumGespeeld = 100
MinMin = 1
HoeveelGespeeld = 0 

MaxGroteFlight = 0
MaxAmateurMensenSpelen = 0

weer = True

while weer:
    Persoon =[]
    FlightIndeling =[]
    Dubbel=[]
    AantalDubbel=0
    PersonenBeschikbaar=[]

    for x in range(AantalPersonen):
        PersonenBeschikbaar.append(x)
        AppendPersoon()
        Persoon[x].update({"nummer": x})
        Persoon[x].update({"naam": "persoon_"+str(x)})
        Persoon[x].update({"hcp": random.randint(0, 54)})
    if Pro:
        Persoon[0]["WilNiet"].append(1)
        Persoon[1]["WilNiet"].append(0)
    if Buggies:
        Persoon[2].update({"buggy": True})
        AantalPersonen = AantalPersonen - 1
        Persoon[3].update({"buggy": True})
        AantalPersonen = AantalPersonen - 1
        FlightVerdeling=[4,3,3,3,3] 

    random.shuffle(PersonenBeschikbaar)
    flightnr=0
    for y in range(AantalSpeelDagen):
        PersonenBeschikbaarVandaag = PersonenBeschikbaar.copy()
        dag = y + 1
        flight = 0
        for p in FlightVerdeling:
            flight = flight + 1
            AppendFlight()
            FlightIndeling[flightnr].update({"Dag": dag})            
            FlightIndeling[flightnr].update({"Flight": flight})
            FlightIndeling[flightnr].update({"Grote": p})
            FlightIndeling[flightnr].update({"flightnr": flightnr})
            for s in range(p):           
                found=False
                teller = 0 
#                random.shuffle(PersonenBeschikbaarVandaag)  # This option rand
                for kandidaat in PersonenBeschikbaarVandaag:
                    if KanDeze(kandidaat,flightnr,p):
                        FlightIndeling[flightnr]["Personen"].append(PersonenBeschikbaarVandaag.pop(teller))
                        Persoon[kandidaat]["WelkeDag"].append(dag)
                        Persoon[kandidaat]["WelkeFlight"].append(flight)
                        found=True
                        random.shuffle(PersonenBeschikbaarVandaag)
                        break
                    teller += 1                              
                if not found:                      
                    AppendDubbel()
                    welke=KandidaatMinsteDubbels()
                    dubbel=PersonenBeschikbaarVandaag[welke]
                    Dubbel[AantalDubbel].update({"Persoon": dubbel})
                    Dubbel[AantalDubbel].update({"flightnr": flightnr})
                    AantalDubbel = AantalDubbel + 1
                    Persoon[dubbel]["WelkeDag"].append(dag)
                    Persoon[dubbel]["WelkeFlight"].append(flight)
                    FlightIndeling[flightnr]["Personen"].append(dubbel)
                    PersonenBeschikbaarVandaag.pop(welke)
            flightnr = flightnr + 1   
    
    if Counter > TestRun:
        Creteria_0 = True
    else:
        if AantalDubbel < LowestDubbel:
            LowestDubbel = AantalDubbel
        if Pro:
            size = len(Persoon[0]["met_wie_gespeeld"] + Persoon[1]["met_wie_gespeeld"])
            if size > MaxAmateurMensenSpelen:
                MaxAmateurMensenSpelen = size
        Counter = Counter + 1
    
    if (Creteria_0 & (AantalDubbel == LowestDubbel)):
        size = len(Persoon[0]["met_wie_gespeeld"] + Persoon[1]["met_wie_gespeeld"])
        if size == MaxAmateurMensenSpelen:
            print("Aantal dubbels", LowestDubbel)
            print("MaxSpelers", MaxAmateurMensenSpelen)
            for x in range(AantalPersonen):
                print(Persoon[x])
            for x in FlightIndeling:
                print(x)
            for x in Dubbel:
                print(x)   


