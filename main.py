import sys
from translate import translate
from process import process_text
from export import export

file_name = sys.argv[1]
typed_text, written_text = translate(file_name)
details = process_text(typed_text, written_text)
export(details)
