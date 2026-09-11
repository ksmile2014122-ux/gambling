import random
### 연서님 코드 
def Randgame(my_money):
    while True:
        palyer = random.randint(1, 30)
        computer = random.randint(1, 30)
        i = int(input("계속 하시려면 1번을 눌러주세요. 원하지 않는다면 2번을 눌러주세요 : "))

        if i == 1:
            if palyer > computer:
                my_money += 1000 
                print("이겼습니다!! 🥳")
                print(f"{palyer}가 당신 숫자입니다.")
                print(f"{computer}가 딜러 숫자입니다.")
                print(f"{my_money}가 당신이 소지한 돈입니다.")
            
            elif palyer < computer:
                my_money -=  1000
                
                print("졌습니다")
                print(f"{palyer}가 당신 숫자입니다.")
                print(f"{computer}가 딜러 숫자입니다.")
                print(f"{my_money}가 당신이 소지한 돈입니다.")
                if my_money <= 0:
                    print("돈을 다 잃었습니다. 게임 오버!")
                    break
    
            else:
                print(f"{palyer}가 당신 숫자입니다.")
                print(f"{computer}가 딜러 숫자입니다.")
                print(f"{my_money}가 당신이 소지한 돈입니다.")
                print("비겼습니다! 다시 진행합니다.")
        elif i == 2:
            print("게임을 종료합니다.")
            print(f"{my_money}가 당신이 소지한 돈입니다.")
            break

### 조경인 코드 
def gambling_sibmanwon(money) : 

    while True : 
        if money < 100000 : 
            print("가진 돈을 모두 잃었습니다. 게임장을 나가주세요, 택시비는 지원해드릴께요 :) ")
            break
        elif money >= 100000 : 
            aa= int(input("다음판을 진행합니다. 게임을 그만두고 싶다면 0을 계속진행하시려면 1을 입력하세요 "))
            if aa == 1 : 
                dealer = random.randint(1,30)
                user = random.randint(1, 30)
                if user > dealer :
                    print(f"당신은 이겼습니다. 당신의 숫자는 {user}이고, 딜러의 숫자는 {dealer}") 
                    money += 100000
                    print(f"총금액은 : {money:,} 입니다. ") 
                elif user == dealer :
                    print(f"당신의 숫자와 딜러의 숫자가 {dealer}로 같습니다.")
                    print(f"총금액은 : {money:,} 입니다. ") 
                elif user < dealer : 
                    print(f"당신은 졌습니다. 당신의 숫자는 {user}이고, 딜러의 숫자는 {dealer}") 
                    money -= 100000
                    print(f"총금액은 : {money:,} 입니다. ")
            elif aa == 0 : 
                break
            
