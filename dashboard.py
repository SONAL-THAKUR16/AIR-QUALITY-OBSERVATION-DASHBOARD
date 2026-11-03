import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from air_quality import StationReading
df = pd.read_csv("data/air_quality.csv")
print("\n========== AIR QUALITY DATA ==========")
print(df)
df["date"] = pd.to_datetime(df["date"])
valid_readings = []
for _, row in df.iterrows():
    reading = StationReading(
        row["date"],
        row["station"],
        row["pm25"],
        row["temperature"]
    )
    if reading.is_valid():
        valid_readings.append(reading)
print("\n========== VALIDATION ==========")
print("Total readings:", len(df))
print("Valid readings:", len(valid_readings))
print("Invalid readings:", len(df) - len(valid_readings))

pm25_values = np.array([reading.pm25 for reading in valid_readings])
average_pm25 = np.mean(pm25_values)
maximum_pm25 = np.max(pm25_values)
minimum_pm25 = np.min(pm25_values)

print("\n========== NUMPY ANALYSIS ==========")
print("Average PM2.5:", round(average_pm25, 2))
print("Maximum PM2.5:", maximum_pm25)
print("Minimum PM2.5:", minimum_pm25)

anomalies = [
    reading for reading in valid_readings
    if reading.is_anomaly()
]
print("\n========== ANOMALIES ==========")
for reading in anomalies:
    print(
        reading.date.date(),
        "|",
        reading.station,
        "| PM2.5:",
        reading.pm25
    )

station_average = df.groupby("station")["pm25"].mean()

print("\n========== AVERAGE PM2.5 BY STATION ==========")
print(station_average.round(2))

date_average = df.groupby("date")["pm25"].mean()

print("\n========== AVERAGE PM2.5 BY DATE ==========")
print(date_average.round(2))

plt.figure(figsize=(10, 5))
for station in df["station"].unique():
    station_data = df[df["station"] == station]

    plt.plot(
        station_data["date"],
        station_data["pm25"],
        marker="o",
        label=station
    )
plt.xlabel("Date")
plt.ylabel("PM2.5 (µg/m³)")
plt.title("PM2.5 Trend by Station")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
plt.figure(figsize=(8, 5))

plt.hist(
    df["pm25"],
    bins=6,
    edgecolor="black"
)
plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("Frequency")
plt.title("Distribution of PM2.5 Readings")
plt.tight_layout()
plt.show()