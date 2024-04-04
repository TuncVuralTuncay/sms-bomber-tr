import unittest
from unittest.mock import patch
from sms import SendSms

class TestSendSms(unittest.TestCase):

    def setUp(self):
        self.phone = "1234567890"
        self.mail = "test@gmail.com"
        self.sms = SendSms(self.phone, self.mail)

    @patch('sms.requests.post')
    def test_KahveDunyasi_success(self, mock_post):
        mock_post.return_value.status_code = 200
        self.sms.KahveDunyasi()
        self.assertEqual(self.sms.adet, 1)

    @patch('sms.requests.post')
    def test_KahveDunyasi_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        self.sms.KahveDunyasi()
        self.assertEqual(self.sms.adet, 0)

if __name__ == '__main__':
    unittest.main()