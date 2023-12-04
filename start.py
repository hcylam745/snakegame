from snake_game import snakegame

run_greedy = False
run_bfs = False
run_player = False
run_bfs_longest = True

game = snakegame(False, run_greedy, run_bfs, run_player, run_bfs_longest)

game.start()