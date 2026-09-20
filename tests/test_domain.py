"""Unit tests for Customer domain model and data access repository."""

import json
from pathlib import Path
import pytest

from src.data_access import load_customers
from src.domain import Customer


def test_instantiate_customer_successfully():
    """T-02 Verification: Instantiates a Customer instance successfully."""
    customer = Customer(id=100, name="Test User", email="test@example.com")
    assert customer.id == 100
    assert customer.name == "Test User"
    assert customer.email == "test@example.com"


def test_customer_from_dict_and_to_dict():
    """T-02 Acceptance: Safely converts dictionaries to Customer instances."""
    data = {"id": 1, "name": "Maria Gomez", "email": "maria.gomez@gmail.com"}
    customer = Customer.from_dict(data)

    assert isinstance(customer, Customer)
    assert customer.id == 1
    assert customer.name == "Maria Gomez"
    assert customer.email == "maria.gomez@gmail.com"
    assert customer.to_dict() == data


def test_customer_from_dict_validation():
    """Tests validation on missing fields and invalid types."""
    with pytest.raises(TypeError, match="Customer data must be a dictionary"):
        Customer.from_dict(["not", "a", "dict"])  # type: ignore

    with pytest.raises(ValueError, match="Customer data must contain 'id', 'name', and 'email'"):
        Customer.from_dict({"id": 1, "name": "Maria"})

    with pytest.raises(ValueError, match="Customer data must contain 'id', 'name', and 'email'"):
        Customer.from_dict({"name": "Maria", "email": "maria@example.com"})


def test_load_customers_from_real_file():
    """Tests loading customers from actual customers.json."""
    customers = load_customers("customers.json")

    assert len(customers) >= 5
    for c in customers:
        assert isinstance(c, Customer)
        assert c.id is not None
        assert c.name
        assert c.email


def test_load_customers_file_not_found(tmp_path: Path):
    """Tests error when JSON file does not exist."""
    non_existent = tmp_path / "non_existent.json"
    with pytest.raises(FileNotFoundError, match="Customer data file not found"):
        load_customers(non_existent)


def test_load_customers_corrupted_json(tmp_path: Path):
    """Tests error when JSON file is corrupted."""
    corrupted_file = tmp_path / "corrupt.json"
    corrupted_file.write_text("{ invalid_json }", encoding="utf-8")

    with pytest.raises(ValueError, match="Corrupted or invalid JSON"):
        load_customers(corrupted_file)


def test_load_customers_not_a_list(tmp_path: Path):
    """Tests error when root JSON element is not a list."""
    invalid_structure_file = tmp_path / "not_a_list.json"
    invalid_structure_file.write_text(json.dumps({"id": 1}), encoding="utf-8")

    with pytest.raises(ValueError, match="must be a list of objects"):
        load_customers(invalid_structure_file)
