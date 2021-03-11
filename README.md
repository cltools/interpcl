
interpcl
========

**interpolate angular power spectra**

A very small package that does interpolation of angular power spectra for random
fields on the sphere.

Install with pip:

    pip install interpcl

Then import into your code:

    from interpcl import interpcl

Functionality is absolutely minimal at this point. Please open an issue on
GitHub if you want to see added functionality.


Documentation
=============

```py
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

```
