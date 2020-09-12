from argparse import ArgumentParser
from flask import Flask
from flask import jsonify
from werkzeug.utils import import_string

import blockchain
import wallet

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello, world'

if __name__ == '__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('-p', '--port', default=5000,
                      type=int, help='port to listen on')
  args = parser.parse_args()
  port = args.port

  app.run(host='127.0.0.1', port=port, threaded=True, debug=True)

