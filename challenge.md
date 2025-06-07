# How to run it

1. Docker
    > [!IMPORTANT]
    > To run this, you must have Docker installed in your machine

    1. You must clone the repository and move to the cloned repository:
    ```bash
    cd yourfolder/
    git clone https://github.com/AlejandroBlanco2001/DjangoTest.git
    cd DjangoTest
    ```
    2. Run the following commands to create and build the docker image:

    ```bash
    docker build -t task:latest . 
    docker run -p 127.0.0.1:8000:8000 task:latest
    ```
2. Without Docker
    > [!IMPORTANT]
    > To run this, you must have Python installed

    1. You must clone the repository and move to the cloned repository:
    ```bash
    cd yourfolder/
    git clone https://github.com/AlejandroBlanco2001/DjangoTest.git
    cd DjangoTest
    ```
    2. Run this command to install all the dependencies on a venv
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

    3. Run the following command to migrate and start the server
    ```bash
    cd task
    python manage.py makemigrations tasksmanagement
    python manage.py migrate
    python managy.py runserver 0.0.0.0:8000
    ```

# Allowed operations

- Labels
    - GET, PUT, DELETE Specific Label (/api/label/{id})
    - GET All labels from user (/api/label)
    - POST Create a new label (/api/label)
    - GET All labels with their task (/api/label/{id}/tasks)
- Task 
    - GET, PUT, DELETE Specific task (/api/task/{id})
    - GET All tasks from user (/api/task)
    - POST Create a new task (/api/task)
    - GET All labels with their task (/api/task/{id}/labels)
    - POST Link one task to a label (/api/task/{id})
    - DELETE Unlink one task to a label (/api/task/{id})
- Auth
    - POST To register (api/auth/register)
    - POST To register (api/auth/login)

# How to make request

>[!IMPORTANT]
> You must Register and Login, this will automatically set the token for the other requests

Inside of this repository there is a Collection V2 from Postman that you can use it, to check the available request, examples of the payload and execute them.