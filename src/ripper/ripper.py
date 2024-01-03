import PyPDF2


class PDFSplitter:
    def __init__(self, input_pdf_path, output_pdf_base_path):
        self.input_pdf_path = input_pdf_path
        self.output_pdf_base_path = output_pdf_base_path

    def split(self):
        pdf_file = open(self.input_pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        for page in range(total_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page])

            output_pdf_path = f"{self.output_pdf_base_path}_page_{page + 1}.pdf"
            with open(output_pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

        pdf_file.close()
