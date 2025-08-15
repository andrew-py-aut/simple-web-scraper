# Simple Web Scraper

A simple Python script to scrape quotes from `http://quotes.toscrape.com` and save them into a CSV file. This project is for demonstration purposes, showing a clean and basic web scraping setup.

## Features

- Scrapes quote text, author, and tags.
- Saves the data to a CSV file (`quotes.csv`).
- Clean, commented, and structured code.
- Basic logging for monitoring the process.

## Requirements

- Python 3.6+
- The libraries listed in `requirements.txt`.

## How to Set Up and Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/andrew-py-aut/simple-web-scraper.git
    cd simple-web-scraper
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS and Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the scraper:**
    ```bash
    python scraper.py
    ```

## Output

After running the script, a new file named `quotes.csv` will be created in the project directory with the following columns:

- `text`
- `author`
- `tags`