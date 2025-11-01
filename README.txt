# Spam Message Classifier

A machine learning project that detects spam messages using a Naive Bayes classifier with a Flask web interface.

## Project Structure
- kishore.py     : Training script that creates the spam detection model
- app.py         : Flask web application to serve the spam detector
- data/          : Directory containing the training dataset
- model/         : Directory containing trained model files
- templates/     : HTML templates for the web interface
- static/        : CSS and JavaScript files for styling and interactivity

## Requirements
- Python 3.11 or later
- Required Python packages (install using pip):
  - pandas
  - scikit-learn
  - flask

## Setup Instructions

1. Install required packages:
   ```
   python -m pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python kishore.py
   ```
   This will:
   - Load the spam dataset
   - Train a Naive Bayes classifier
   - Save the model and vectorizer to the 'model' directory

3. Run the web application:
   ```
   python app.py
   ```
   - The app will be available at http://127.0.0.1:5000
   - Open this URL in your web browser

## Usage
1. Open your web browser and go to http://127.0.0.1:5000
2. Enter a message in the text box
3. Click "Check Message"
4. The system will classify the message as either spam or not spam

## Project Files Description
- kishore.py: Contains the machine learning model training code
- app.py: Flask application that serves the web interface
- requirements.txt: List of Python package dependencies
- templates/index.html: Main webpage template
- static/css/style.css: CSS styling for the web interface
- static/js/script.js: JavaScript for handling form submission
- data/spam.csv: Training dataset for spam classification

## Troubleshooting
1. If you see "ModuleNotFoundError", run:
   ```
   python -m pip install -r requirements.txt
   ```

2. If you see "FileNotFoundError" for model files:
   ```
   python kishore.py
   ```

3. If the web page doesn't load, ensure:
   - Flask app is running (python app.py)
   - You're using the correct URL (http://127.0.0.1:5000)

## Notes
- The model is trained on a simple dataset for demonstration
- The web interface uses modern CSS with animations
- The application supports real-time classification