from flask import Flask


app = Flask('teste')
@app.route('/ola')
def ola():
    return '<h1>Olá mundo no Flask!</h1>'

app.run(debug=True)