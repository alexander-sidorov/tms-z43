import json

from django.http import JsonResponse
from django.test import TestCase


class TestTask402Test(TestCase):
    def test_index(self):
        resp = self.client.get("/tasks/402/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/html", resp["Content-Type"])

    def test_api_get(self):
        resp: JsonResponse = self.client.get("/tasks/402/api/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("application/json", resp["Content-Type"])

        payload = json.loads(resp.content)
        self.assertTrue(payload.get("ok"))
        self.assertEqual(payload.get("number"), 0)

    def test_api_post_empty_request(self):
        resp = self.client.post("/tasks/402/api/")
        self.assertEqual(resp.status_code, 422)
        self.assertIn("application/json", resp["Content-Type"])

    def test_api_post_malformed_number(self):
        data = {
            "ok": True,
            "result": "fcuk",
        }
        resp = self.client.post("/tasks/402/api/", data=data)
        self.assertEqual(resp.status_code, 422)
        self.assertIn("application/json", resp["Content-Type"])

    def test_api_post_malformed_json(self):
        data = {
            "ok": True,
            "xxx": "yyy",
        }
        resp = self.client.post("/tasks/402/api/", data=data)
        self.assertEqual(resp.status_code, 422)
        self.assertIn("application/json", resp["Content-Type"])

    def test_api_post_ok(self):
        data = {
            "ok": True,
            "number": 111,
        }

        for _ in "12":
            resp = self.client.post(
                "/tasks/402/api/",
                content_type="application/json",
                data=data,
            )
            self.assertEqual(resp.status_code, 200)
            self.assertIn("application/json", resp["Content-Type"])

        self.assertIn("task402", self.client.session)
        self.assertEqual(self.client.session["task402"], 222)
