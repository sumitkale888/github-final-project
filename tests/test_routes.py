import unittest

from service import app
from service.routes import _ACCOUNTS
import service.routes as routes


class TestAccounts(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        _ACCOUNTS.clear()
        routes._NEXT_ID = 1

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["service"], "Accounts")

    def test_create(self):
        response = self.client.post("/accounts", json={
            "name": "John Doe",
            "email": "john@doe.com",
            "address": "123 Main St",
            "phone_number": "555-1212",
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["id"], 1)

    def test_create_requires_fields(self):
        response = self.client.post("/accounts", json={"name": "John"})
        self.assertEqual(response.status_code, 400)

    def test_list_and_read(self):
        self.client.post("/accounts", json={
            "name": "John Doe", "email": "john@doe.com", "address": "123 Main St"
        })
        self.assertEqual(self.client.get("/accounts").status_code, 200)
        response = self.client.get("/accounts/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "John Doe")

    def test_read_missing(self):
        self.assertEqual(self.client.get("/accounts/99").status_code, 404)

    def test_update(self):
        self.client.post("/accounts", json={
            "name": "John Doe", "email": "john@doe.com", "address": "123 Main St"
        })
        response = self.client.put("/accounts/1", json={"phone_number": "555-1111"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["phone_number"], "555-1111")

    def test_update_missing(self):
        self.assertEqual(self.client.put("/accounts/99", json={}).status_code, 404)

    def test_delete(self):
        self.client.post("/accounts", json={
            "name": "John Doe", "email": "john@doe.com", "address": "123 Main St"
        })
        self.assertEqual(self.client.delete("/accounts/1").status_code, 204)
        self.assertEqual(self.client.get("/accounts/1").status_code, 404)

    def test_delete_missing(self):
        self.assertEqual(self.client.delete("/accounts/99").status_code, 404)


if __name__ == "__main__":
    unittest.main()
