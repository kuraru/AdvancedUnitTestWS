from fastapi.testclient import TestClient
from bs4 import BeautifulSoup
from main import app
import pytest

client = TestClient(app)

def test_index_html_structure():
    # Fetch the root page
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Verify title
    assert soup.title is not None
    assert "Note Creator" in soup.title.string

    # Verify existence of main heading
    h1 = soup.find("h1")
    assert h1 is not None
    assert "Note Creator" in h1.text

    # Verify form container heading
    h3 = soup.find("h3", string="Create a New Note")
    assert h3 is not None

    # Verify input fields
    title_input = soup.find("input", {"id": "title"})
    assert title_input is not None
    assert title_input.get("placeholder") == "Enter note title"

    content_textarea = soup.find("textarea", {"id": "content"})
    assert content_textarea is not None
    assert content_textarea.get("placeholder") == "Enter note content"

    # Verify buttons
    create_button = soup.find("button", string="Create Note")
    assert create_button is not None
    assert "createNote()" in create_button.get("onclick", "")

    delete_all_button = soup.find("button", string="Delete All Notes")
    assert delete_all_button is not None
    assert "deleteAllNotes()" in delete_all_button.get("onclick", "")

    # Verify notes container
    notes_container = soup.find("div", {"id": "notes-container"})
    assert notes_container is not None
    assert notes_container.find("h3", string="Your Notes") is not None
    
    notes_list = soup.find("ul", {"id": "notes-list"})
    assert notes_list is not None
