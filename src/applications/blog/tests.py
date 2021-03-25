from django.test import TestCase

from applications.blog.models import Post


class TestBlogTest(TestCase):
    def test_post_list(self):
        resp = self.client.get("/b/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])

    def test_post_detail(self):
        resp = self.client.get("/b/p/")
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get("/b/p/1/")
        self.assertEqual(resp.status_code, 404)

        post = Post()
        post.save()
        resp = self.client.get(post.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])
