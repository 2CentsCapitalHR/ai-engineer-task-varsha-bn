# app.py
import gradio as gr
import os
import json
from doc_processor import analyze_and_annotate
from pathlib import Path
import uuid

with open("checklists.json", "r") as fh:
    CHECKLISTS = json.load(fh)

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def determine_process(uploaded_files):
    for f in uploaded_files:
        name = f.name.lower()
        if "articles" in name or "aoa" in name or "incorporation" in name:
            return "Company Incorporation: Private Company Limited"
    return "Unknown"

def process_uploads(files):
    local_paths = []
    for f in files:
        out_name = os.path.join("outputs", f"{uuid.uuid4().hex}_{f.name}")
        with open(out_name, "wb") as fh:
            fh.write(f.read())
        local_paths.append(out_name)

    process = determine_process(files)
    checklist_entry = CHECKLISTS.get(process)
    required_count = len(checklist_entry["required_documents"]) if checklist_entry else 0
    uploaded_names = [os.path.basename(p) for p in local_paths]

    missing = []
    if checklist_entry:
        for req in checklist_entry["required_documents"]:
            found = any(req.lower().split()[0] in nm.lower() or req.lower() in nm.lower() for nm in uploaded_names)
            if not found:
                missing.append(req)

    reports = []
    for p in local_paths:
        r = analyze_and_annotate(p, OUTPUT_DIR, checklist_entry)
        reports.append(r)

    summary = {
        "process": process,
        "documents_uploaded": len(local_paths),
        "required_documents": required_count,
        "missing_documents": missing,
        "individual_reports": reports
    }

    out_json = os.path.join(OUTPUT_DIR, f"report_{uuid.uuid4().hex}.json")
    with open(out_json, "w") as fh:
        json.dump(summary, fh, indent=2)

    first_reviewed = reports[0]["reviewed_file"] if reports else None
    json_text = json.dumps(summary, indent=2)
    return first_reviewed, json_text

with gr.Blocks() as demo:
    gr.Markdown("# ADGM Corporate Agent — Document Reviewer (Demo)")
    with gr.Row():
        upload = gr.File(file_count="multiple", label="Upload .docx files", file_types=[".docx"])
    run_btn = gr.Button("Run Review")
    out_file = gr.File(label="Reviewed .docx (downloadable)")
    out_json = gr.Textbox(label="Structured JSON Report", lines=20)
    run_btn.click(fn=process_uploads, inputs=[upload], outputs=[out_file, out_json])

if __name__ == "__main__":
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)
