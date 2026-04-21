from homework_10 import log_event
import unittest
import os


class LogFileMixin:
    def read_log_file(self):
        with open("login_system.log", "r", encoding="utf-8") as f:
            return f.read()


class TestLogEvent(unittest.TestCase, LogFileMixin):
    def test_log_file_created_and_contains_message(self):
        log_event("userX", "success")
        self.assertTrue(os.path.exists("login_system.log"))
        content = self.read_log_file()
        self.assertIn("INFO - Login event - Username: userX, Status: success", content)

    def test_log_file_contains_success(self):
        log_event("user_10", "success")
        content = self.read_log_file()
        self.assertIn("INFO - Login event - Username: user_10, Status: success", content)

    def test_log_file_contains_failed(self):
        log_event("user_11", "failed")
        content = self.read_log_file()
        self.assertIn("ERROR - Login event - Username: user_11, Status: failed", content)

    def test_log_file_contains_expired(self):
        log_event("user_12", "expired")
        content = self.read_log_file()
        self.assertIn("WARNING - Login event - Username: user_12, Status: expired", content)



if __name__ == "__main__":
    unittest.main()