from flask import Flask, request, jsonify

app = Flask(__name__)

# dict of random spell names for testing purposes
# will need to connect actual database in future
spell_database = {'fire', 'wind', 'thunder', 'stupify', 'shazam'}

@app.route('/check_spell', methods=['GET'])
def check_spell():
    try:
        # get spell
        spell_name = request.args.get('name')
        
        if spell_name:
            result = spell_name in spell_database
            return jsonify({"result": result})        
        
        # respond data
        return jsonify({"error": "No spell entered"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
