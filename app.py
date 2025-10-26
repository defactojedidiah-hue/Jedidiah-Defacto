from flask import Flask, jsonify, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    # This returns real HTML with design
    html_page = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                backdrop-filter: blur(12px);
                width: 90%;
                max-width: 450px;
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 20px;
            }
            a {
                background: #ffeaa7;
                color: #2d3436;
                padding: 10px 25px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }
            a:hover {
                background: #fab1a0;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Flask API 👋</h1>
            <p>"Keep believing in yourself — consistency creates success."</p>
            <a href="/student">View Student Info</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_page)

@app.route('/student')
def get_student():
    # JSON data with extra info
    return jsonify({
        "name": "Jedidiah",
        "grade": 14,
        "section": "Stallman",
        "height": 159,
        "weight": 62,
        "sex": "M",
        "inspiring_message": "Keep pushing forward — your hard work will pay off!"
    })

if __name__ == '__main__':
    app.run(debug=True)
