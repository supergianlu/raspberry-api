from flask import Flask, jsonify, abort, make_response

#Create a flask object
app = Flask(__name__)

#Return an error json instead the page 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#Run the code below this function when someone access to this URL of the server
@app.route('/api/v1.0/getRange/<int:timestamp_from>/<int:timestamp_to>', methods=['GET'])
def get_range(timestamp_from, timestamp_to):

    json = []

    #TODO inserisco nell'array json tutti i valori del file csv corrispondenti al range di input
    for i in range(0, 10):
        element = {
            'timestamp': 'timespamp csv',
            'students' : 'students csv'
        }
        json.append(element)
    
    if len(json) == 0:
        abort(404)
    return jsonify({'json': json})

#server listen on the port 80 and return any errors
if __name__ == '__main__':
    app.run(host='192.168.1.100', port = 80, debug = True)













    
