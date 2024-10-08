from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from BE import plot_Run

# Create Flask App and config database
app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def data():
    if request.method == "POST":
        vo2max = request.form['vo2max']
        vlamax = request.form['vlamx']
        bw = request.form['bw']
        ks1 = request.form['ks1']
        ks2 = request.form['ks2']
        volrel = request.form['volrel']

        result = pred(vo2max, vlamax, bw, ks1, ks2, volrel)
        print(result)
        return result

    else:
        print("Problem")
        return render_template("index.html")


def pred(vo2max: float, vlamax: float, bw: int, ks1: float, ks2: float, volrel: float):
    output = plot_Run.plot_Run(vo2max, vlamax, bw, ks1, ks2, volrel)
    return output


if __name__ == "__main__":
    app.run(debug=True)

# Kill process
# sudo lsof -i :<PortNumber>
# kill -9 <PID>
