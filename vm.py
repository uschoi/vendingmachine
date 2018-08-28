class VendingMachine:
    def __init__(self):
        self._change = 0


    def run(self, raw):

        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]
        i = 0
        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다."

        elif cmd == "동전":
            coin = params[0]
            self._change += int(coin)
            return coin + "원을 넣었습니다."

        elif cmd == "음료":
            beverage = params[0]
            known_beverage = {
                "커피": 150,
                "우유": 200,
                "밀크커피": 300,
            }

            if beverage not in known_beverage:
                return "알 수 없는 음료입니다."
            price = known_beverage[beverage]
            if self._change < price:
                return "잔액이 부족합니다."
            self._change = self._change - price
            return "가격은 " + str(price) + "원입니다."

        elif cmd == "반환":
            self._change = int(params[0])
            coins = [ 500, 100, 50, 10 ]
            coin_numbers = []
            while self._change != 0:
                num500 = self._change // 500
                self._change -= num500 * 500
                coin_numbers.append(num500)
                num100 = self._change // 100
                self._change -= num100 * 100
                coin_numbers.append(num100)
                num50 = self._change // 50
                self._change -= num50 * 50
                coin_numbers.append(num50)
                num10 = self._change // 10
                self._change -= num10 * 10
                coin_numbers.append(num10)
                print("잔액은:" + ",".join([str(coin) + "원" for coin in coin_numbers]) + "입니다.")
            return "잔액이 0원입니다."
        else:
            return "알 수 없는 명령입니다."





#  잔액을 반환하게 만들기
#  음료 커피를 누르면 돈이 부족하다거나, 음료와함께 잔액을 반환하며 잔액을 표시
