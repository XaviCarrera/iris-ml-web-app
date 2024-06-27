from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load our model
with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)
    prediction = model.predict(final_input)
    output = prediction[0]
    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(debug=True)