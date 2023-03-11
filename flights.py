import random
import json

AantalPersonen = 18
AantalSpeelDagen = 5
##FlightsPerDag = 4
## MaximaleFlightGrote = 4
## MinimaleFlightGrote = 3
## TestRemain = AantalPersonen % MaximaleFlightGrote
## TestDevide = TestRemain / MinimaleFlightGrote
###FlightVerdeling=[4,4,4,3,3] # testing

def SpelersInvoer():
# TODO : This has to be a webpage to enter names / hcp / buggie etc. use database    
#    AantalPersonen = 18
    for x in range(AantalPersonen):
        PersonenBeschikbaar.append(x)
        AppendPersoon()
        Persoon[x].update({"nummer": x})
    Persoon[0].update({"naam": "Mathijs"})
    Persoon[0].update({"hcp": 0})
    Persoon[1].update({"naam": "Paul"})
    Persoon[1].update({"hcp": 6})
    Persoon[2].update({"naam": "Bob/Constance"})
    Persoon[2].update({"hcp": 40})
    Persoon[2].update({"buggy": True})        
    Persoon[3].update({"naam": "Ad/Ans"})
    Persoon[3].update({"hcp": 40})
    Persoon[3].update({"buggy": True})        
    Persoon[4].update({"naam": "Simke"})
    Persoon[4].update({"hcp": 13})
    Persoon[5].update({"naam": "Jacqie"})
    Persoon[5].update({"hcp": 10})
    Persoon[6].update({"naam": "Annemieke"})
    Persoon[6].update({"hcp": 6})
    Persoon[7].update({"naam": "Wil"})
    Persoon[7].update({"hcp": 30})
    Persoon[8].update({"naam": "Jose"})
    Persoon[8].update({"hcp": 30})
    Persoon[9].update({"naam": "Henk"})
    Persoon[9].update({"hcp": 30})
    Persoon[10].update({"naam": "Annemiek"})
    Persoon[10].update({"hcp": 30})
    Persoon[11].update({"naam": "Rene"})
    Persoon[11].update({"hcp": 30})
    Persoon[12].update({"naam": "Marie Jose"})
    Persoon[12].update({"hcp": 30})
    Persoon[13].update({"naam": "Jan Willem"})
    Persoon[13].update({"hcp": 30})
    Persoon[14].update({"naam": "Marga"})
    Persoon[14].update({"hcp": 30})
    Persoon[15].update({"naam": "Bart"})
    Persoon[15].update({"hcp": 30})
    if Pro:
        Persoon[0]["WilNiet"].append(1)
        Persoon[1]["WilNiet"].append(0)
def SuggestFlightVerdeling(x):
    # Initialize the list of valid permutations to empty
    AantalBuggies=0
    global AantalPersonen
    if Buggies:
        for x in range(AantalPersonen):
            if x == AantalPersonen:
                break
            if Persoon[x]["buggy"]:
                AantalPersonen = AantalPersonen - 1
                Persoon.pop()
                PersonenBeschikbaar.pop()
                AantalBuggies = AantalBuggies + 1
    permutations = {}
    def generate_permutations(current_permutation, remaining_sum):
        if remaining_sum == 0:
            if x in permutations:
                permutations[x].append(current_permutation)
            else:
                permutations[x] = [current_permutation]
        elif remaining_sum > 0:
            generate_permutations(current_permutation + [3], remaining_sum - 3)
            generate_permutations(current_permutation + [4], remaining_sum - 4)

    generate_permutations([], x)

    test = permutations[next(iter(permutations))]
    if AantalBuggies:
        tel = 0
        for OneArray in test:
            tel = 0
            for d in range(len(OneArray)):
                if OneArray[d] == 3:
                    tel = tel + 1
            if tel >= AantalBuggies:
                return OneArray
                break
    else:            
        return test[-1]
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
        "MoetSamen" : [],
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
    AantalBuggies=0
    if (Persoon[kandidaat]["buggy"]):
        AantalBuggies=AantalBuggies+1
    if kandidaat in FlightIndeling[flightnr]["Personen"]: # Deze zou al in flight zijn
        print("Moet niet kunnen ",kandidaat, flightnr)
        GeefTerug = False
    if ((Persoon[kandidaat]["buggy"]) & (grote == 4)):
        GeefTerug = False
    for controle in FlightIndeling[flightnr]["Personen"]: # Kijk of kandidaat ooit met een van de andere in flight heb gespeeld
        if kandidaat in Persoon[controle]["met_wie_gespeeld"]:
            GeefTerug = False
        if kandidaat in Persoon[controle]["WilNiet"]:
            GeefTerug = False
        if (Persoon[controle]["buggy"]):
            if AantalBuggies > 0:
                GeefTerug = False
            AantalBuggies=AantalBuggies+1
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
    # TODO : Add the possibility "rather not"
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
    flight_colors = {
        1: "#FFDAB9",  # peachpuff
        2: "#B0E0E6",  # powderblue
        3: "#90EE90",  # lightgreen
        4: "#FFB6C1",  # lightpink
        5: "#3FB3C1",  # 
        6: "#44B3D8",  #         
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
    html+= "<p>"
    
    html += "</style>\n</head>\n<body>\n<h1>Golf Schedule</h1>\n<table>\n<thead>\n<tr>\n<th>Day</th>\n"
    for g in range(len(FlightVerdeling)):
        g =g + 1
        html+= "<th>Flight "+str(g)+ "</th>\n"
    html += "</tr>\n</thead>\n<tbody>\n"
    for day in range(AantalSpeelDagen):
        day = day + 1
        html += f"<tr>\n<td>{day}</td>\n"
        for r in range(len(FlightVerdeling)):
            r=r+1
            players = FindPlayers(day, r)
            html += f"<td class=\'flight"+str(r)+"'"+">"
            for s in range(players[1]):
                naam = Persoon[int(players[0][s])]["naam"]
                bold = Persoon[int(players[0][s])]["buggy"]
                if bold:
                    naam = "<strong>"+naam+"</strong>"
                html += f"{naam}"+" || "
            html+= "</td>\n"
        html += "</tr>\n"

    html += "</tbody>\n</table>\n</body>\n</html>\n"

    # Create a matrix to store the matches between the golfers
    matrix = [[0 for _ in range(len(Persoon))] for _ in range(len(Persoon))]

    # Fill in the matrix with 1 if two golfers played against each other
    for golfer in Persoon:
        i = golfer['nummer']
#        i = list(Persoon.keys()).index(nummer)
        for tegenstander in golfer['met_wie_gespeeld']:
            poep = golfer['met_wie_gespeeld']
            j = tegenstander
            # TODO : BLock colour of flight and maybe day number / or double 
            matrix[i][j] = matrix[i][j] + 1
            matrix[j][i] = matrix[j][i] + 1

    # Create an HTML table to display the matrix
    html += '<p>'
    html += '<table border="1">'
    html += '<tr><th></th>'
    for golfer in Persoon:
        html += '<th>' + golfer["naam"] + '</th>'
    html += '</tr>'
    for i in range(len(Persoon)):
        html += '<tr><th>' + Persoon[i]["naam"] + '</th>'
        for j in range(len(Persoon)):
            if matrix[i][j] > 1:
#                html += '<td>X</td>'
                html += '<td>' + str(matrix[i][j]) + '</td>'
            else:
                html += '<td></td>'
        html += '</tr>'
    html += '</table>'


    with open("golf_schedule.html", "w") as f:
        f.write(html)    

Creteria_0=False
Creteria_1=False
Pro = True
Buggies = True
MaxFlight = 4
MinFlight = 3
FlightVerdeling= []

TestRun=1000
Counter=0
HoeveelFlights = 1000
optellen=0

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

#PersonenBeschikbaar=[]
#Persoon =[]
#SpelersInvoer()

while weer:
    FlightIndeling =[]
    Dubbel=[]
    AantalDubbel=0

    PersonenBeschikbaar=[]
    Persoon =[]
    SpelersInvoer()

    if len(FlightVerdeling) == 0:
        FlightVerdeling = SuggestFlightVerdeling(AantalPersonen)

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
            # TODO : This must be made different, maybe wrte all possibilities to SQL then use flask  
            input("Press Enter to continue...")
            if optellen < HoeveelFlights:
                optellen = optellen + 1
                with open('flights.json', 'a') as fp:
                    json.dump(FlightIndeling, fp)
            else:
                break