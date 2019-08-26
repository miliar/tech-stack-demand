from helper import get_html


class JobDescriptionScraper:
    def __init__(self, url):
        self.url = url

    def get_job_description(self):
        html = get_html(self.url)
        return html.find('div', id="jobDescriptionText").get_text()
