import docker  # Importing the Docker SDK for Python.

# Function to retrieve and list all Docker images along with their created date and size.
def list_images(client):
    print("\nList of Docker Images:")
    images = client.images.list()  # Retrieving a list of images.
    for idx, img in enumerate(images, start=1):  # Enumerating through images, start=1 makes the index 1-based.
        created = img.attrs['Created']  # Getting the creation date of the image.
        size = img.attrs['Size']  # Getting the size of the image.
        print(f"{idx}. {img.short_id} - {img.tags} - Created: {created} - Size: {size/(1024*1024):.2f} MB")  # Printing the index, short_id, tags, created date, and size of each image.
    return images  # Returning the list of images for further processing.

# Function to retrieve and list all Docker containers (including stopped ones) along with their created date and status.
def list_containers(client):
    print("\nList of Docker Containers:")
    containers = client.containers.list(all=True)  # Retrieving a list of all containers, including stopped ones.
    for idx, container in enumerate(containers, start=1):  # Enumerating through containers, start=1 makes the index 1-based.
        container.reload()  # Refreshing the information of the container.
        created = container.attrs['Created']  # Getting the creation date of the container.
        status = container.status  # Getting the status of the container.
        print(f"{idx}. {container.short_id} - {container.name} - Created: {created} - Status: {status}")  # Printing the index, short_id, name, created date, and status of each container.
    return containers  # Returning the list of containers for further processing.

# Function to delete a specific Docker image selected by the user.
def delete_image(client):
    images = list_images(client)  # Calling the list_images function to get the list of images and allow the user to select one.
    try:
        choice = int(input("\nEnter the image number to delete (0 to cancel): "))  # Prompting the user for the image number to delete.
        if choice == 0:  # If the user enters 0, the function will return and no image will be deleted.
            return
        image_to_delete = images[choice - 1]  # Subtracting 1 from choice because the list index is 0-based.
        client.images.remove(image=image_to_delete.id)  # Deleting the selected image.
        print("Image deleted successfully.")
    except (IndexError, ValueError):  # Handling exceptions for invalid input and invalid selection.
        print("Invalid choice, please enter a valid number.")
    except docker.errors.APIError as e:  # Handling exceptions raised by the Docker API.
        print(f"An error occurred: {e}")

# Function to delete a specific Docker container selected by the user.
def delete_container(client):
    containers = list_containers(client)  # Calling the list_containers function to get the list of containers and allow the user to select one.
    try:
        choice = int(input("\nEnter the container number to delete (0 to cancel): "))  # Prompting the user for the container number to delete.
        if choice == 0:  # If the user enters 0, the function will return and no container will be deleted.
            return
        container_to_delete = containers[choice - 1]  # Subtracting 1 from choice because the list index is 0-based.
        container_to_delete.remove()  # Deleting the selected container.
        print("Container deleted successfully.")
    except (IndexError, ValueError):  # Handling exceptions for invalid input and invalid selection.
        print("Invalid choice, please enter a valid number.")
    except docker.errors.APIError as e:  # Handling exceptions raised by the Docker API.
        print(f"An error occurred: {e}")

# Function to delete all available Docker images.
def delete_all_images(client):
    try:
        client.images.prune(filters={"dangling": False})  # This command will remove all images not used by existing containers.
        print("All images deleted successfully.")
    except docker.errors.APIError as e:  # Handling exceptions raised by the Docker API.
        print(f"An error occurred: {e}")

# Function to delete all stopped Docker containers.
def delete_all_containers(client):
    try:
        client.containers.prune()  # This command will remove all containers that are not running.
        print("All containers deleted successfully.")
    except docker.errors.APIError as e:  # Handling exceptions raised by the Docker API.
        print(f"An error occurred: {e}")
