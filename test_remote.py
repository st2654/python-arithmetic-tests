from remote import fetch_status


def test_fetch_status():
    assert fetch_status() == "ok"
