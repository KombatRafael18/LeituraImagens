# ocr-catalogo

## Passo 1: Instale o pytesseract e o pillow
pip install pytesseract
pip install Pillow

## Passo 2: Instale o Tesseract-OCR (programa externo)
1. Baixe o instalador aqui: https://github.com/UB-Mannheim/tesseract/wiki
2. Instale e anote o caminho, geralmente algo como: C:\Program Files\Tesseract-OCR\tesseract.exe
3. No seu código Python, adicione: pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"