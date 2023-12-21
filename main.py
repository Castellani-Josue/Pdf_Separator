import PyPDF2

def extract_pages(input_path, output_path, pages_to_extract):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Crée un nouveau writer PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Ajoute les pages spécifiées
        for page_number in pages_to_extract:
            # Les pages sont 0-indexées => 1ere page à indice 0 et 2eme à 1 et ainsi de suite
            pdf_writer.add_page(pdf_reader.pages[page_number - 1]) # mais ds notre cas c 1-indexéees donc on f -1

        # Écrit le nouveau PDF
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Exemple d'utilisation : extrait les pages 1 et 2du fichier Énoncé.pdf et crée un nouveau fichier document_exmpl.pdf
extract_pages(r'C:\Users\josue\Desktop\Dev_Mobile2023_2024\Énoncé.pdf', 'document_exmpl.pdf', [1,2])
