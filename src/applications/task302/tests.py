from django.test import TestCase


class TestTask302Test(TestCase):
    def test_index(self):
        resp = self.client.get("/tasks/302/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])
