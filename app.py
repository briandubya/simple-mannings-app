from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        channel_width = float(request.form.get('channel_width'))
        bank_slope = float(request.form.get('bank_slope'))
        channel_depth = float(request.form.get('channel_depth'))
        mannings_n = float(request.form.get('mannings_n'))
        channel_slope = float(request.form.get('channel_slope'))
        initial_depth = float(request.form.get('initial_depth'))
        target_flow_rate = float(request.form.get('flow_rate'))

        # Iteratively get the depth and flow rate using the Manning's equation
        new_depth, flow_rate = calculate_mannings(channel_width, bank_slope, mannings_n, channel_slope, initial_depth, target_flow_rate)

        # Prepare data for visualization
        visualization_data = prepare_visualization_data(channel_width, bank_slope, new_depth, channel_depth)

        return render_template('result.html', new_depth=new_depth, flow_rate=flow_rate, mannings_n=mannings_n, channel_slope=channel_slope, visualization_data=visualization_data)

    return render_template('index.html')

# Wrapper function to calculate the flow rate, depth within the channel
def calculate_mannings(channel_width, bank_slope, mannings_n, channel_slope, initial_depth, target_flow_rate):
    # Function to calculate the area of a trapezoid.
    def get_area(channel_width, bank_slope, depth): 
        return (channel_width + bank_slope * depth) * depth

    # Calculate the flow rate for a given depth of flow
    def calculate_mannings_equation(channel_width, depth, bank_slope, mannings_n, channel_slope):
        area = get_area(channel_width, bank_slope, depth)
        wetted_perimeter = channel_width + 2 * depth * math.sqrt(1 + bank_slope**2)
        hydraulic_radius = area / wetted_perimeter
        return ((1 / mannings_n) * area * hydraulic_radius ** (2/3)) * channel_slope ** 0.5

    # Iteratively using a binary search method calculate the Mannings equation by adjusting the depth of flow till the calculated flow rate matches the target flow rate
    flow_rate = calculate_mannings_equation(channel_width, initial_depth, bank_slope, mannings_n, channel_slope)
    new_depth = initial_depth
    while abs(flow_rate - target_flow_rate) > 0.0001:  # Tolerance for convergence
       if flow_rate < target_flow_rate:
            depth_lower = new_depth
            depth_upper = new_depth * 2
       else:
            depth_upper = new_depth
            depth_lower = new_depth / 2
       new_depth = (depth_upper + depth_lower) / 2
       flow_rate = calculate_mannings_equation(channel_width, new_depth, bank_slope, mannings_n, channel_slope)

    return round(new_depth, 3), round(flow_rate, 3)

def prepare_visualization_data(channel_width, bank_slope, new_depth, channel_depth):
    return {
        "channel_width": channel_width,
        "bank_slope": bank_slope,
        "water_depth": new_depth,
        "channel_depth": channel_depth,
    }

if __name__ == '__main__':
    app.run(debug=True)

