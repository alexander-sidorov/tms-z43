from django.test import TestCase


class TestTask103Test(TestCase):
    def test_index(self):
        resp = self.client.get("/tasks/103/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])
