import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def download_riddles():
    print("[INFO]  What's up, we are starting to parse the site: https://zagadkivse.ru/")
    #  Setup
    count = 1
    driver = webdriver.Chrome("driver\chromedriver.exe")
    url = "https://zagadkivse.ru/hitrye-zagadki/"
    
    #  Getting HTML
    driver.get(url)
    time.sleep(1)
    #  Find Button
    button = driver.find_element(By.ID, "loadmore")

    try:
        # Press Button
        while True:
            print(f"[INFO] Pages loaded: {count}")
            button.click()
            time.sleep(0.8)
            count += 1

    except Exception as ex:
            print(f"[INFO] All Pages loaded")
    finally:
        source = driver.page_source
        #save_file("source/zagadki.html", source)
        driver.close()
        driver.quit()
        return source


def save_file(name, source):
    with open(name, "w", encoding="utf-8") as file:
        file.write(source)


def load_source(file):
    with open(file, "r", encoding="utf-8") as file:
        return file.read()


def pars_html(html):
    result = ""
    print(f"[INFO] Starting Parsing")
    #src = load_source("source\zagadki.html")
    #soup = BeautifulSoup(src, "lxml")
    soup = BeautifulSoup(html, "lxml")
    all_riddle = soup.find(class_="riddle-list")
    numbers = all_riddle.find_all(class_="riddle-text-nmbr")
    riddles = all_riddle.find_all(class_="riddle-text-content")
    correct_answer = all_riddle.find_all(class_="correct-answer")
    for i in range(len(numbers)):
        result += f"{numbers[i].text}\n{riddles[i].text.strip()}\nОтвет: {correct_answer[i].text}"
        result += "\n---------------------------------------------------------------------\n"
    save_file("result.txt", result)
    print(f"[INFO] File result.txt Save in Work Dirrecrory, have a good day!)")
    time.sleep(5)



if __name__ == "__main__":
    pars_html(download_riddles())
