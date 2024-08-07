import sys
from translate import translate
from process import process_text
from export import export
from detail import sort_details

file_name = sys.argv[1]
typed_text, written_text = translate(file_name)
details = process_text(typed_text)
details += process_text(written_text)
export(sort_details(details))
sys.exit()
