from flask import Flask, jsonify, request

from flask_cors import CORS

from snake_game import snakegame

player_queue = []

app = Flask(__name__)

cors = CORS(app)

game = snakegame(False, False, False, True, 300)

@app.route("/user_input", methods=["POST"])
def user_input():
    # input format:
    # {
    #   "direction": "up/down/left/right"
    # }
    

    # not really sure why, but the controls are inverted.
    direction = request.json["direction"]
    if direction == "up":
        game.down()
    elif direction == "right":
        game.left()
    elif direction == "down":
        game.up()
    elif direction == "left":
        game.right()
    else:
        return "Incorrect direction given. ", 400
    
    return "Direction successfully sent! "
    

@app.route("/get_map", methods=["GET"])
def get_map():
    return game.returnTiles()

@app.route("/start_game", methods=["GET"])
def start_game():
    if (game.game_begun == True):
        return "Game in progress. Please wait."
    game.start()
    return "Game successfully started"