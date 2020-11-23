#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot-methods/blob/master/LICENSE

import unittest

import numpy

import awkward0
import uproot_methods
from uproot_methods import *

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_vector2(self):
        a = TVector2(4.4, 5.5)
        assert a.dot(a) == 49.61
        assert a + TVector2(1000, 2000) == TVector2(1004.4, 2005.5)
        assert a - TVector2(1000, 2000) == TVector2(-995.6, -1994.5)
        assert TVector2(1000, 2000) - a == TVector2(995.6, 1994.5)
        assert a * 1000 == TVector2(4400, 5500)
        assert 1000 * a == TVector2(4400, 5500)
        assert a / 1000 == TVector2(0.0044, 0.0055)
        assert 1000 / a == TVector2(227.27272727272725, 181.8181818181818)
        assert a**2 == 49.61
        assert a**1 == 7.043436661176133
        assert abs(a) == 7.043436661176133
        assert -a == TVector2(-4.4, -5.5)
        assert +a == TVector2(4.4, 5.5)

        a += TVector2(100, 200)
        assert a == TVector2(104.4, 205.5)
        a *= 10
        assert a == TVector2(1044, 2055)

    def test_vector2_array(self):
        a = TVector2Array(numpy.zeros(10), numpy.arange(10))
        assert a.tolist() == [TVector2(0, 0), TVector2(0, 1), TVector2(0, 2), TVector2(0, 3), TVector2(0, 4), TVector2(0, 5), TVector2(0, 6), TVector2(0, 7), TVector2(0, 8), TVector2(0, 9)]
        assert a[5] == TVector2(0, 5)
        assert a.y.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.mag2.tolist() == [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
        assert (a + TVector2(1000, 2000))[5] == TVector2(1000, 2005)
        assert (a + TVector2(1000, 2000) == TVector2Array(numpy.full(10, 1000), numpy.arange(2000, 2010))).tolist() == [True, True, True, True, True, True, True, True, True, True]
        assert (a**2).tolist() == [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
        assert (a**3).tolist() == [0.0, 1.0, 8.0, 27.0, 64.0, 125.0, 216.0, 343.0, 512.0, 729.0]

    def test_vector2_jagged(self):
        TVector2Jagged = type("TVector2Jagged", (awkward0.JaggedArray, uproot_methods.classes.TVector2.ArrayMethods), {})
        a = TVector2Jagged.fromoffsets([0, 3, 3, 5, 10], TVector2Array(numpy.zeros(10), numpy.arange(10)))
        a._generator = uproot_methods.classes.TVector2.TVector2
        a._args = ()
        a._kwargs = {}
        assert a.tolist() == [[TVector2(0, 0), TVector2(0, 1), TVector2(0, 2)], [], [TVector2(0, 3), TVector2(0, 4)], [TVector2(0, 5), TVector2(0, 6), TVector2(0, 7), TVector2(0, 8), TVector2(0, 9)]]
        assert a.x.tolist() == [[0.0, 0.0, 0.0], [], [0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
        assert a.y.tolist() == [[0, 1, 2], [], [3, 4], [5, 6, 7, 8, 9]]
        assert (a + TVector2(1000, 2000)).tolist() == [[TVector2(1000, 2000), TVector2(1000, 2001), TVector2(1000, 2002)], [], [TVector2(1000, 2003), TVector2(1000, 2004)], [TVector2(1000, 2005), TVector2(1000, 2006), TVector2(1000, 2007), TVector2(1000, 2008), TVector2(1000, 2009)]]
        assert (a + TVector2Array(numpy.full(4, 1000), numpy.arange(1000, 5000, 1000))).tolist() == [[TVector2(1000, 1000), TVector2(1000, 1001), TVector2(1000, 1002)], [], [TVector2(1000, 3003), TVector2(1000, 3004)], [TVector2(1000, 4005), TVector2(1000, 4006), TVector2(1000, 4007), TVector2(1000, 4008), TVector2(1000, 4009)]]

    def test_vector3(self):
        a = TVector3(4.4, 5.5, 0)
        assert a.dot(a) == 49.61
        assert a.cross(a) == TVector3(0,0,0)
        assert a + TVector3(1000, 2000, 0) == TVector3(1004.4, 2005.5, 0)
        assert a - TVector3(1000, 2000, 0) == TVector3(-995.6, -1994.5, 0)
        assert TVector3(1000, 2000, 0) - a == TVector3(995.6, 1994.5, 0)
        assert a * 1000 == TVector3(4400, 5500, 0)
        assert 1000 * a == TVector3(4400, 5500, 0)
        assert a / 1000 == TVector3(0.0044, 0.0055, 0)
        assert 1000 / (a + TVector3(0, 0, 1)) == TVector3(227.27272727272725, 181.8181818181818, 1000)
        assert a**2 == 49.61
        assert a**1 == 7.043436661176133
        assert abs(a) == 7.043436661176133
        assert -a == TVector3(-4.4, -5.5, 0)
        assert +a == TVector3(4.4, 5.5, 0)
        arot = a.rotatez(numpy.pi)
        self.assertAlmostEqual(arot.x,-a.x)
        self.assertAlmostEqual(arot.y,-a.y)
        self.assertAlmostEqual(arot.z,a.z)

        a += TVector3(100, 200, 0)
        assert a == TVector3(104.4, 205.5, 0)
        a *= 10
        assert a == TVector3(1044, 2055, 0)
        assert a.angle(a) == 0
        assert a.angle(a * 3) == 0
        self.assertAlmostEqual(a.angle(-2 * a), numpy.pi)
        self.assertAlmostEqual(a.angle(a.rotatez(0.01)), 0.01)
        self.assertAlmostEqual(a.angle(a.rotatez(-0.01)), 0.01)
        assert a.angle(a * 0) == 0


    def test_vector3_array(self):
        a = TVector3Array(numpy.zeros(10), numpy.arange(10), numpy.zeros(10))
        assert a.tolist() == [TVector3(0, 0, 0), TVector3(0, 1, 0), TVector3(0, 2, 0), TVector3(0, 3, 0), TVector3(0, 4, 0), TVector3(0, 5, 0), TVector3(0, 6, 0), TVector3(0, 7, 0), TVector3(0, 8, 0), TVector3(0, 9, 0)]
        assert a[5] == TVector3(0, 5, 0)
        assert a.y.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.mag2.tolist() == [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
        assert (a + TVector3(1000, 2000, 0))[5] == TVector3(1000, 2005, 0)
        assert (a + TVector3(1000, 2000, 0) == TVector3Array(numpy.full(10, 1000), numpy.arange(2000, 2010), numpy.zeros(10))).tolist() == [True, True, True, True, True, True, True, True, True, True]
        assert (a**2).tolist() == [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
        assert (a**3).tolist() == [0.0, 1.0, 8.0, 27.0, 64.0, 125.0, 216.0, 343.0, 512.0, 729.0]
        arot = a.rotatez(numpy.pi)
        for aroti, ai in zip(arot.tolist(),a.tolist()):
            self.assertAlmostEqual(aroti.x,-ai.x)
            self.assertAlmostEqual(aroti.y,-ai.y)
            self.assertAlmostEqual(aroti.z,ai.z)

        numpy.testing.assert_almost_equal(a.angle(a), numpy.zeros_like(a))
        numpy.testing.assert_almost_equal(a.angle(3 * a), numpy.zeros_like(a))
        # first element is null vector, skip it, should return 0
        numpy.testing.assert_almost_equal(a[1:].angle(-2 * a[1:]), numpy.ones_like(a[1:]) * numpy.pi)

    def test_vector3_jagged(self):
        TVector3Jagged = type("TVector3Jagged", (awkward0.JaggedArray, uproot_methods.classes.TVector3.ArrayMethods), {})
        a = TVector3Jagged.fromoffsets([0, 3, 3, 5, 10], TVector3Array(numpy.zeros(10), numpy.arange(10), numpy.zeros(10)))
        a._generator = uproot_methods.classes.TVector3.TVector3
        a._args = ()
        a._kwargs = {}
        assert a.tolist() == [[TVector3(0, 0, 0), TVector3(0, 1, 0), TVector3(0, 2, 0)], [], [TVector3(0, 3, 0), TVector3(0, 4, 0)], [TVector3(0, 5, 0), TVector3(0, 6, 0), TVector3(0, 7, 0), TVector3(0, 8, 0), TVector3(0, 9, 0)]]
        assert a.x.tolist() == [[0.0, 0.0, 0.0], [], [0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
        assert a.y.tolist() == [[0, 1, 2], [], [3, 4], [5, 6, 7, 8, 9]]
        assert (a + TVector3(1000, 2000, 0)).tolist() == [[TVector3(1000, 2000, 0), TVector3(1000, 2001, 0), TVector3(1000, 2002, 0)], [], [TVector3(1000, 2003, 0), TVector3(1000, 2004, 0)], [TVector3(1000, 2005, 0), TVector3(1000, 2006, 0), TVector3(1000, 2007, 0), TVector3(1000, 2008, 0), TVector3(1000, 2009, 0)]]
        assert (a + TVector3Array(numpy.full(4, 1000), numpy.arange(1000, 5000, 1000), numpy.zeros(4))).tolist() == [[TVector3(1000, 1000, 0), TVector3(1000, 1001, 0), TVector3(1000, 1002, 0)], [], [TVector3(1000, 3003, 0), TVector3(1000, 3004, 0)], [TVector3(1000, 4005, 0), TVector3(1000, 4006, 0), TVector3(1000, 4007, 0), TVector3(1000, 4008, 0), TVector3(1000, 4009, 0)]]
        arot = a.rotatez(numpy.pi)
        for aroti, ai in zip(arot.flatten().tolist(),a.flatten().tolist()):
            self.assertAlmostEqual(aroti.x,-ai.x)
            self.assertAlmostEqual(aroti.y,-ai.y)
            self.assertAlmostEqual(aroti.z,ai.z)

    def test_lorentzvector(self):
        a = TLorentzVector(4.4, 5.5, 0, 0)
        assert a.dot(a) == -49.61
        assert a + TLorentzVector(1000, 2000, 0, 0) == TLorentzVector(1004.4, 2005.5, 0, 0)
        assert a - TLorentzVector(1000, 2000, 0, 0) == TLorentzVector(-995.6, -1994.5, 0, 0)
        assert TLorentzVector(1000, 2000, 0, 0) - a == TLorentzVector(995.6, 1994.5, 0, 0)
        assert a * 1000 == TLorentzVector(4400, 5500, 0, 0)
        assert 1000 * a == TLorentzVector(4400, 5500, 0, 0)
        assert a / 1000 == TLorentzVector(0.0044, 0.0055, 0, 0)
        assert 1000 / (a + TLorentzVector(0, 0, 1, 1)) == TLorentzVector(227.27272727272725, 181.8181818181818, 1000, 1000)
        assert a**2, -49.61
        assert (a + TLorentzVector(0, 0, 0, 10))**1 == 7.098591409568521
        assert abs(a + TLorentzVector(0, 0, 0, 10)) == 7.098591409568521
        assert -a == TLorentzVector(-4.4, -5.5, 0, 0)
        assert +a == TLorentzVector(4.4, 5.5, 0, 0)
        arot = a.rotatez(numpy.pi)
        self.assertAlmostEqual(arot.x,-a.x)
        self.assertAlmostEqual(arot.y,-a.y)
        self.assertAlmostEqual(arot.z,a.z)
        assert arot.t == a.t

        a += TLorentzVector(100, 200, 0, 0)
        assert a == TLorentzVector(104.4, 205.5, 0, 0)
        a *= 10
        assert a == TLorentzVector(1044, 2055, 0, 0)

    def test_lorentzvector_array(self):
        a = TLorentzVectorArray(numpy.zeros(10), numpy.arange(10), numpy.zeros(10), numpy.zeros(10))
        assert a.tolist() == [TLorentzVector(0, 0, 0, 0), TLorentzVector(0, 1, 0, 0), TLorentzVector(0, 2, 0, 0), TLorentzVector(0, 3, 0, 0), TLorentzVector(0, 4, 0, 0), TLorentzVector(0, 5, 0, 0), TLorentzVector(0, 6, 0, 0), TLorentzVector(0, 7, 0, 0), TLorentzVector(0, 8, 0, 0), TLorentzVector(0, 9, 0, 0)]
        assert a[5] == TLorentzVector(0, 5, 0, 0)
        assert a.y.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert a.mag2.tolist() == [0.0, -1.0, -4.0, -9.0, -16.0, -25.0, -36.0, -49.0, -64.0, -81.0]
        assert (a + TLorentzVector(1000, 2000, 0, 0))[5] == TLorentzVector(1000, 2005, 0, 0)
        assert (a + TLorentzVector(1000, 2000, 0, 0) == TLorentzVectorArray(numpy.full(10, 1000), numpy.arange(2000, 2010), numpy.zeros(10), numpy.zeros(10))).tolist() == [True, True, True, True, True, True, True, True, True, True]
        assert (a**2).tolist() == [0.0, -1.0, -4.0, -9.0, -16.0, -25.0, -36.0, -49.0, -64.0, -81.0]
        arot = a.rotatez(numpy.pi)
        for aroti, ai in zip(arot.tolist(),a.tolist()):
            self.assertAlmostEqual(aroti.x,-ai.x)
            self.assertAlmostEqual(aroti.y,-ai.y)
            self.assertAlmostEqual(aroti.z,ai.z)
            assert aroti.t==ai.t

    def test_ptetaphim_array(self):
        a = TLorentzVectorArray.from_ptetaphim(
            numpy.full(5, 20.),
            numpy.linspace(-5, 5, 5),
            numpy.linspace(-numpy.pi, numpy.pi, 6)[:-1],
            numpy.linspace(0, 20., 5),
        )
        assert (a * 5).tolist() == [
            PtEtaPhiMassLorentzVector(pt=100, eta=-5,   phi=-numpy.pi + 0*numpy.pi/5, mass=0),
            PtEtaPhiMassLorentzVector(pt=100, eta=-2.5, phi=-numpy.pi + 2*numpy.pi/5, mass=25),
            PtEtaPhiMassLorentzVector(pt=100, eta=0,    phi=-numpy.pi + 4*numpy.pi/5, mass=50),
            PtEtaPhiMassLorentzVector(pt=100, eta=2.5,  phi=-numpy.pi + 6*numpy.pi/5, mass=75),
            PtEtaPhiMassLorentzVector(pt=100, eta=5,    phi=-numpy.pi + 8*numpy.pi/5, mass=100)
        ]
        assert a.sum().p < 1e-10
        assert a.sum().mass == numpy.hypot(20 * numpy.cosh(a.eta), a.mass).sum()

    def test_lorentzvector_jagged(self):
        TLorentzVectorJagged = type("TLorentzVectorJagged", (awkward0.JaggedArray, uproot_methods.classes.TLorentzVector.ArrayMethods), {})
        a = TLorentzVectorJagged.fromoffsets([0, 3, 3, 5, 10], TLorentzVectorArray(numpy.zeros(10), numpy.arange(10), numpy.zeros(10), numpy.zeros(10)))
        a._generator = uproot_methods.classes.TLorentzVector.TLorentzVector
        a._args = ()
        a._kwargs = {}
        assert a.tolist() == [[TLorentzVector(0, 0, 0, 0), TLorentzVector(0, 1, 0, 0), TLorentzVector(0, 2, 0, 0)], [], [TLorentzVector(0, 3, 0, 0), TLorentzVector(0, 4, 0, 0)], [TLorentzVector(0, 5, 0, 0), TLorentzVector(0, 6, 0, 0), TLorentzVector(0, 7, 0, 0), TLorentzVector(0, 8, 0, 0), TLorentzVector(0, 9, 0, 0)]]
        assert a.x.tolist() == [[0.0, 0.0, 0.0], [], [0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
        assert a.y.tolist() == [[0, 1, 2], [], [3, 4], [5, 6, 7, 8, 9]]
        assert (a + TLorentzVector(1000, 2000, 0, 0)).tolist() == [[TLorentzVector(1000, 2000, 0, 0), TLorentzVector(1000, 2001, 0, 0), TLorentzVector(1000, 2002, 0, 0)], [], [TLorentzVector(1000, 2003, 0, 0), TLorentzVector(1000, 2004, 0, 0)], [TLorentzVector(1000, 2005, 0, 0), TLorentzVector(1000, 2006, 0, 0), TLorentzVector(1000, 2007, 0, 0), TLorentzVector(1000, 2008, 0, 0), TLorentzVector(1000, 2009, 0, 0)]]
        assert (a + TLorentzVectorArray(numpy.full(4, 1000), numpy.arange(1000, 5000, 1000), numpy.zeros(4), numpy.zeros(4))).tolist() == [[TLorentzVector(1000, 1000, 0, 0), TLorentzVector(1000, 1001, 0, 0), TLorentzVector(1000, 1002, 0, 0)], [], [TLorentzVector(1000, 3003, 0, 0), TLorentzVector(1000, 3004, 0, 0)], [TLorentzVector(1000, 4005, 0, 0), TLorentzVector(1000, 4006, 0, 0), TLorentzVector(1000, 4007, 0, 0), TLorentzVector(1000, 4008, 0, 0), TLorentzVector(1000, 4009, 0, 0)]]
        arot = a.rotatez(numpy.pi)
        for aroti, ai in zip(arot.flatten().tolist(),a.flatten().tolist()):
            self.assertAlmostEqual(aroti.x,-ai.x)
            self.assertAlmostEqual(aroti.y,-ai.y)
            self.assertAlmostEqual(aroti.z,ai.z)
            assert aroti.t==ai.t
