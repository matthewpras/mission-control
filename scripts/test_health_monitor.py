import unittest
from unittest.mock import patch, mock_open
import os
import json
import time
import datetime

# Import the script to be tested
import health_monitor

class TestHealthMonitor(unittest.TestCase):

    def setUp(self):
        # Ensure a clean state for each test
        if os.path.exists(health_monitor.STATE_FILE):
            os.remove(health_monitor.STATE_FILE)

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_get_state_existing_file(self, mock_exists, mock_open_func):
        # Simulate an existing state file
        mock_open_func.return_value.read.return_value = '{"last_daily": 100, "last_weekly": 200, "last_monthly": 300}'
        
        state = health_monitor.get_state()
        self.assertEqual(state, {"last_daily": 100, "last_weekly": 200, "last_monthly": 300})
        mock_exists.assert_called_with(health_monitor.STATE_FILE)
        mock_open_func.assert_called_with(health_monitor.STATE_FILE, 'r')

    @patch('os.path.exists', return_value=False)
    def test_get_state_no_existing_file(self, mock_exists):
        # Simulate no existing state file
        state = health_monitor.get_state()
        self.assertEqual(state, {"last_daily": 0, "last_weekly": 0, "last_monthly": 0})
        mock_exists.assert_called_with(health_monitor.STATE_FILE)

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False) # Ensure no file exists initially
    def test_save_state(self, mock_exists, mock_open_func):
        # Simulate saving a new state
        test_state = {"last_daily": 1000, "last_weekly": 2000, "last_monthly": 3000}
        health_monitor.save_state(test_state)
        mock_open_func.assert_called_with(health_monitor.STATE_FILE, 'w')
        written_content = "".join([call.args[0] for call in mock_open_func.return_value.write.call_args_list])
        self.assertEqual(written_content, json.dumps(test_state, indent=2))

if __name__ == '__main__':
    unittest.main()
