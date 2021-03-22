from django.test import TestCase


class TestTask304Test(TestCase):
    def test_index(self):
        resp = self.client.get("/tasks/304/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])
