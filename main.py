from scripts_directory import Converter
import sys

try:
    if len(sys.argv) < 3:
        print("Usage: python main.py <director input>(./text_samples) <director output>(./text_converted_to_audio)")
        sys.exit()
    input = sys.argv[1]
    output = sys.argv[2]
    c = Converter(input, output)
    c.extract_text()
    c.converter()
except:
    print("Invalid parameters")
