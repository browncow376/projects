import scrapy

class RedditSpider(scrapy.Spider):
    name = "reddit"
    start_urls = ["https://www.reddit.com/r/pics/"]

    def parse(self, response):
        links = response.xpath("//img/@src")
        html = ""

        for link in links:
            url = link.get()

            if any(extension in url for extension in
            [".jpg", ".gif", ".png"]):
                html += """<a href="{url}"
                target="_blank">
                <img src="{url}" height="50%"
                width="33%"
                <a/>""".format(url=url)

                with open("pics.html", "a") as page:
                    page.write(html)
                    page.close





    

