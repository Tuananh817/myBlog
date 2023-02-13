from django.test import TestCase,SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
     def test_page_home_status(self):
         respon = self.client.get('/')
         self.assertEquals(respon.status_code, 200)
