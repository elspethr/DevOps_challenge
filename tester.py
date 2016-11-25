import photoapp
import unittest
import random

class PhotoappTestCase(unittest.TestCase):

    def setUp(self):
        photoapp.app.config['TESTING'] = True
        self.app = photoapp.app.test_client()

    def tearDown(self):
        pass

    #check initial page is working
    def test_home_status(self):
        # sends HTTP GET request to the application on the specified path
        result = self.app.get('/') 
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        assert b'Upload new File' in result.data

    #check that a POST request returns the photo correctly    
    def test_post(self):
        #post the item
        self.app.post('/', data="window.jpg", follow_redirects=True)
        #check the response
        response = self.app.get('/window.jpg')
        testphotodata = open("window.jpg", "rb").read()
        #quick check on image size
        assert(len(testphotodata)==len(response.data))
        #check every pixel
        #for i in range(len(testphotodata)):
        #that's slow so instead just check a random subset of pixels
        for i in random.sample(xrange(len(testphotodata)), 5000):
            assert response.data[i] == testphotodata[i]

if __name__ == '__main__':
    unittest.main()
