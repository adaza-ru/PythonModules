import sys
import importlib.util
import importlib.metadata
import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np


DEPENDENCIES = ["pandas", "numpy", "matplotlib", "requests"]


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    all_present = True

    for lib in DEPENDENCIES:
        spec = importlib.util.find_spec(lib)
        if spec is None:
            print(f"[MISSING] {lib} - Knowledge not found in the Matrix")
            all_present = False
        else:
            version = importlib.metadata.version(lib)
            print(f"[OK] {lib} ({version}) - Ready for download")

    if not all_present:
        print("\nERROR: Missing packages detected.")
        print("Install via PIP: pip install -r requirements.txt")
        print("Install via POETRY: poetry install")
        sys.exit(1)
    return True


def load_and_simulate_data():

    cities = {
        "Almería": (36.83, -2.46), "Cádiz": (36.52, -6.28),
        "Córdoba": (37.88, -4.77), "Granada": (37.17, -3.59),
        "Huelva": (37.26, -6.94), "Jaén": (37.76, -3.78),
        "Málaga": (36.72, -4.42), "Sevilla": (37.38, -5.98)
    }

    print("\nAnalyzing Matrix data (Andalucía Weather Hub)...")

    results = []
    try:
        for city, (lat, lon) in cities.items():
            url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}"
                   f"&longitude={lon}&current_weather=true")
            response = requests.get(url, timeout=5)
            temp = response.json()['current_weather']['temperature']
            results.append({"City": city, "Real_Temp": temp})

        df = pd.DataFrame(results)
        noise = np.random.normal(0, 1.5, size=len(df))
        df['Matrix_Temp'] = df['Real_Temp'] + noise

        print(f"Processing {len(df)} data points from Open-Meteo...")
        return df

    except Exception as e:
        print(f"API Connection lost: {e}")
        sys.exit(1)


def generate_visualization(df):

    print("Generating visualization...")
    plt.figure(figsize=(12, 6))
    x = range(len(df['City']))
    plt.bar(x, df['Real_Temp'], width=0.4, label='Realidad (Open-Meteo)',
            align='center', color='skyblue')
    plt.bar(x, df['Matrix_Temp'], width=0.4, label='Constructo (NumPy)',
            align='edge', color='limegreen', alpha=0.7)

    plt.xticks(x, df['City'])
    plt.title("Monitorización Térmica: Andalucía en la Matrix")
    plt.ylabel("Temperatura (ºC)")
    plt.legend()

    output = "matrix_analysis.png"
    plt.savefig(output)
    print(f"Analysis complete! Results saved to: {output}")


if __name__ == "__main__":
    if check_dependencies():
        data = load_and_simulate_data()
        generate_visualization(data)
