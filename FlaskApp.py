from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

tasks = [
    {
        "name": "Junaid",
        "contact": "** I am The developer of this App. **",
        "done": False,
        "id": 1,
    },
    {
        "name": "pepper",
        "contact": "9845370709",
        "done": False,
        "id": 1,
    },
    {
        "name": "Nathan Mason",
        "contact": "2468231075",
        "done": False,
        "id": 2,
    },
    {
        "name": "Tammy Stephens",
        "contact": "2029490263",
        "done": False,
        "id": 3,
    },
    {
        "name": "Melvin Peters",
        "contact": "2042695050",
        "done": False,
        "id": 4,
    },
    {
        "name": "Stephanie Hanson",
        "contact": "5981397487",
        "done": False,
        "id": 5,
    },
]


@app.route("/")
def home():
    file = open("index.html", "r")
    home = file.read()
    return home


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({"status": "error", "message": "Please provide the data!"}, 400)

    task = {
        "id": tasks[-1]["id"] + 1,
        "name": request.json["name"],
        "contact": request.json.get("contact", ""),
        "done": False,
    }
    tasks.append(task)
    return jsonify({"status": "success", "message": "Task added succesfully!"})


@app.route("/get-data")
def get_task():
    return jsonify({"data": tasks})


if __name__ == "__main__":
    app.run(debug=True)
