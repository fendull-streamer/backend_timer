from flask import Flask, request, make_response
import json

app = Flask(__name__)

state = {"t": 0}

#sets the amount of time left on the timer. expects t in seconds
@app.route('/settime')
def settime():
    t = request.args.get('t')
    if t is None:
        return make_response("Arg t is required", 400)
    try:
        state['t'] = int(t)
    except:
        return make_response("Arg t must be an integer", 400)

    return make_response("Success", 200)

@app.route('/gettime')
def gettime():
    return make_response(json.dumps(state), 200)

if __name__ == '__main__':
    app.run(host='localhost', port=3001)
