# VO2max Tool

The **VO2max Tool** is a web application designed to estimate an individual’s VO2 max, a key indicator of cardiovascular fitness.
This tool leverages various physiological and demographic inputs to provide accurate predictions and visualizations.
The backend is based on the formulae and code of the following article: [Anaerobic Threshold via VO2max and vLamax v2](https://www.kaggle.com/code/rasaff57/anaerobic-threshold-via-vo2max-and-vlamax-v2/notebook)
The application is built using **Flask**, **numpy**, and **matplotlib**, offering users an intuitive interface to interact with the model.

## Features
- **Data Prediction**: Estimate different values as predticted marathon time, AT-speed, AT-percent, FatMax and CarbMax and lactate steady state.
- **Visualization**: Generate plots to visualize the relationship between input features and VO2 max.
- **User-Friendly Interface**: A simple web-based interface for easy interaction and data input.
- **Create a PDF**: Simply create a PDF with input values, your plot and the output data.

<img src="https://github.com/Mr-MubelBubel/VO2max-Tool/blob/6b1cedb03285f01e286236e491e6f68fbdae7d19/docs/input-pic.png" width="900px">
<img src="https://github.com/Mr-MubelBubel/VO2max-Tool/blob/6b1cedb03285f01e286236e491e6f68fbdae7d19/docs/output-pic.png" width="500px">


## Installation

### Prerequisites
Ensure that you have Python 3.10+ installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step-by-step Instructions:

#### For Windows

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mr-MubelBubel/VO2max-Tool.git
   cd VO2max-Tool
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

   Open your browser and go to `http://127.0.0.1:5000/` to access the application.

#### For macOS and Linux

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mr-MubelBubel/VO2max-Tool.git
   cd VO2max-Tool
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
  Make sure, that you have [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask), [Flask-Core](https://pypi.org/project/Flask-Cors/), [Matplotlib](https://matplotlib.org/stable/install/index.html), [Numpy](https://numpy.org/install/) installed over **[pip](https://pip.pypa.io/en/stable/installation/)**.
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**
   Make sure, that you are in the right directory of the main.py file.
   ```bash
   python main.py
   ```

   Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

- Input the required parameters in the web form.
- For the PDF click on the **Download PDF** button.
- For medical use.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Mr-MubelBubel/VO2max-Tool/blob/main/LICENSE) file for more details.

---

Feel free to adjust any sections as needed! If you require further modifications or additional information, just let me know!
