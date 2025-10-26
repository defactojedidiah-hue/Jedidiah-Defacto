from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Jedidiah ",
        "grade": 14,
        "section": "Stallman"
    })

if __name__ == '__main__':
    app.run(debug=True)
