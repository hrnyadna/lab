import matplotlib.pyplot as plt
import statsmodels.api as sm

data = sm.datasets.co2.load_pandas().data
data = data.resample('ME').mean()
data = data["1958":"1980"]

plt.figure(figsize=(10, 5))
plt.plot(data, label="CO₂ Concentration", color="teal")
plt.xlabel("Год")
plt.ylabel("Концентрация CO₂ (ppm)")
plt.title("Динамика концентрации CO₂ (1958–1980)")
plt.legend()
plt.grid()
plt.show()