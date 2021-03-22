from django.test import TestCase


class TestBlogTest(TestCase):
    def test_index(self):
        resp = self.client.get("/b/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])
