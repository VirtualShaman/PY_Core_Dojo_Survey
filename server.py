from flask import Flask, render_template,request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST", "GET"])
def process():

    name = request.form.get("Name")
    location = request.form.get("Locations")
    language = request.form.get("Languages")
    comment = request.form.get("Comment")

    return render_template('result.html', name=name, location=location, language=language, comment=comment)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
