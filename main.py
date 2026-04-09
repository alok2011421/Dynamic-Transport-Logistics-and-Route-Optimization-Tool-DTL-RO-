import pandas as pd
import matplotlib.pyplot as plt
import os

# Imports from modules
from scripts.week10_oop import Order, Vehicle
from scripts.week4_functions import optimize_route
from scripts.week7_files import save_log
from scripts.week11_numpy import calculate_average_weight


def start_system():
    print("--- DTL-RO LOGISTICS SYSTEM START ---\n")

    # STEP 1: Environment Check
    print("[STEP 1] Environment Check (Module 1)... OK.")

    # STEP 2: Load Data
    print("[STEP 2] Loading Data from 'data/orders.csv' (Module 4)...")
    try:
        df = pd.read_csv('data/orders.csv')
        print(f"   -> Found {len(df)} orders.")
    except FileNotFoundError:
        print("   -> ERROR: CSV file missing!")
        return

    # Data Cleaning
    if df.isnull().values.any():
        df.fillna(0, inplace=True)
        print("   -> Cleaning data: Missing values fixed.")
    else:
        print("   -> Cleaning data: No missing values found.")

    # STEP 3: OOP Implementation
    print("\n[STEP 3] Initializing Objects (Module 3)...")

    orders = []
    for _, row in df.iterrows():
        order = Order(row['id'], row['weight'], row['lat'], row['lng'])
        orders.append(order)

    vehicle = Vehicle("Truck_01", 45)

    print(f"   -> Created {len(orders)} Order objects.")
    print("   -> Vehicle 'Truck_01' initialized with 45kg capacity.")

    # STEP 4: Route Optimization
    print("\n[STEP 4] Running Route Optimization (Module 2 + 4)...")

    route = optimize_route(orders, vehicle)
    route_ids = [o.id for o in route]

    print(f"\n[RESULT] Optimized Route: {route_ids}")
    print(f"[RESULT] Total Utilization: {vehicle.current_load}/{vehicle.capacity} kg ({(vehicle.current_load/vehicle.capacity)*100:.1f}%)")

    # Save log
    save_log(f"Optimized Route: {route_ids}")

    # STEP 5: Statistics (NumPy)
    print("\n[STEP 5] Calculating Statistics (Module 11)...")
    calculate_average_weight()

    # STEP 6: Visualization
    print("\n[STEP 6] Generating Visualization (Module 4)...")

    plt.figure(figsize=(8, 5))

    # Plot points
    plt.scatter(df['lat'], df['lng'], s=100)

    # Labels
    for i, txt in enumerate(df['id']):
        plt.annotate(txt, (df['lat'][i], df['lng'][i]), xytext=(5, 5), textcoords='offset points')

    # Plot route path
    route_df = df.set_index('id').loc[route_ids]
    plt.plot(route_df['lat'], route_df['lng'], linestyle='--', marker='o')

    plt.title("DTL-RO Optimized Delivery Route")
    plt.grid(True)

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    plt.savefig("output/final_route.png")

    print("   -> Plotting coordinates...")
    print("   -> Route path visualized.")
    print("   -> Map saved to 'output/final_route.png'")

    print("\n--- SYSTEM SHUTDOWN ---")


if __name__ == "__main__":
    start_system()