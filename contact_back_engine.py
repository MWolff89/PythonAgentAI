from llama_index.tools import FunctionTool
import os

note_file = os.path.join("data", "contact_back.txt")


def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w")

    with open(note_file, "a") as f:
        f.writelines([note + "\n"])

    return "note saved"


contact_back_note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="contact_back_note_saver",
    description="this tool can save a text based note to a file for the user and is used when the user has a complaint, a feedback, or simply needs to be contacted back by a human representative for further assistance.",
)
