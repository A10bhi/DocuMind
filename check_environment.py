import sys
import pymupdf
import PIL
import pandas

print("Python:", sys.version)
print("Executable:", sys.executable)
print("PyMuPDF:", pymupdf.VersionBind)
print("Pillow:", PIL.__version__)
print("Pandas:", pandas.__version__)