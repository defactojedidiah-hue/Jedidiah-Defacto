from flask import Flask, jsonify, request
app = Flask(__name__)

# --- Original Code (kept) ---
@app.route('/')
def home():
    # New: Return a styled HTML page
    return """
    <html>
    <head>
        <title>Jedidiah's Flask API</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #74b9ff, #a29bfe);
                color: white;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.3em;
                max-width: 500px;
                line-height: 1.5em;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                backdrop-filter: blur(10px);
            }
            a {
                color: #ffeaa7;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Flask API 👋</h1>
            <p>“Success doesn’t come from what you do occasionally; it comes from what you do consistently.”</p>
            <p><a href="/student">View Student Info →</a></p>
        </div>
    </body>
    </html>
    """

@app.route('/student')
def get_student():
    # Added new details
    return jsonify({
        "name": "Jedidiah",
        "grade": 14,
        "section": "Stallman",
        "height": 159,
        "weight": 62,
        "sex": "M",
        "inspiring_message": "Keep pushing forward — your hard work will pay off!"
    })

# --- Keep this as is ---
if __name__ == '__main__':
    app.run(debug=True)
