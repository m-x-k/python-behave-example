from selenium import webdriver

def before_scenario(context, scenario):
        context.browser =  webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')


#Just copied it from the exisiting library
def after_step(context, step):
    # on step failure
    if step.status == "failed":
        # creates a screenshot for each step-failure and behave is called with
        #  the parameter -D screenshot
        if 'screenshot' in context.config.userdata:
            image = context.browser.get_screenshot_as_png()
            context.embed('image/jpg', image)

        # enables the debugger for each step-failure and behave is called with
        #  the parameter -D debug_on_error
        if 'debug_on_error' in context.config.userdata:
            import ipdb
            ipdb.post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    #add a script to
    context.browser.quit()