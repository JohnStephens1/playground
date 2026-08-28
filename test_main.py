from main import say_hi


def test_main() -> None:
    assert say_hi() == "hi"
