# ===============================================
# PROFESSIONAL DATA ANALYSIS PORTFOLIO
# Domains: Retail, Education, Weather, Healthcare, Finance
# Skills: Data Cleaning, Analysis, Visualization, Insights
# ===============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# PROJECT 1 : RETAIL SALES ANALYSIS
# -------------------------------------------------
def retail_analysis():

    print("\n--- RETAIL SALES ANALYSIS ---")

    data = {
        "Product": ["Shirt","Jeans","Shoes","Jacket","Tshirt","Shoes","Shirt"],
        "Region": ["North","South","East","West","North","South","East"],
        "Sales": [2000,3000,2500,4000,1500,2700,1800]
    }

    df = pd.DataFrame(data)

    # Data Cleaning
    df.drop_duplicates(inplace=True)

    # Analysis
    region_sales = df.groupby("Region")["Sales"].sum()

    # Visualization
    region_sales.plot(kind="bar",title="Retail Sales by Region")
    plt.show()

    # Business Insight
    print("Insight: West region has the highest sales potential.")

# -------------------------------------------------
# PROJECT 2 : EDUCATION PERFORMANCE ANALYSIS
# -------------------------------------------------
def education_analysis():

    print("\n--- EDUCATION PERFORMANCE ANALYSIS ---")

    data = {
        "Student": ["A","B","C","D","E"],
        "Math": [85,78,92,70,88],
        "Science": [80,75,90,65,85],
        "English": [88,79,91,72,86]
    }

    df = pd.DataFrame(data)

    # Data Cleaning
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Analysis
    df["Average"] = df[["Math","Science","English"]].mean(axis=1)

    # Visualization
    df.plot(x="Student", y="Average", kind="bar", title="Student Average Scores")
    plt.show()

    # Insight
    print("Insight: Student C has the highest academic performance.")

# -------------------------------------------------
# PROJECT 3 : WEATHER DATA ANALYSIS
# -------------------------------------------------
def weather_analysis():

    print("\n--- WEATHER ANALYSIS ---")

    data = {
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Temperature": [30,32,31,29,33,34,35],
        "Humidity": [60,65,55,70,50,45,40]
    }

    df = pd.DataFrame(data)

    # Cleaning
    df.dropna(inplace=True)

    # Visualization
    plt.plot(df["Day"],df["Temperature"], marker='o')
    plt.title("Weekly Temperature Trend")
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.show()

    # Insight
    print("Insight: Temperature increases towards weekend.")

# -------------------------------------------------
# PROJECT 4 : HEALTHCARE DATA ANALYSIS
# -------------------------------------------------
def healthcare_analysis():

    print("\n--- HEALTHCARE ANALYSIS ---")

    data = {
        "Patient": ["P1","P2","P3","P4","P5"],
        "Age": [25,40,35,50,28],
        "BloodPressure": [120,140,130,150,125]
    }

    df = pd.DataFrame(data)

    # Analysis
    avg_bp = df["BloodPressure"].mean()

    # Visualization
    df.plot(x="Patient", y="BloodPressure", kind="bar", title="Patient Blood Pressure")
    plt.show()

    # Insight
    print("Average Blood Pressure:", avg_bp)
    print("Insight: Patients above age 40 tend to have higher BP.")

# -------------------------------------------------
# PROJECT 5 : FINANCE STOCK ANALYSIS
# -------------------------------------------------
def finance_analysis():

    print("\n--- FINANCE STOCK ANALYSIS ---")

    data = {
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "StockPrice": [100,110,108,120,130,125]
    }

    df = pd.DataFrame(data)

    # Visualization
    plt.plot(df["Month"],df["StockPrice"], marker='o')
    plt.title("Stock Price Trend")
    plt.xlabel("Month")
    plt.ylabel("Price")
    plt.show()

    # Insight
    print("Insight: Stock shows upward growth trend.")

# -------------------------------------------------
# MAIN PORTFOLIO EXECUTION
# -------------------------------------------------
def main():

    print("DATA ANALYST PROFESSIONAL PORTFOLIO")
    print("-----------------------------------")

    retail_analysis()
    education_analysis()
    weather_analysis()
    healthcare_analysis()
    finance_analysis()

    print("\nPortfolio Completed Successfully")

if __name__ == "__main__":
    main()