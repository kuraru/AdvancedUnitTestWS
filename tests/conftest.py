import os
import sys

# Ensure the 'src' directory is on sys.path so tests can import packages like
# 'AsyncConverterLib' and 'NoteCreatorLib' using absolute imports.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)
