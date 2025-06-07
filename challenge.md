# How to run it

> [!IMPORTANT]
> To run this, you must have Docker installed in your machine

1. Clone the repository
2. Run the following commands

```bash
docker build -t task:latest . 
docker run -p 127.0.0.1:8000:8000 task:latest
```
