import json
from pathlib import Path


def test_customers_json_exists_and_is_valid():
    file_path = Path("customers.json")
    assert file_path.exists(), "customers.json must exist in repository root"

    with open(file_path, "r", encoding="utf-8") as f:
        customers = json.load(f)

    assert isinstance(customers, list), "customers.json root must be a list"
    assert len(customers) >= 5, "customers.json must contain at least 5 customers"

    emails = set()
    gmail_count = 0
    has_maria = False
    has_maria_accent = False

    for customer in customers:
        assert isinstance(customer.get("id"), (int, str)), "Customer id must be int or str"
        assert isinstance(customer.get("name"), str) and customer["name"], "Customer name must be non-empty str"
        assert isinstance(customer.get("email"), str) and customer["email"], "Customer email must be non-empty str"

        email = customer["email"]
        assert email not in emails, f"Duplicate email found: {email}"
        emails.add(email)

        if "@gmail.com" in email:
            gmail_count += 1
        if "Maria" in customer["name"]:
            has_maria = True
        if "María" in customer["name"]:
            has_maria_accent = True

    assert gmail_count >= 1, "Must contain customers with @gmail.com"
    assert has_maria and has_maria_accent, "Must contain variations of Maria (with and without accent)"
