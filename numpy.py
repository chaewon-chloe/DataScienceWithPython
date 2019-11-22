def wigner_density(num):
    import numpy as np
    num = np.float(num)
    if num >= -2 and num <= 2:
        return (np.sqrt(4-(num**2)))/(2*np.pi)
    else:
        return 0
        
        
def generate_wigner(n):
    import numpy as np
    if n <= 0:
        raise ValueError("Input value must be a positive integer.")
    elif type(n)!=int and type(n)!=np.int:
        raise TypeError("Please enter an integer value.")
    else:
        a = np.random.normal(0, np.sqrt(1/n), n*n).reshape(n,n)
        a = np.tril(a)
        for i in range(n):
            for j in range(i+1,n):
                a[i,j]=a[j,i]
        return np.matrix(a)
        
        
 def get_spectrum(a):
    import numpy as np
    w,y = np.linalg.eigh(a)
    return np.sort(w)    
    
# for array test
a = np.random.normal(0, np.sqrt(1/5), 5*5).reshape(5,5)
a = np.tril(a)
for i in range(5):
    for j in range(i+1,5):
        a[i,j]=a[j,i]

get_spectrum(a)



import matplotlib.pyplot as plt
%matplotlib inline

size = [100, 200, 500, 1000]
vfun = np.vectorize(wigner_density)
n = np.arange(-2,2.001,0.001)

plt.figure(figsize=(8, 24))

for i in range(4):
    plt.subplot(411+i)
    plt.xlim(-2.3,2.3)
    plt.ylim(0,0.41);
    plt.title("sample size =" + str(size[i]))
    plt.plot(n,vfun(n),'-r', lw=2)
    plt.hist(get_spectrum(generate_wigner(size[i])),30, facecolor='blue', density=True)

_ = plt.show()


import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
%matplotlib inline
labels = np.load(file = 'labels.npy')
points = np.loadtxt(fname ='points.dlm', delimiter ='\t')

labels.shape, points.shape


# Dividing data by labels
points0 = points[labels==0]
points1 = points[labels==1]


# For problem 2-(3)
mu0 = np.array([.2,.7])
sigma0 = np.array([[.015,-.011],[-.011,.018]])
mvn0 = st.multivariate_normal(mu0,sigma0)
x0,y0 = np.mgrid[0:1:.01, 0:1:.01]
pos0 = np.empty(x0.shape + (2,))
pos0[:,:,0] = x0; pos0[:,:,1] = y0

mu1 = np.array([.65,.3])
sigma1 = np.array([[.016,-.011],[-.011,.016]])
mvn1 = st.multivariate_normal(mu1,sigma1)
x1,y1 = np.mgrid[0:1:.01, 0:1:.01]
pos1 = np.empty(x1.shape + (2,))
pos1[:,:,0] = x1; pos1[:,:,1] = y1

# Elipse levels
levels=[st.chi2.ppf(q=1-.95, df=2),st.chi2.ppf(q=1-.68, df=2)]

# Outliers
outlier0 = tuple(points0[points0[:,0]>0.6][0])
outlier1 = tuple(points1[points1[:,0]>0.8][0])

# Plotting
plt.figure(figsize=(8,8))
plt.xlim(0,1)
plt.ylim(0,1)

# Scatter plot (Problem 2-(2))
plt.plot(points0[:,0],points0[:,1],'xb',points1[:,0],points1[:,1],'xr', ms=6)

# Ellipse
plt.contour(x0,y0,mvn0.pdf(pos0), colors='b', levels = levels)
plt.contour(x1,y1,mvn1.pdf(pos1), colors='r', levels = levels)

# Outlier annotation
plt.annotate('Outlier of Label 0',xy=outlier0, xytext=(.0,.2), fontsize=12
             , arrowprops=dict(facecolor='black', width =0.2, headlength=6, headwidth=6))
plt.annotate('Outlier of Label 1',xy=outlier1, xytext=(.4,.8), fontsize=12
             , arrowprops=dict(facecolor='black', width = 0.2, headlength=6, headwidth=6))
_ = plt.show()
