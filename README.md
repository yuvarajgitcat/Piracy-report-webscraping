
# **Piracy and Armed Robbery Report Scraping Tool 🛳️**

This project automates the extraction of piracy and armed robbery incident reports from the International Maritime Bureau (IMB) website. 
The extracted data includes incident dates, types of attacks, vessel details, and geographical coordinates, which is stored in a structured 
format (Excel/CSV) for further analysis.

## **Features**
- Extracts incident reports with key details:
  - **Incident Date**
  - **Attack Type**
  - **Vessel Type**
  - **Location Details** and **Coordinates**
  - **Incident Narration**
- Fetches data dynamically by scraping report URLs from the main page.
- Outputs the scraped data as an Excel file for analysis.

## **Technologies Used**
- **Python**
- **BeautifulSoup** – for web scraping
- **Requests** – for making HTTP requests
- **Pandas** – for data manipulation and Excel export

## **Setup and Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies**
   Make sure you have Python installed. Then, install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

3. **Run the Script**
   Navigate to the folder containing the script and run:
   ```bash
   python scraping.py
   ```

## **How it Works**

1. **Access the Home Page:**
   The script starts by scraping the homepage of the IMB's live piracy reports.

2. **Extract Report URLs:**
   It dynamically extracts the links to detailed incident reports.

3. **Scrape Incident Details:**
   Each report is accessed, and relevant details like **location**, **coordinates**, and **narration** are extracted.

4. **Save Data:**
   The data is saved into an Excel file (`piracy_incident_report.xlsx`) for further analysis.

## **Sample Data Extracted**
| Date       | Attack Type    | Vessel Type | Location        | Coordinates          | Narration                               |
|------------|----------------|-------------|----------------|---------------------|----------------------------------------|
| 2024-10-26 | Armed Robbery  | Tanker      | Gulf of Guinea | N13°45’52", E120°57’42" | Pirates boarded the vessel and stole cargo. |

## **Usage Scenarios**
- **Maritime Security Analysis:**  
  Researchers and analysts can use the data to identify patterns in piracy incidents.
- **Risk Assessment:**
  Shipping companies can assess risks along specific routes using incident reports.

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## **License**
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## **Contact**
For any inquiries, reach out to:
**yuvaraj** – yuvarajr0326@gmail.com  
GitHub:yuvarajgitcat(https://github.com/yuvarajgitcat)
