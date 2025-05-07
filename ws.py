from bs4 import BeautifulSoup
import csv

def scrap_ioa(input_file, companies):
    with open(input_file, 'r', encoding="utf-8") as file1:
        content = file1.read()

        soup = BeautifulSoup(content, 'lxml')
        company_divs = soup.find_all('div', class_='basicInfo')

        for div in company_divs:
            span_name = div.find('span', itemprop='name')
            span_address = div.find('span', itemprop='streetAddress')
            span_postal_code = div.find('span', itemprop='postalCode')
            span_addressLocality = div.find('span', itemprop='addressLocality')
            span_region = div.find('span', itemprop='addressRegion')
            phones = div.find_all('span', itemprop='telephone')
            phone_numbers = [phone.get_text(strip=True) for phone in phones]
            span_phones = ', '.join(phone_numbers)
            span_url_tag = div.find('a', itemprop='url')
            span_url = span_url_tag['href'] if span_url_tag and 'href' in span_url_tag.attrs else ''

            if span_region and span_region.get_text(strip=True) != 'Ιωαννίνων':
                continue

            # Collect data into a list
            span = [
                span_name.get_text(strip=True) if span_name else '',
                span_address.get_text(strip=True) if span_address else '',
                span_postal_code.get_text(strip=True) if span_postal_code else '',
                span_addressLocality.get_text(strip=True) if span_addressLocality else '',
                span_region.get_text(strip=True) if span_region else '',
                span_phones,
                span_url
            ]

            if span not in companies:
                companies.append(span)

# Collect all data into the companies array
companies = []
scrap_ioa('e1.html', companies)
scrap_ioa('e2.html', companies)
scrap_ioa('e3.html', companies)
scrap_ioa('e4.html', companies)
scrap_ioa('e5.html', companies)
scrap_ioa('e6.html', companies)
scrap_ioa('e7.html', companies)
scrap_ioa('e8.html', companies)
scrap_ioa('e9.html', companies)
scrap_ioa('e10.html', companies)

# Write all data from companies to the output file
with open('output.csv', 'w', newline='', encoding="utf-8-sig") as file2:
    csv_writer = csv.writer(file2)
    # Write the header row
    csv_writer.writerow(['Name', 'Address', 'Postal Code', 'Locality', 'Region', 'Phones', 'Website'])
    # Write all rows from the companies array
    csv_writer.writerows(companies)

print("Data written to output.csv")