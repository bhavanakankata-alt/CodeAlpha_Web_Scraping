# CodeAlpha Web Scraping

## Project Overview
This project is part of the CodeAlpha Data Analytics Internship.

The project demonstrates web scraping using Python to collect book information from a public practice website and save the collected data as a CSV dataset.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected
The scraper collects:
- Book Title
- Price
- Availability
- Rating
- Product URL

## Output
The scraped data is saved in:

`books_data.csv`

The Python source code is available in:

`web_scraping.py`

## How It Works
1. Sends requests to the website.
2. Reads the HTML content.
3. Uses BeautifulSoup to extract book information.
4. Stores the extracted data in a Pandas DataFrame.
5. Saves the data as a CSV file.

## Project Files
- `web_scraping.py` — Python web scraping code
- `books_data.csv` — scraped book dataset
- `README.md` — project documentation
