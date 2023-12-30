# Simple Mannings App

## Overview
The Simple Mannings App is a web application designed for hydrologists, civil engineers, and environmental scientists to calculate and visually analyze water flow in a prismatic trapezoidal channel. The app uses the Mannings equation to iteratively solve the unknown depth of flow for a given flow rate. 

## What is Manning's Equation?
Manning's equation is an empirical formula used to calculate the velocity of water in an open channel flow. The metric version of the equation is:

The flow rate \( Q \) using Manning's equation for an open channel is given by:

$$ \[ Q = \frac{1}{n} A R^{2/3} S^{1/2} \] $$

where:

- \( Q \) is the flow rate ($\( m^3/s \$)),
- \( n \) is the Manning's roughness coefficient (\$( s/m^{1/3} \$)),
- \( A \) is the cross-sectional area of flow ($\( m^2 \$)),
- \( R \) is the hydraulic radius (\( m \)), which is the area of flow divided by the wetted perimeter,
- \( S \) is the slope of the energy grade line, which is often approximated as the slope of the channel bed if the flow is uniform.

$R = A / P$

For a prismatic channel, which is a channel with a constant cross-sectional shape and size along its length, the area A and the wetted perimeter P can be calculated based on the channel's geometric dimensions.


## Project Files
- app.py
The main Python file for the Flask application, containing route definitions, the  calculation logic using Manning's equation, and data preparation to render using Chart.js.

- templates/index.html
The entry point of the application. This HTML file contains a form that captures user inputs for channel dimensions and flow characteristics.

- templates/result.html
This HTML file presents the calculated results, including the water depth and flow rate. It also provides a visualization of the channel and water level using Chart.js.

- static/script.js
A JavaScript file that renders the Chart.js graph based on the calculation results. It updates the chart to represent the channel cross-section and the water level. It also gives a warning if the water level is above the channel depth. Which represents an overflow scenario.

## Code Structure
The application is designed with a straightforward control flow:

Users enter the required inputs through the web interface (index.html).
![image](https://github.com/briandubya/simple-mannings-app/assets/61367457/dc160f54-1b17-4578-bc9e-1858c8fcd495)

After form submission, app.py processes the POST route using Flask, performing the neccessary calculations. 
The calculation of the water depth is not straightforward due to the nature of the Manning's equation. The application employs an iterative approach using a binary search-like algorithm to find the depth that yields the target flow rate. It follows the following logic, 

    - Users provide an initial guess for the water depth y.
    - Calculation of the flow rate Q using the guessed y.
    - Adjusting the guess based on whether the calculated Q is higher or lower than the target flow rate.
    - Narrowing the search range by halving it in each iteration.
    - Repeating the process until the guess is sufficiently accurate within a defined tolerance.

The results are then passed to result.html, where they are displayed in a formatted table along with a dynamically generated Chart.js graph, visually depicting the channel cross-section and water level.
![image](https://github.com/briandubya/simple-mannings-app/assets/61367457/0872a267-4851-49ca-9144-3d7a236ea975)
