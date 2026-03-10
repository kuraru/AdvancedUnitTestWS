import pytest
from fastapi.testclient import TestClient
from main import app, note_creator
import os

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    # Ensure a fresh start for each test
    note_creator.delete_all()
    yield
    note_creator.delete_all()

def test_create_note():
    response = client.post("/notes/", json={"title": "Test Title", "content": "Test Content"})
    assert response.status_code == 200
    assert response.json() == {"title": "Test Title", "content": "Test Content"}

def test_get_notes():
    client.post("/notes/", json={"title": "Note 1", "content": "Content 1"})
    client.post("/notes/", json={"title": "Note 2", "content": "Content 2"})
    
    response = client.get("/notes/")
    assert response.status_code == 200
    notes = response.json()
    assert len(notes) == 2
    assert notes[0]["title"] == "Note 1"
    assert notes[1]["title"] == "Note 2"

def test_get_note_by_id():
    client.post("/notes/", json={"title": "Single Note", "content": "Some content"})
    notes = client.get("/notes/").json()
    note_id = notes[0]["id"]
    
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Single Note"

def test_get_note_not_found():
    response = client.get("/notes/9999")
    assert response.status_code == 404

def test_delete_note():
    client.post("/notes/", json={"title": "To Delete", "content": "Bye bye"})
    notes = client.get("/notes/").json()
    note_id = notes[0]["id"]
    
    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Note deleted successfully"}
    
    # Verify it's gone
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 404
