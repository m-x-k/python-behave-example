def launch_website(context):
    driver = context.browser
    driver.get("http://www.bbc.co.uk")
    assert "BBC" in driver.title


def click_on_link(context):
    driver = context.browser
    link = driver.find_element_by_link_text('News')
    link.click()

def check_page_title(context):
    driver = context.browser
    assert "BBC News" in driver.title