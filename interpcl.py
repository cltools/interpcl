'''interpcl: interpolate angular power spectra

author: Nicolas Tessore <n.tessore@ucl.ac.uk>
license: MIT

'''

__version__     = '2021.03.10'

__all__ = [
    'interpcl',
]


import numpy as np


def interpcl(lout, l, cl, llin=10, left=0, right=0):
    r'''interpolate angular power spectrum

    Interpolate an angular power spectrum :math:`C(l)` using linear-linear
    interpolation for :math:`l \le l_{\rm lin}` and log-log interpolation for
    :math:`l > l_{\rm lin}`.

    Parameters
    ----------
    lout : int or array_like
        The output mode numbers. If an integer is given, the interpolation is
        done over the integer array ``0, 1, ..., lout``.
    l, cl : array_like
        Input angular power spectrum. Must be one-dimensional arrays.
    llin : int, optional
        Threshold for linear-linear or log-log interpolation. Default is ``10``.
    left, right : float, optional
        Fill value for l that are smaller or larger than the input range.
        Default is ``0``.

    Returns
    -------
    clout: array_like
        Interpolated angular power spectrum of the same shape as ``lout`` if
        ``lout`` is an array, or of length ``lout+1`` if ``lout`` is an integer.

    '''

    if np.ndim(lout) == 0:
        lout = np.arange(lout+1)

    clout = np.empty_like(lout, dtype=float)

    clout[lout <= llin] = np.interp(lout[lout <= llin], l, cl,
                                    left=left, right=right)

    clout[lout > llin] = np.exp(np.interp(np.log(lout[lout > llin]),
                                          np.log(l[l>0]), np.log(cl[l>0]),
                                          left=left, right=right))

    return clout
