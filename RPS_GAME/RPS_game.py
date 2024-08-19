class Game:
    number_of_trials = 4
    first_gamer_score = 0
    second_gamer_score = 0

    def __init__(self, first_gamer, second_gamer):
        x = first_gamer.getChoice()
        y = second_gamer.getChoice()
        if (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
            Game.first_gamer_score += 1
        elif (y == 1 and x == 2) or (y == 2 and x == 3) or (y == 3 and x == 1):
            Game.second_gamer_score += 1
        Game.number_of_trials -= 1


class FirstGamer:
    def __init__(self, number):
        self.number = number

    def setChoice(self, number):
        self.number = number

    def getChoice(self):
        return self.number


class SecondGamer:
    def __init__(self, number):
        self.number = number

    def setChoice(self, number):
        self.number = number

    def getChoice(self):
        return self.number


while Game.number_of_trials > 0:
    print("1-Rock\n2-Scissors\n3-Paper\n")
    first_player_choice = int(input("first player: please choose a number "))
    second_player_choice = int(input("second player: please choose a number "))

    f = FirstGamer(first_player_choice)
    s = SecondGamer(second_player_choice)
    g = Game(f, s)

if Game.number_of_trials == 0:
    if Game.first_gamer_score > Game.second_gamer_score:
        print(f"The first player wins with a score of {Game.first_gamer_score} !")
    elif Game.first_gamer_score < Game.second_gamer_score:
        print(f"The second player wins with a score of {Game.second_gamer_score} !")
    else:
         print("It's a draw!")
