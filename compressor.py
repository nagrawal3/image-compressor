import os
from PIL import Image

def compress_jpg_to_pdf(input_jpg, output_pdf, max_size_bytes=1048576):
    min_quality = 10
    max_quality = 95
    quality = max_quality
    step = 5
    temp_jpg = "temp.jpg"
    
    # Open image
    img = Image.open(input_jpg).convert("RGB")
    
    while quality >= min_quality:
        # Save compressed JPG to temporary file
        img.save(temp_jpg, "JPEG", quality=quality)
        
        # Create PDF from compressed image
        compressed_img = Image.open(temp_jpg)
        compressed_img.save(output_pdf, "PDF", resolution=100.0)
        
        size = os.path.getsize(output_pdf)
        if size <= max_size_bytes:
            print(f"Success: PDF file size is {size/1024:.2f} KB at quality={quality}")
            os.remove(temp_jpg)
            return True
        quality -= step

    print("Failed: Could not compress to target size")
    os.remove(temp_jpg)
    return False

# Example usage:
compress_jpg_to_pdf("Aarush_OCI_Parental_Authorization.jpg", "output.pdf", max_size_bytes=1048576)
