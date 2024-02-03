import requests
import pytest


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(post_id):
    # Make an API request to get a specific post
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    json_data = response.json()
    # Assert the status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response contains the expected post ID
    assert response.json()["id"] == post_id
    assert json_data["id"] == post_id
