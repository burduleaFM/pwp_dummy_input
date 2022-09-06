from flask import Flask, jsonify, json, request


app = Flask(__name__)


@app.route('/welldesigns', methods=['GET'])
def get_all_well_desings():
    dwts_id = request.args.get('dwts_id', None)
    
    with open('welldesings.json', 'r') as welldesigns:
        data = json.loads(welldesigns.read())


    if not dwts_id:
        return {'data': [], 'msg': 'Dwts id not found'}, 404

    for row in data:
        for _, val in row.items():
            if row['dwtsId'] == dwts_id:
                return jsonify(row), 200
    return {'data': data}, 404


if __name__ == '__main__':
    app.run(debug=True)
