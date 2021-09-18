import numpy as np
import matplotlib.pyplot as plt

def f(X,Y): #Returns the velocities dX,dY (which are just the vectors) at certain points X,Y (or R,Theta)
    dX = 3*X-X**3
    dY = 1+2*X**2
    return dX,dY

def vectors(X,Y,cart_pol): #In this function you can tell if you're in X,Y or R,Theta. 
    if cart_pol == 'cartesian':
        dX,dY = f(X,Y)
    if cart_pol == 'polar':
        R = np.sqrt(X ** 2 + Y ** 2)
        Theta = np.arctan(X / Y)

        dR,dTheta = f(R,Theta)

        dX = X / np.sqrt(X ** 2 + Y ** 2) * dR - Y * dTheta
        dY = Y / np.sqrt(X ** 2 + Y ** 2) * dR + X * dTheta

    else:
        print('set cart_pol to "cartesian" or "polar"')
    return dX,dY

def plot(X,Y,dX,dY): #This function takes the points (X,Y) and the vectors (dX,dY)
    fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=[10,5])
    ax1.streamplot(X,Y,dX,dY, density=1)
    ax2.quiver(X,Y,dX,dY,scale=50,scale_units='width',color='blue')
    fig.show()

x = np.linspace(-2, 2, 25) #Don't use a too big number density, otherwise the vector field is not clear
y = np.linspace(-2, 2, 25)
X, Y = np.meshgrid(x, y)
dX,dY = vectors(X,Y,'polar') #Get velocities at certain points. 

plot(X,Y,dX,dY)
