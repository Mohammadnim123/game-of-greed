import random
from collections import Counter
class GameLogic:
    @staticmethod
    def calculate_score(x):
        score=0
        count = Counter(x).most_common(6)
        # print(count)
        if len(count)==6:
            score+=(1500)
        else:
            if len(count)==3 and (count[0][1]==count[1][1]==count[2][1]):
                score+=(1500)
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
    def if_cheater(tup1,tup2):
        if tup2 == 'q':
            return False
        ntup1=Counter(tup1).most_common(6)
        ntup2=Counter(tup2).most_common(6)
        index_j=0
        arr_1=[]
        if_cheater=1
        for i in ntup2:
            if len(ntup2)>len(ntup1):
                if_cheater=0*if_cheater
                break
            for j in ntup1:
                arr_1.append(j[0])
                if i[0] == j[0]:
                    index_j+=1
                    if i[1]<=j[1]:
                        if_cheater=1*if_cheater
                    elif i[1]>j[1] :
                        if_cheater=0*if_cheater
                        ntup1,ntup2='cheater','cheater'
            if i[0] not in arr_1:
                if_cheater=0*if_cheater
        return if_cheater  
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