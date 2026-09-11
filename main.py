# Randgame() : 1,000원
# Game() : 10,000원
# gambling_sibmanwon : 100,000원 
# gambling_1million() : 1,000,000원
import random

while True : 
    money = int(input("가지고 있는 돈: ")) 

    if money <= 1000 : 
        Randgame(money)

    elif 1000 < money <= 10000 :
        print("참여할 금액대를 선택해주세요")
        print("1번 : 1,000원")
        print("2번 : 10,000원")
        print("3번 : 종료하기 ")
        a = int(input(" "))
        if a == 1 : 
            Randgame(money)
        elif a == 2 : 
            Game(money)
        elif a == 3 : 
            break
    elif 10000 < money <= 100000 : 
        print("참여할 금액대를 선택해주세요")
        print("1번 : 1,000원")
        print("2번 : 10,000원")
        print("3번 : 100,000원")
        print(" 4번 : 종료하기 ")
        a = int(input(" "))
        if a == 1 : 
            Randgame(money)
        elif a == 2 : 
            Game(money)
        elif a ==3 : 
            gambling_sibmanwon(money)
        elif a == 4 : 
            break
    elif money >= 1000000 : 
            print("참여할 금액대를 선택해주세요")
            print("1번 : 1,000원")
            print("2번 : 10,000원")
            print("3번 : 100,000원")
            print("4번 : 1,000,000원")
            print("5번 : 종료하기 ")
            a = int(input(" "))
            if a == 1 : 
                Randgame(money)
            elif a == 2 : 
                Game(money)
            elif a ==3 : 
                gambling_sibmanwon(money)
            elif a == 4 : 
                gambling_1million(money)
            elif a == 5 : 
                break


        
