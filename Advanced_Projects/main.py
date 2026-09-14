#Main script to run the Docker (start,stop,restart,delete) functions 
from docker-manager import connect_to_docker, list_containers, start_container, stop_container, restart_container, delete_container


def main():
    client = connect_to_docker()
    if client is None:
        return

    while True:
        print("\nDocker Container Management Menu:")
        print("1. List all containers")
        print("2. Start a container")
        print("3. Stop a container")
        print("4. Restart a container")
        print("5. Delete a container")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            list_containers(client)
        elif choice == '2':
            container_id = input("Enter the container ID or name to start: ")
            start_container(client)
        elif choice == '3':
            container_id = input("Enter the container ID or name to stop: ")
            stop_container(client)
        elif choice == '4':
            container_id = input("Enter the container ID or name to restart: ")
            restart_container(client)
        elif choice == '5':
            container_id = input("Enter the container ID or name to delete: ")
            delete_container(client)
        elif choice == '6':
            print("Exiting Docker Container Management.")
            break
        else:
            print("Invalid choice. Please try again.")   
            
if __name__ == "__main__":
    main()