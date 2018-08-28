from vm import VendingMachine

def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다." == m.run("잔액")

def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다." == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다." == m.run("동전 100")
    assert "잔액은 100원입니다." == m.run("잔액")


def test_accumulation_of_change():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다." == m.run("잔액")

def test_unknown_cmd():
    m = VendingMachine()
    assert "알 수 없는 명령입니다." == m.run("aw")

def test_음료_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피가 나왔습니다." == m.run("음료 커피")
    assert "잔액은 350원입니다." == m.run("잔액")

def test_모르는음료_뽑기():
    m = VendingMachine()
    m.run("동전 500")
    assert "알 수 없는 음료입니다." == m.run("음료 사이다")
    assert "잔액은 500원입니다." == m.run("잔액")

def test_동전부족_음료뽑기():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다." == m.run("음료 커피")
    assert "잔액은 100원입니다." == m.run("잔액")

def test_특정액수_반환명령():
    m = VendingMachine()
    assert "잔액은:500원, 100원, 100원, 50원, 10원, 10원, 10원입니다." == m.run("반환 780")
