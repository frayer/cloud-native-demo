import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--port', '-p', type=int, required=False, help="port number", default=5000)
parser.add_argument('--host', type=str, required=False, help="port number", default='0.0.0.0')
parser.add_argument('--redis-host', type=str, required=False, help="port number", default='localhost')
parser.add_argument('--redis-port', type=str, required=False, help="port number", default='6379')

args = parser.parse_args()
