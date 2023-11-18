from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def clean_data(address):
    # 如果地址包含 "號"，则只保留 "號" 之前的部分
    if '號' in address:
        address = address.split('號', 1)[0] + '號'

    return address.strip()  # 移除字符串首尾的空白字符


# 设置你的 WebDriver 路径，例如 Chrome 驱动器
# driver_path = r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe"

# 创建一个 WebDriver 实例
driver = webdriver.Edge()

# 目标网页的URL
url = "https://map.dosw.gov.taipei/taipeiWelfare_map/all_new/baby_map.aspx#"

try:
    # 打开网页
    driver.get(url)

    # 查找并点击页面上的某个元素，例如通过元素的 XPath 定位
    element_xpath = "/html/body/form/div[5]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/a[1]"
    element = driver.find_element(By.XPATH ,element_xpath)
    element.click()

    element_xpath = "/html/body/form/div[5]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/a[1]"
    element = driver.find_element(By.XPATH ,element_xpath)
    element.click()

    element_xpath = "/html/body/form/div[5]/div[2]/div/div[1]/div[2]/div[3]/div/div[1]/div[2]/a[1]"
    element = driver.find_element(By.XPATH ,element_xpath)
    element.click()


    element_xpath = "/html/body/form/div[5]/div[2]/div/div[2]/div[1]"
    element = driver.find_element(By.XPATH ,element_xpath)
    element.click()

    # 使用 WebDriverWait 等待特定条件出现，例如等待某个 class 的元素出现
    wait = WebDriverWait(driver, 10)  # 最长等待时间为10秒
    element_to_wait_for = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-card-title"))
    )
    

    # 在此处可以继续执行其他交互操作或操作页面元素
    titles = driver.find_elements(By.CLASS_NAME, "list-card-title")
    addresses = driver.find_elements(By.CLASS_NAME, "list-card-content")

    title_list = []
    address_list = []

    for title in titles:
        title_text = title.find_element(By.TAG_NAME, "span").text
        title_list.append(title_text)

    for address in addresses:
        address_text = address.find_elements(By.TAG_NAME, "li")
        for spec_address in address_text:
            spec_address_text = spec_address.text
            if "地址：" in spec_address_text:
                # 移除 "地址：" 字样
                cleaned_address = clean_data(spec_address_text.replace("地址：", ""))
                address_list.append(cleaned_address)

    print(title_list)

    csv_file = "kindergardens.csv"

    with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)

        # 写入标题行
        writer.writerow(['Name', 'Address'])

        # 写入数据行
        for title, address in zip(title_list, address_list):
            writer.writerow([title, address])

except Exception as e:
    print("发生错误：", str(e))

finally:
    # 关闭浏览器窗口
    driver.quit()

