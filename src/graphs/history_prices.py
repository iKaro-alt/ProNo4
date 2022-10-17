#!/usr/bin/env python3
import matplotlib.pyplot as plt

def history(data):
    plt.plot(data)
    plt.ylabel('Close')
    plt.grid()
    plt.show()
    return 0
