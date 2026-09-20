"""Search logic engine for filtering customers."""

from typing import Optional
import unicodedata

from src.data_access import load_customers
from src.domain import Customer


def normalize_text(text: str) -> str:
    """Normalizes text by trimming whitespace, lowercasing, and stripping diacritics/accents."""
    trimmed = text.strip().lower()
    decomposed = unicodedata.normalize("NFD", trimmed)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def search_customers(
    query: str,
    customers: Optional[list[Customer]] = None,
) -> list[Customer]:
    """Filters customers by name or email matching the query.

    Matches are case-insensitive, accent-insensitive, and results are sorted
    alphabetically by customer name.

    Args:
        query: The search term.
        customers: Optional list of Customer objects. If omitted, loads from storage.

    Returns:
        List of matching Customer objects ordered alphabetically by name.
    """
    if customers is None:
        customers = load_customers()

    normalized_query = normalize_text(query)
    if not normalized_query:
        return []

    matches: list[Customer] = []
    for customer in customers:
        norm_name = normalize_text(customer.name)
        norm_email = normalize_text(customer.email)

        if normalized_query in norm_name or normalized_query in norm_email:
            matches.append(customer)

    # Sort results alphabetically by customer name (accent and case-insensitive)
    matches.sort(key=lambda c: normalize_text(c.name))
    return matches
