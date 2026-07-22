import os
import re
import shutil
import requests
from bs4 import BeautifulSoup

# =====================================================================
# TOOL 1: FILE ORGANISER
# =====================================================================
def organize_jpg_files(source_folder, destination_folder):
    """Moves all .jpg files from a source folder to a destination folder."""
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"[+] Created directory: {destination_folder}")

    try:
        files = os.listdir(source_folder)
    except FileNotFoundError:
        print(f"[-] Error: Source folder '{source_folder}' does not exist.")
        return

    moved_count = 0
    for file_name in files:
        if file_name.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            
            shutil.move(source_path, destination_path)
            print(f"[->] Moved: {file_name}")
            moved_count += 1

    print(f"[✓] Task complete. Total files moved: {moved_count}\n")

# =====================================================================
# TOOL 2: EMAIL EXTRACTOR
# =====================================================================
def extract_emails(input_file, output_file):
    """Extracts unique email addresses from a text file and saves them."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"[-] Error: Input file '{input_file}' was not found.\n")
        return

    found_emails = re.findall(email_pattern, content)
    unique_emails = set(found_emails)

    with open(output_file, 'w', encoding='utf-8') as file:
        for email in unique_emails:
            file.write(email + '\n')

    print(f"[✓] Extraction complete. Found {len(unique_emails)} unique emails. Saved to {output_file}\n")

# =====================================================================
# TOOL 3: WEBPAGE TITLE SCRAPER
# =====================================================================
def scrape_page_title(url, output_file):
    """Scrapes the title of a webpage and saves it to a file."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        page_title = soup.title.string.strip() if soup.title else "No Title Found"

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"URL: {url}\n")
            file.write(f"Title: {page_title}\n")

        print(f"[✓] Scraping complete. Title saved: '{page_title}'\n")

    except requests.exceptions.RequestException as error:
        print(f"[-] Scraping error: {error}\n")

# =====================================================================
# MAIN MENU INTERFACE
# =====================================================================
def main():
    while True:
        print("=== PYTHON AUTOMATION TOOLKIT ===")
        print("1. Move .jpg files to a new folder")
        print("2. Extract emails from a text file")
        print("3. Scrape a website title")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        print("-" * 40)

        if choice == '1':
            src = input("Enter source folder path: ").strip()
            dst = input("Enter destination folder path: ").strip()
            organize_jpg_files(src, dst)
            
        elif choice == '2':
            infile = input("Enter input text file name/path: ").strip()
            outfile = input("Enter output file name to save emails: ").strip()
            extract_emails(infile, outfile)
            
        elif choice == '3':
            target_url = input("Enter website URL (e.g., https://example.com): ").strip()
            outfile = input("Enter output file name to save the title: ").strip()
            scrape_page_title(target_url, outfile)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("[-] Invalid choice. Please enter a number from 1 to 4.\n")

if __name__ == "__main__":
    main()