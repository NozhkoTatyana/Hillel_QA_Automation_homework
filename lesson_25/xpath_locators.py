# HEADER
BTN_ABOUT_TEXT = "//button[text()='About']"  #1
BTN_ABOUT_CONTAINS  = "(//button[contains(@class,'btn')])[1]"  #2
BTN_GUEST_lOGIN_IN = "//button[contains(@class,'header-link -guest')]"  #3
BTN_SIGN_IN = "//button[text()='Sign In']"  #4

# MAIN
BTN_SIGN_UP = "//div[contains(@class,'hero-descriptor')]/button"  #5
VIDEO_PLAYER = "//div[@id = 'player-controls']"  #6
BTN_PLAY_VIDEO = "//button[contains(@title,'Воспроизвести') or contains(@aria-label,'Воспроизвести')]"  #7

# Page Garage
BTN_MY_PROFILE = "//button[@id = 'userNavDropdown']"  #8
DD_BTN_FUEL_EXPENSES =  "(//nav[contains(@class, 'user')]/a)[2]"  #9
DD_BTN_INSTRUCTIONS = "(//nav[contains(@class, 'user')]/a)[3]"   #10
DD_LOGOUT = "//button[contains(@class, 'dropdown-item') and text()='Logout']"  #11
BTN_ADD_CAR = "//button[text()='Add car']"  #12
DD_BRAND_SELECT = "//*[@id='addCarBrand']"  #13
OPT_BRAND_FORD = "//select[@id='addCarBrand']/option[contains(text(),'Ford') or @value='2: 3']" #14
DD_MODEL_SELECT = "//select[@id='addCarModel']" #15
INPUT_MILEAGE = "//input[@id='addCarMileage']"   #16
BTN_CLOSE = "//button[@aria-label='Close' and contains(@class,'close')]" #17


# PAGE INSTRUCTIONS
OPT_BRAND_FIAT = "//div[contains(@class, 'brand')]/ul/li[text()='Fiat']"  #18
OPT_MODEL_AUDI_TT = "//button[@id='modelSelectDropdown']"  #19
BTN_SEARCH = "//button[text()='Search']"  #20
CARD_INSTRUCTION_SPARK_PLUGS = "//div[contains(@class, 'instructions_content')]//li[6]"  #21

# Form Login
INPUT_EMAIL = "//input[@id='signinEmail']"  #22
INPUT_PASSWORD = "//input[@id='signinPassword']"  #23
ERR_MSG_EMAIL_REQUIRED = "//input[@id='signinEmail']/following-sibling::div[@class='invalid-feedback']/p"  #24
BTN_LOGIN = "//button[text()='Login']"  #25




