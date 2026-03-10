from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from NoteCreatorLib.note_creator import NoteCreator
import os

app = FastAPI(title="Note Creator API")

# Add CORS middleware to allow requests from any origin (helpful for local HTML files)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

note_creator = NoteCreator()

class Note(BaseModel):
    id: Optional[int] = None
    title: str
    content: str

class NoteCreate(BaseModel):
    title: str
    content: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Look for index.html in the same directory as main.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "index.html")
    with open(file_path, "r") as f:
        return f.read()

@app.post("/notes/", response_model=NoteCreate)
def create_note(note: NoteCreate):
    try:
        note_creator.create_note(note.title, note.content)
        return note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/", response_model=List[Note])
def get_notes():
    try:
        rows = note_creator.get_notes()
        return [{"id": row[0], "title": row[1], "content": row[2]} for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    try:
        row = note_creator.get_note_by_id(note_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return {"id": row[0], "title": row[1], "content": row[2]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    try:
        row = note_creator.get_note_by_id(note_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Note not found")
        note_creator.delete_note_by_id(note_id)
        return {"message": "Note deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notes/")
def delete_all_notes():
    try:
        note_creator.delete_all()
        return {"message": "All notes deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
