import os
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

SEARCH_URLS = {
    "Europe": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer&location=Europe&f_TPR=r86400&geoId=91000000",
    "Tunisia": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer&location=Tunisia&f_TPR=r86400&geoId=104219930",
    "Qatar": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer&location=Qatar&f_TPR=r86400&geoId=101732936",
    "UAE": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer&location=United%20Arab%20Emirates&f_TPR=r86400&geoId=104305776",
    "Saudi Arabia": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer&location=Saudi%20Arabia&f_TPR=r86400&geoId=100459316",
}

def scrape_jobs(url):
    """Scrapes job listings from a given LinkedIn search URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="base-card")
    
    jobs = []
    for card in job_cards:
        try:
            title_tag = card.find("h3", class_="base-search-card__title")
            company_tag = card.find("h4", class_="base-search-card__subtitle")
            location_tag = card.find("span", class_="job-search-card__location")
            link_tag = card.find("a", class_="base-card__full-link")
            
            clean_link = ""
            if link_tag and 'href' in link_tag.attrs:
                match = re.search(r"(https:\/\/www\.linkedin\.com\/jobs\/view\/\d+)", link_tag['href'])
                if match:
                    clean_link = match.group(1)

            if title_tag and company_tag and location_tag and clean_link:
                job = {
                    "title": title_tag.get_text(strip=True),
                    "company": company_tag.get_text(strip=True),
                    "location": location_tag.get_text(strip=True),
                    "link": clean_link
                }
                jobs.append(job)
        except Exception as e:
            print(f"Error parsing a job card: {e}")
            continue
            
    return jobs

def generate_html(all_jobs):
    """Generates an HTML string for the email body."""
    if not all_jobs:
        return "<p>No new junior developer jobs found in the last 24 hours.</p>"

    html = "<html><body>"
    html += f"<h1>Junior Developer Job Digest - {datetime.now().strftime('%Y-%m-%d')}</h1>"
    
    for region, jobs in all_jobs.items():
        if jobs:
            html += f"<h2>{region} ({len(jobs)} new)</h2>"
            html += "<ul>"
            for job in jobs:
                html += (
                    f"<li>"
                    f"<strong>{job['title']}</strong> at {job['company']} - <em>{job['location']}</em><br/>"
                    f"<a href='{job['link']}'>Apply Here</a>"
                    f"</li>"
                )
            html += "</ul>"
            html += "<hr/>"
            
    html += "</body></html>"
    return html

if __name__ == "__main__":
    all_new_jobs = {}
    print("Starting job scraping process...")
    for region, url in SEARCH_URLS.items():
        print(f"Scraping jobs for {region}...")
        jobs_found = scrape_jobs(url)
        if jobs_found:
            all_new_jobs[region] = jobs_found
        print(f"Found {len(jobs_found)} jobs for {region}.")

    print("Generating email content...")
    email_body = generate_html(all_new_jobs)
    
    with open("job_offers.html", "w", encoding="utf-8") as f:
        f.write(email_body)
    
    print("Scraping complete. 'job_offers.html' has been created.")