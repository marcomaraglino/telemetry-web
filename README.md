# Formula Student Car Sensor Dashboard

A real-time dashboard application built with Dash to visualize sensor data from a Formula Student car.

## Features

- Real-time visualization of multiple sensor data:
  - Speed (10 Hz sampling rate)
  - Temperature (1 Hz sampling rate) 
  - Pressure (2 Hz sampling rate)
- Configurable sampling rates for each sensor
- Rolling time window display (last 20 seconds)
- Dockerized application for easy deployment

## Prerequisites

- Docker
- Python 3.9+ (if running locally)

## Quick Start with Docker

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd formula-dashboard
   ```

2. Build the Docker image:
   ```bash
   docker build -t formula-dashboard .
   ```

3. Run the container:
   ```bash
   docker run -p 8050:8050 formula-dashboard
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8050
   ```

## Local Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Project Structure

formula-dashboard/
├── main.py           # Main application file
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
└── README.md # Documentation