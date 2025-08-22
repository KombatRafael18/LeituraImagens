from PIL import Image
import pytesseract

# Caminho do executável do Tesseract (ajuste se necessário)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imagem = Image.open("./imagens/005.14057.jpg")
texto = pytesseract.image_to_string(imagem, lang="eng")

print("Texto extraído:", texto)
