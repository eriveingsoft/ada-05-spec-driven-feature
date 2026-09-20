"""CLI entry point for Customer Search."""

import argparse
from pathlib import Path
import sys
from typing import Optional, Sequence

# Ensure UTF-8 output encoding across platforms
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure project root is in sys.path when script is executed directly
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


from src.search_logic import (
    ERROR_MIN_LENGTH,
    MSG_NO_RESULTS,
    SearchResult,
    SearchValidationError,
    search_customers,
)



def format_customer_output(result: SearchResult) -> str:
    """Formats the search result into user-facing output."""
    if not result:
        return result.message or MSG_NO_RESULTS

    lines = []
    for customer in result:
        lines.append(f"ID: {customer.id} | Nombre: {customer.name} | Correo: {customer.email}")
    return "\n".join(lines)


def run_cli(argv: Optional[Sequence[str]] = None) -> int:
    """CLI execution entrypoint.

    Returns:
        Exit code: 0 on success, 1 on validation or execution error.
    """
    parser = argparse.ArgumentParser(
        description="Buscador de clientes por nombre o correo electrónico.",
    )
    parser.add_argument(
        "term",
        nargs="?",
        default=None,
        help="Término de búsqueda (nombre o correo)",
    )
    parser.add_argument(
        "--name",
        dest="name",
        default=None,
        help="Buscar específicamente por nombre de cliente",
    )
    parser.add_argument(
        "--email",
        dest="email",
        default=None,
        help="Buscar específicamente por correo electrónico",
    )
    parser.add_argument(
        "-q",
        "--query",
        dest="query",
        default=None,
        help="Término de búsqueda general",
    )

    args = parser.parse_args(argv)

    query: Optional[str] = None
    field: Optional[str] = None

    if args.name is not None:
        query = args.name
        field = "name"
    elif args.email is not None:
        query = args.email
        field = "email"
    elif args.query is not None:
        query = args.query
    elif args.term is not None:
        query = args.term

    if query is None:
        print(ERROR_MIN_LENGTH, file=sys.stderr)
        return 1

    try:
        results = search_customers(query=query, field=field)
        output = format_customer_output(results)
        print(output)
        return 0
    except SearchValidationError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Error inesperado: {exc}", file=sys.stderr)
        return 1


def main() -> None:
    """Main function called when executed from command line."""
    sys.exit(run_cli())


if __name__ == "__main__":
    main()
