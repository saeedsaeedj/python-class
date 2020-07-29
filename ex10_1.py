import numpy as np
import matplotlib.pyplot as plt
x=2
i=x**2
x=np.arange(0,2*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
if (np.sin(90)==1):
    print('darage ast')
else:
    print('radiyan ast')
plt.plot(y)
plt.plot(z)

q=np.linspace(-1,1,num=500)
print(q)

print(q[53])
plt.figure()
plt.plot(np.sin(2*np.pi*q))

plt.show()
