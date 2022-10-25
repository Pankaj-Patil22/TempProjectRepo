from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import traceback
 
class FlaskAppWrapper():
    def __init__(self):
        __name__ = '__main__'
        self.application = Flask(__name__)
        print("has to be ",__name__)
        self._config()
        
        @self.application.route('/', methods = ['GET'])
        def index():
            return jsonify({'message': 'Hello World!'})
    
    def get_app(self):
        return self.application
         
    def _config(self):
        CORS(self.application)
        self.application.secret_key = os.urandom(24)
    
    

    def run(self, debug,  host, port):
        self.application.run()


def main():
    application = FlaskAppWrapper()
    application.run(True, host='0.0.0.0', port=5000)
    return application

if __name__ == '__main__':
    main()