from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import threading


try: 
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    # Tìm ô tìm kiếm
    search_box = driver.find_element(By.XPATH, '//input[@id="search"]')

    # Gõ từ khóa vào ô tìm kiếm
    search_box.send_keys("@Boymuscleworkout")

    # Nhấn Enter để tìm kiếm
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # Tìm và nhấp vào liên kết của kênh
    video_link = driver.find_element(By.XPATH, '//*[@id="subscribers" and contains(text(), "@Boymuscleworkout")]')
    video_link.click()
    time.sleep(5)

    # Chuyển sang tab mới
    driver.switch_to.window(driver.window_handles[-1])

    # Tìm và nhấp vào tab "Playlists"
    playlists = driver.find_element(By.XPATH, '//yt-tab-shape[@tab-title="Playlists"]')
    playlists.click()
    time.sleep(5)

    # Tìm tất cả các phần tử có id là "video-title"
    elements = driver.find_elements(By.XPATH,'//a[@id="video-title"]')
    driver.quit()
    time.sleep(30)

except :
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/@Boymuscleworkout/playlists")
    time.sleep(10)
    # Tìm tất cả các phần tử có id là "video-title"
    elements = driver.find_elements(By.XPATH,'//a[@id="video-title"]')
    driver.quit()
    time.sleep(30)

# Hàm thực thi cho mỗi luồng
def run_thread(keyword):
    driver = webdriver.Chrome()

    try: 
        driver.get("https://www.youtube.com/")

        # Tìm ô tìm kiếm
        search_box = driver.find_element(By.XPATH, '//input[@id="search"]')

        # Gõ từ khóa vào ô tìm kiếm
        search_box.send_keys("@Boymuscleworkout")

        # Nhấn Enter để tìm kiếm
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Tìm và nhấp vào liên kết của kênh
        video_link = driver.find_element(By.XPATH, '//*[@id="subscribers" and contains(text(), "@Boymuscleworkout")]')
        video_link.click()
        time.sleep(5)

        playlists = driver.find_element(By.XPATH, '//yt-tab-shape[@tab-title="Playlists"]')
        playlists.click()
        time.sleep(5)
        watch_video = driver.find_element(By.XPATH, '//a[@id="video-title" and contains(text(), "{}")]'.format(keyword))
        watch_video.click()
        time.sleep(10)
        driver.save_screenshot("screenshot_{}.png".format(keyword))
        print("Screenshot taken for keyword: {}".format(keyword))

        # while True:
        #     # Chụp ảnh màn hình
        #     driver.save_screenshot("screenshot_{}.png".format(keyword))
        #     print("Screenshot taken for keyword: {}".format(keyword))

        #     # Chờ 10 phút trước khi chụp ảnh màn hình tiếp theo
        #     time.sleep(600)

        #Đóng trình duyệt khi kết thúc
        driver.quit()
    
    except: 
            
        driver.get("https://www.youtube.com/@Boymuscleworkout/playlists")
        time.sleep(10)
        watch_video = driver.find_element(By.XPATH, '//a[@id="video-title" and contains(text(), "{}")]'.format(keyword))
        watch_video.click()
        time.sleep(10)

        driver.save_screenshot("screenshot_{}.png".format(keyword))
        print("Screenshot taken for keyword: {}".format(keyword))

        # while True:
        #     # Chụp ảnh màn hình
        #     driver.save_screenshot("screenshot_{}.png".format(keyword))
        #     print("Screenshot taken for keyword: {}".format(keyword))

        #     # Chờ 10 phút trước khi chụp ảnh màn hình tiếp theo
        #     time.sleep(600)

        # Đóng trình duyệt khi kết thúc
        driver.quit()

# Số lượng luồng bạn muốn chạy
n_threads = len(elements)

# Tạo và khởi chạy các luồng
threads = []
for element in elements:
    thread = threading.Thread(target=run_thread, args=(element.text,))
    thread.start()
    threads.append(thread)

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

print("Done!")
