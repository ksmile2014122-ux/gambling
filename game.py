import random

def Game():

    money = int(input("보유 금액: "))

    while True:

        # 10000보다 적으면 게임 종료
        if money < 10000:
            print("보유 금액이 10000원보다 작습니다.")
            print("게임이 종료됩니다.")
            break

        user_card = random.randint(1, 30)
        dealer_card = random.randint(1, 30)

        print()
        print("게임을 시작합니다.")
        print(f"user 카드: {user_card}")
        print(f"dealer 카드: {dealer_card}")

        # 승리
        if user_card > dealer_card:
            money += 10000
            print("결과: user의 승리입니다!")
            print("10000원을 획득했습니다.")

        # 패배
        elif user_card < dealer_card:
            money -= 10000
            print("결과: dealer의 승리입니다!")
            print("10000원을 잃었습니다.")

        # 무승부
        else:
            print("결과: 무승부입니다.")

        print(f"현재 보유 금액: {money}원")

        mode = input("Go? or Stop?: ").lower()

        if mode == "go":
            print("다음 게임을 시작합니다.")

        elif mode == "stop":
            print("게임을 종료합니다.")
            print(f"최종 보유 금액: {money}원")
            break

        else:
            print("다시 선택해주세요.")


Game()