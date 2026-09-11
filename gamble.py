
import random

def gambling_1million():

    cash = int(input("사용할 금액을 입력해주세요: "))

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

gambling_1million()

