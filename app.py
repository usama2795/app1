from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    background-color: #282c34;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 20%;
                }
                .highlight {
                    color: yellow; /* Change this to any color you like */
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>Hello, my name is <span class="highlight">Usama</span> and this is my app!</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
