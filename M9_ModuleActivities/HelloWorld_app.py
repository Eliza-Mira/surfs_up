from flask import Flask

# create a new Flask app instance.
app = Flask(__name__)

# Create first route (the starting point).

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/123')
def hello_world123():
    return 'Hello world_123'
