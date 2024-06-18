import time

for i in range(10):
    print("Reporte: {i}")
    
    latitude = "19.378368"
    longitude = "-99.178380"

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    import requests
    import json

    data_text = requests.get(url).text

    data_json = json.loads(data_text)

    #data_json # { ..., "hourly": { "time": [ ... ], "temperature_2m": [ ... ], "relative_humidity_2m": [ ... ], "wind_speed_10m": [ ... ] } }

    times = data_json["hourly"]["time"] # [ ... ]
    temperatures = data_json["hourly"]["temperature_2m"] # [ ... ]
    humidities = data_json["hourly"]["relative_humidity_2m"] # [ ... ]
    wind_speeds = data_json["hourly"]["wind_speed_10m"] # [ ... ]

    import pandas as pd

    data = pd.DataFrame({
        "TIEMPO": times, # [ ... ]
        "TEMPERATURA": temperatures,
        "HUMEDAD": humidities,
        "VIENTO": wind_speeds,
    })

    data["LATITUD"] = latitude
    data["LONGITUD"] = longitude

    data.to_csv(f"reporte_{i}.csv", index=False)

    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.lmplot(data, x="TEMPERATURA", y="HUMEDAD")
    plt.savefig(f"reporte_{i}")
    
    time.sleep(20)