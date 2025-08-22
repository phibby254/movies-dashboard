# BMI Application

This is a simple Body Mass Index (BMI) application that calculates BMI based on user-provided weight and height. It categorizes the BMI value into different health categories.

## Features

- Calculate BMI using weight and height.
- Determine BMI category (Underweight, Normal weight, Overweight, Obesity).
- Input validation for weight and height.

## Installation

To get started with the BMI application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd bmi-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the BMI calculator, you can run the `bmi_calculator.py` script. You can also import the `BMICalculator` class in your own Python scripts to utilize its functionality.

### Example

```python
from src.bmi_calculator import BMICalculator

calculator = BMICalculator()
bmi = calculator.calculate_bmi(weight=70, height=1.75)
category = calculator.get_bmi_category(bmi)

print(f"BMI: {bmi}, Category: {category}")
```

## Running Tests

To ensure the application works as expected, you can run the unit tests located in the `tests` directory:

```
pytest tests/test_bmi_calculator.py
```

## License

This project is licensed under the MIT License.