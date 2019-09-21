from helper import get_html


class JobDescriptionScraper:
    def __init__(self, url):
        self.html = get_html(url)

    def get_job_description(self):
        return self.html.find('div', id="jobDescriptionText").get_text()

    def get_job_company(self):
        return next(self.html.find('div', class_='jobsearch-JobInfoHeader-subtitle').stripped_strings)
