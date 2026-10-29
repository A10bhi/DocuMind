# DocuMind Installation and Environment Setup

This guide explains how to configure the development environment for DocuMind on Windows using Python, VS Code, Tesseract OCR, and Jupyter.

## 1. Prerequisites

Install the following software:

- Python 3.12
- Git for Windows
- Visual Studio Code
- Microsoft Python extension for VS Code
- Microsoft Jupyter extension for VS Code
- Tesseract OCR for Windows

Use the official download pages:

- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads
- VS Code: https://code.visualstudio.com/
- Tesseract Windows installer: https://github.com/UB-Mannheim/tesseract/wiki

The Tesseract Windows installer is maintained separately from the main Tesseract project.

## 2. Install Python 3.12

Install Python 3.12. The development environment for this project was created using Python 3.12.10.

Verify the installation in PowerShell:

```powershell
py -3.12 --version
```

Expected output:

```text
Python 3.12.10
```

A later Python 3.12 patch release may also work.

## 3. Install Git

Verify Git:

```powershell
git --version
```

Configure your Git identity using your own name and email address:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Replace the example values with your own details.

## 4. Create the Project Folder

The original development folder was:

```text
D:\ML Project\DocuMind
```

Create the folder if it does not already exist. Open it in VS Code using **File → Open Folder**.

For a fresh clone of the repository, use:

```powershell
git clone https://github.com/A10bhi/DocuMind.git
cd DocuMind
```

If you already have the project folder, do not clone it into itself.

## 5. Create a Virtual Environment

From the project root, run:

```powershell
py -3.12 -m venv .venv
```

Activate the environment in the VS Code PowerShell terminal:

```powershell
.\.venv\Scripts\Activate.ps1
```

The terminal prompt should display `(.venv)`.

Verify Python:

```powershell
python --version
```

Expected version: Python 3.12.x.

If PowerShell blocks activation, consult the official Python documentation or use the VS Code terminal's Command Prompt profile. Avoid changing system security policies unnecessarily.

## 6. Upgrade pip

With the virtual environment active:

```powershell
python -m pip install --upgrade pip
```

Confirm pip is associated with the virtual environment:

```powershell
python -m pip --version
```

The displayed path should point into the project's `.venv` directory.

## 7. Install Python Dependencies

Install the libraries used in the initial environment:

```powershell
python -m pip install pymupdf pillow pandas pytesseract opencv-python numpy scikit-learn matplotlib jupyter ipykernel
```

These libraries serve the following purposes:

- `pymupdf`: PDF access and text extraction.
- `pillow`: Image loading and manipulation.
- `pandas`: Tabular data processing.
- `pytesseract`: Python interface to Tesseract OCR.
- `opencv-python`: Image preprocessing.
- `numpy`: Numerical operations and image arrays.
- `scikit-learn`: Machine learning.
- `matplotlib`: Charts and visualizations.
- `jupyter`: Notebook tools.
- `ipykernel`: Python kernel integration.

## 8. Install Tesseract OCR

Install the Windows Tesseract OCR application using the UB Mannheim installer page:

https://github.com/UB-Mannheim/tesseract/wiki

The default installation directory used for this project is:

```text
C:\Program Files\Tesseract-OCR
```

Keep the English language data selected during installation.

### Configure Windows PATH

Add the following directory to your Windows user PATH:

```text
C:\Program Files\Tesseract-OCR
```

Open Environment Variables, select the user `Path` variable, choose Edit, add a new entry, and save the changes.

Restart VS Code after changing PATH so new terminals inherit the updated environment.

Verify Tesseract:

```powershell
tesseract --version
```

If Windows cannot find the command, test the executable directly:

```powershell
& "C:\Program Files\Tesseract-OCR\tesseract.exe" --version
```

If the direct command works but `tesseract --version` does not, check the PATH entry and restart the terminal.

## 9. Verify Python Can Access Tesseract

With `.venv` active, run:

```powershell
python -c "import pytesseract; print('Tesseract version:', pytesseract.get_tesseract_version())"
```

The output should show the installed Tesseract version.

## 10. Register the Jupyter Kernel

Register the project's virtual environment:

```powershell
python -m ipykernel install --user --name documind --display-name "Python (DocuMind)"
```

List the available kernels:

```powershell
python -m jupyter kernelspec list
```

Look for the `documind` kernel.

## 11. Configure VS Code

Install or enable the Microsoft Python and Jupyter extensions.

Open the project folder and select the Python interpreter:

```text
D:\ML Project\DocuMind\.venv\Scripts\python.exe
```

For notebooks, select the **Python (DocuMind)** kernel or the matching `.venv` Python environment.

## 12. Create the Environment Test Notebook

Create a notebook named:

```text
01_environment_test.ipynb
```

Add and run the following code:

```python
import sys
import fitz
import PIL
import pandas as pd
import pytesseract
import cv2
import numpy as np
import sklearn
import matplotlib
import jupyter

print("DocuMind environment is working!")
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)
print("Tesseract version:", pytesseract.get_tesseract_version())
```

Expected results:

- The success message is displayed.
- The Python executable points to the project's `.venv`.
- OpenCV and NumPy versions are displayed.
- Tesseract's version is displayed without errors.

Save the notebook with **Ctrl + S**.

## 13. Verify Other Installed Tools

Check scikit-learn:

```powershell
python -c "import sklearn; print(sklearn.__version__)"
```

Check Matplotlib:

```powershell
python -c "import matplotlib; print(matplotlib.__version__)"
```

Check Jupyter:

```powershell
python -m jupyter --version
```

Check ipykernel:

```powershell
python -c "import ipykernel; print(ipykernel.__version__)"
```

## 14. Git and GitHub

Initialize a Git repository if necessary:

```powershell
git init
git branch -M main
```

Configure `.gitignore` to exclude local environments, caches, secrets, and generated files. A typical initial version is:

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
data/
outputs/
.pytest_cache/
```

Review the exclusions before committing real documents or datasets. Some projects need sample data tracked separately, while private or sensitive documents should not be committed.

Stage and commit project files:

```powershell
git add .
git commit -m "Set up DocuMind Python environment"
```

Connect to the GitHub repository if it is not already configured:

```powershell
git remote add origin https://github.com/A10bhi/DocuMind.git
git push -u origin main
```

If `origin` already exists, inspect it with `git remote -v` instead of adding it again.

For subsequent updates:

```powershell
git status
git add README.md INSTALLATION.md
git commit -m "Add project setup documentation"
git push
```

## 15. Troubleshooting

### Python command not found

Check Python 3.12:

```powershell
py -3.12 --version
```

### Libraries are missing in VS Code

Confirm the selected interpreter is the project's `.venv`, activate the environment, and reinstall the required package.

### Tesseract is not recognized

Verify the executable exists, check the Windows PATH entry, and restart VS Code.

### Notebook uses the wrong Python environment

Use the notebook's kernel selector and choose the project's `.venv` environment or **Python (DocuMind)**.

### Git refuses to push

Check the configured remote and branch:

```powershell
git remote -v
git branch
git status
```

Follow GitHub's authentication prompts if authentication is required.

## 16. Reproducibility Notes

This guide documents the initial Windows development setup. Package versions may change over time.

For reproducible installations, maintain a dependency lock or pinned requirements file once the project dependencies have stabilized.

Do not commit the `.venv` folder. It is machine-specific and can be recreated using the instructions above.

---

**Next development milestone:** Run the first practical OCR experiment using a sample image and verify that the recognized text matches the source image.
