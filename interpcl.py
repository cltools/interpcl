# interpcl: interpolate angular power spectra
#
# author: Nicolas Tessore <n.tessore@ucl.ac.uk>
# license: MIT
'''

Interpolate angular power spectra (:mod:`interpcl`)
===================================================

.. currentmodule:: interpcl

A very small package that does interpolation of angular power spectra for
random fields on the sphere.

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

__version__     = '2021.5.20'

__all__ = [
    'interpcl',
]


import numpy as np
from scipy.interpolate import interp1d


def interpcl(l, cl, lmax=None, dipole=True, monopole=False, **kwargs):
    r'''interpolate angular power spectrum

    Interpolate an angular power spectrum :math:`C(l)` using spline
    interpolation.  Given input modes `l`, `cl`, returns the power spectrum for
    all integer modes from 0 to `lmax`, or the highest input mode if `lmax` is
    not given.  The dipole is computed if `dipole` is ``True``, or set to zero,
    and similarly for `monopole`.

    Parameters
    ----------
    l, cl : array_like
        Input angular power spectrum. Must be one-dimensional arrays.
    lmax : int, optional
        Highest output mode. If not set, the highest input mode is used.
    dipole : bool, optional
        Compute the dipole (``True``), or set it to zero (``False``).
    monopole : bool, optional
        Compute the monopole (``True``), or set it to zero (``False``).
    **kwargs : dict, optional
        Keyword arguments for :class:`scipy.interpolate.interp1d`.

    Returns
    -------
    clout : array_like
        Interpolated angular power spectrum.

    '''

    fv = kwargs.pop('fill_value', 'extrapolate')

    if lmax is None:
        lmax = np.max(l)

    lout = np.arange(lmax+1)
    clout = interp1d(l, cl, fill_value=fv, **kwargs)(lout)

    if dipole is False:
        clout[1] = 0
    if monopole is False:
        clout[0] = 0

    return clout
