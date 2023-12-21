import PyPDF2

def extract_pages(input_path, output_path, pages_to_extract):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Crée un nouveau writer PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Ajoute les pages spécifiées
        for page_number in pages_to_extract:
            # Les pages sont 0-indexées
            pdf_writer.add_page(pdf_reader.pages[page_number - 1])

        # Écrit le nouveau PDF
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Exemple d'utilisation : extrait les pages 2 et 17 du fichier dossierStageTFE2023-24.pdf et crée un nouveau fichier document_chrh.pdf
extract_pages(r'C:\Users\josue\Documents\ECOLE\Stage\dossierStageTFE2023-24.pdf', 'document_chrh.pdf', [2, 17])
