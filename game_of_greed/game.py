from game_logic import GameLogic, Banker

class Game:
    def __init__(self, roller=GameLogic.roll_dice):
        self.roller= roller

    @staticmethod
    def print_roll(roll):
        roll_as_string = [str(i) for i in roll]
        to_be_printed = ','.join(roll_as_string)
        print(to_be_printed)
        # print(','.join([str(i) for i in roll]))
        
    @staticmethod
    def split(x):
        y = [int(i) for i in str(x)]
        return tuple(y)

    def play(self):
        round = 1
        num_dice = 6
        score = 0

        print("Welcome to Game of Greed")
        response = input("Wanna play?")
        if response == 'n':
            print("OK. Maybe another time")
        elif response == 'y':
           
            print(f"Starting round {round}")
            print(f"Rolling {num_dice} dice...")
            roll = self.roller(num_dice)
            Game.print_roll(roll)
            what_next = input("Enter dice to keep (no spaces), or (q)uit:")
            if what_next == 'q' or what_next == 'quit':
                print(f"Total score is {score} points")
                print(f"Thanks for playing. You earned {score} points")
            elif what_next != ('q' or 'quit'):
                while what_next:
                        if len(what_next) > 6:
                            what_next = input("Enter dice to keep (no spaces), or (q)uit:") 
                        else:
                            break
                
                input_dice = int(what_next)
                print(Game.split(input_dice))
                            
                
                
            
if __name__ == "__main__":
    user = Game()
    user.play()
    