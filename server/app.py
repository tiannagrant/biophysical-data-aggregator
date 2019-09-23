from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/startQuery', methods = ['POST'])
def query():
    _query = request.form['inputQuery']

    print('Received query: ' + _query)

if __name__ == '__main__':
    app.run()


