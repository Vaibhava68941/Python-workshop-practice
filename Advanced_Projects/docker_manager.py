import docker
from docker.errors import DockerException, APIError, NotFound

def connect_to_docker():
    try:
        client = docker.from_env()
        if client.ping():
            print("Successfully connected to Docker.")
        else:
            print("Failed to connect to Docker.")
        return client  
    except DockerException as e:
        print(f"Error connecting to Docker: {e}")
        return None
    
def list_containers(client):
    try:
        containers = client.containers.list(all=True)
        if not containers:
            print("No containers found.")
        else:
            for container in containers:
                print(f"Container ID: {container.short_id}, Name: {container.name}, Status: {container.status}") 
    except APIError as e:
        print(f"Error listing containers: {e}")
        return None
    
def start_container(client):  
    try:
        stopped_container = client.containers.list(all=True, filters={"status": "exited"})
        
        user_input = input("Enter the container ID or name to start: list of stopped containers:\n") 
        
        container = client.containers.get(user_input)
        
        if container not in stopped_container:
            print(f"No container found with ID or name")  
            
        else:
            container.start() 
            print(f"Container {container.name} started successfully.")
            
            container.reload()
            
            is_running = container.status
            print(f"Container {container_id} is now {is_running}.")  
            
    except NotFound as e: 
        print(f"container not found with {user_input}: {e},Please verify id and then try again")
    except APIError as e:
        print(f"API error occurred while starting the container: {e}")  

def stop_container(client):       
    try:
        running_container = client.containers.list(filters={"status": "running"})  
        
        user_input = input("Enter the container ID or name of runnning container to stop: (check list of running containers to get ID) :\n")
        
        container = client.containers.get(user_input)   
        
        if container not in running_container:
            print(f"No running container found with ID or name {user_input}.")  
        else:
            container.stop()  
            print(f"Container {container.name} stopped successfully.")
            
            container.reload()
            
    except NotFound as e:
        print(f"Container not found with ID or name {user_input}: {e}. Please verify the ID and try again.")
    except APIError as e:
       print(f"API error occurred while stopping the container: {e}")  
       
def restart_container(client):
    try:
        running_container = client.containers.list(filters={"status": "running"})
        
        user_input = input("Enter the container ID or name of the running container to restart: (check list of running containers to get ID):\n")
        
        container = client.containers.get(user_input)
        
        if container not in running_container:
            print(f"No running container found with ID or name {user_input}.")
        else:
            container.restart()
            print(f"Container {container.name} restarted successfully.")
            
            container.reload()
            
    except NotFound as e:
        print(f"Container not found with ID or name {user_input}: {e}. Please verify the ID and try again.")
    except APIError as e:
        print(f"API error occurred while restarting the container: {e}")
        
def delete_container(client):
    try:
        all_containers = client.containers.list(all=True)
        
        user_input = input("Enter the container ID or name of the container to delete: (check list of all containers to get ID):\n")
        
        container = client.containers.get(user_input)
        
        if container not in all_containers:
            print(f"No container found with ID or name {user_input}.")
        else:
            container.remove(force=True)
            print(f"Container {container.name} deleted successfully.")
            
    except NotFound as e:
        print(f"Container not found with ID or name {user_input}: {e}. Please verify the ID and try again.")
    except APIError as e:
        print(f"API error occurred while deleting the container: {e}")
        
        
        
        
        