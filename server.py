from flask import Flask, send_from_directory, render_template_string
from flask_socketio import SocketIO, emit
import os
import time
from threading import Thread, Event

app = Flask(__name__)
socketio = SocketIO(app)

last_modified_time = 0
stop_event = Event()

@app.route('/')
def serve_spa():
    return send_from_directory('.', 'spa5.html')

@app.route('/headlines.json')
def serve_json():
    return send_from_directory('.', 'headlines.json')

def watch_file_changes():
    global last_modified_time
    while not stop_event.is_set():
        current_time = os.path.getmtime('headlines.json')
        if current_time != last_modified_time:
            last_modified_time = current_time
            socketio.emit('reload', namespace='/reload')
        time.sleep(5)  # Check every 5 seconds

@socketio.on('connect', namespace='/reload')
def client_connected():
    print("Client connected")

if __name__ == '__main__':
    watcher_thread = Thread(target=watch_file_changes)
    watcher_thread.start()
    try:
        socketio.run(app, host='0.0.0.0', port=8080, debug=True)
    finally:
        stop_event.set()
        watcher_thread.join()
