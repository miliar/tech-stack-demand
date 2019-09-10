from flask import Flask, render_template, request, redirect, url_for, flash
from helper import get_producer
from config import KAFKA_OUTPUT_TOPIC


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
producer = get_producer()


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        producer.send(KAFKA_OUTPUT_TOPIC, {'query': request.form['query'],
                                           'city': request.form['city']})
        flash(('I will update the graph for your search: '
               f"{request.form['query']} in "
               f"{request.form['city'] if request.form['city'] else 'Germany'}!"))
        return redirect(url_for('home'))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
