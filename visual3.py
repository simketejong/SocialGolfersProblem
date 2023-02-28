# Define the Persoon dictionary with the name of the golfer and the golfer he played against
Persoon = {
    'Golfer 1': {'naam': 'Golfer 1', 'met_wie_gespeeld': ['Golfer 2', 'Golfer 3']},
    'Golfer 2': {'naam': 'Golfer 2', 'met_wie_gespeeld': ['Golfer 1', 'Golfer 3']},
    'Golfer 3': {'naam': 'Golfer 3', 'met_wie_gespeeld': ['Golfer 1', 'Golfer 2']},
    'Golfer 4': {'naam': 'Golfer 4', 'met_wie_gespeeld': ['Golfer 1', 'Golfer 2', 'Golfer 3']}
}

# Create a matrix to store the matches between the golfers
matrix = [[0 for _ in range(len(Persoon))] for _ in range(len(Persoon))]

# Fill in the matrix with 1 if two golfers played against each other
for golfer in Persoon:
    i = list(Persoon.keys()).index(golfer)
    for tegenstander in Persoon[golfer]['met_wie_gespeeld']:
        j = list(Persoon.keys()).index(tegenstander)
        matrix[i][j] = 1
        matrix[j][i] = 1

# Create an HTML table to display the matrix
html = '<table border="1">'
html += '<tr><th></th>'
for golfer in Persoon:
    html += '<th>' + golfer + '</th>'
html += '</tr>'
for i in range(len(Persoon)):
    html += '<tr><th>' + list(Persoon.keys())[i] + '</th>'
    for j in range(len(Persoon)):
        if matrix[i][j] == 1:
            html += '<td>X</td>'
        else:
            html += '<td></td>'
    html += '</tr>'
html += '</table>'

# Print the HTML code for the matrix
print(html)
