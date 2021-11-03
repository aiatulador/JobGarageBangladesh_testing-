import random
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.by import By

report = Report()

driver = webdriver.Edge(
    executable_path="D:\\AAAAAAAAAAAAAA\\edgedriver_win64\\msedgedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Job Garage Bangladesh',
    release_name='Test V1',
    selenium_driver=driver
)
driver.get('http://127.0.0.1:8000/')

# Test Case 1

try:
    report.write_step(
        'Go To About Us page',
        status=report.status.Start,
        test_number=1
    )

    driver.find_element(By.XPATH,"//a[contains(text(),'About Us')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/about/"
    time.sleep(2)
    report.write_step(
        'Successfully Open to the About Us Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Open About Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 2

try:
    report.write_step(
        'Go To Create Account page',
        status=report.status.Start,
        test_number=2
    )
    driver.back()
    driver.find_element(By.XPATH,"//a[contains(text(),'Create Account')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/register/"
    time.sleep(2)
    report.write_step(
        'Successfully Open to the Create Account Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Open Create Account Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 3

try:
    report.write_step(
        'Sign Up',
        status=report.status.Start,
        test_number=3
    )

    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("vini")
    driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys("Vinicius")
    driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys("Junior")
    driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys("18201019@uap-bd.edu")
    driver.find_element(By.XPATH, '//*[@id="id_password1"]').send_keys("asdf7485")
    driver.find_element(By.XPATH, '//*[@id="id_password2"]').send_keys("asdf7485")
    driver.find_element(By.XPATH, '/html/body/div/div/form/button').click()


    assert driver.current_url == "http://127.0.0.1:8000/login/"
    time.sleep(2)
    report.write_step(
        'Successfully Registered',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Registered',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 4

try:
    report.write_step(
        'Log in',
        status=report.status.Start,
        test_number=4
    )

    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("vini")
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("asdf7485")
    driver.find_element(By.XPATH, '/html/body/div/div/form/button').click()

    assert driver.current_url == "http://127.0.0.1:8000/"
    time.sleep(2)
    report.write_step(
        'Successfully Logged in',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Log in',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 5

try:
        report.write_step(
            'Go to Find Work Page',
            status=report.status.Start,
            test_number=5
        )

        driver.find_element(By.XPATH, '/html/body/div[3]/a[2]/button').click()
        assert driver.current_url == "http://127.0.0.1:8000/find_work/"
        time.sleep(2)
        report.write_step(
            'Successfully Open to the Find Work Page',
            status=report.status.Pass,
            screenshot=True
        )
except AssertionError:
        report.write_step(
            'Failed to ope Find Work Page',
            status=report.status.Fail,
            screenshot=True
        )
except Exception as e:
        report.write_step(
            'Something went wrong!</br>{e}',
            status=report.status.Warn,
            screenshot=True
        )

# Test Case 6

try:
        report.write_step(
            'Go to User Profile Page',
            status=report.status.Start,
            test_number=6
        )

        driver.find_element(By.XPATH, '//*[@id="navbar-main"]/div/a[4]').click()
        assert driver.current_url == "http://127.0.0.1:8000/profile/"
        time.sleep(2)
        report.write_step(
            'Successfully Open to the User Profile Page',
            status=report.status.Pass,
            screenshot=True
        )
except AssertionError:
        report.write_step(
            'Failed to open User Profile Page',
            status=report.status.Fail,
            screenshot=True
        )
except Exception as e:
        report.write_step(
            'Something went wrong!</br>{e}',
            status=report.status.Warn,
            screenshot=True
        )
# Test Case 7

try:
        report.write_step(
            'Go to Password Change Page',
            status=report.status.Start,
            test_number=7
        )

        driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div[2]/a[2]').click()
        assert driver.current_url == "http://127.0.0.1:8000/password_change/"
        time.sleep(2)
        report.write_step(
            'Successfully Open to the Password Change Page',
            status=report.status.Pass,
            screenshot=True
        )
except AssertionError:
        report.write_step(
            'Failed to open Password Change Page',
            status=report.status.Fail,
            screenshot=True
        )
except Exception as e:
        report.write_step(
            'Something went wrong!</br>{e}',
            status=report.status.Warn,
            screenshot=True
        )

# Test Case 8

try:
        report.write_step(
            'Password Change',
            status=report.status.Start,
            test_number=8
        )

        driver.find_element(By.XPATH, '//*[@id="id_old_password"]').send_keys("asdf7485")
        driver.find_element(By.XPATH, '//*[@id="id_new_password1"]').send_keys("asdf748596")
        driver.find_element(By.XPATH, '//*[@id="id_new_password2"]').send_keys("asdf748596")
        driver.find_element(By.XPATH, '/html/body/div/div/form/button').click()

        assert driver.current_url == "http://127.0.0.1:8000/password_change/done/"
        time.sleep(2)
        report.write_step(
            'Password Successfully Changed',
            status=report.status.Pass,
            screenshot=True
        )
except AssertionError:
        report.write_step(
            'Failed to Change Password',
            status=report.status.Fail,
            screenshot=True
        )
except Exception as e:
        report.write_step(
            'Something went wrong!</br>{e}',
            status=report.status.Warn,
            screenshot=True
        )

# Test Case 9

try:
    report.write_step(
        'Go To Profile',
        status=report.status.Start,
        test_number=9
    )

    driver.find_element(By.XPATH,"/html/body/div/a").click()
    assert driver.current_url == "http://127.0.0.1:8000/profile/"
    time.sleep(2)
    report.write_step(
        'Successfully Open to Profile Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Profile Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 10

try:
        report.write_step(
            'Update Profile',
            status=report.status.Start,
            test_number=10
        )
        # driver.back()

        driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/a').click()
        driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("")
        driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys("")
        driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys("")
        driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys("")

        driver.find_element(By.XPATH, '//*[@id="id_about"]').send_keys("Winger")
        driver.find_element(By.XPATH, '//*[@id="id_age"]').send_keys("22")

        driver.find_element(By.XPATH, '//*[@id="id_profession"]').send_keys("Winger")
        driver.find_element(By.XPATH, '//*[@id="id_address"]').send_keys("La Rozas De Madrid")
        driver.find_element(By.XPATH, '//*[@id="id_city"]').send_keys("Madrid")
        driver.find_element(By.XPATH, '//*[@id="id_country"]').send_keys("Spain")
        driver.find_element(By.XPATH, '//*[@id="id_phone"]').send_keys("648256984")
        driver.find_element(By.XPATH, '/html/body/div/div/form/button').click()

        assert driver.current_url == "http://127.0.0.1:8000/profile/"
        time.sleep(2)
        report.write_step(
            'Profile Successfully Updated',
            status=report.status.Pass,
            screenshot=True
        )
except AssertionError:
        report.write_step(
            'Failed to update Profile',
            status=report.status.Fail,
            screenshot=True
        )
except Exception as e:
        report.write_step(
            'Something went wrong!</br>{e}',
            status=report.status.Warn,
            screenshot=True
        )

# Test Case 11

try:
    report.write_step(
        'Log out',
        status=report.status.Start,
        test_number=11
    )

    driver.find_element(By.XPATH, '//*[@id="navbar-main"]/div/a[4]').click()

    assert driver.current_url == "http://127.0.0.1:8000/logout/"
    time.sleep(2)
    report.write_step(
        'Successfully Logged out',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Log out',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


# Report Generation
report.generate_report()
driver.quit()

print("Job Garage Bangladesh Testing Completed.")