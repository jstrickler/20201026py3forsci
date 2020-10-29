#!/usr/bin/env python
import numpy as np
import scipy.fftpack as ff


def main():
    np.info(ff.fft)  # <1>

    print('-' * 60)

    np.source(ff.fft)  # <2>




if __name__ == '__main__':
    main()
