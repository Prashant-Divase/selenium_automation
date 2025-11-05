import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger("pytest-automation")

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)
        self.driver.implicitly_wait(5)  # optional: global implicit wait

    # -------------------------
    # BASIC ELEMENT ACTIONS
    # -------------------------
    def click(self, by_locator):
        """Wait and click an element"""
        logger.info(f"Clicking on element: {by_locator}")
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        """Wait and type text"""
        logger.info(f"Typing '{text}' into element: {by_locator}")
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        """Return text of an element"""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        text = element.text
        logger.info(f"Text from {by_locator} -> {text}")
        return text

    def is_visible(self, by_locator):
        """Check if element is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            logger.info(f"Element visible: {by_locator}")
            return True
        except:
            logger.warning(f"Element not visible: {by_locator}")
            return False

    # -------------------------
    # MOUSE ACTIONS (ActionChains)
    # -------------------------
    def hover(self, by_locator):
        """Hover the mouse over an element"""
        logger.info(f"Hovering over element: {by_locator}")
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        self.actions.move_to_element(element).perform()

    def right_click(self, by_locator):
        """Right-click on an element"""
        logger.info(f"Right-clicking element: {by_locator}")
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        self.actions.context_click(element).perform()

    def double_click(self, by_locator):
        """Double-click on an element"""
        logger.info(f"Double-clicking element: {by_locator}")
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        self.actions.double_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        """Drag element from source to target"""
        logger.info(f"Dragging from {source_locator} to {target_locator}")
        source = self.wait.until(EC.presence_of_element_located(source_locator))
        target = self.wait.until(EC.presence_of_element_located(target_locator))
        self.actions.drag_and_drop(source, target).perform()

    def move_by_offset(self, x, y):
        """Move the mouse by pixel offset"""
        logger.info(f"Moving mouse by offset x={x}, y={y}")
        self.actions.move_by_offset(x, y).perform()

    # -------------------------
    # KEYBOARD ACTIONS
    # -------------------------
    def press_enter(self):
        logger.info("Pressing ENTER key")
        self.actions.send_keys(Keys.ENTER).perform()

    def press_escape(self):
        logger.info("Pressing ESC key")
        self.actions.send_keys(Keys.ESCAPE).perform()

    def key_combination(self, modifier, key):
        """Perform key combination like CTRL+A or CTRL+S"""
        logger.info(f"Performing key combo: {modifier}+{key}")
        self.actions.key_down(modifier).send_keys(key).key_up(modifier).perform()
