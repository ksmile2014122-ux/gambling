import random

def gambling_sibmanwon() : 
    money = int(input("사용할 총 금액을 입력하세요 : ")) 

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
            
gambling()
123