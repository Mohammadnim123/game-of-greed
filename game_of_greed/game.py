from game_of_greed.game_logic import GameLogic, Banker
class Game:
    def __init__(self, roller=GameLogic.roll_dice):
        self.roller= roller
    @staticmethod
    def print_roll(roll):
        if roll == 'q':
            return 'q'
        roll_as_string = [str(i) for i in roll]
        to_be_printed = ','.join(roll_as_string)
        print(to_be_printed)
        # print(','.join([str(i) for i in roll]))
    @staticmethod
    def totuple(x):
        y = [int(i) for i in str(x)]
        return tuple(y)
    def play(self):
        is_it_zilch =False
        is_it_cheater=False
        is_it_roll_again = 0 #to see if roll again more than 4
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
                if GameLogic.calculate_score(roll)==0:
                    is_it_zilch =True
                    print('Zilch!!! Round over')
                    print(f"You banked {new_banker.shelved} points in round {round}")
                    print(f"Total score is {new_banker.balance} points")
                    continue
                what_next = input("Enter dice to keep (no spaces), or (q)uit: ")
                if what_next == 'q':
                    if is_it_roll_again >= 4:
                        print(f"Total score is {new_banker.balance} points")
                        print(f"Thanks for playing. You earned {new_banker.balance} points")
                        break  
                    elif is_it_cheater or is_it_zilch:
                        print(f"Thanks for playing. You earned {new_banker.balance} points")
                        break
                    else:
                        print(f"Total score is {new_banker.balance} points")
                        print(f"Thanks for playing. You earned {new_banker.balance} points")
                        break
                else:
                    while GameLogic.if_cheater(roll,Game.totuple(what_next))==0:
                        is_it_cheater=True
                        print('Cheater!!! Or possibly made a typo...')
                        Game.print_roll(roll)
                        what_next = input("Enter dice to keep (no spaces), or (q)uit: ")
                if what_next == 'q' or what_next == 'quit':
                    if is_it_cheater:
                        print(f"Thanks for playing. You earned {new_banker.balance} points")
                        break
                    else:
                        print(f"Total score is {new_banker.balance} points")
                        print(f"Thanks for playing. You earned {new_banker.balance} points")
                        break
                else:
                    
                    num_dice = num_dice - len(what_next)
                    what_next = int(what_next)
                    to_topule = Game.totuple(what_next)
                    new_banker.shelved = GameLogic.calculate_score(to_topule)
                    print(f"You have {new_banker.shelved} unbanked points and {num_dice} dice remaining")
                    new_responce = input("(r)oll again, (b)ank your points or (q)uit ")
                    if new_responce == 'b':
                        new_banker.balance = new_banker.balance + new_banker.shelved
                        print(f"You banked {new_banker.shelved} points in round {round}")
                        new_banker.shelved = 0
                        print(f"Total score is {new_banker.balance} points")

                    elif new_responce == 'q':
                        if is_it_cheater:
                            print(f"Thanks for playing. You earned {new_banker.balance} points")
                            break
                        else:
                            print(f"Total score is {new_banker.balance} points")
                            print(f"Thanks for playing. You earned {new_banker.balance} points")
                            break

                    
                    while new_responce == 'r':
                            is_it_roll_again += 1
                            print(f"Rolling {num_dice} dice...")
                            roll = self.roller(num_dice)
                            Game.print_roll(roll)
                            if GameLogic.calculate_score(roll)==0:
                                is_it_zilch =True
                                new_banker.shelved = 0
                                print('Zilch!!! Round over')
                                print(f"You banked {new_banker.shelved} points in round {round}")
                                print(f"Total score is {new_banker.balance} points")
                                break
                            what_next = input("Enter dice to keep (no spaces), or (q)uit: ")
                            if what_next == 'q':
                                
                                print(f"Thanks for playing. You earned {new_banker.balance} points")
                                break
                         

                            else:
                                num_dice = num_dice - len(what_next)
                                what_next = int(what_next)
                                to_topule = Game.totuple(what_next)
                                add_value = GameLogic.calculate_score(to_topule)
            
        
                                new_banker.shelved += add_value
                                add_value = 0
                                print(f"You have {new_banker.shelved} unbanked points and {num_dice} dice remaining")
                                new_responce = input("(r)oll again, (b)ank your points or (q)uit ")
                                if new_responce == 'r':
                                    continue
                              
                                        
                                elif new_responce == 'b':
                                    new_banker.balance = new_banker.balance + new_banker.shelved
                                    print(f"You banked {new_banker.shelved} points in round {round}")
                                    new_banker.shelved = 0
                                    print(f"Total score is {new_banker.balance} points")
                                    break
                            
                                    



                        
                            



if __name__ == "__main__":
    user = Game()
    user.play()