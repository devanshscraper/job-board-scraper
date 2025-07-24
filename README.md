# LinkedIn Job Scraper

This project is a production-ready LinkedIn job scraper built using Selenium. It extracts job listings directly from LinkedIn based on search filters and user inputs.

## 🔍 Features

- ✅ Scroll automation for loading dynamic content
- ✅ Handles pagination with "Next" button
- ✅ Extracts:
  - Company Name
  - Job Title
  - Job Description
- ✅ Saves data to a `.txt` file
- ✅ Error handling and retry logic
- ✅ Manual login for first run (LinkedIn may ask for verification in later sessions)

## 🧰 Tech Stack

- Python
- Selenium
- Pickle
- Random
- Time

## 📁 Output Format

The extracted data is saved in plain text (`scraped_data.txt`). Each job listing includes the company name, job title, and full job description.

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/your-username/linkedin-job-scraper.git
cd linkedin-job-scraper
