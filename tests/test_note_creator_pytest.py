import pytest
from unittest.mock import MagicMock, patch

from NoteCreatorLib.note_creator import NoteCreator


@pytest.fixture
def mock_sqlite():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    with patch("NoteCreatorLib.note_creator.sqlite3.connect", return_value=mock_conn) as mock_connect:
        yield mock_connect, mock_conn, mock_cursor


def test_create_note_executes_insert_and_commit(mock_sqlite):
    mock_connect, mock_conn, mock_cursor = mock_sqlite
    nc = NoteCreator()

    nc.create_note("title", "content")
    
    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_called_with(
        "INSERT INTO notes (title, content) VALUES (?, ?)", ("title", "content")
    )
    assert mock_conn.commit.call_count == 2


def test_get_notes_fetches_all_rows(mock_sqlite):
    _, _, mock_cursor = mock_sqlite
    mock_cursor.fetchall.return_value = [(1, "t1", "c1"), (2, "t2", "c2")]
    nc = NoteCreator()

    result = nc.get_notes()

    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_called_with("SELECT * FROM notes")
    assert result == [(1, "t1", "c1"), (2, "t2", "c2")]


def test_get_note_by_id_uses_parameterized_query_and_fetchone(mock_sqlite):
    _, _, mock_cursor = mock_sqlite
    mock_cursor.fetchone.return_value = (1, "t1", "c1")
    nc = NoteCreator()

    result = nc.get_note_by_id(1)

    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_called_with("SELECT * FROM notes WHERE id = ?", (1,))
    assert result == (1, "t1", "c1")


def test_get_note_by_title_uses_parameterized_query_and_fetchone(mock_sqlite):
    _, _, mock_cursor = mock_sqlite
    mock_cursor.fetchone.return_value = (3, "hello", "world")
    nc = NoteCreator()

    result = nc.get_note_by_title("hello")

    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_called_with("SELECT * FROM notes WHERE title = ?", ("hello",))
    assert result == (3, "hello", "world")


def test_delete_note_by_id_executes_delete_and_commit(mock_sqlite):
    _, mock_conn, mock_cursor = mock_sqlite
    nc = NoteCreator()

    nc.delete_note_by_id(5)

    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_called_with("DELETE FROM notes WHERE id = ?", (5,))
    assert mock_conn.commit.call_count == 2


def test_delete_all_executes_delete_and_commit(mock_sqlite):
    _, mock_conn, mock_cursor = mock_sqlite
    nc = NoteCreator()

    nc.delete_all()

    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_called_with("DELETE FROM notes")
    assert mock_conn.commit.call_count == 2


def test_close_connection_closes_connection(mock_sqlite):
    _, mock_conn, _ = mock_sqlite
    nc = NoteCreator()

    nc.close_connection()

    mock_conn.close.assert_called_once()


def test_destructor_calls_close_connection_once(mock_sqlite):
    _, mock_conn, _ = mock_sqlite
    nc = NoteCreator()

    # Explicitly delete to trigger __del__
    del nc

    # close should be called once due to __del__
    mock_conn.close.assert_called_once()
