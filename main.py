from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from BE import plot_Run

# Create Flask App
app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def data():
    if request.method == "POST":
        vo2max = float(request.form['vo2max'])
        vlamax = float(request.form['vlamax'])
        bw = float(request.form['bw'])
        ks1 = float(request.form['ks1'])
        ks2 = float(request.form['ks2'])
        volrel = float(request.form['volrel'])

        result = pred(vo2max, vlamax, bw, ks1, ks2, volrel)
        return result

    else:
        return render_template("index.html")


def pred(vo2max: float, vlamax: float, bw: float, ks1: float, ks2: float, volrel: float):
    output = plot_Run.plot_Run(vo2max, vlamax, bw, ks1, ks2, volrel)
    return output


if __name__ == "__main__":
    app.run(debug=True)

# Kill process
# sudo lsof -i :<PortNumber>
# kill -9 <PID>
