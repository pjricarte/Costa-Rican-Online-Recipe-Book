from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------------------------------------------
# Continue the data here please
# -----------------------------------------------------------------

recipes = {
    "desayuno": {
        "Gallo Pinto": {
            "image": "gallo_pinto.jpg",
            "ingredients_es": [
                "1 taza de arroz",
                "1 taza de frijoles negros cocidos",
                "1 cebolla picada",
                "Culantro picado",
                "Salsa Lizano"
            ],
            "ingredients_en": [
                "1 cup rice",
                "1 cup cooked black beans",
                "1 chopped onion",
                "Chopped cilantro",
                "Lizano sauce"
            ],
            "steps_es": [
                "Sofría la cebolla.",
                "Agregue los frijoles y mezcle.",
                "Añada el arroz y la Salsa Lizano.",
                "Mezcle todo hasta calentar."
            ],
            "steps_en": [
                "Sauté the onion.",
                "Add the beans and mix.",
                "Add the rice and Lizano sauce.",
                "Mix everything until warm."
            ]
        }
    },

    "almuerzo": {},
    "cena": {}
}

# -----------------------------------------------------------------
# ROUTES
# -----------------------------------------------------------------

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/list/<meal>")
def list_foods(meal):
    foods = recipes.get(meal, {})
    return render_template("list_foods.html", meal=meal, foods=foods)

@app.route("/recipe/<meal>/<food>")
def recipe(meal, food):
    data = recipes[meal][food]
    return render_template("recipe.html", meal=meal, food=food, data=data)

if __name__ == "__main__":
    app.run(debug=True)