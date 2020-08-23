import random
from collections import Counter
import random
from collections import Counter
class GameLogic:
    @staticmethod
    def calculate_score(x):
        score=0
        count = Counter(x).most_common(6)
        print(count)
        if len(count)==6:
            score+=(1500)
        else:
            if len(count)==3 and (count[0][1]==count[1][1]==count[2][1]):
                score+=(750)
            else:
                i=0
                while i < len(count):
                    value=count[i][0]
                    times =count[i][1]
                    if value:
                        if times < 3:
                            if value ==1:
                                score+= (times*100)
                            elif value ==5:
                                score+= (times*50)
                            else:
                                score+= (0)
                        elif 3<= times <= 6:
                            if value == 1:
                                score+= ( (times -2) * 1000)
                            elif value > 1:
                                score+=( (times -2) * (value*100))
                    i+=1
        return score
    @staticmethod
    def roll_dice(dice_number):
        output = []
        for i in range(dice_number):
            output.append(random.randint(1,6))
        return tuple(output) 
    
class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0
    
    def shelf(self,num):
        self.shelved += num
    
    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance
    
    def clear_shelf(self):
        self.shelved = 0
    
if __name__ == "__main__":
    print(GameLogic.roll_dice(5))
    print(GameLogic.roll_dice(1))
    print(GameLogic.calculate_score((1,1,2,2,3,3)))
    print(GameLogic.calculate_score((5, 5, 5, 2, 2, 3))) 
    print(GameLogic.calculate_score((6,6,6,6,6,1)))
    