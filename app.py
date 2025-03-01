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
            </style>
        </head>
        <body>
            <h1>Hello, my name is Usama and this is my app!</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)

