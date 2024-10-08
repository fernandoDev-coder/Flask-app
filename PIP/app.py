from flask import Flask, render_template

app = Flask(__name__)


class User:
    def __int__(self):
        self.nombre = ""

    def nombre_aleatorio(self, parametro):
        print()


# crear variable
user = User()
# EL SELF NO HAY QUE PONERLO ES INTRINSECO
user.nombre_aleatorio("hola")


@app.route("/")
def home():
    User.query()
    lista_strings = ["a", "b", "c"]
    return render_template("index.html", strings=lista_strings)


if __name__ == "__main__":
    app.run(debug=True)
