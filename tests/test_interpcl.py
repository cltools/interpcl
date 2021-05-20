import pytest


def test_interpcl():
    import numpy as np
    from interpcl import interpcl

    l = np.geomspace(2., 100., 20)
    cl = np.exp(-(np.log(l) - np.log(10))**2/5)

    icl = interpcl(l, cl)
    assert len(icl) == 101
    assert icl[0] == 0
    assert icl[1] != 0

    icl = interpcl(l, cl, lmax=200)
    assert len(icl) == 201

    icl = interpcl(l, cl, dipole=False)
    assert icl[1] == 0

    icl = interpcl(l, cl, monopole=True)
    assert icl[0] != 0
