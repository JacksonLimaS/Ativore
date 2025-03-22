import fitz  # PyMuPDF

def pdf_to_jpg_pymupdf(pdf_path, output_path, zoom=2):
    """
    Converte cada página de um PDF em uma imagem JPG usando PyMuPDF.

    Args:
        pdf_path (str): Caminho para o arquivo PDF de entrada.
        output_path (str): Caminho base para salvar as imagens JPG (ex: 'imagem_pagina').
        zoom (int): Fator de zoom para aumentar a resolução da imagem (opcional).
    """
    try:
        pdf_document = fitz.open(pdf_path)
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            
            # Aumenta a resolução da imagem
            mat = fitz.Matrix(zoom, zoom)
            
            pix = page.get_pixmap(matrix=mat)
            
            output_file = f"{output_path}_{page_number + 1}.jpg"
            pix.save(output_file)
        pdf_document.close()
        print("PDF convertido para JPG com sucesso usando PyMuPDF!")
    except Exception as e:
        print(f"Erro ao converter PDF para JPG usando PyMuPDF: {e}")

# Exemplo de uso:
pdf_to_jpg_pymupdf("C:/Users/OTY8513/Downloads/ATIVORE - Automação dos reports/31-12-2024 (B) D2F BVI Ltd/BalanceSheet.pdf", "C:/Users/OTY8513/Downloads/ATIVORE - Automação dos reports/pagina", zoom=2)