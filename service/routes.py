"""REST routes for the Accounts service."""
from flask import jsonify, request

_ACCOUNTS = {}
_NEXT_ID = 1


@app.get("/")
def index():
    return jsonify({"service": "Accounts", "status": "running"})


@app.post("/accounts")
def create_account():
    global _NEXT_ID
    data = request.get_json(silent=True) or {}
    required = ("name", "email", "address")
    if any(not data.get(field) for field in required):
        return jsonify({"error": "name, email and address are required"}), 400

    account = {
        "id": _NEXT_ID,
        "name": data["name"],
        "email": data["email"],
        "address": data["address"],
        "phone_number": data.get("phone_number"),
    }
    _ACCOUNTS[_NEXT_ID] = account
    _NEXT_ID += 1
    return jsonify(account), 201


@app.get("/accounts")
def list_accounts():
    return jsonify(list(_ACCOUNTS.values())), 200


@app.get("/accounts/<int:account_id>")
def read_account(account_id):
    account = _ACCOUNTS.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account), 200


@app.put("/accounts/<int:account_id>")
def update_account(account_id):
    account = _ACCOUNTS.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json(silent=True) or {}
    for field in ("name", "email", "address", "phone_number"):
        if field in data:
            account[field] = data[field]
    return jsonify(account), 200


@app.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    if account_id not in _ACCOUNTS:
        return jsonify({"error": "Account not found"}), 404
    del _ACCOUNTS[account_id]
    return "", 204
