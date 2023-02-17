import os
import PyPDF2


def split_pdf(input_pdf_path, output_dir):
    # Open the input PDF
    input_pdf = open(input_pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(input_pdf)

    # Get the total number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Split the PDF into 10-page chunks
    for i in range(0, num_pages, 10):
        # Create a new PDF writer
        pdf_writer = PyPDF2.PdfWriter()

        # Add 10 pages to the new PDF
        for j in range(i, min(i+10, num_pages)):
            pdf_writer.add_page(pdf_reader.pages[j])

        # Save the new PDF to a file
        output_path = os.path.join(output_dir, f'{i+1}-{i+10}.pdf')
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    # Close the input PDF
    input_pdf.close()


split_pdf("Epstein-Docs.pdf", "pages")
