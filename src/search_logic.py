"""Search logic engine for filtering customers and validating queries."""

from typing import Optional
import unicodedata

from src.data_access import load_customers
from src.domain import Customer

# Required error and informational messages defined in SPEC.md
ERROR_MIN_LENGTH = "Error: El término de búsqueda debe tener al menos 2 caracteres válidos."
ERROR_INVALID_CHARS = (
    "Error: El término de búsqueda contiene caracteres no permitidos. "
    "Solo se permiten letras, números, @, espacios y puntos."
)
MSG_NO_RESULTS = "No se encontraron clientes para el término de búsqueda."


class SearchValidationError(ValueError):
    """Raised when search query fails validation rules."""

    pass


class SearchResult(list[Customer]):
    """Represents the search response containing customers and optional informational message."""

    def __init__(self, items: list[Customer], message: Optional[str] = None) -> None:
        super().__init__(items)
        self.message = message

    def __str__(self) -> str:
        if self.message and not self:
            return self.message
        return super().__str__()


def is_valid_char(ch: str) -> bool:
    """Checks if character is allowed: letters, numbers, @, spaces, and dots."""
    return ch.isalnum() or ch in ("@", ".", " ")


def validate_query(query: str) -> str:
    """Validates the search query according to SPEC rules.

    - Cleans whitespace (trim).
    - Length must be >= 2 characters.
    - Only letters, numbers, @, spaces, and dots are allowed.

    Returns:
        The trimmed query.

    Raises:
        SearchValidationError: If validation fails.
    """
    if not isinstance(query, str):
        raise SearchValidationError(ERROR_MIN_LENGTH)

    trimmed = query.strip()
    if len(trimmed) < 2:
        raise SearchValidationError(ERROR_MIN_LENGTH)

    if not all(is_valid_char(ch) for ch in trimmed):
        raise SearchValidationError(ERROR_INVALID_CHARS)

    return trimmed


def normalize_text(text: str) -> str:
    """Normalizes text by trimming whitespace, lowercasing, and stripping diacritics/accents."""
    trimmed = text.strip().lower()
    decomposed = unicodedata.normalize("NFD", trimmed)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def search_customers(
    query: str,
    customers: Optional[list[Customer]] = None,
) -> SearchResult:
    """Validates query and filters customers by name or email matching the query.

    Matches are case-insensitive, accent-insensitive, and results are sorted
    alphabetically by customer name.

    Args:
        query: The search term.
        customers: Optional list of Customer objects. If omitted, loads from storage.

    Returns:
        SearchResult containing matching Customer objects ordered alphabetically
        by name, or an empty SearchResult with MSG_NO_RESULTS.

    Raises:
        SearchValidationError: If the query fails validation rules.
    """
    cleaned_query = validate_query(query)

    if customers is None:
        customers = load_customers()

    normalized_query = normalize_text(cleaned_query)

    matches: list[Customer] = []
    for customer in customers:
        norm_name = normalize_text(customer.name)
        norm_email = normalize_text(customer.email)

        if normalized_query in norm_name or normalized_query in norm_email:
            matches.append(customer)

    # Sort results alphabetically by customer name (accent and case-insensitive)
    matches.sort(key=lambda c: normalize_text(c.name))

    if not matches:
        return SearchResult([], message=MSG_NO_RESULTS)

    return SearchResult(matches)

