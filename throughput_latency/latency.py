from matplotlib import pyplot as plt
import numpy as np

data = {}
data['Just DB'] = [8480, 18176, 12008, 13831, 14770, 18319, 17743, 17632, 18204, 20935]
data['Memcached +DB'] = [374, 430, 461, 427, 670, 765, 3142, 12962, 1835]

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

ax.set_ylim([0,np.max(data['Just DB'])+500])
plt.ylabel("Average latency (Miliseconds)")
plt.show()
