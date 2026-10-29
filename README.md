# DocuMind — Machine Learning OCR Project

DocuMind is a Python-based Optical Character Recognition (OCR) and document-processing project. Its goal is to extract text from PDFs and images, process the extracted information, and eventually convert unstructured documents into structured, usable data.

This project is being developed step by step, starting with environment setup and OCR fundamentals before progressing toward machine learning and document understanding.

## Project Goals

- Extract text from scanned documents and images.
- Read and process PDF documents.
- Improve OCR results through image preprocessing.
- Organize extracted information into structured datasets.
- Explore machine learning techniques for document classification and information extraction.
- Build a reproducible and maintainable Python application.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Main programming language |
| Tesseract OCR | OCR engine for recognizing text |
| pytesseract | Python interface for Tesseract |
| PyMuPDF | PDF reading and text extraction |
| Pillow | Image loading and manipulation |
| OpenCV | Image preprocessing |
| NumPy | Numerical operations and image arrays |
| pandas | Data processing and tabular data |
| scikit-learn | Machine learning |
| Matplotlib | Data visualization |
| Jupyter | Interactive development and experiments |
| VS Code | Development environment |
| Git and GitHub | Version control and source code hosting |

## Current Project Status

- [x] Python environment configured
- [x] Virtual environment created
- [x] Git repository initialized and connected to GitHub
- [x] Core PDF and image-processing libraries installed
- [x] Tesseract OCR installed and verified
- [x] Jupyter notebook environment configured
- [x] Initial environment verification completed
- [ ] First practical OCR experiment
- [ ] PDF and image text extraction pipeline
- [ ] Image preprocessing workflow
- [ ] Structured data extraction
- [ ] Machine learning features and evaluation

## Project Structure

```text
DocuMind/
├── .venv/                     # Local Python environment (not committed)
├── .gitignore                 # Files excluded from Git
├── check_environment.py       # Environment verification script
├── 01_environment_test.ipynb  # Initial Jupyter environment test
├── README.md                  # Project overview
└── INSTALLATION.md            # Setup and installation guide
```

Additional folders and files will be introduced as the project develops.

## Getting Started

1. Install Python 3.12, Git, and Visual Studio Code.
2. Install the Python and Jupyter extensions in VS Code.
3. Install Tesseract OCR and configure Windows PATH.
4. Create and activate a Python virtual environment.
5. Install the project dependencies.
6. Register the environment as a Jupyter kernel.
7. Run the environment verification notebook.

See [INSTALLATION.md](INSTALLATION.md) for the complete instructions.

## Environment Verification

The initial environment test confirms that Python can import the required libraries and communicate with Tesseract OCR.

Example output:

```text
DocuMind environment is working!
Python version: 3.12.10
OpenCV version: 5.0.0
NumPy version: 2.5.4
Tesseract version: 5.5.3.20260724
```

Version numbers above reflect the initial development environment and may differ on other systems.

## Development Approach

DocuMind is being built incrementally:

1. Environment and dependency setup
2. OCR fundamentals and sample documents
3. PDF and image text extraction
4. Image preprocessing and OCR improvements
5. Structured information extraction
6. Machine learning experiments
7. Testing, evaluation, and documentation

## Future Scope

Potential future capabilities include batch document processing, structured output in CSV or JSON, document classification, OCR quality evaluation, and a user-friendly interface.

## License

A license has not yet been selected. Licensing details will be added when the project is ready for release.
