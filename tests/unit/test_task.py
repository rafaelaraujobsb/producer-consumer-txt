import unittest
from io import StringIO
from unittest.mock import patch

from producer_consumer_txt.services.queue import task_write_json_to_file


class TestTask(unittest.TestCase):

    @patch("producer_consumer_txt.services.queue.open", return_value=StringIO())
    def test_write_file_empty(self, mock_open):
        self.assertIsNone(task_write_json_to_file({"name": "rafael"}))

    @patch("producer_consumer_txt.services.queue.open")
    def test_write_file_not_empty(self, mock_open):
        file = StringIO()
        file.write('[{"name": "rafael"}]')
        file.seek(0)

        mock_open.return_value = file
        self.assertIsNone(task_write_json_to_file({"age": 23}))

    @patch("producer_consumer_txt.services.queue.open")
    def test_write_file_invalid_append(self, mock_open):
        file = StringIO()
        file.write('{"name": "rafael"}')
        file.seek(0)

        mock_open.return_value = file
        with self.assertRaises(AttributeError):
            task_write_json_to_file({"age": 23})
