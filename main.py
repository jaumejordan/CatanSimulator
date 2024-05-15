from Managers.GameDirector import GameDirector


def main():
    wins_per_player = [0,0,0,0]
    game_director = GameDirector()
    try:
        games_to_play = int(input('Number of games to be played: '))
    except ValueError:
        games_to_play = 0
    if isinstance(games_to_play, int) and games_to_play > 0:
        for i in range(games_to_play):
            print('......')
            winner_id = game_director.game_start(i + 1)
            wins_per_player[winner_id] = wins_per_player[winner_id]+1
    else:
        print('......')
        print('Invalid quantity')
    print('------------------------')
    print('SUMMARY:')
    for i in range(4):
        print("J"+str(i)+"'s wins: "+str(wins_per_player[i]))
    game_director.trace_loader.export_every_game_to_file()
    return


if __name__ == '__main__':
    main()
