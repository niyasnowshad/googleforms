while True:
    from selenium import webdriver
    import random
    #selenium
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    # option.add_argument("--headless")
    # option.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path='chromedriver', options=option)
    #google forms link
    browser.get("https://forms.gle/ivPCEK9dW7k4K3Uf8")
    #boxes classnames
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    #name
    file1 = open('names.txt', 'r')
    lines = file1.readlines()
    for i in range(0,25):
        rand_line = random.randint(1,4500)
        x=lines[rand_line]
        textboxes[0].send_keys(x)
        print(x)
        break
    #multiple choice
    a = random.randint(0, 5)
    radiobuttons[a].click()
    b = random.randint(6, 11)
    radiobuttons[b].click()
    c = random.randint(12, 17)
    radiobuttons[c].click()
    d = random.randint(18, 23)
    radiobuttons[d].click()
    e = random.randint(24, 29)
    radiobuttons[e].click()
    #submit button
    submitbutton.click()
    browser.close()
