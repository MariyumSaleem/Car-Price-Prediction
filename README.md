# Car Price Prediction Web App

This repository contains a web application for predicting car prices based on user inputs such as the car's company, model, year of manufacture, fuel type, and kilometers driven. The application uses a machine learning model(Linear regression) for predictions and provides a user-friendly interface.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [How It Works](#how-it-works)
4. [Setup Instructions](#setup-instructions)
5. [Project Structure](#project-structure)
6. [Features](#features)
7. [Screenshots](#screenshots)
8. [Future Enhancements](#future-enhancements)
9. [Contributors](#contributors)

---

## Introduction

The **Car Price Prediction Web App** is designed to estimate the price of a used car based on key features provided by the user. The app leverages a machine learning model trained on a dataset of cleaned car records(Cleaned by using preprocessing techniques). The user interacts with a sleek, responsive interface to input the required data, and the app provides an instant prediction.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas
- **Model Serialization**: Pickle

---

## How It Works

1. **Data Input**: The user provides details such as car company, model, manufacturing year, fuel type, and kilometers driven via a web form.
2. **Prediction**: The app sends the input data to the Flask backend, where a pre-trained Linear Regression model processes it to generate a price prediction.
3. **Output**: The predicted price is displayed on the screen.

---

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or above
- Pip package manager

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/MariyumSaleem/Car-Price-Prediction.git
   cd Car-Price-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the dataset (`Cleaned Car.csv`) and the pre-trained model (`LinearRegressionModel.pkl`) are in the project directory.

4. Run the Flask application:
   ```bash
   python application.py
   ```

5. Open the app in your browser:
   ```plaintext
   http://127.0.0.1:5000/
   ```

---

## Project Structure

```
Car-Price-Prediction/
│
├── application.py        # Main Flask application
├── Cleaned Car.csv       # Dataset used for model training
├── LinearRegressionModel.pkl  # Pre-trained ML model
├── templates/
│   └── index.html        # Frontend HTML file
├── static/
│   ├── css/
│   │   └── style.css     # Custom CSS for styling
└── requirements.txt      # Python dependencies
```

---

## Features

- Interactive and responsive user interface.
- Predicts car prices based on:
  - Car company
  - Car model
  - Manufacturing year
  - Fuel type
  - Kilometers driven
- Real-time predictions powered by a trained Linear Regression model.

---

## Screenshots

<img width="873" alt="car prediction" src="https://github.com/user-attachments/assets/59e4f7f3-35ab-4dae-bf15-8dbf6b1d7916">


---

## Future Enhancements

- Add more advanced machine learning models for better accuracy.
- Expand the dataset to include more car brands and features.
- Deploy the application online using services like AWS, Heroku, or Google Cloud.
- Implement user authentication for saving past predictions.

---

## Contributors

This project is developed and maintained by:
- **Mariam Saleem**  
  GitHub: [MariyumSaleem](https://github.com/MariyumSaleem)

---
 
