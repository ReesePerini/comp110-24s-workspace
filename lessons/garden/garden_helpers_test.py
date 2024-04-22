"""Test my garden functions."""

__author__ = "730384323"


from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_use_case() -> None:
    """Test basic use case for add_by_kind function."""
    x: dict[str, list[str]] = {"vegetables": ["cucumber"], "flower": ["zinnia"]}
    add_by_kind(x, "tree", "peach")
    assert x == {"vegetables": ["cucumber"], "flower": ["zinnia"], "tree": ["peach"]}


def test_add_by_kind_edge_case() -> None:
    """Test edge case for add_by_kind function."""
    x: dict[str, list[str]] = {}
    add_by_kind(x, "flower", "zinnia")
    assert x == {"flower": ["zinnia"]}


def test_add_by_date_use_case() -> None:
    """Test basic use case for add_by_date function."""
    y: dict[str, list[str]] = {"November": ["tulips"], "May": ["cucumber"]}
    add_by_date(y, "May", "carrots")
    assert y == {"November": ["tulips"], "May": ["cucumber", "carrots"]}


def test_add_by_date_edge_case() -> None:
    """Test edge case for add_by_date function."""
    y: dict[str, list[str]] = {}
    add_by_date(y, "May", "cucumber")
    assert y == {"May": ["cucumber"]}


def test_lookup_by_kind_and_date_use_case() -> None:
    """Test basic use case for lookup_by_kind_and_date function."""
    x: dict[str, list[str]] = {"vegetable": ["cucumber"], "flower": ["tulips", "zinnia"]}
    y: dict[str, list[str]] = {"November": ["tulips"], "May": ["cucumber", "zinnia"]}
    ret_value: str = lookup_by_kind_and_date(x, y, "vegetable", "May")
    assert ret_value == "vegetables to plant in May: ['cucumber']"
    

def test_lookup_by_kind_and_date_edge_case() -> None:
    """Test edge case for lookup_by_kind_and_date function."""
    x: dict[str, list[str]] = {"vegetable": ["cucumber"], "flower": ["tulips", "zinnia"]}
    y: dict[str, list[str]] = {"November": ["tulips"], "May": ["cucumber", "zinnia"]}
    ret_value: str = lookup_by_kind_and_date(x, y, "vegetable", "November")
    assert ret_value == "No vegetables to plant in November"