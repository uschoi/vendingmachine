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
            if self._change == 0:
                return "잔액이 0원입니다."

            coins = [500, 100, 50, 10]  # no space after,be4 bracket
            coin_counts = []
            for coin in coins:
                n = self._change // coin  # sequential processing
                self._change -= n * coin
                coin_counts.append(n)

            coins_to_return = []
            for coin, coin_count in zip(coins, coin_counts):
                coins_to_return += [str(coin) + "원"] * coin_count
            return "잔액은:" + ", ".join(coins_to_return) + "입니다."
        else:
            return "알 수 없는 명령입니다."





#  잔액을 반환하게 만들기
#  음료 커피를 누르면 돈이 부족하다거나, 음료와함께 잔액을 반환하며 잔액을 표시
