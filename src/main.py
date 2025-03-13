import random
import time

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


GAME_SEVER_ADDRESS = "http://localhost:8080"  # change this to your game server address
# create webdriver object
driver = webdriver.Chrome()
driver.get(GAME_SEVER_ADDRESS)

maze = driver.find_element(By.ID, "mazeCanvas")
left = driver.find_element(By.ID, "btnLeft")
up = driver.find_element(By.ID, "btnUp")
right = driver.find_element(By.ID, "btnRight")
down = driver.find_element(By.ID, "btnDown")
current_move_state = driver.find_element(By.ID, "currentMoveState")
msg_box = driver.find_element(By.ID, "msgBox")
current_player_position = driver.find_element(By.ID, "currentPlayerPosition")  # (x, y)

# create action chain object
actions = ActionChains(driver)


def try_move_left():
    actions.click(left).perform()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        print(
            f"current move state is valid, current player position: {current_player_position.text}"
        )
        return True


def try_move_right():
    actions.click(right).perform()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        print(
            f"current move state is valid, current player position: {current_player_position.text}"
        )
        return True


def try_move_up():
    actions.click(up).perform()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        print(
            f"current move state is valid, current player position: {current_player_position.text}"
        )
        return True


def try_move_down():
    actions.click(down).perform()
    # check if current move state is "valid"
    if current_move_state.text == "valid":
        print(
            f"current move state is valid, current player position: {current_player_position.text}"
        )
        return True


def try_move_all_directions():
    if try_move_left():
        print("can move left")
    else:
        print("cannot move left")

    if try_move_right():
        print("can move right")
    else:
        print("cannot move right")

    if try_move_up():
        print("can move up")
    else:
        print("cannot move up")

    if try_move_down():
        print("can move down")
    else:
        print("cannot move down")


"""
DO NOT CHANGE CODE ABOVE THIS LINE

"""


def solution():
    # Random Walk
    directions = [try_move_left, try_move_right, try_move_up, try_move_down]
    random.shuffle(directions)
    for direction in directions:
        if direction():
            print(f"moved {direction.__name__}")
            return True
    print("no valid move")
    return False


"""
DO NOT CHANGE ANY OF THE CODE BELOW THIS LINE
"""
if __name__ == "__main__":
    start_time = time.strftime("%H:%M:%S")
    end_time = time.strftime("%H:%M:%S")
    start_epoch = time.time()
    while True:
        solution()
        if msg_box.text != "":
            end_time = time.strftime("%H:%M:%S")
            end_epoch = time.time()
            print(f"msg box: {msg_box.text}")
            break

    print(f"start time: {start_time}")
    print(f"end time: {end_time}")
    print(f"total seconds: {end_epoch - start_epoch}")
    with open("results.txt", "a") as f:
        f.write(f"start time: {start_time}\n")
        f.write(f"end time: {end_time}\n")
        f.write(f"total seconds: {end_epoch - start_epoch}\n")
        f.write("--------------------------------------------------\n")
