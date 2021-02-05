#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt


# main function for this Python code
if __name__ == "__main__":
    # load previous data    
    
    myx = np.load('random50000.npy')

    # create histogram of our data
    n, bins, patches = plt.hist(myx, 50, density=True, facecolor='r', alpha=0.75)

    # plot formating options
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Uniform random number')
    plt.grid(True)
    
    plt.savefig('random50000.png')

    # show figure (program only ends once closed
    plt.show()
