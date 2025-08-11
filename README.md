<<<<<<< HEAD
# ADGM Corporate Agent — Document Reviewer (Take-home submission)

This repository is a ready-to-run demo for the AI Engineer Intern take-home assignment.
It provides a minimal, well-documented system to:

- Accept `.docx` uploads (demo uses local files),
- Identify document types (rule-based),
- Run simple rule-based red-flag checks,
- Annotate the `.docx` file by appending review comments,
- Produce a structured JSON report.

## What is included
- `app.py` - Gradio demo UI (accepts .docx files)
- `doc_processor.py` - Core document parsing, detection, annotation logic
- `rag.py` - RAG helper placeholders (indexing & embedding helpers)
- `checklists.json` - Minimal checklist mapping (expand from Data Sources.pdf)
- `templates/example_AoA_before.docx` - example input file
- `outputs/` - generated reviewed file and report.json (demo)
- `requirements.txt`

## How to run locally
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Linux/macOS
   venv\Scripts\activate    # on Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the demo UI:
   ```bash
   python app.py
   ```
   Open the Gradio URL shown in the terminal (usually http://127.0.0.1:7860).

## Notes
- This is a minimal, human-readable implementation intended for a take-home task demo.
- For production or stronger legal checks, integrate a legal LLM with RAG using the ADGM docs (from the provided Data Sources PDF).
- I included an example input and a generated reviewed file in `outputs/` for demonstration. Use those as templates.

=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vgbm4cZ0)
>>>>>>> 287c509271cca441daf52b6ef8e1ea1f6b1c1103
