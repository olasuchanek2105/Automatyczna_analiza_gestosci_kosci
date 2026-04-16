import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt
import os


file_path = r'C:\Users\Supri\Desktop\2024_sentinel_sron_data\00ba2312cab12f013293d0c63f194223\response.tiff'

p_lat, p_lon = 45.47, 55.09
min_lat, max_lat = 45.24542220625224, 45.694577793747754
min_lon, max_lon = 54.769761360603056, 55.41023863939695

if not os.path.exists(file_path):
    print(f"Plik nie istnieje: {file_path}")
else:
   
    image_data = tiff.imread(file_path)
    h, w = image_data.shape[:2]

   
    b11 = image_data[:, :, 10].astype(np.float32)
    b12 = image_data[:, :, 11].astype(np.float32)
    
   
    methane_index = (b11 - b12) / (b11 + b12 + 1e-6)

   
    vmin = np.percentile(methane_index, 5)
    vmax = np.percentile(methane_index, 95)

    
    x = (p_lon - min_lon) / (max_lon - min_lon) * w
    y = (max_lat - p_lat) / (max_lat - min_lat) * h

   
    plt.figure(figsize=(12, 12))
    
  
    img = plt.imshow(methane_index, cmap='magma', vmin=vmin, vmax=vmax)
    plt.colorbar(img, label='Intensywność absorpcji metanu')
    
  
    plt.scatter([x], [y], s=200, facecolors='none', edgecolors='cyan', linewidths=2, label='Źródło (CSV)')
    
    plt.title(f"Analiza spektralna metanu\nLokalizacja: {p_lat}, {p_lon}", fontsize=15)
    plt.axis('off')
    plt.show()

    plt.title("Drugi plot")
    plt.axis('off')
    plt.show()

