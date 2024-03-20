from game import Game
from start import Start
from game_over import restart

if __name__ == '__main__':
    while True:
        Start().run()
        Game().run()

