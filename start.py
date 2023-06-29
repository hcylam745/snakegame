from snake_game import snakegame

run_greedy = False
run_bfs = False
run_player = True

game = snakegame(False, run_greedy, run_bfs, run_player)
game.start()