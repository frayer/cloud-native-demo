from arguments import args
from flask import Flask, Response, request, json
import logging
import os
import redis
import time

app = Flask(__name__)

LISTEN_HOST = args.host
LISTEN_PORT = args.port
REDIS_HOST = args.redis_host
REDIS_PORT = args.redis_port

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
livenessDelay = 0

@app.route('/')
def root():
    data = json.dumps({
        "appName": "cloud-native-demo",
        "version": "1.0.0",
        "redis-host": REDIS_HOST,
        "env": {
            "host": os.getenv('HOSTNAME'),
            "user_defined_1": os.getenv('USER_DEFINED_1'),
            "user_defined_2": os.getenv('USER_DEFINED_2'),
            "user_defined_3": os.getenv('USER_DEFINED_3')
        }
    })
    return Response(data, mimetype="application/json")

@app.route('/live')
def live_get():
    time.sleep(livenessDelay)
    return Response(json.dumps({"delay": livenessDelay}), status=200, mimetype="application/json")

@app.route('/live', methods=['POST'])
def live_post():
    global livenessDelay
    livenessDelay = request.get_json()['delay']
    return Response(json.dumps({"delay": livenessDelay}), status=200, mimetype="application/json")

@app.route('/ready')
def ready():
    redis_ready = False

    try:
        redis_ready = redis_client.ping()
    except:
        logging.warning("python connection down")

    response = Response(mimetype="application/json")

    if redis_ready:
        response.status = "200"
        response.response = json.dumps({
            "redis_connection": "up"
        })
    else:
        response.status = "503"
        response.response = json.dumps({
            "redis_connection": "down"
        })

    return response

if __name__ == '__main__':
    app.run(host=LISTEN_HOST, port=LISTEN_PORT)
