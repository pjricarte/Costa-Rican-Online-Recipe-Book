from flask import Flask, render_template

app = Flask(__name__)

# Recipe data (you can expand this)
recipes = {
    "desayuno": [
        {
            "name": "Gallo Pinto",
            "es": "El gallo pinto es un plato tradicional de arroz y frijoles mezclados con especias.",
            "en": "Gallo pinto is a traditional dish of rice and beans mixed with spices."
        },
        {
            "name": "Huevos Rancheros",
            "es": "Huevos rancheros servidos con tortillas y salsa fresca.",
            "en": "Ranch-style eggs served with tortillas and fresh salsa."
        }
    ],
    "almuerzo": [
        {
            "name": "Casado",
            "es": "El casado incluye arroz, frijoles, plátanos, ensalada y una proteína.",
            "en": "Casado includes rice, beans, plantains, salad, and a protein."
        },
        {
            "name": "Sopa Negra",
            "es": "Una sopa de frijoles negros con huevo duro y cilantro.",
            "en": "A black bean soup with boiled egg and cilantro."
        }
    ],
    "cena": [
        {
            "name": "Arroz con Pollo",
            "es": "Arroz con pollo con verduras frescas y especias.",
            "en": "Chicken rice with fresh vegetables and spices."
        },
        {
            "name": "Olla de Carne",
            "es": "Un guiso tradicional de carne con vegetales.",
            "en": "A traditional beef stew with vegetables."
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html", recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)