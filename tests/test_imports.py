import unittest
import SentenceToVector

class TestPackage(unittest.TestCase):
    def test_core_import(self):
        """
            just a blank test that tests for the try..except cases in the package for data required
        """
        self.assertRaises(LookupError)

    def test_bag_of_words(self):
        """
            testing to see if the sentence to bag of words converter works
            feel free to add more cases to test but ensure the mapping between the two lists is correct
        """
        bow_test_obj = SentenceToVector.BOWConvert()

        test_string_list = [
            "THis is a TesT, string - please check if ; this works"
        ]
        valid_operated = [
            ['this', 'test', 'string', 'please', 'check', 'work']
        ]

        on_calculation = [bow_test_obj.convert(to_convert) for to_convert in test_string_list]

        self.assertListEqual(valid_operated, on_calculation)


if __name__ == '__main__':
    unittest.main()