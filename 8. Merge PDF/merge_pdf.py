import os
from tkinter import Tk, Button, Label, filedialog
from PyPDF2 import PdfWriter, PdfReader

def merge_pdfs(file_paths, output_path):
    pdf_writer = PdfWriter()

    for file_path in file_paths:
        pdf_reader = PdfReader(file_path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)

    print("PDF files merged successfully.")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        selected_files.append(file_path)
        status_label.config(text=f"Selected: {', '.join(selected_files)}")
        merge_button.config(state="normal")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        global output_folder
        output_folder = folder_path
        folder_label.config(text=f"Selected folder: {output_folder}")
        merge_button.config(state="normal")

def merge_files():
    if selected_files:
        output_file_path = os.path.join(output_folder, "merged_output.pdf")
        merge_pdfs(selected_files, output_file_path)
        status_label.config(text="PDF files merged successfully.")
    else:
        status_label.config(text="No PDF files selected.")

# Create the main window
root = Tk()
root.title("PDF Merger")

# Create a label
info_label = Label(root, text="Select PDF files one by one:")
info_label.pack(pady=10)

# Initialize list to store selected file paths
selected_files = []

# Create a button to select file
select_button = Button(root, text="Select File", command=select_file)
select_button.pack(pady=5)

# Create a label to display selected file paths
status_label = Label(root, text="")
status_label.pack(pady=5)

# Create a button to select output folder
folder_button = Button(root, text="Select Output Folder", command=select_folder)
folder_button.pack(pady=5)

# Create a label to display selected output folder
folder_label = Label(root, text="")
folder_label.pack(pady=5)

# Create a button to merge files
merge_button = Button(root, text="Merge PDFs", command=merge_files, state="disabled")
merge_button.pack(pady=5)

# Run the main event loop
root.mainloop()
