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

# How to run it

> [!IMPORTANT]
> To run this, you must have Docker installed in your machine

1. Clone the repository
2. Run the following commands

```bash
docker build -t task:latest . 
docker run -p 127.0.0.1:8000:8000 task:latest
```

# How to make request

>[!IMPORTANT]
> You must Register and Login, this will automatically set the token for the other requests

Inside of this repository there is a Collection V2 from Postman that you can use it, to check the available request, examples of the payload and execute them.