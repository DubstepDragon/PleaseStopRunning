if __name__ == "__main__":
    from game import *

    pygame.init()

    GAME = Game()
    GAME.newGame()
    GAME.run() #GAME LOOP

    pygame.quit()

