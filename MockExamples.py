import unittest
from unittest.mock import patch
from unittest.mock import Mock

def get_user_name(user_id):
    return "Alice"
def send_email(to, message):
    print(f"Email to {to}: {message}")
def notify_user(email, message):
    send_email(email, message)

class TestAPI(unittest.TestCase):
  def setUp(self):
    self.fake_api = Mock()
    self.fake_api.get_data.return_value = {'temp': 25}
  def tearDown(self):
    del self.fake_api
  def test_weather_api(self):
    self.result = self.fake_api.get_data()
    self.assertEqual(self.result,{'temp':25})
  @patch('MockExamples.get_user_name')
  def test_get_user_name_with_patch(self, mock_get_user):
      mock_get_user.return_value = "Bob"
      result = get_user_name(123)
      self.assertEqual(result, "Bob")
  @patch("MockExamples.send_email")
  def test_mock_call(self, mock_send):
    notify_user("user@test.com", "Hello!")
    mock_send.assert_called_with("user@test.com", "Hello!")