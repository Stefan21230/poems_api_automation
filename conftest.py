import pytest
import requests


@pytest.fixture(scope="session")
def api_session():
    """
    Fixture za deljenje HTTP sesije između testova.
    """
    session = requests.Session()
    session.headers.update({"User-Agent": "pytest-session"})
    base_url = "https://poetrydb.org"
    session.base_url = base_url
    yield session
    session.close()