from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import log

page = {
	"name"         : "home",
	"title"        : "Home",
	"parent"       : None,
	"path"         : "home",
	"active_xpath" : None,
	"link_xpath"   : None,
	"ident_xpath"  : "//a[@href='/portal/settings/account']//descendant::span[text()='Account']",
	"ident_id"     : None,
}

username_menu_xpath = "//img[@class='account-avatar']//following-sibling::span[@class='account-name']"
logout_button_xpath = "//li[@class='account-dropdown-item']//descendant::span[text()='Logout']"
login_title_xpath = "//div[@class='signin-title' and contains(text(), 'Shopee Seller Centre')]"
home_log = log.get_logger(logger_name="lib.shopee.web.page.home", logging_level="info")

#################################################
#                 Navigations                   #
#################################################
def logout(webdriver, waiting_time=30):
	try:
		wait_event = WebDriverWait(webdriver, waiting_time)
		action = ActionChains(webdriver)
		username_menu = wait_event.until(ec.visibility_of_element_located((By.XPATH, username_menu_xpath)))
		action.move_to_element(username_menu).perform()
		logout_button = wait_event.until(ec.element_to_be_clickable((By.XPATH, logout_button_xpath)))
		logout_button.click()
		wait_event.until(ec.visibility_of_element_located((By.XPATH, login_title_xpath)))
		home_log.info("Successfully logout")
		return True

	except:
		home_log.error("Failed to logout")
		print(traceback.format_exc())
		return False