from flask import Flask, request, jsonify
from rmq_consumer import RMQConsumer
import grpc_consumer

app = Flask(__name__)
consumer = RMQConsumer()

@app.route('/search', methods=['GET'])
def search_files():
    search_text = request.args.get('query')
    results = consumer.call(search_text)
    return jsonify({'results': results})

@app.route('/files', methods=['GET'])
def get_files():
    files = grpc_consumer.list_files()
    return jsonify(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
