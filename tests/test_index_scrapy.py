import scrapy
from scrapy.http import HtmlResponse
import os

class IndexSpider(scrapy.Spider):
    name = "index_spider"
    
    def start_requests(self):
        # Path to index.html
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'index.html'))
        file_url = f'file:///{file_path.replace(os.sep, "/")}'
        yield scrapy.Request(url=file_url, callback=self.parse)

    def parse(self, response):
        self.logger.info(f"Visited {response.url}")
        
        # Verify title
        title = response.css('title::text').get()
        assert "Note Creator" in title
        self.logger.info(f"Title: {title}")

        # Verify main heading
        h1 = response.css('h1::text').get()
        assert "Note Creator" in h1
        self.logger.info(f"H1: {h1}")

        # Verify form exists
        form_h3 = response.xpath('//h3[contains(text(), "Create a New Note")]').get()
        assert form_h3 is not None

        # Verify input fields
        assert response.css('input#title').get() is not None
        assert response.css('textarea#content').get() is not None

        # Verify buttons
        create_btn = response.xpath('//button[contains(text(), "Create Note")]').get()
        assert create_btn is not None
        assert 'createNote()' in create_btn

        delete_all_btn = response.xpath('//button[contains(text(), "Delete All Notes")]').get()
        assert delete_all_btn is not None
        assert 'deleteAllNotes()' in delete_all_btn

        # Verify notes container
        assert response.css('div#notes-container').get() is not None
        assert response.css('ul#notes-list').get() is not None
        
        self.logger.info("All scrap tests passed!")
