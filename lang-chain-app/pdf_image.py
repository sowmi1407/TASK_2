from pdf2image import convert_from_path
from pathlib import Path

def save_pdf_pages_as_images(pdf_path, output_dir):
    
    pages = convert_from_path(pdf_path, dpi=300)
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, page in enumerate(pages):
        image_filename = output_dir / f"page{i+1}.png"
        page.save(image_filename, "PNG")
        print(f"Saved: {image_filename}")

if __name__ == "__main__":
    
    pdf_file = "task2_images.pdf"
    
    output_folder = "."
    
    save_pdf_pages_as_images(pdf_file, output_folder)