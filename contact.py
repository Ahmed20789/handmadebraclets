from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Send the email or save the data to a database

    return jsonify({
        'status': 'success',
        'message': 'Message received'
    })

if __name__ == '__main__':
    app.run(debug=True)