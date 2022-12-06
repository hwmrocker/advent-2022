import sys
from pathlib import Path

input_txt = Path(__file__).parent / "input"
from .task_a import main

if len(sys.argv) > 1:
    if sys.argv[1] == "a":
        ...
    elif sys.argv[1] == "b":
        from .task_b import main


print(main(input_txt=input_txt.read_text()))
