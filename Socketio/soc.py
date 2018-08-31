from flask import Flask,render_template,url_for
from flask_socketio import SocketIO,emit
import os

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio=SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on('submit')
def com(data):
    selection = data['selection']
    emit("my response", {'selection':selection},broadcast=True)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ =='__main__':
    socketio.run(app)
