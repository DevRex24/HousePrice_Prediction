# House Price Predictor 🏠

A machine learning web application that predicts house prices based on house size using linear regression. The application provides both a user-friendly web interface and a REST API for programmatic access.

## Features ✨

- **Web Interface**: Interactive form for house price prediction with real-time validation
- **REST API**: JSON-based API endpoint for integration with other applications
- **Machine Learning Model**: Linear regression model trained on housing data
- **Input Validation**: Comprehensive validation for house size inputs (1-10,000 sq ft)
- **Responsive Design**: Modern, mobile-friendly interface with gradient backgrounds
- **Error Handling**: Robust error handling for both web and API interfaces

## Tech Stack 🛠️

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn (Linear Regression)
- **Data Processing**: pandas, numpy
- **Frontend**: HTML5, CSS3, Font Awesome icons
- **Model Persistence**: pickle

## Project Structure 📁

```
house_pricing/
│
├── app.py                 # Flask web application
├── model.py              # Model training script
├── test_model.py         # Model testing and validation
├── Housing_Price.csv     # Training dataset
├── house_price_model.pkl # Trained model (generated)
├── templates/
│   └── form.html         # Web interface template
└── README.md            # Project documentation
```

## Installation & Setup 🚀

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd house_pricing
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install flask pandas scikit-learn numpy
```

### Step 4: Train the Model
```bash
python model.py
```
This will:
- Load the housing data from `Housing_Price.csv`
- Train a linear regression model
- Save the trained model as `house_price_model.pkl`
- Display model performance metrics

### Step 5: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage 📋

### Web Interface
1. Open your browser and navigate to `http://localhost:5000`
2. Enter the house size in square feet (1-10,000)
3. Click "Predict Price" to get the estimated house price
4. The result will be displayed with proper formatting

### API Endpoint
**POST** `/predict`
```json
{
    "size": 1500
}
```

**Response:**
```json
{
    "price": 250000.50
}
```

**Error Response:**
```json
{
    "error": "House size must be a positive number"
}
```

### Example API Usage with curl
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"size": 1500}'
```

## Model Details 🤖

- **Algorithm**: Linear Regression
- **Features**: House size (square feet)
- **Target**: House price (USD)
- **Performance Metrics**: 
  - Mean Absolute Error (MAE)
  - R² Score
- **Validation**: 80/20 train-test split

### Model Training
The model training process includes:
1. Data loading and preprocessing
2. Price per square foot calculation
3. Train-test split (80/20)
4. Linear regression fitting
5. Performance evaluation
6. Model serialization

## Testing 🧪

Run the test script to validate model performance:
```bash
python test_model.py
```

This will:
- Display dataset information
- Show size and price ranges
- Calculate correlation between size and price
- Test predictions on sample data points

## Input Validation ✅

The application includes comprehensive input validation:
- **Positive Numbers**: Size must be greater than 0
- **Maximum Size**: Size cannot exceed 10,000 sq ft
- **Numeric Input**: Only numeric values are accepted
- **Error Messages**: Clear, user-friendly error messages

## Styling & UI 🎨

The web interface features:
- **Modern Design**: Clean, professional appearance
- **Gradient Background**: Light blue gradient background
- **Responsive Layout**: Works on desktop and mobile devices
- **Hover Effects**: Interactive elements with smooth transitions
- **Font Awesome Icons**: Professional iconography



