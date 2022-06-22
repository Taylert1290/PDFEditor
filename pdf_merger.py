import PyPDF2
import os
from PIL import Image

class PDFEditor:

    def exclude_page(self, input_file, output_file, exclusion_pages):
        pdfWriter = PyPDF2.PdfFileWriter()
        pdf = open(input_file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)
        for pageNum in range(pdfReader.numPages):
            if pageNum not in exclusion_pages:
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        pdfOutputFile = open(output_file, 'wb')
        pdfWriter.write(pdfOutputFile)

    def split_page(self, input_file, output_file, page_num):
        """
        :param page_num: index of page to split off
        :return:
        """
        pdfWriter = PyPDF2.PdfFileWriter()
        pdf = open(input_file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)
        for pageNum in range(pdfReader.numPages):
            if pageNum == page_num:
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        pdfOutputFile = open(output_file, 'wb')
        pdfWriter.write(pdfOutputFile)



    def merge(self, input_directory, output_file):
        files = sorted(os.listdir(input_directory))
        pdfWriter = PyPDF2.PdfFileWriter()
        for file in files:
            pdf = open(input_directory+file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdf)
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        pdfOutputFile = open(output_file, 'wb')
        pdfWriter.write(pdfOutputFile)
        print('done')

class Image2PDF:

    def convert_image(self, input_file, output_file):
        input_iamge = Image.open(input_file)
        output = input_iamge.convert('RGB')
        output.save(output_file)
