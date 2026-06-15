import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text


def find_career_page(company_url):
    html = get_html(company_url)
    soup = BeautifulSoup(html, "html.parser")

    career_keywords = [
        "careers",
        "career",
        "jobs",
        "join us",
        "work with us",
        "open positions",
        "opportunities",
    ]

    for link in soup.find_all("a", href=True):
        text = link.get_text(" ", strip=True).lower()
        href = link["href"].lower()

        for keyword in career_keywords:
            if keyword in text or keyword in href:
                return urljoin(company_url, link["href"])

    return None


def find_open_position(career_url):
    html = get_html(career_url)
    soup = BeautifulSoup(html, "html.parser")

    job_keywords = [
        "engineer",
        "analyst",
        "developer",
        "manager",
        "consultant",
        "data",
        "software",
        "product",
    ]

    for link in soup.find_all("a", href=True):
        text = link.get_text(" ", strip=True).lower()
        href = link["href"].lower()

        for keyword in job_keywords:
            if keyword in text or keyword in href:
                return urljoin(career_url, link["href"])

    return None


def run_job_source_agent():
    print("===================================")
    print(" JOBNOVA AI JOB SOURCE AGENT DEMO")
    print("===================================")

    company_name = input("\nEnter company name: ")
    company_url = input("Enter company website URL: ")

    print("\nSearching company website...")
    career_url = find_career_page(company_url)

    if not career_url:
        print("\nCareer page not found automatically.")
        career_url = input("Paste career page URL manually: ")

    print("Career page found:", career_url)

    print("\nSearching for one open position...")
    open_position_url = find_open_position(career_url)

    if not open_position_url:
        print("\nOpen position URL not found automatically.")
        open_position_url = input("Paste one open position URL manually: ")

    print("\n===================================")
    print(" FINAL RESULT")
    print("===================================")
    print("Company name:", company_name)
    print("Career page URL:", career_url)
    print("Open position URL:", open_position_url)


if __name__ == "__main__":
    run_job_source_agent()