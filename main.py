from scripts_directory import Converter
from scripts_directory import GUI
import sys

try:
    if len(sys.argv) < 3:
        print("Usage: python main.py <director input>(./text_samples) <director output>(./text_converted_to_audio)")
        sys.exit()

    project_input = sys.argv[1]
    project_output = sys.argv[2]
    c = Converter(project_input, project_output)
    c.extract_text()
    c.converter()

    gui = GUI(project_output)
    gui.gui()

except:
    print("Invalid parameters")
