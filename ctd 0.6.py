import random
import cv2
import numpy as np

def display_message(message):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    text_size = cv2.getTextSize(message, font, font_scale, thickness)[0]
    width = text_size[0] + 50
    height = text_size[1] + 50
    image = np.zeros((height, width, 3), np.uint8)
    image[:] = (255, 255, 255)
    x = int((width - text_size[0]) / 2)
    y = int((height + text_size[1]) / 2)
    cv2.putText(image, message, (x, y), font, font_scale, (255, 0, 0), thickness)
    cv2.imshow("Message", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def game():
    bags = [10, 10, 10]
    while True:
        try:
            player_name = input("Username: ")
            if not player_name.isdigit():
                break
            else:
                raise ValueError("Enter Letters only!!")
        except ValueError as e:
            print(e)

    player = player_name
    while True:
        if player == player_name:
            print(bags)
            while True:
                try:
                    choice = int(input("Select a bag (1, 2, 3): "))
                    if choice not in [1, 2, 3] or bags[choice - 1] == 0:
                        raise ValueError("Are you dumb!!! Select a bag (1, 2, 3): ")
                    break
                except ValueError as e:
                    print(e)
                except:
                    print("Ahhh! Enter a digit only!")
            while True:
                try:
                    num_objects = int(input("Select number of objects (1-5): "))
                    if num_objects not in range(1, 6) or num_objects > bags[choice - 1]:
                        raise ValueError("EH EH Invalid! Select number of objects (1-5): ")
                    break
                except ValueError as e:
                    print(e)
                except:
                    print("Enter a digit only")
            bags[choice - 1] -= num_objects
            player = "Computer"
        else:
            choices = [i for i, x in enumerate(bags) if x != 0]
            choice = random.choice(choices) + 1
            num_objects = random.randint(1, 5)
            if num_objects > bags[choice - 1]:
                num_objects = bags[choice - 1]
            bags[choice - 1] -= num_objects
            print("The Computer removed", num_objects, "from bag", choice)
            player = player_name
        if sum(bags) == 0:
            if player == player_name:
                display_message("Computer Wins that means you lose sucker.")
                
            else:
                display_message("Congratulations " + player_name + " you won!")
            break

if __name__ == "__main__":
    game()
