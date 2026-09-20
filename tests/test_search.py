"""Tests for the customer search logic engine."""

import pytest

from src.domain import Customer
from src.search_logic import normalize_text, search_customers


@pytest.fixture
def sample_customers() -> list[Customer]:
    return [
        Customer(id=1, name="Maria Gomez", email="maria.gomez@gmail.com"),
        Customer(id=2, name="María López", email="maria.lopez@empresa.com"),
        Customer(id=3, name="José Pérez", email="jose.perez@gmail.com"),
        Customer(id=4, name="Carlos Rodríguez", email="carlos.rodriguez@hotmail.com"),
        Customer(id=5, name="Ana García", email="ana.garcia@gmail.com"),
        Customer(id=6, name="Juan Martínez", email="juan.martinez@yahoo.com"),
    ]


def test_normalize_text():
    """Validates trimming, lowercase, and accent removal."""
    assert normalize_text("  José  ") == "jose"
    assert normalize_text("MARÍA") == "maria"
    assert normalize_text("  Carlos  ") == "carlos"
    assert normalize_text("ana.garcia@gmail.com") == "ana.garcia@gmail.com"


def test_search_by_name_exact_and_accent_insensitive_ts_01(sample_customers):
    """TS-01: Exact/partial search by name (case and accents ignored)."""
    # Searching without accent finds accented name
    results_jose = search_customers("Jose", sample_customers)
    assert len(results_jose) == 1
    assert results_jose[0].name == "José Pérez"

    # Searching with accent finds accented name
    results_jose_accent = search_customers("José", sample_customers)
    assert len(results_jose_accent) == 1
    assert results_jose_accent[0].name == "José Pérez"

    # Searching 'maria' finds both 'Maria Gomez' and 'María López'
    results_maria = search_customers("maria", sample_customers)
    assert len(results_maria) == 2
    assert [c.name for c in results_maria] == ["Maria Gomez", "María López"]

    # Searching uppercase with accent 'MARÍA' finds both
    results_maria_upper = search_customers("MARÍA", sample_customers)
    assert len(results_maria_upper) == 2
    assert [c.name for c in results_maria_upper] == ["Maria Gomez", "María López"]


def test_search_by_email_domain_partial_ts_02(sample_customers):
    """TS-02: Partial search by email domain."""
    results_gmail = search_customers("@gmail", sample_customers)
    assert len(results_gmail) == 3
    # Ordered alphabetically by customer name: Ana García, José Pérez, Maria Gomez
    assert [c.name for c in results_gmail] == ["Ana García", "José Pérez", "Maria Gomez"]

    results_hotmail = search_customers("hotmail.com", sample_customers)
    assert len(results_hotmail) == 1
    assert results_hotmail[0].name == "Carlos Rodríguez"


def test_search_results_alphabetical_ordering_ts_05():
    """TS-05: Validates correct alphabetical ordering of returned results by name."""
    customers = [
        Customer(id=1, name="Zoe Williams", email="zoe@example.com"),
        Customer(id=2, name="Ángel Torres", email="angel@example.com"),
        Customer(id=3, name="Bernardo Ramos", email="bernardo@example.com"),
        Customer(id=4, name="Ana Gómez", email="ana@example.com"),
    ]
    results = search_customers("example.com", customers)
    names = [c.name for c in results]
    assert names == ["Ana Gómez", "Ángel Torres", "Bernardo Ramos", "Zoe Williams"]


def test_search_trims_query_whitespace(sample_customers):
    """Search rules: whitespace at beginning and end is trimmed."""
    results = search_customers("   Jose   ", sample_customers)
    assert len(results) == 1
    assert results[0].name == "José Pérez"


def test_search_matches_both_name_and_email(sample_customers):
    """If search matches name fragment of one customer and email of another, both are returned."""
    # 'perez' matches name 'José Pérez' and if someone had 'perez' in email, both match
    custom_list = [
        Customer(id=1, name="José Pérez", email="jose@example.com"),
        Customer(id=2, name="Laura Gomez", email="perez_family@example.com"),
        Customer(id=3, name="Otro Usuario", email="otro@example.com"),
    ]
    results = search_customers("perez", custom_list)
    assert len(results) == 2
    assert [c.name for c in results] == ["José Pérez", "Laura Gomez"]


def test_search_using_default_storage():
    """Validates search_customers loading data directly from customers.json when customers is None."""
    results = search_customers("maria")
    assert len(results) >= 2
    assert results[0].name == "Maria Gomez"
    assert results[1].name == "María López"
