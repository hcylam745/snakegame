from flask import Flask, jsonify, request

from flask_cors import CORS

from snake_game import snakegame

player_queue = []

app = Flask(__name__)

cors = CORS(app)

game = snakegame(False, False, False, True, 1000)

@app.route("/user_input", methods=["POST"])
def user_input():
    # input format:
    # {
    #   "direction": "up/down/left/right"
    # }
    
    direction = request.json["direction"]
    if direction == "up":
        game.up()
    elif direction == "right":
        game.right()
    elif direction == "down":
        game.down()
    elif direction == "left":
        game.left()
    else:
        return "Incorrect direction given. ", 400
    
    return "Direction successfully sent! "
    

@app.route("/get_map", methods=["GET"])
def get_map():
    return game.returnTiles()

@app.route("/start_game", methods=["GET"])
def start_game():
    game.start()
    return "Game successfully started"