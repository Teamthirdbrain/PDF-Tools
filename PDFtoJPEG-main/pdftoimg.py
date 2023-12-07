import fitz
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Open file manager to select PDF file
root = tk.Tk()
root.withdraw()
pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Open the PDF file
pdf_file = fitz.open(pdf_path)

# Iterate over each page in the PDF and save as JPEG
for page_number in range(len(pdf_file)):
    page = pdf_file[page_number]
    pix = page.get_pixmap()
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Ask user for file name before saving
    save_name = filedialog.asksaveasfilename(
        initialfile=f"page_{page_number + 1}.jpeg",
        defaultextension=".jpeg",
        filetypes=[("JPEG Files", "*.jpeg")],
    )
    
    image.save(save_name, 'JPEG')

# Close the PDF file
pdf_file.close()
