import numpy as np
import pandas as pd

def calculate_average_weight():
    try:
        df = pd.read_csv('data/orders.csv')
        weights = df['weight'].values

        avg = np.mean(weights)

        print(f"Average weight from dataset: {avg}")

        return avg

    except Exception as e:
        print("Error reading data:", e)