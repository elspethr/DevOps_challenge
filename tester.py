import photoapp
import unittest

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
        rv = self.app.post('/', data="window.jpg")
        assert b'Upload new File' not in rv.data

if __name__ == '__main__':
    unittest.main()
