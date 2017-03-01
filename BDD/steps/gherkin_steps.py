from behave import *
import BDD.impl.test_implementation as impl


@Given('I visit the website www.bbc.co.uk')
def step_impl(context):
    impl.launch_website(context)


@When('I click on the news link')
def step_impl(context):
    impl.click_on_link(context)

@Then('the bbc news page is opened')
def step_impl(context):
    impl.check_page_title(context)