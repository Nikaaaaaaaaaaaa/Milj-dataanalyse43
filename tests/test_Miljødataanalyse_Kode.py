#Setup
#import sys
#sys.path.append('../notebooks')
from os import sys, path
sys.path.append('../notebooks')
import unittest
import Miljødataanalyse_Kode

class test_One(unittest.TestCase):
    dict = {
        "Germany": "Berlin", 
        "Canada": "Ottawa", 
        "England": "London" }
    def test_vis_manglende_verdier(dict):
        result = vis_manglende_verdier(dict)
        self.assertTrue(result)
        


#class test_Miljødataanalyse_Kode(unittest.TestCase):
#    def test_One(df, df_cleaned):
#        assert df != df_cleaned#

#    try:
#        test_One(df, df_cleaned)
#    except AssertionError as e:
#        print(e)
#    pass

#Testing
#def ():
    #assert
#    def test_df_equal(df1, df2):
#    assert df1.shape == df2.shape

# Run the test
#try:
    #the test def
#except AssertionError as e:
#    print(e)

#def test_df_change(df, df_cleaned):
#    assert df != df_cleaned

#try:
#    test_df_change()
#except AssertionError as e:
#    print(e)

if __name__ == "__main__":
    unittest.main()
