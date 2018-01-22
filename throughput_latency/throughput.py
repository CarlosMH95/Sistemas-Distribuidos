from matplotlib import pyplot as plt
import numpy as np

data = {}
data['Just DB'] = [6.1, 5.9, 6, 6.2, 6.1, 6, 5.89, 5.9, 5.9, 5.9]
data['Memcached +DB'] = [9.7, 19.8, 28.1, 39.9, 48.4, 56.3, 50.7, 24.4, 83.7, 84.17]

color_dict = {'Just DB':'white', 'Memcached +DB':'white'}
controls = ['Just DB', 'Memcached +DB']

fig, ax = plt.subplots()

boxplot_dict = ax.boxplot(
    [data[x] for x in ['Just DB', 'Memcached +DB']],
    positions = [1, 1.5],
    labels = controls, 
    patch_artist = True,
    widths = 0.25)

i=0
for b in boxplot_dict['boxes']:
    lab = ax.get_xticklabels()[i].get_text()
    b.set_facecolor(color_dict[lab]) 
    i += 1

ax.set_ylim([0,np.max(data['Memcached +DB'])+10])
plt.ylabel("Throughput (Requests per second)")
plt.show()
