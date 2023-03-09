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
def FindPlayers(dag, groep):
    for d in FlightIndeling:
        if ((d["Dag"]  == dag) & (d["Flight"]  == groep)):
            return d["Personen"], d["Grote"]
def MakeHtml():
 #   days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#    players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11", "Player 12", "Player 13", "Player 14", "Player 15", "Player 16"]
    flight_colors = {
        1: "#FFDAB9",  # peachpuff
        2: "#B0E0E6",  # powderblue
        3: "#90EE90",  # lightgreen
        4: "#FFB6C1",  # lightpink
        5: "#3FB3C1",  # 
}

    # Generate the HTML table
    html = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<title>Golf Schedule</title>\n<style>\ntable {\nborder-collapse: collapse;\nmargin: 20px;\n}\nth, td {\npadding: 10px;\ntext-align: center;\nborder: 1px solid black;\n}\n"
    for flight_num, color in flight_colors.items():
        html += f".flight{flight_num} {{ background-color: {color}; }}\n"
    html += "</style>\n</head>\n<body>\n<h1>Golf Schedule</h1>\n<table>\n<thead>\n<tr>\n<th>Day</th>\n"
    for g in range(len(FlightVerdeling)):
        g =g + 1
        html+= "<th>Flight "+str(g)+ "</th>\n"
    html += "</tr>\n</thead>\n<tbody>\n"
#        htmp+= "<th>Flight 1</th>\n<th>Flight 2</th>\n<th>Flight 3</th>\n<th>Flight 4</th>\n</tr>\n</thead>\n<tbody>\n"
#    for day in range(AantalSpeelDagen):
#        day = day + 1
#        html += f"<tr>\n<td>{day}</td>\n"
#        players = FindPlayers(day, 1)
#        html += f"<td class='flight1'>{players[0][0]}, {players[0][1]}, {players[0][2]}, {players[0][3]}</td>\n"
#        players = FindPlayers(day, 2)
#        html += f"<td class='flight2'>{players[0][0]}, {players[0][1]}, {players[0][2]}</td>\n"
#        players = FindPlayers(day, 3)
#        html += f"<td class='flight3'>{players[0][0]}, {players[0][1]}, {players[0][2]}</td>\n"
#        players = FindPlayers(day, 4)
#        html += f"<td class='flight4'>{players[0][0]}, {players[0][1]}, {players[0][2]}</td>\n"
#        players = FindPlayers(day, 5)
#        html += f"<td class='flight5'>{players[0][0]}, {players[0][1]}, {players[0][2]}</td>\n"
#        html += "</tr>\n"

    for day in range(AantalSpeelDagen):
        day = day + 1
        html += f"<tr>\n<td>{day}</td>\n"
        for r in range(len(FlightVerdeling)):
            r=r+1
            players = FindPlayers(day, r)
            html += f"<td class=\'flight"+str(r)+"'"+">"
            for s in range(players[1]):
                html += f"{players[0][s]},"
            html+= "</td>\n"
        html += "</tr>\n"

    html += "</tbody>\n</table>\n</body>\n</html>\n"
    # Write the HTML to a file
    with open("golf_schedule.html", "w") as f:
        f.write(html)    

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
            MakeHtml()            
            input("Press Enter to continue...")
