from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Test 1: Verify homepage loads within 3 seconds
    start_time = time.time()
    driver.get("https://seth-agbavitor.github.io/portfolio/")  
    load_time = time.time() - start_time
    if load_time <= 3:
        print(f"Test 1 passed: Homepage loaded in {load_time:.2f} seconds.")
    else:
        print(f"Test 1 failed: Homepage loaded in {load_time:.2f} seconds, exceeding 3 seconds.")

    # Test 2: Verify "Master Thesis" link directs to correct GitHub page
    thesis_link = driver.find_element(By.LINK_TEXT, "View on GitHub")
    thesis_link.click()
    time.sleep(2)  # Wait for redirection
    expected_url = "https://github.com/Seth-Agbavitor/Master-Thesis-Scheduling-and-Running-Software-Test-Cases-Based-on-AI"
    current_url = driver.current_url
    if expected_url in current_url:
        print("Test 2 passed: Master Thesis link directs to the correct GitHub page!")
    else:
        print(f"Test 2 failed: Expected {expected_url}, but got {current_url}")

    # Test 3-6: Verify scrolling behavior for About, Skills, Projects, and Contact
    driver.get("https://seth-agbavitor.github.io/portfolio/")  # Return to homepage
    sections = {
        "About": "about",
        "Skills": "skills",
        "Projects": "projects",
        "Contact": "contact"
    }

    for section_name, section_id in sections.items():
        # Scroll to the section using its ID
        driver.execute_script(f"document.getElementById('{section_id}').scrollIntoView();")
        time.sleep(1)  # Allow time for scroll to complete

        # Verify the section is in view
        element = driver.find_element(By.ID, section_id)
        is_visible = driver.execute_script(
            "return arguments[0].getBoundingClientRect().top >= 0 && "
            "arguments[0].getBoundingClientRect().bottom <= window.innerHeight;",
            element
        )
        if is_visible:
            print(f"Test {section_name} passed: Scrolling to {section_name} section works.")
        else:
            print(f"Test {section_name} failed: {section_name} section not fully visible after scroll.")

except Exception as e:
    print(f"Test failed: {str(e)}")

finally:
    # Close the browser
    driver.quit()