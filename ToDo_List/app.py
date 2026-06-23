from flask import Flask, render_template, request, redirect

app = Flask(__name__)

task_dic = {}

# Load tasks from file
try:
    file = open("tasks.txt", "r")
    for line in file:
        data = line.strip().split(",")
        task_dic[int(data[0])] = {
            "task": data[1]
        }
    file.close()
except FileNotFoundError:
    pass


def save_tasks():
    file = open("tasks.txt", "w")
    for task_id in task_dic:
        file.write(str(task_id) + "," + task_dic[task_id]["task"] + "\n")
    file.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task_id = int(request.form["id"])
        task = request.form["task"]

        task_dic[task_id] = {
            "task": task
        }

        save_tasks()

        return redirect("/view")

    return render_template("add.html")


@app.route("/view")
def view():
    return render_template("view.html", tasks=task_dic)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        task_id = int(request.form["id"])

        if task_id in task_dic:
            del task_dic[task_id]
            save_tasks()

        return redirect("/view")

    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)