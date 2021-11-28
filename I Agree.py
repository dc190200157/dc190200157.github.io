WebDriverWait wait = new 
WebDriverWait(driver , 5000); 
wait.until(driver -> driver.switchTo().frame(0)); 
WebElement agree = driver.findElement(By.id("introAgreeButton")); 
agree.click();


driver.switch_to.frame(0) driver.find_element_by_id("introAgreeButton").click() driver.switch_to.default_content() print("begone foul demon of google terms")