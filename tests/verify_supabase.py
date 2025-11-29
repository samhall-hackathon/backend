import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.supabase.supabase import SupabaseClient
from src.schedule.model import Schedule

class TestSupabaseClient(unittest.TestCase):
    @patch("src.supabase.supabase.create_client")
    def test_get_latest_schedule_version(self, mock_create_client):
        # Setup mock
        mock_supabase = MagicMock()
        mock_create_client.return_value = mock_supabase
        
        # Mock the chain: table().select().order().limit().execute()
        mock_response = MagicMock()
        mock_response.data = [{"version": 5}]
        
        (mock_supabase.table.return_value
            .select.return_value
            .order.return_value
            .limit.return_value
            .execute.return_value) = mock_response

        # Test
        client = SupabaseClient("http://test.url", "test-key")
        version = client.get_latest_schedule_version()
        
        self.assertEqual(version, 5)
        
        # Verify calls
        mock_supabase.table.assert_called_with("schedule")
        mock_supabase.table.return_value.select.assert_called_with("version")
        mock_supabase.table.return_value.select.return_value.order.assert_called_with("version", desc=True)

    @patch("src.supabase.supabase.create_client")
    def test_get_latest_schedule_version_empty(self, mock_create_client):
        # Setup mock for empty result
        mock_supabase = MagicMock()
        mock_create_client.return_value = mock_supabase
        
        mock_response = MagicMock()
        mock_response.data = []
        
        (mock_supabase.table.return_value
            .select.return_value
            .order.return_value
            .limit.return_value
            .execute.return_value) = mock_response

        # Test
        client = SupabaseClient("http://test.url", "test-key")
        version = client.get_latest_schedule_version()
        
        self.assertEqual(version, 0)

    @patch("src.supabase.supabase.create_client")
    def test_write_schedule(self, mock_create_client):
        # Setup mock
        mock_supabase = MagicMock()
        mock_create_client.return_value = mock_supabase
        
        # Test data
        schedules = [
            Schedule(
                version=1,
                customer_id="c1",
                employee_id="e1",
                week_day=1,
                period="morning",
                hours=4.0
            ),
            Schedule(
                version=1,
                customer_id="c2",
                employee_id="e2",
                week_day=2,
                period="afternoon",
                hours=3.5
            )
        ]

        # Test
        client = SupabaseClient("http://test.url", "test-key")
        client.write_schedule(schedules)
        
        # Verify calls
        mock_supabase.table.assert_called_with("schedule")
        
        expected_data = [s.model_dump() for s in schedules]
        mock_supabase.table.return_value.insert.assert_called_with(expected_data)
        mock_supabase.table.return_value.insert.return_value.execute.assert_called_once()

if __name__ == "__main__":
    unittest.main()
