# PDF-Tools
This repository contains three pdf tools 
# 1)PDFtoJPEG
PDF to JPEG Converter
This Python script allows users to convert each page of a PDF file to a JPEG image. It utilizes the fitz module from the PyMuPDF library to handle the PDF file and the PIL (Python Imaging Library) library to save the PDF pages as JPEG images.

# Features:
-Select a PDF file using the file manager dialog.
-Iterate over each page in the PDF and convert it to a JPEG image.
-Prompt the user to specify a file name and location for each image.
-Save the converted JPEG images with the chosen file names and locations.

# Prerequisites:
-PyMuPDF library: Install using pip install PyMuPDF.
-Pillow library: Install using pip install Pillow.

# Usage:
-Run the script using Python.
-The file manager dialog will open for you to select a PDF file.
-Each page of the PDF will be converted to a JPEG image.
-For each converted image, the script will prompt you to provide a file name and location.
-After selecting a file name and location for each image, the JPEG files will be saved accordingly.
![image](https://github.com/GuhanAein/PDFtoJPEG/assets/102289063/2aef4968-53ce-498c-8a05-55c1fc97355a)
![image](https://github.com/GuhanAein/PDFtoJPEG/assets/102289063/ee4620d2-be30-43ee-bdcb-28517a0bb89b)
![image](https://github.com/GuhanAein/PDFtoJPEG/assets/102289063/2ec9f60d-d768-49f0-8c12-0d2726ea7f0b)

now the file will be saved


#Note:
Make sure to have both PyMuPDF and Pillow installed before running the script.
The converted images will be saved with the chosen file names and locations specified by the user.


# 2)PDF Splitter

A Python script that allows you to split a PDF file into multiple smaller PDF files based on page ranges.

## Description

This Python script uses the PyPDF2 library to split a given PDF file into multiple smaller PDFs. You can specify the number of splits you want and provide the starting and ending page numbers for each split. The script then creates separate PDF files for each split, allowing you to efficiently extract specific sections of a larger PDF document.

## Features

- Interactive user interface using `tkinter` for selecting the input PDF file and output directory.
- Specify the number of splits and the page ranges for each split.
- Customizable output file names for each split.

## Getting Started

1. Make sure you have Python installed on your system.
2. Clone this repository: `git clone https://github.com/your-username/pdf-splitter.git`
3. Navigate to the project directory: `cd pdf-splitter`
4. Install required dependencies: `pip install PyPDF2`
5. Run the script: `python pdfsplit.py`

## Usage

1. Run the script and follow the prompts to select the input PDF file.
2. Specify the output directory where the split PDF files will be saved.
3. Provide the number of splits you want to create.
4. For each split, enter the starting and ending page numbers.
5. Enter a custom name for each split PDF.


![Screenshot from 2023-08-08 22-08-40](https://github.com/GuhanAein/PDF_Splitter/assets/102289063/9239e59c-6183-4cbc-9267-d2fa360a9aa4)
![Screenshot from 2023-08-08 22-25-47](https://github.com/GuhanAein/PDF_Splitter/assets/102289063/2736ec36-3d96-4fe1-ab85-d9f1c989d920)
![Screenshot from 2023-08-08 22-26-09](https://github.com/GuhanAein/PDF_Splitter/assets/102289063/77c0003d-2a5e-446a-8783-59df36b3b2f8)
![Screenshot from 2023-08-08 22-28-23](https://github.com/GuhanAein/PDF_Splitter/assets/102289063/7d97da2f-8df2-4441-ab4b-f6e2f280844b)
![Screenshot from 2023-08-08 22-28-52](https://github.com/GuhanAein/PDF_Splitter/assets/102289063/519ab41b-c811-4a30-935e-46e852bfd775)



The resulting split PDF files will be saved in the chosen output directory.

# 3)PDFMERGER
Python  code for merging the pdf

Run the code and there will be a opening of dialog box in the window select the pdf files and run it will ask where to save and the name of the merged pdf.

