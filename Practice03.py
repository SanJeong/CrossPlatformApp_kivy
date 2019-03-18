import random

class GameManager(object):
    def __init__(self):
        pass

    def play(self):
        # loop
        while True:
            self.create()
            print("You got it!")
            x = input("Would you want to play more? (y/n)")
            if x == "n":
                break

    def create(self):
        rm = RuleManager()
        rm.start()


class RuleManager(object):
    def __init__(self):
        self.num = random.sample(range(0, 10), 3)
        print(self.num)
        self.out = 0
        self.strike = 0
        self.ball = 0
        pass

    def start(self):

        repeat = 0
        while True:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
        
            if self.evaluate(num1, num2, num3) == True:
                break
            else:
                repeat += 1
                if self.out >= 9:
                    print("out")
                else:
                    print(str(self.ball) + "ball, " +str(self.strike)+"strike")
                
                print("Currently you tried " + str(repeat) + "times")
    
    def evaluate(self, num1, num2, num3):
        if num1 == self.num[0] and num2 == self.num[1] and num3 == self.num[2]:
            return True
        else:
            nlist = [num1,num2,num3]
            self.strike = 0; self.ball = 0; self.out = 0
            for i in range(0,3):
                for j in range(0,3):
                    if(self.num[i] == nlist[j] and i == j):
                        self.strike += 1
                        self.out = False
                    elif (self.num[i] == nlist[j] and i != j):
                        self.ball += 1
                        self.out = False
                    else:
                        self.out += 1
            return False

gm = GameManager()
gm.play()
