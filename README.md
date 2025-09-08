# Berlin Rent Price Analysis

This project performs an **exploratory data analysis (EDA)** on rental prices in different districts of Berlin.  
It was built with **Python**, using data analysis and visualization libraries such as `pandas`, `matplotlib`, and `seaborn`.

## 📂 Project Structure

python_project_4/
├── env/ # virtual environment
├── data/
│ └── berlin_rent.csv # dataset with simulated rental data
├── images/ # generated plots
│ ├── distribution_prices.png
│ ├── average_price.png
│ └── relationship_sqm_price.png
├── berlin_rent_analysis.py # main analysis script
├── README.md # English version
└── README.de.md # German version

## ⚙️ Technologies Used
- Python 3.13
- pandas
- matplotlib
- seaborn

## 📊 Analysis Performed
1. Initial dataset exploration (`head`, `info`, `describe`)
2. Calculation of average rent price by district
3. Visualizations:
   - Distribution of rental prices
   - Average rent price by district (bar chart)
   - Relationship between apartment size (sqm) and rent price (scatter plot)

## 📸 Example Results

### Distribution of rental prices
![Distribution of rental prices](./images/distribution_prices.png)

### Average rent price by district
![Average rent price by district](./images/average_price.png)

### Relationship between size (sqm) and rent price
![Relationship sqm vs rent price](./images/relationship_sqm_price.png)

## 🚀 How to Run the Project

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
Install dependencies:
pip install pandas matplotlib seaborn
Run the script:
python3 berlin_rent_analysis.py
🙋 Author
Project developed by Paula Espinoza Gaspar
 This project is part of my portfolio for Werkstudent positions.
