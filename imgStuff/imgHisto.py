import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter

img = Image.open('imgObjects/3.jpg').convert('L')
imgAr = np.array(img)
pixelAr = imgAr.flatten()
d =  dict(Counter(pixelAr))

print(d)

plt.hist(pixelAr, 255)
plt.xlim([0, 255])
plt.show(block=False)

pxl = list(d.keys())
pxl.sort()
freq = [d[x] for x in pxl]
print(freq)
plt.plot(freq)
plt.show()