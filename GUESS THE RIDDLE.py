level1 = [" What has to be broken before you can use it?",
          " What gets wet while drying?",
          " What goes up but never comes down?"]
          
level2 = [" David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?",
          " I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?",
          " What is black when it’s clean and white when it’s dirty?",
          " What goes up and down but doesn’t move?"]


print("welcome to guess the riddle game")
print("In this there are two level to play the game press enter")
enter = input()
level1a = 4

print("level 1")
print("in this level you have 5 change to give right answer")

while True:
    print("so your first riddle is",level1[0])
    ans = input().lower()
    if ans!="egg":
        for i in range(4):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so thnk again and enter")
            th = input()
            if th == "egg":

                break
            level1a = level1a - 1
        if level1a < 1:
            print("game over")
            break
    level1a = 4

    print("correct answer now go to the next riddle")
    print("so your second riddle is", level1[1])
    ans = input().lower()
    if ans != 'towel':
        for i in range(4):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so think again and enter")
            th = input()
            if th == "towel":

                break
            level1a = level1a-1
        if level1a<1:

            print("game over")
            break

    level1a = 4

    print("correct answer now go to the next riddle")
    print("so your second riddle is", level1[2])
    ans = input().lower()
    if ans != 'age':
        for i in range(4):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so think again and enter")
            th = input()
            if th == "age":

                break
            level1a = level1a-1
        if level1a<1:

            print("game over")
            break

    level1a = 2
    print("congratulation you successfully pass the level 1")
    print("now go to the next level")
    print("level 2")
    print("in this level you have only 3 change to give the right answer")
    print("so your first riddle is", level2[0])
    ans = input().lower()
    if ans != "david":
        for i in range(2):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so thnk again and enter")
            th = input()
            if th == "david":
                break
            level1a = level1a - 1
        if level1a < 1:
            print("game over")
            break
    level1a = 2
    print("correct answer now go to the next riddle")
    print("so your second riddle is", level2[1])
    ans = input().lower()
    if ans != 'shadow':
        for i in range(2):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so think again and enter")
            th = input()
            if th == "shadow":
                break
            level1a = level1a - 1
        if level1a < 1:
            print("game over")
            break


    level1a = 2
    print("correct answer now go to the next riddle")
    print("so your second riddle is", level2[2])
    ans = input().lower()
    if ans != 'blackboard':
        for i in range(2):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so think again and enter")
            th = input()
            if th == "blackboard":
                break
            level1a = level1a - 1
        if level1a < 1:
            print("game over")
            break


    level1a = 2
    print("correct answer now go to the next riddle")
    print("so your second riddle is", level2[3])
    ans = input().lower()
    if ans != 'stairs'or 'staircase':
        for i in range(2):
            print("incorrect answer")
            print(f"you have {level1a} chance left to geve the answer so think again and enter")
            th = input()
            if th == "stairs"or'staircase':
                break
            level1a = level1a - 1
        if level1a < 1:
            print("game over")
            break

    print("congratulation you successfully pass the level 2")
    print("you are the winner of this game")
    ans = input()
    
