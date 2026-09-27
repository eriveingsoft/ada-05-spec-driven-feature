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


@pytest.mark.parametrize("none_field", ["id", "name", "email"])
def test_customer_from_dict_rejects_none_fields_ac_06(none_field):
    """AC-06: Rejects dictionaries with explicit None values in required fields (ValueError)."""
    valid_data = {"id": 1, "name": "Maria Gomez", "email": "maria.gomez@gmail.com"}
    data_with_none = {**valid_data, none_field: None}

    with pytest.raises(ValueError, match=f"Customer field '{none_field}' cannot be None"):
        Customer.from_dict(data_with_none)


@pytest.mark.parametrize(
    "field,empty_value",
    [
        ("name", ""),
        ("name", "   "),
        ("name", " \t \n "),
        ("email", ""),
        ("email", "   "),
        ("email", " \t \n "),
    ],
)
def test_customer_from_dict_rejects_empty_or_whitespace_strings_ac_07(field, empty_value):
    """AC-07: Rejects dictionaries with empty or whitespace-only strings in name or email."""
    valid_data = {"id": 1, "name": "Maria Gomez", "email": "maria.gomez@gmail.com"}
    data_with_empty = {**valid_data, field: empty_value}

    with pytest.raises(ValueError, match=f"Customer field '{field}' cannot be empty or blank"):
        Customer.from_dict(data_with_empty)


def test_customer_from_dict_prevents_casting_none_to_literal_string_ac_06():
    """AC-06 / Issue #1: Precludes casting None to the literal string 'None'."""
    data = {"id": 1, "name": None, "email": "maria@example.com"}
    with pytest.raises(ValueError, match="Customer field 'name' cannot be None"):
        Customer.from_dict(data)


def test_customer_from_dict_valid_edge_cases():
    """Validates that valid edge-case IDs (0, string) are handled correctly."""
    customer_zero = Customer.from_dict({"id": 0, "name": "Zero User", "email": "zero@example.com"})
    assert customer_zero.id == 0

    customer_str_id = Customer.from_dict({"id": "USR-100", "name": "User Str", "email": "user@example.com"})
    assert customer_str_id.id == "USR-100"


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
