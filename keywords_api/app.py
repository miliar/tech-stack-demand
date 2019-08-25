from flask import Flask, jsonify, request
import redis


app = Flask(__name__)
database = redis.Redis(
    host='redis',
    port=6379,
    password='password')


@app.route('/keywords/<words>')
def get_keywords(words):
    words = {database.get(word) for word in words.split()}
    return jsonify(list({word.decode("utf-8") for word in words if word}))


@app.route('/keywords', methods=['PUT'])
def update_keywords():
    pipeline = database.pipeline()
    for key, value in request.json.items():
        pipeline.set(key, value)
    return (jsonify(pipeline.execute()), 201)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
