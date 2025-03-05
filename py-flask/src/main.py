from flask import Flask, jsonify, render_template

app = Flask(__name__)

class Ventilyator:
    def __init__(self):
        self.sostoyanie = "Выключен"
        self.skorost = "Выключен"
        self.povorota = False

    def vklyuchit(self):
        if self.sostoyanie == "Выключен":
            self.sostoyanie = "Включен"
            self.skorost = "Медленная"
            return "Вентилятор включен и находится в режиме медленной скорости."

    def uvelichit_skorost(self):
        if self.skorost == "Медленная":
            self.skorost = "Средняя"
            return "Вентилятор переключился на среднюю скорость."
        elif self.skorost == "Средняя":
            self.skorost = "Быстрая"
            return "Вентилятор переключился на самую быструю скорость."

    def umenshit_skorost(self):
        if self.skorost == "Средняя":
            self.skorost = "Медленная"
            return "Вентилятор переключился на медленную скорость."
        elif self.skorost == "Быстрая":
            self.skorost = "Средняя"
            return "Вентилятор переключился на среднюю скорость."

    def vyklyuchit(self):
        self.sostoyanie = "Выключен"
        self.skorost = "Выключен"
        self.povorota = False
        return "Вентилятор выключен."

    def povorot(self):
        if self.sostoyanie == "Включен":
            self.povorota = not self.povorota
            return "Вентилятор поворот " + ("включен." if self.povorota else "выключен.")

    def get_status(self):
        return {
            "status": self.sostoyanie,
            "speed": self.skorost,
            "rotation": "Включен" if self.povorota else "Выключен"
        }

ventilyator = Ventilyator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<action>', methods=['GET'])
def control(action):
    actions = {
        "vklyuchit": ventilyator.vklyuchit,
        "uvelichit": ventilyator.uvelichit_skorost,
        "umenshit": ventilyator.umenshit_skorost,
        "vyklyuchit": ventilyator.vyklyuchit,
        "povorot": ventilyator.povorot
    }
    if action in actions:
        message = actions[action]()
        return jsonify(ventilyator.get_status())
    else:
        return jsonify({"status": "Неверное действие"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)