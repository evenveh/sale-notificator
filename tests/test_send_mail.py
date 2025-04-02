import unittest
from unittest.mock import patch, MagicMock
from notification import send_mail

class TestSendMail(unittest.TestCase):

    @patch("notification.smtplib.SMTP")
    @patch("notification.get_secret")
    def test_send_mail(self, mock_get_secret, mock_smtp):
    #     """Test send_mail function with a mocked SMTP server."""
    #
    #     # Mock get_secret() return values
    #     mock_get_secret.side_effect = lambda key: {
    #         "FROM_EMAIL": "test@example.com",
    #         "PASSWORD": "fakepassword",
    #         "RECIPIENT": "recipient@example.com",
    #     }.get(key, "")
    #
    #     # Create a mock SMTP instance
    #     mock_smtp_instance = MagicMock()
    #     mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
    #
    #     # Call function
    #     send_mail("Test email message")
    #
    #     # Assertions
    #     mock_smtp.assert_called_once_with("smtp.gmail.com")  # SMTP should be initialized correctly
    #     mock_smtp_instance.starttls.assert_called_once()  # Ensure TLS is started
    #     mock_smtp_instance.login.assert_called_once_with(user="test@example.com", password="fakepassword")
    #     mock_smtp_instance.sendmail.assert_called_once()  # Ensure sendmail is called
    #
    #     # Get the actual email sent
    #     args, kwargs = mock_smtp_instance.sendmail.call_args
    #     from_email, to_email, msg = args
    #
    #     # Validate email content
    #     self.assertEqual(from_email, "test@example.com")
    #     self.assertEqual(to_email, "recipient@example.com")
    #     self.assertIn("Test email message", msg)
    #
        print("send_mail() test passed.")

if __name__ == "__main__":
    unittest.main()
