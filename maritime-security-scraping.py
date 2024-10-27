import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the ICC piracy report site
base_url = 'https://www.icc-ccs.org'
home_url = f'{base_url}/index.php/piracy-reporting-centre/live-piracy-report'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

# Function to extract data safely
def extract_data(soup, element_id):
    element = soup.find('div', id=element_id)
    return element.text if element else None

def extract_coordinates(soup):
    coord_div = soup.find('div', class_='coord')
    if coord_div:
        lat = coord_div.find('input', class_='latdms')['value'].strip()
        lng = coord_div.find('input', class_='lngdms')['value'].strip()
        return f"{lat}, {lng}"  # Combine latitude and longitude
    return None


# Send a GET request to the home page
response = requests.get(home_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all report links in divs with class "btn-group"
    report_links = [
        base_url + div.find('a', href=True)['href']
        for div in soup.find_all('div', class_='btn-group')
        if div.find('a', href=True)
    ]

    # List to store incident data
    incident_data = []

    # Loop through each report link and scrape data
    for report_url in report_links:
        report_response = requests.get(report_url, headers=headers)
        
        if report_response.status_code == 200:
            report_soup = BeautifulSoup(report_response.text, 'html.parser')

            # Collect data into a dictionary
            data = {
                'Date and Time Incident Received by PRC': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___date_time_inc_received_ro'),
                'Attack Number': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___attack_no_ro'),
                'Type of Attack': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___type_attack_ro'),
                'Type of Vessel': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___type_ro'),
                'Location Detail': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___location_detail_ro'),
                'Coordinates': extract_coordinates(report_soup),
                'Narrations': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___narrations_ro'),
                'Date of Incident': extract_data(report_soup, 'jos_fabrik_icc_ccs_piracymap2016___date_of_incident_ro'),
            }
            incident_data.append(data)

    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(incident_data)

    # Save the DataFrame to an Excel file
    df.to_excel('Apiracy_incident_report.xlsx', index=False)
    print("Data saved to piracy_incident_report.xlsx")

else:
    print(f"Failed to retrieve data from home page. Status code: {response.status_code}")
