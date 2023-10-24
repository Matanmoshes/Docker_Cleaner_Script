# main.py

import sys  # Importing the sys module for system-specific parameters and functions.
from functions import (  # Importing functions from the docker_utils file.
    list_images,
    list_containers,
    delete_image,
    delete_container,
    delete_all_images,
    delete_all_containers,
)
import docker  # Importing the Docker SDK for Python.

def main():
    """The main function of the script, providing the interface for the user's choices."""
    client = docker.from_env()  # Creating a Docker client using the default environment configuration.

    while True:  # Starting an infinite loop to continuously present the menu to the user.
        print("\nOptions:")  # Printing available options to the console.
        print("1. List images")
        print("2. List containers")
        print("3. Delete an image")
        print("4. Delete a container")
        print("5. Delete all images")
        print("6. Delete all containers")
        print("7. Exit")

        try:
            choice = int(input("\nEnter your choice: "))  # Asking the user for their choice.

            # Matching the user's choice to the corresponding function.
            if choice == 1:
                list_images(client)
            elif choice == 2:
                list_containers(client)
            elif choice == 3:
                delete_image(client)
            elif choice == 4:
                delete_container(client)
            elif choice == 5:
                delete_all_images(client)
            elif choice == 6:
                delete_all_containers(client)
            elif choice == 7:
                sys.exit()  # Exiting the script if the user chooses this option.
            else:
                print("Invalid choice, please choose a number between 1 and 7.")  # Error message for an invalid choice outside the 1-7 range.
        except ValueError:  # Handling exceptions for non-integer inputs.
            print("Invalid input, please enter a valid number.")
        except KeyboardInterrupt:  # Handling a user interrupt (Ctrl+C).
            sys.exit()  # Exiting the script if a keyboard interrupt occurs.

if __name__ == "__main__":
    main()  # Ensuring the main function is called only when the script is executed directly (not imported).
