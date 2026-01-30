from dataclasses import dataclass
from toon import Topic

@dataclass
class Question:
    text: str
    answer: str
    topic: Topic


QUESTIONS = [
    # -------- OOPS --------
    Question("What keyword creates a class?", "class", Topic.OOPS),
    Question("What is self referring to?", "object", Topic.OOPS),
    Question("Which method runs automatically?", "__init__", Topic.OOPS),

    # -------- EXCEPTIONS --------
    Question("Which block handles errors?", "except", Topic.EXCEPTIONS),
    Question("Which block runs always?", "finally", Topic.EXCEPTIONS),
    Question("Keyword to raise error?", "raise", Topic.EXCEPTIONS),

    # -------- FILE HANDLING --------
    Question("Which mode reads file?", "r", Topic.FILE_HANDLING),
    Question("Which mode writes file?", "w", Topic.FILE_HANDLING),
    Question("Which function closes file?", "close", Topic.FILE_HANDLING),

    # -------- REGEX --------
    Question("Which module handles regex?", "re", Topic.REGEX),
    Question("Symbol for digit in regex?", "\\d", Topic.REGEX),
    Question("Function to search pattern?", "search", Topic.REGEX),
]
# -----------------------------