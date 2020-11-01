import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        N = len(data[0])
        stat = ( sum(data[0]) / N - sum(data[1]) / N ) / np.sqrt( 20 / N )
        self.assertTrue( np.abs( stat - testStatistic( data[0], 2, data[1], 4) )<1e-7, "The test statistic has not been computed correctly" )
        
    def test_pvalue(self) : 
        tval = testStatistic( data[0], 2, data[1], 4 )
        if tval>0 : pval = 2*scipy.stats.norm.cdf(-tval)
        else : pval = 2*scipy.stats.norm.cdf(tval)
        self.assertTrue( np.abs( pval - pvalue( data[0], 2, data[1], 4) )<1E-7, "Your function for determining the p-value is not working correctly" )
