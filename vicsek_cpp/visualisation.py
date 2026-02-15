import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import sys

filename = "positions.csv"
box_size = 10.0
Interval = 50

try:
    print(f"Reading {filename}...")
    df = pd.read_csv(filename)

    df.columns = df.columns.str.strip()
    print("Colums found:", df.columns.tolist())
except FileNotFoundError: # not gonna happen but just a precaution
    print(f"Error: Could not find {filename}. Have you run the C++ simulation first?")
    sys.exit(1)


#getting a list of unique time steps
steps = df["time"].unique()
print(f"Found {len(steps)} time steps with {len(df[df["time"]==0])} particles each.")

#setting up the plot
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_title("Vicsek model using C++")
ax.set_xlabel("X position")
ax.set_ylabel("Y position")

scatter, = ax.plot([], [], "bo", markersize=5)

def update(frame_time):
    #filtering data
    filtered_data = df[df["time"] == frame_time]

    #updating scatter plot
    scatter.set_data(filtered_data["x"], filtered_data["y"])

    return scatter,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=steps,
    interval = Interval,
    blit=True
)

print("Starting animation window...")
plt.show()