# Python Multiple File Downloader

This is a Python script that allows you to download PDF files from a list of URLs provided in a CSV file. It utilizes the `requests` library for making HTTP requests, `BeautifulSoup` for HTML parsing, and the `csv` library for reading CSV files.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)

## Usage

1. Clone this repository to your local machine.

   ```sh
   git clone https://github.com/devTarak/Python-Multiple-File-Downloader.git
   cd Python-Multiple-File-Downloader
   ```

2. Create a virtual environment (optional but recommended).

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies.

   ```sh
   pip install -r requirements.txt
   ```

4. Prepare your CSV file:

   Create a CSV file named `source-file-list.csv` with a single column containing the URLs you want to download PDFs from.

   Example `source-file-list.csv`:
   ```
   java-tutorials-for-beginners-1/
   java-tutorials-for-beginners-2/
   java-tutorials-for-beginners-3/
   java-tutorials-for-beginners-4/
   java-tutorials-for-beginners-5/
   ```

5. Edit the script:

   Replace the placeholder base URL in the script with your actual base URL.

6. Run the script:

   ```sh
   python main.py
   ```

   The script will create a folder named `downloaded_pdfs` (if it doesn't exist) and download the PDF files from the URLs in the CSV file into that folder.

## Notes

- Make sure the URLs in your CSV file are correctly formatted and point to the pages containing the PDF links.
- The script assumes that the PDF links end with `.pdf` and that they can be directly accessed using their URLs.

## License

This project is licensed under the [MIT License](LICENSE).
## Developer
This Script is Developed by [Tarak Rahman](https://devtarak.github.io/)
