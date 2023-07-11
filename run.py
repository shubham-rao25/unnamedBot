from chatapp import create_app, socketio

app = create_app()

if __name__ == "__main__":
    socketio.run(app, host="172.20.10.2")