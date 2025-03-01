from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, my name is Mubeen and this is my app!"

if __name__ == '__main__':
    app.run(debug=True)
