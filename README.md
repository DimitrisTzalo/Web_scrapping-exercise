# 🏢 Company Data Scraper for Ioannina Region

This Python script extracts structured business information from multiple HTML files and consolidates it into a CSV file. The focus is on companies located in the **Ioannina** region (`Ιωαννίνων`) in Greece and are recognized by Chamber of Commerce of Ioannina.

## 📄 Features

- Parses HTML files using BeautifulSoup
- Filters businesses based on region
- Extracts:
  - Company name
  - Address
  - Postal code
  - Locality
  - Phone numbers
  - Website URL
- Outputs results to `output.csv`

## 🧰 Requirements

- Python 3.2
- `beautifulsoup4`
- `lxml`

Install dependencies using pip:

```bash
pip install beautifulsoup4 lxml
```

## 🚀 Usage

The website we are using is [xo.gr](https://www.xo.gr/).
For every input HTML file we use a keyword that can find the companies and 
the keywrods we are using are:
`1. πληροφορική
 2. εταιρείες πληροφορικής
 3. υπηρεσίες πληροφορικής
 4. τεχνική υποστήριξη
 5. κατασκευή ιστοσελίδων
 6. web design
 7. προγραμματισμός
 8. λογισμικό
 9. υπολογιστές
 10. digital marketing`

For each keyword we create the appropriate input file

  
Place your HTML files (`e1.html`, `e2.html`, ..., `e10.html`) in the same directory as the script, then run:

```bash
python ws.py
```

Output will be saved as `output.csv`.

## 📁 Output Format

The CSV file will contain the following columns:

- Name
- Address
- Postal Code
- Locality
- Region
- Phones (comma-separated)
- Website

## 📌 Notes


- Only entries from the `Ιωαννίνων` region are included.
- Duplicate entries are filtered out.

