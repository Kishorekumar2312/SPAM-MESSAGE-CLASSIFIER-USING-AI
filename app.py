from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your model and vectorizer
model = pickle.load(open('model/spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = [message]
    vect = vectorizer.transform(data)
    prediction = model.predict(vect)[0]

    if prediction == 1:
        result = "🚨 Spam"
    else:
        result = "✅ Not Spam"

    # return the result within the webpage
    return render_template('index.html', prediction=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
