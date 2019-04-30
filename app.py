import csv
from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()

def main():
    with open('Carbondioxide.csv') as cofile:
        readCofile = csv.reader(cofile, delimiter= ',')
        numLine = readCofile.line_num
        countries = []
        headers = []

        year = input("Give me a year ")
        whatCountry = input("Give me a country ")

        for row in readCofile:
            numLine += 1
            if numLine == 5:
                headers = (row)
                index = headers.index(year)
            if numLine > 5:
                country = row[0]
                countries.append(country)
                if row[0] == whatCountry:
                    emissions=(row[index])
                    if emissions == "":
                        print("There is no data for this selection")
                    else:
                        print("The emissions are ",emissions)



    with open('Population.csv') as pofile:
        readPofile = csv.reader(pofile, delimiter= ',')
        numLine = readPofile.line_num
        pCountries = []
        pHeaders = []

        pYear = input("Give me a year ")
        pWhatCountry = input("Give me a country ")

        for row in readPofile:
            numLine += 1
            if numLine == 5:
                pHeaders = (row)
                pIndex = pHeaders.index(pYear)
            if numLine > 5:
                pCountry = row[0]
                countries.append(pCountry)
                if row[0] == pWhatCountry:
                    population=(row[pIndex])
                    if population == "":
                        print("There is no data for this selection")
                    else:
                        print("The population is ",population)

main()
