# Backend Timer

## Setup

- Make sure you have python installed
- clone this repository and cd into it
- `python -m pip install --user virtualenv`
- `virtualenv env`
- Activate the virtual env: `env\Scripts\activate` on Windows, `source env/bin/activate` on Unix
- `pip install -r requirements.txt`
- `python backend_timer_server.py`


## Use

Now that you are running the server (on localhost:3001), you can set the time left with localhost:3001/settime?t=<time_in_seconds>. You can retrieve the time left with localhost:3001/gettime. All timer logic can and should be handled on the front end, this server is just for maintaining state
