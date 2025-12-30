import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrap_jobs(keyword):
    page = 0
    jobs_data = []

    while True:
        url = f"https://wuzzuf.net/search/jobs/?a=hpb&q={keyword}&start={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        # Titles
        titles = soup.find_all("h2", {'class': 'css-m604qf'})
        if not titles:
            break

        titles_lst = [title.a.text.strip() for title in titles]
        links = ['https://wuzzuf.net' + title.a['href'] for title in titles]

        # Occupations
        occupations = soup.find_all("div", {'class': 'css-1lh32fc'})
        occupations_lst = [occ.text.strip() for occ in occupations]

        # Companies
        companies = soup.find_all("a", {'class': 'css-17s97q8'})
        companies_lst = [comp.text.strip() for comp in companies]

        # Specs
        specs = soup.find_all("div", {'class': 'css-y4udm8'})
        specs_lst = [spec.text.strip() for spec in specs]

        # Company Location
        locations = soup.find_all("span", {'class': 'css-5wys0k'})
        locations_lst = [loc.text.strip() for loc in locations]

        # List of dicts
        for i in range(len(titles_lst)):
            jobs_data.append({
                'Keyword': keyword,
                'Title': titles_lst[i],
                'Link': links[i],
                'Occupation': occupations_lst[i] if i < len(occupations_lst) else None,
                'Company': companies_lst[i] if i < len(companies_lst) else None,
                'Location': locations_lst[i] if i < len(locations_lst) else None,
                'Specs': specs_lst[i] if i < len(specs_lst) else None
            })

        page += 1
        time.sleep(1) 

    return jobs_data

def main():
    keywords = ["machine learning", "data analysis", "data science", "business intelligence"]
    all_jobs = []

    for keyword in keywords:
        print(f"Scraping jobs for: {keyword}")
        jobs = scrap_jobs(keyword.replace(" ", "+"))
        all_jobs.extend(jobs)

    df = pd.DataFrame(all_jobs)
    df.to_csv("all_jobs.csv", index=False, encoding="utf-8-sig")
    print("All jobs scraped successfully!")

if __name__ == "main":
    main()