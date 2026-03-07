1000406_Jeyaditya_AIY1_SA_Rocket_path_visualisation

# Aerospace Mission Control & Flight Simulator
Link to access app - [https://1000406-jeyaditya-aiy1-sa-rocket-path-visualisation.streamlit.app/]

## Mathematics for AI — Summative Assessment
Project Overview

Aerospace Mission Control & Flight Simulator is an interactive Streamlit web application developed as part of the Mathematics for AI course. The project integrates data analytics, mathematical modeling, and simulation techniques to explore and predict rocket flight dynamics.

The application serves two primary purposes:

* Analyze historical rocket mission data to uncover trends and correlations between mission parameters.
*  Simulate new flight trajectories using physics-based models grounded in classical mechanics and numerical computation.

This project bridges theoretical mathematics with practical aerospace applications, offering an engaging platform for both data-driven insights and real-time simulation.

# Features
## Data Preprocessing

* Cleans and structures raw rocket mission datasets.
* Handles DD-MM-YYYY date formats and null values efficiently.
* Ensures consistent data types for accurate analysis and visualization.

## Exploratory Data Analysis (EDA)

  * Interactive visualizations powered by Plotly and Seaborn.
      Key analytical charts include:
          Payload vs. Fuel Consumption
          Mission Cost vs. Success Rate
          Correlation Heatmap for identifying inter-variable relationships.
    * Enables dynamic filtering and comparison across multiple missions.

## Flight Simulation

   * Implements a real-time physics engine based on Newton’s Second Law (F = ma).
   * Models variable mass due to fuel burn and atmospheric drag effects.
   * Uses numerical integration (Euler or Runge-Kutta methods) to compute altitude and velocity over time.
   * Generates interactive trajectory plots that evolve dynamically as simulation parameters change.

## Mathematical Concepts

The project integrates several mathematical foundations central to AI and aerospace modeling:

  *  Differential Equations:
      Used to model rocket motion, accounting for acceleration, drag, and mass variation over time.
  * Linear Algebra:
      Supports matrix-based computations for data correlation and transformation.
  * Statistics:
      Applied in exploratory data analysis to identify trends, correlations, and performance metrics.

These mathematical tools collectively enable accurate simulation and insightful data interpretation.

## Technologies Used

## Category
Tools & Libraries
* Frontend Framework
   Streamlit
* Data Handling
   Pandas, NumPy
* Visualization
  Plotly, Seaborn, Matplotlib

# How to Run

  * Clone the repository:git clone https://github.com/your-username/aerospace-mission-control.git cd aerospace-mission-control
  * Install dependencies:pip install -r requirements.txt
  * Run the Streamlit app:streamlit run app.py
  * Access the application.
  * Open the local URL displayed in the terminal (typically http://localhost:8501) to launch the web interface.

# Future Enhancements

  * Integration of machine learning models for mission success prediction.
  * Addition of 3D trajectory visualization using advanced rendering libraries.
  * Expansion of the dataset to include satellite and interplanetary missions.

# Credits

Developed as part of the Mathematics for AI course to demonstrate the synergy between mathematical theory, computational modeling, and aerospace engineering.

* Student Name: A Jeyaditya
* Registration number: 1000406
* CRS Facilitator: Syed Ali Beema
* Institution: Jain Vidyalaya IB World School
* Course: Mathematics for AI
* Year: 2026
