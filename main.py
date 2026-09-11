# Randgame() : 1,000원
# Game() : 10,000원
# gambling_sibmanwon : 100,000원 
# gambling_1million() : 1,000,000원
import random
def gambling_1million(cash):

    while True:
        print()
        print(f"{1000000:,}원짜리 도전을 시작합니다!")
        print("1. 그만하기")
        print("2. 계속하기")

        dealer_num = random.randint(1, 30)
        player_num = random.randint(1, 30)


        if cash >= 1000000:

            choose = int(input("선택해주세요: "))

            if choose == 1 :
                print("게임을 종료합니다.")
                break
            if choose == 2: 
                if dealer_num < player_num:
                    cash += 1000000
                    print()
                    print(f"당신은 {1000000:,}원을 얻었습니다!")
                    print(f"남은금액: {cash:,}")
                    print(f"딜러의 숫자: {dealer_num}")
                    print(f"당신의 숫자: {player_num}")

                elif dealer_num == player_num:
                    print(f"딜러의 숫자: {dealer_num}")
                    print(f"당신의 숫자: {player_num}")
                    print("딜러와 당신의 숫자가 같습니다. 번호를 다시 뽑겠습니다.")

                elif dealer_num > player_num:
                    cash -= 1000000
                    print()
                    print(f"당신은 {1000000:,}원을 잃었습니다...")
                    print(f"남은금액: {cash:,}")
                    print(f"딜러의 숫자: {dealer_num}")
                    print(f"당신의 숫자: {player_num}")

                    if cash < 1000000:
                        print(f"당신의 남은 금액은 {cash:,}원입니다. 게임을 계속 할 수 없습니다. 나가주세요.")
                        print("게임을 종료합니다.")
                        break

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


        
