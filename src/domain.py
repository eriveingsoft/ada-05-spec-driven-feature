"""Domain model for Customer."""

from dataclasses import dataclass
from typing import Any, Union


@dataclass(frozen=True)
class Customer:
    """Represents a customer entity in memory."""

    id: Union[int, str]
    name: str
    email: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Customer":
        """Safely creates a Customer instance from a dictionary.

        Raises:
            TypeError: If data is not a dictionary.
            ValueError: If required fields ('id', 'name', 'email') are missing,
                if any required field is None, or if 'name' or 'email' is empty.
        """
        if not isinstance(data, dict):
            raise TypeError("Customer data must be a dictionary")
        if "id" not in data or "name" not in data or "email" not in data:
            raise ValueError("Customer data must contain 'id', 'name', and 'email'")

        for field in ("id", "name", "email"):
            if data[field] is None:
                raise ValueError(f"Customer field '{field}' cannot be None")

        if not str(data["name"]).strip():
            raise ValueError("Customer field 'name' cannot be empty or blank")

        if not str(data["email"]).strip():
            raise ValueError("Customer field 'email' cannot be empty or blank")

        return cls(
            id=data["id"],
            name=str(data["name"]),
            email=str(data["email"]),
        )

    def to_dict(self) -> dict[str, Any]:
        """Converts the Customer instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
