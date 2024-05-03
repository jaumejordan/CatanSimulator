from Managers.GameDirector import GameDirector


def main():
    game_director = GameDirector()
    try:
        games_to_play = int(input('Number of games to be played: '))
    except ValueError:
        games_to_play = 0
    if isinstance(games_to_play, int) and games_to_play > 0:
        for i in range(games_to_play):
            print('......')
            game_director.game_start(i + 1)
    else:
        print('......')
        print('Invalid quantity')
    print('------------------------')
    game_director.trace_loader.export_every_game_to_file()
    return


if __name__ == '__main__':
    main()
