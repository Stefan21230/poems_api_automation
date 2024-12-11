import pytest
import json


@pytest.mark.parametrize("author", ["Adam Lindsay Gordon", "Alan Seeger", "Alexander Pope"])
def test_linecount_in_poems(api_session, author):
    """
    Test verifies that the API returns status 200 and matches the line count in poems.
    """
    response = api_session.get(f"{api_session.base_url}/author/{author}")
    if response.status_code == 200:
        author_poems = json.loads(response.text)
        for poem in author_poems:
            linecount = int(poem["linecount"])
            lines = poem["lines"]
            lines_number = len([line for line in lines if line.strip()])
            assert linecount == lines_number, (f"Expected linecount is {linecount},"
                                               f" but actually poem have {lines_number} lines")
    else:
        assert False, f"Expected status 200 but got {response.status_code}"


@pytest.mark.parametrize("title, expected_author", [(" Thoughts On The Works Of Providence", "Phillis Wheatley"),
                                                    ("\"All Is Vanity, Saith the Preacher\"", "George Gordon,"
                                                                                              " Lord Byron"),
                                                    ("\"And the sins of the fathers shall be\"", "Stephen Crane")])
def test_titles_for_poems(api_session, title, expected_author):
    """
    Test verifies that the API returns status 200 and that the author associated with a given title
    matches the expected author.
    """
    response = api_session.get(f"{api_session.base_url}/title/{title}")
    if response.status_code == 200:
        title_poems = json.loads(response.text)
        for title_poem in title_poems:
            title_author = title_poem["author"]
            assert title_author == expected_author, (f"Expected author for title {title} is {expected_author},"
                                                     f" but got {title_author}")
    else:
        assert False, f"Expected status 200 but got {response.status_code}"
