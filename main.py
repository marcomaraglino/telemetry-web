import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objs as go
import random

# Initialize the Dash app
app = dash.Dash(__name__)

# Initialize separate DataFrames for each sensor
df_speed = pd.DataFrame(columns=['time', 'speed'])
df_temperature = pd.DataFrame(columns=['time', 'temperature'])
df_pressure = pd.DataFrame(columns=['time', 'pressure'])
time_counter = 0

# Separate functions for each sensor
def generate_speed_data():
    global time_counter
    time_counter += 1
    return time_counter, random.uniform(0, 100)

def generate_temperature_data():
    return time_counter, random.uniform(20, 30)

def generate_pressure_data():
    return time_counter, random.uniform(980, 1020)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Formula Student Car Sensor Dashboard'),

    dcc.Graph(id='speed-graph'),
    dcc.Graph(id='temperature-graph'),
    dcc.Graph(id='pressure-graph'),

    # Separate interval components for each sensor
    dcc.Interval(
        id='speed-interval',
        interval=100,  # 100ms (10 Hz)
        n_intervals=0
    ),
    dcc.Interval(
        id='temperature-interval',
        interval=1000,  # 1000ms (1 Hz)
        n_intervals=0
    ),
    dcc.Interval(
        id='pressure-interval',
        interval=500,  # 500ms (2 Hz)
        n_intervals=0
    )
])

# Separate callbacks for each sensor
@app.callback(
    Output('speed-graph', 'figure'),
    Input('speed-interval', 'n_intervals')
)
def update_speed(n):
    global df_speed
    time, speed = generate_speed_data()
    df_speed.loc[len(df_speed)] = [time, speed]
    recent_data = df_speed[df_speed['time'] >= time - 20]
    
    return {
        'data': [go.Scatter(x=recent_data['time'], y=recent_data['speed'], mode='lines+markers', name='Speed')],
        'layout': go.Layout(title='Speed over Time', xaxis={'title': 'Time (s)'}, yaxis={'title': 'Speed (km/h)'})
    }

@app.callback(
    Output('temperature-graph', 'figure'),
    Input('temperature-interval', 'n_intervals')
)
def update_temperature(n):
    global df_temperature
    time, temperature = generate_temperature_data()
    df_temperature.loc[len(df_temperature)] = [time, temperature]
    recent_data = df_temperature[df_temperature['time'] >= time - 20]
    
    return {
        'data': [go.Scatter(x=recent_data['time'], y=recent_data['temperature'], mode='lines+markers', name='Temperature')],
        'layout': go.Layout(title='Temperature over Time', xaxis={'title': 'Time (s)'}, yaxis={'title': 'Temperature (°C)'})
    }

@app.callback(
    Output('pressure-graph', 'figure'),
    Input('pressure-interval', 'n_intervals')
)
def update_pressure(n):
    global df_pressure
    time, pressure = generate_pressure_data()
    df_pressure.loc[len(df_pressure)] = [time, pressure]
    recent_data = df_pressure[df_pressure['time'] >= time - 20]
    
    return {
        'data': [go.Scatter(x=recent_data['time'], y=recent_data['pressure'], mode='lines+markers', name='Pressure')],
        'layout': go.Layout(title='Pressure over Time', xaxis={'title': 'Time (s)'}, yaxis={'title': 'Pressure (hPa)'})
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
