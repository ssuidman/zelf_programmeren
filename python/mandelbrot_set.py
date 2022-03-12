import numpy as np
import matplotlib.pyplot as plt

N = 15
ranges = np.zeros([N,4])
ranges[0] = -2,1,-1,1
ranges[1] = -1,0.5,-0.25,1
ranges[2] = -0.7,0.4,0,1
ranges[3] = -0.5,0.25,0.5,1
ranges[4] = -0.25,0,0.8,1
ranges[5] = -0.2,-0.05,0.825,0.925
ranges[6] = -0.2,-0.1,0.86,0.925
ranges[7] = -0.16,-0.13,0.89,0.92
ranges[8] = -0.154,-0.151,0.9075,0.909
ranges[9] = -0.1517,-0.1515,0.9075,0.9078
ranges[10] = -0.151615,-0.15159,0.907695,0.907708
ranges[11] = -0.151607,-0.151605,0.907704,0.907706
ranges[12] = -0.151607,-0.151605,0.907704,0.907706

fig,ax = plt.subplots(nrows=3,ncols=3)
for i in range(3):
    for j in range(3):
        x0,x1,y0,y1 = ranges[i*3+j]
        x0_new,x1_new,y0_new,y1_new = ranges[i*3+j+1]
        x_range = np.linspace(x0,x1,300)
        y_range = np.linspace(y0,y1,300)[::-1]

        mandelbrot_set = np.zeros([len(x_range),len(y_range)])
        for m,x in enumerate(x_range):
            if m%100==0:
                print(i,j,m)
            for n,y in enumerate(y_range):
                c = x+y*1j
                z = 0
                count = 0
                while np.abs(z)<2:
                    z = z**2 + c
                    count += 1
                    if count > 50:
                        break
                mandelbrot_set[m][n] = count
                if count > 50:
                    mandelbrot_set[m][n] = 0   

        ax[i][j].imshow(np.transpose(mandelbrot_set),extent=[x0,x1,y0,y1],cmap='gnuplot2') 
        ax[i][j].hlines(y0_new,xmin=x0_new,xmax=x1_new,color='r')
        ax[i][j].hlines(y1_new,xmin=x0_new,xmax=x1_new,color='r')
        ax[i][j].vlines(x0_new,ymin=y0_new,ymax=y1_new,color='r')
        ax[i][j].vlines(x1_new,ymin=y0_new,ymax=y1_new,color='r')
        ax[i][j].set_xticks([])
        ax[i][j].set_yticks([])
        if i==2:
            ax[i][j].set_xlabel('Re(z)')
        if j==0:
            ax[i][j].set_ylabel('Im(z)')


