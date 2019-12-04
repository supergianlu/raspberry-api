from flask import Flask, jsonify, abort, make_response
import csv

#Create a flask object
app = Flask(__name__)

#Return an error json instead the page 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#Run the code below this function when someone access to this URL of the server
@app.route('/api/v1.0/getRange/<int:timestamp_from>/<int:timestamp_to>', methods=['GET'])
def get_range(timestamp_from, timestamp_to):
    #print("richiesta:", timestamp_from, timestamp_to)
    json = []
    with open("../counting_people/letture.csv") as csvfile:
        csvreader = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
        for row in csvreader:
            if(int(row[0])>= timestamp_from and int(row[0]) <= timestamp_to):
               json.append({'timestamp':row[0], 'students':row[1]})

    if len(json) == 0:
        abort(404)
    return jsonify({'json': json})

#server listen on the port 80 and return any errors
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug = True)
