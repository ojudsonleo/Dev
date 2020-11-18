from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


house_prices = np.random.normal(200000, 25000, 5000)
plt.polar(house_prices)
plt.show()

