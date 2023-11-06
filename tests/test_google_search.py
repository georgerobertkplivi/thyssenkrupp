from assertpy import assert_that

from pages.google import GoogleSearchPage
from tests.base_test import BaseTest


class GoogleTest(BaseTest, GoogleSearchPage):

    def test_search_thyssenkrupp(self):

        text = "thyssenkrupp"
        index_link = "4"

        self.wait_for_page_to_load()

        self.fill_text_area(text)

        self.click_suggestion(text)

        assert_that(self.is_element_present(self.NEWS_TAB)).is_true()

        self.click_news_tab()

        self.click_link_by_index_position(index_link)

        page_source = self.get_page_source()

        keyword_count = page_source.lower().count(text.lower())

        # Display the results
        print(f'The keyword "{text}" appears {keyword_count} times in the search results.')

