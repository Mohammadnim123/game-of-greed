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
            if len(count)==3:
                times1,times2,times3 =count[0][1],count[1][1],count[2][1]
                if times1==times2==times3 :
                    score+=(750)
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
                    elif times-2 >= 1:
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




if __name__ == "__main__":
    print(GameLogic.roll_dice(5))
    print(GameLogic.roll_dice(1))
    print(GameLogic.calculate_score((1,1,1,1,1,1)))