from seleniumbase import BaseCase


class GoogleSearchPage(BaseCase):
    TEXT_AREA = "//textarea[@id='APjFqb']"
    NEWS_TAB = "//a[normalize-space()='News']"
    SEARCH_BUTTON = "//button[@aria-label='Google Search']"

    def fill_text_area(self, text):
        self.type(self.TEXT_AREA, text)

    def wait_for_page_to_load(self):
        self.is_element_present(self.NEWS_TAB)

    def click_news_tab(self):
        self.click(self.NEWS_TAB)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def click_link_by_index_position(self, index):
        # NEWS_LINK = "(//div[@role='heading'])[" + index + "]"
        NEWS_LINK = "(//div[contains(@aria-level,'3')])[" + index + "]"
        self.click(NEWS_LINK)

    def click_suggestion(self, search_term):
        SUGGEST = "//span[normalize-space()='" + search_term + "']"
        self.click(SUGGEST)


