from game_of_greed.game_logic import GameLogic, Banker

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
        round = 0
        
        score = 0
        
        
        new_banker = Banker()

        print("Welcome to Game of Greed")
        response = input("Wanna play?")
        if response == 'n':
            print("OK. Maybe another time")
        elif response == 'y':
            
            while True:
                num_dice = 6
                round += 1
                print(f"Starting round {round}")
                print(f"Rolling {num_dice} dice...")
                roll = self.roller(num_dice)
                Game.print_roll(roll)
                what_next = input("Enter dice to keep (no spaces), or (q)uit: ")
                if what_next == 'q' or what_next == 'quit':
                    print(f"Total score is {new_banker.balance} points")
                    print(f"Thanks for playing. You earned {new_banker.balance} points")
                    break
                elif what_next != ('q' or 'quit'):
                    length = len(what_next)
                    num_dice = num_dice - length
                    input_dice = int(what_next)
                    to_top = Game.split(input_dice)
                    new_banker.shelved = GameLogic.calculate_score(to_top)
                    print(f"You have {new_banker.shelved} unbanked points and {num_dice} dice remaining")
                    new_responce = input("(r)oll again, (b)ank your points or (q)uit ")
                    if new_responce == 'b':
                        new_banker.balance = new_banker.balance + new_banker.shelved
                        print(f"You banked {new_banker.shelved} points in round {round}")
                        new_banker.shelved = 0
                        print(f"Total score is {new_banker.balance} points")

                    elif new_responce == 'q':
                        
                        print(f"Total score is {new_banker.balance} points")
                        print(f"Thanks for playing. You earned {new_banker.balance} points")
                        break
                    
                     
                            
                    
                    

                            
                
                
            
if __name__ == "__main__":
    user = Game()
    user.play()
    