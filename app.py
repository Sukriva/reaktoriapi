import csv
from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app)

#Getting a list of countries
@app.route('/countries', methods=['GET'])
def get_countries():
    with open('Population.csv') as pofile:
        readPofile = csv.reader(pofile, delimiter= ',')
        numLine = readPofile.line_num
        countries = []

        for row in readPofile:
            numLine += 1
            if numLine > 5:
                country = row[0]
                countries.append(country)

    pofile.close()

    return jsonify({'countries':countries})

#Getting emissions and per capita by country, and years
@app.route('/country', methods=['GET'])
def get_countryData():
    country = request.args.get("country")
    #opening the file
    with open('Carbondioxide.csv') as cofile:
        readCofile = csv.reader(cofile, delimiter= ',')
        numLine = readCofile.line_num
        headers = []
        emissions = []

        #looping through the information and adding it to lists
        for row in readCofile:
            numLine += 1
            if numLine == 5:
                headers = (row[4:-1])
            if numLine > 5:
                if row[0] == country:
                    emission=(row[4:-1])
                    emissions=(emission)

    with open('Population.csv') as pofile:
        readPofile = csv.reader(pofile, delimiter= ',')
        numLine = readPofile.line_num
        populations = []
        perCapita = []

        for row in readPofile:
            numLine += 1
            if numLine > 5:
                if row[0] == country:
                    population=(row[4:-1])
                    populations=(population)

    #counting per capita based on the emissions and population of a country
    index = 0
    while index < len(populations):
        pop = populations[index]
        ems = emissions[index]
        if ems !="" and pop !="":
            capita = float(ems) / int(pop)
            capita = format(capita, ".5f")
            perCapita.append(capita)
        else:
            perCapita.append(0)
        index = index + 1

    pofile.close()
    cofile.close()
    
    return jsonify({'emissions':emissions, 'headers':headers, 'perCapita': perCapita})


if __name__ == '__main__':
    app.run()
