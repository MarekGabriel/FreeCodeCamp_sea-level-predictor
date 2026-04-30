# Sea Level Predictor

This project is part of the ***Data Analysis with Python*** certification from freeCodeCamp.

## Project Description

In this project we have to analyze a dataset of global average sea level changes since 1880 and use it to predict future sea level rise up to the year 2050.
The goal is to visualize historical data and apply linear regression to estimate future trends.

Objectives:
* Create a scatter plot of historical sea level measurements
* Calculate the line of best fit using linear regression
* Predict future sea level rise through 2050
* Compare long-term trends with more recent data (from year 2000 onwards)

## Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* SciPy

## Dataset

https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/refs/heads/main/epa-sea-level.csv

Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

## How to Run

1. Clone the repository:
   git clone https://github.com/MarekGabriel/FreeCodeCamp_sea-level-predictor.git

2. Navigate to the project folder:
   cd FreeCodeCamp_sea-level-predictor

3. Run the script:
   sea_level_predictor.py

## Example Usage

Input:

no input needed (when running sea_level_predictor.py it imports proper data from .csv)

Output:

To be reached when calling function implemented:
* `sea_level_predictor.draw_plot()`

<p float="left">
  <img src="/scatter.png" width="250"/>
</p>

## Project Structure

* sea_level_predictor.py — main function: `draw_plot()` implementation
* main.py — An entrypoint file to be used in development. It imports main function implemented and runs unit tests automatically.
* test_module.py — unit tests provided by freeCodeCamp

## License

This project is licensed under the MIT License.
