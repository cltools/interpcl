# interpcl: interpolate angular power spectra
#
# author: Nicolas Tessore <n.tessore@ucl.ac.uk>
# license: MIT
'''

Interpolate angular power spectra (:mod:`interpcl`)
===================================================

.. currentmodule:: interpcl

A very small package that does interpolation of angular power spectra for random
fields on the sphere.

Install with pip::

    pip install interpcl

Then import into your code::

    from interpcl import interpcl

Functionality is absolutely minimal at this point. Please open an issue on
GitHub if you want to see added functionality.


Reference/API
-------------

.. autosummary::
   :toctree: api
   :nosignatures:

   interpcl

'''

__version__     = '2021.4.13'

__all__ = [
    'interpcl',
]


import numpy as np
from scipy.interpolate import interp1d


def interpcl(lout, l, cl, llin=10, **kwargs):
    r'''interpolate angular power spectrum

    Interpolate an angular power spectrum :math:`C(l)` using spline
    interpolation.  For scales :math:`l > l_{\rm lin}`, the interpolation is
    done in log-log space, i.e. spline interpolation of :math:`\log C(\log l)`.

    Parameters
    ----------
    lout : int or array_like
        The output mode numbers. If an integer is given, the interpolation is
        done over the integer array ``0, 1, ..., lout``.
    l, cl : array_like
        Input angular power spectrum. Must be one-dimensional arrays.
    llin : int, optional
        Threshold for log-log interpolation. Default is ``10``.
    **kwargs : dict, optional
        Keyword arguments for :class:`scipy.interpolate.interp1d`.

    Returns
    -------
    clout : array_like
        Interpolated angular power spectrum of the same shape as `lout` if
        `lout` is an array, or of length ``lout+1`` if `lout` is an integer.

    '''

    fv = kwargs.pop('fill_value', 'extrapolate')

    if np.ndim(lout) == 0:
        lout = np.arange(lout+1)

    clout = np.empty_like(lout, dtype=float)

    clout[lout <= llin] = interp1d(l, cl, fill_value=fv, **kwargs)(lout[lout <= llin])
    clout[lout > llin] = np.exp(interp1d(np.log(l[l>0]), np.log(cl[l>0]), fill_value=fv, **kwargs)(np.log(lout[lout > llin])))

    return clout
