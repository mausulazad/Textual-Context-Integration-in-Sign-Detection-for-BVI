import time
from flask import Flask

app = Flask(__name__)

#Dummy route for starting out
@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}