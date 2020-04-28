import pytest
from src.exercise import remove_last

def test_exercise(capsys):
    strings = ["First","Second","Third"]

    remove_last(strings)

    assert strings == ["First","Second"]

    strings = []

    remove_last(strings)

    assert strings == []
