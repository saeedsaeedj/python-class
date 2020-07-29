import numpy as np
vec1=np.array([-1.,4.,-9.])
mat1=np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
vec2=(np.pi/4)*vec1
vec2=np.cos(vec2)
vec3=vec1+2*vec2
vec4=mat1*vec3
np.transpose(mat1)
np.linalg.det(mat1)
print(np.min(mat1))
'''
if np.max(mat1,axis=-1)==np.sum and sumrow==sumdiag and sumrow==sumflip:
print('this is a magic matrix')
'''
n=np.random.rand(10,10)
print(n)
mul=n[:5][:5]
print(mul)
mur=n[5:][:5]
print(mur)
mll=n[:5][5:]
mlr=n[5:][5:]
