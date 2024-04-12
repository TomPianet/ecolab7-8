import matplotlib.pylab as plt
import numpy as np

x = np.linspace(0, 223, 50)
y = x**2
y2 = x**3/100

# plt.rcParams.update({'font.size': 16})
plt.figure(figsize = (100, 5))

plt.title("Y =  $X^2$")
plt.plot(x, y)
plt.plot(x, y2)
plt.show()


import matplotlib.pylab as plt
import numpy as np

x = np.linspace(0, 220, 900)
y1 = x**2
y2 = 10*x

plt.rcParams.update({'font.size': 16})
fig, axis = plt.subplots(1, 2, figsize=(20, 10), sharey=False)


axis[0].set_title("Y =  $X^2$")
axis[0].plot(x, y1)

axis[1].set_title("Y = 10*X")
axis[1].plot(x, y2)

plt.show()