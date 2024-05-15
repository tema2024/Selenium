from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def browse_wikipedia():

    driver = webdriver.Chrome()

    try:

        driver.get("https://ru.wikipedia.org")
        query = input("Введите запрос для поиска на Википедии: ")
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(query + Keys.RETURN)

        time.sleep(2)


        first_heading = driver.find_element(By.ID, "firstHeading")
        print(f"Название статьи: {first_heading.text}")


        def show_paragraphs():
            paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p")
            for i, p in enumerate(paragraphs):
                print(f"\nПараграф {i+1}: {p.text}")
                if input("Нажмите Enter для следующего параграфа или введите 'stop' для остановки: ") == 'stop':
                    break


        while True:
            print("\nВыберите действие:")
            print("1 - Показать параграфы текущей статьи")
            print("2 - Перейти на связанную страницу")
            print("3 - Выйти из программы")

            choice = input("Введите номер действия: ")
            if choice == '1':
                show_paragraphs()
            elif choice == '2':
                links = driver.find_elements(By.CSS_SELECTOR, "div#mw-normal-catlinks a")
                for index, link in enumerate(links):
                    print(f"{index + 1} - {link.text}")

                link_choice = int(input("Введите номер страницы для перехода: ")) - 1
                if 0 <= link_choice < len(links):
                    links[link_choice].click()
                    time.sleep(2)  # Пауза для загрузки страницы
                    first_heading = driver.find_element(By.ID, "firstHeading")
                    print(f"Название статьи: {first_heading.text}")
                else:
                    print("Неверный ввод. Пожалуйста, введите корректный номер.")
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")

    finally:
        driver.quit()

if __name__ == "__main__":
    browse_wikipedia()
