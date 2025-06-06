import unittest
from unittest.mock import patch, MagicMock
from notification import send_mail


class TestNotification(unittest.TestCase):

    @patch('notification.get_secret')
    @patch('smtplib.SMTP')
    def test_send_mail_success(self, mock_smtp, mock_get_secret):
        mock_get_secret.side_effect = lambda x: {
            "FROM_EMAIL": "from@example.com",
            "PASSWORD": "password",
        }[x]

        mock_smtp_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_smtp_instance

        send_mail("Test message", "to@example.com")

        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once_with(user="from@example.com", password="password")
        mock_smtp_instance.sendmail.assert_called_once_with(
            from_addr="from@example.com",
            to_addrs="to@example.com",
            msg="Test message"
        )


if __name__ == '__main__':
    unittest.main()
