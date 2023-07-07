from selenium import webdriver
from xhr import smsPlatXhr
from excel.excelUtil import ExcelExport
import time

def choose_browser(browser_type, browser_path):
    browser = ''
    if browser_type == 'Chrome':
        browser = webdriver.Chrome(executable_path=browser_path)
    elif browser_type == 'Firefox':
        browser = webdriver.Firefox(executable_path=browser_path)
    elif browser_type == 'IE':
        browser = webdriver.Ie(executable_path=browser_path)
    return browser

def spider(browser):
    excel_rows = []
    tbody = browser.find_element_by_tag_name("tbody")
    trs = tbody.find_elements_by_tag_name("tr")
    for tr in trs:
        tds = tr.find_elements_by_tag_name("td")
        tokenid = tds[0].text
        token_name = tds[4].text
        token = tds[1].text
        channel = tds[2].text
        change_channel = tds[3].text
        # print(tokenid, token_name, token, channel, change_channel)
        # 限流
        interval, maxCount = smsPlatXhr.getLimitData(token)
        # 频率
        frequency_link = tds[-1].find_elements_by_tag_name("a")[1]
        frequency_url = frequency_link.get_attribute("href")
        browser.switch_to.default_content()
        browser.execute_script(f"window.open('{frequency_url}');")
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(1)
        frequency_window_tbody = browser.find_element_by_tag_name("tbody")
        frequency_window_trs = frequency_window_tbody.find_elements_by_tag_name("tr")
        frequencys = []
        for frequency_window_tr in frequency_window_trs[1:]:
            frequency_time = frequency_window_tr.find_elements_by_tag_name("td")[1].text
            frequency_max_num = frequency_window_tr.find_elements_by_tag_name("td")[2].text
            frequencys.append(f"{frequency_max_num}次/{frequency_time}分")
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        browser.switch_to.frame("centerMainIframe")
        if maxCount is not None and interval is not None:
            flow = f"{maxCount}次/{interval}秒"
        else:
            flow = None
        row = {
            "token_name": token_name,
            "token": token,
            "channel": channel,
            "chang_channel": change_channel,
            "frequency": ",".join(frequencys),
            "flow": flow
        }
        print(row)
        excel_rows.append(row)
    return excel_rows

if __name__=="__main__":
    browser = choose_browser(browser_type="Chrome", browser_path="chromedriver.exe")
    browser.get('http://smsmanager.zwjk.com/admin')

    userinfo = browser.find_element_by_class_name("userinfo")
    input_box = userinfo.find_elements_by_tag_name("input")
    username_input = input_box[0]
    password_input = input_box[1]
    codeImage_input = input_box[2]
    username = input("账号：")
    if username is None or username == '':
        username = "admin"
    username_input.send_keys(username)
    password = input("密码：")
    if password is None or password == '':
        password = "mWwdJp%go4wqNa3"
    password_input.send_keys(password)
    codeImage = input("验证码：")
    codeImage_input.send_keys(codeImage)

    submit_button = browser.find_element_by_id("submit")
    submit_button.click()

    time.sleep(2)
    sidebar_menu = browser.find_element_by_class_name("sidebar-menu")
    link = sidebar_menu.find_element_by_partial_link_text("原短信发送Token接入")
    link.click()
    time.sleep(1)
    token_manager = sidebar_menu.find_element_by_partial_link_text("Token列表")
    token_manager.click()
    time.sleep(1)
    browser.switch_to.frame("centerMainIframe")
    time.sleep(1)

    cookie = input("Cookie: ")
    smsPlatXhr = smsPlatXhr(cookie)

    columns_map = {
        "token_name": "项目名",
        "token": "token",
        "channel": "渠道",
        "chang_channel": "切换短信渠道",
        "frequency": "限频",
        "flow": "限流"
    }

    print("爬取第1页=========================================")
    excel_rows = spider(browser)

    # 分页
    pagination = browser.find_element_by_class_name("pagination")
    lis = pagination.find_elements_by_tag_name("li")
    max_page = int(lis[-2].text)
    page_num = 1
    for i in range(max_page-1):
        time.sleep(2)
        pagination = browser.find_element_by_class_name("pagination")
        lis = pagination.find_elements_by_tag_name("li")
        for li in lis:
            if li.text == "下一页":
                page_num = page_num + 1
                next_page_button = li.find_element_by_tag_name("a")
                browser.execute_script("arguments[0].click();", next_page_button)
                print(f"爬取第{page_num}页=========================================")
                excel_rows.extend(spider(browser))

    ExcelExport.export_excel("原token配置及使用情况统计", columns_map, excel_rows)

