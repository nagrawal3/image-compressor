import subprocess
import os

def compress_pdf(input_path, output_path, target_size=10_000_000):
    gs_compression_levels = ['/ebook', '/screen', '/printer', '/prepress']
    for level in gs_compression_levels:
        subprocess.run([
            'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
            f'-dPDFSETTINGS={level}', '-dNOPAUSE', '-dQUIET', '-dBATCH',
            f'-sOutputFile={output_path}', input_path
        ], check=True)
        if os.path.getsize(output_path) <= target_size:
            print(f'Success: Compressed {output_path} to {os.path.getsize(output_path)} bytes ({level})')
            return True
    print('Failed to compress under 1MB. Try reducing content or splitting PDF.')
    return False

# Example usage:
# compress_pdf('input.pdf', 'compressed.pdf')
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 compress_pdf.py input.pdf output.pdf")
    else:
        compress_pdf(sys.argv[1], sys.argv[2])
