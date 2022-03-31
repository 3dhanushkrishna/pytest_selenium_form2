from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture()
def setUp():
    global MovieName,YearofRelease,Directorname,Distributor,Producer,driver
    MovieName = input("enter the movie name: ")
    YearofRelease = input("enter the year of release: ")
    Directorname = input("enter the director name: ")
    Distributor = input("enter the distributor: ")
    Producer = input("enter the producer: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
def test_movie(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(MovieName)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(YearofRelease)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(Directorname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)
