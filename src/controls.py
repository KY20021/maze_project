import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()

driver.get("http://localhost:8080")

maze = driver.find_element(By.ID, "mazeCanvas")
left = driver.find_element(By.ID, "btnLeft")
up = driver.find_element(By.ID, "btnUp")
right = driver.find_element(By.ID, "btnRight")
down = driver.find_element(By.ID, "btnDown")
current_move_state = driver.find_element(By.ID, "currentMoveState")

# create action chain object
actions = ActionChains(driver)


def move_left():
    # click left button
    actions.click(left).perform()
    time.sleep(1)


def move_right():
    # click right button
    actions.click(right).perform()
    time.sleep(1)


def move_up():
    # click up button
    actions.click(up).perform()
    time.sleep(1)


def move_down():
    # click down button
    actions.click(down).perform()
    time.sleep(1)


def can_move_left():
    move_left()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        return True


def can_move_up():
    move_up()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        return True


def can_move_right():
    move_right()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        return True


def can_move_down():
    move_down()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        player_x = player_x + 1
        return True


def move_all_directions():
    move_left()
    move_up()
    move_right()
    move_down()
    # click down button


def can_move_all_directions():
    if can_move_left():
        print("can move left")
    else:
        print("cannot move left")

    if can_move_right():
        print("can move right")
    else:
        print("cannot move right")

    if can_move_up():
        print("can move up")
    else:
        print("cannot move up")

    if can_move_down():
        print("can move down")
    else:
        print("cannot move down")


# wait for 1 second
time.sleep(1)
for i in range(100):
    # move_all_directions()
    can_move_all_directions()
# click down button
# open localhost:8080
