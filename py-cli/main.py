import os

class Ventilyator:
    def __init__(self):
        self.sostoyanie = "Выключен"
        self.povorota = False

    def vklyuchit(self):
        if self.sostoyanie == "Выключен":
            self.sostoyanie = "Медленно"
            print("Вентилятор включен и находится в режиме медленной скорости.")

    def uvelichit_skorost(self):
        if self.sostoyanie == "Медленно":
            self.sostoyanie = "Средне"
            print("Вентилятор переключился на среднюю скорость.")
        elif self.sostoyanie == "Средне":
            self.sostoyanie = "Быстро"
            print("Вентилятор переключился на самую быструю скорость.")

    def umenshit_skorost(self):
        if self.sostoyanie == "Средне":
            self.sostoyanie = "Медленно"
            print("Вентилятор переключился на медленную скорость.")
        elif self.sostoyanie == "Быстро":
            self.sostoyanie = "Средне"
            print("Вентилятор переключился на среднюю скорость.")

    def vyklyuchit(self):
        self.sostoyanie = "Выключен"
        self.povorota = False
        print("Вентилятор выключен.")

    def povorot(self):
        if self.sostoyanie != "Выключен":
            self.povorota = not self.povorota
            if self.povorota:
                print("Вентилятор начал поворачиваться из стороны в сторону.")
            else:
                print("Вентилятор прекратил поворот.")

    def print_status(self):
        if self.povorota:
            if self.sostoyanie == "Медленно" or self.sostoyanie == "Средне" or self.sostoyanie == "Быстро":
                print(f"Вентилятор работает на скорости {self.sostoyanie} и поворачивается.")
            else:
                print(f"Вентилятор находится в состоянии {self.sostoyanie} и поворачивается.")
        else:
            if self.sostoyanie == "Медленно" or self.sostoyanie == "Средне" or self.sostoyanie == "Быстро":
                print(f"Вентилятор работает на скорости {self.sostoyanie}.")
            else:
                print(f"Вентилятор находится в состоянии {self.sostoyanie}.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    ventilyator = Ventilyator()

    deystviya = {
        "1": ventilyator.vklyuchit,
        "2": ventilyator.uvelichit_skorost,
        "3": ventilyator.umenshit_skorost,
        "4": ventilyator.vyklyuchit,
        "5": ventilyator.povorot
    }

    while True:
        clear_console()
        ventilyator.print_status()
        print("\nУправление вентилятором")
        print("1 - Включить")
        print("2 - Увеличить скорость")
        print("3 - Уменьшить скорость")
        print("4 - Выключить")
        print("5 - Сделать, чтобы вентилятор поворачивался")

        deystvie = input("Выберите действие ('q' для выхода): ")
        if deystvie == 'q':
            clear_console()
            break
        elif deystvie in deystviya:
            deystviya[deystvie]()
        else:
            print("Неверное действие, попробуйте снова.")

if __name__ == "__main__":
    main()