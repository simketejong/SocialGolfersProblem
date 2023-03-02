# Define the Persoon list with the attributes of the golfers
Persoon = [
    {
        "nummer": 1,
        "naam": "Golfer 1",
        "hcp": 18,
        "email": "golfer1@example.com",
        "met_wie_gespeeld": ["Golfer 2", "Golfer 3"],
        "WelkeFlight": ["A"],
        "WelkeDag": ["Maandag"],
        "WilNiet": ["Golfer 4"],
        "buggy": False,
        "dubbel": []
    },
    {
        "nummer": 2,
        "naam": "Golfer 2",
        "hcp": 20,
        "email": "golfer2@example.com",
        "met_wie_gespeeld": ["Golfer 1", "Golfer 3"],
        "WelkeFlight": ["A"],
        "WelkeDag": ["Maandag"],
        "WilNiet": ["Golfer 4"],
        "buggy": False,
        "dubbel": []
    },
    {
        "nummer": 3,
        "naam": "Golfer 3",
        "hcp": 22,
        "email": "golfer3@example.com",
        "met_wie_gespeeld": ["Golfer 1", "Golfer 2"],
        "WelkeFlight": ["A"],
        "WelkeDag": ["Maandag"],
        "WilNiet": ["Golfer 4"],
        "buggy": False,
        "dubbel": []
    },
    {
        "nummer": 4,
        "naam": "Golfer 4",
        "hcp": 24,
        "email": "golfer4@example.com",
        "met_wie_gespeeld": ["Golfer 1", "Golfer 2", "Golfer 3"],
        "WelkeFlight": ["A"],
        "WelkeDag": ["Maandag"],
        "WilNiet": [],
        "buggy": True,
        "dubbel": []
    }
]

# Create a matrix to store the matches between the golfers
matrix = [[0 for _ in range(len(Persoon))] for _ in range(len(Persoon))]

# Fill in the matrix with 1 if two golfers played against each other
for golfer in Persoon:
    i = golfer["nummer"] - 1
    for tegenstander in golfer["met_wie_gespeeld"]:
        j = [persoon["naam"] for persoon in Persoon].index(tegenstander)
        matrix[i][j] = 1
        matrix[j][i] = 1

# Create an HTML table to display the matrix
html = '<table border="1">'
html += '<tr><th></th>'
for golfer in Persoon:
    html += '<th>' + golfer["naam"] + '</th>'
html += '</tr>'
for i in range(len(Persoon)):
    html += '<tr><th>' + Persoon[i]["naam"] + '</th>'
    for j in range(len(Persoon)):
        if matrix[i][j] == 1:
            html += '<td>X</td>'
        else:
            html += '<td></td>'
    html += '</tr>'
html
