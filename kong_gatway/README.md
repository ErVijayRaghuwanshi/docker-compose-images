# Kong API Gateway with FastAPI Microservices (Learning Project)

This project demonstrates how to use Kong API Gateway to manage and route traffic to three independent Python FastAPI microservices. It is designed for learning and experimentation.

## Project Structure

```
kong-fastapi-demo/
│
├── microservice1/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── microservice2/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── microservice3/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── kong/
│   └── kong.yml
│
├── docker-compose.yml
└── README.md
```

## Components

- **Kong**: Open-source API Gateway that manages routing, authentication, rate limiting, and more.
- **FastAPI Microservices**: Three independent Python services, each exposing a `/ping` endpoint.
- **Postgres**: Database for Kong's configuration.
- **Docker Compose**: Orchestrates the entire stack for easy startup.

## How to Run

1. **Install Docker & Docker Compose** (if not already installed).
2. **Clone or download this repository.**
3. **Start the stack:**

```sh
docker-compose up --build
```

4. **Test the endpoints via Kong:**
   - [http://localhost:8000/service1/ping](http://localhost:8000/service1/ping)
   - [http://localhost:8000/service2/ping](http://localhost:8000/service2/ping)
   - [http://localhost:8000/service3/ping](http://localhost:8000/service3/ping)

5. **Kong Admin API** is available at [http://localhost:8001](http://localhost:8001)

---

## Key Learning Points & Considerations

- **Service Registration**: Each microservice is registered as a Kong service, with its own route.
- **Routing**: Kong maps `/service1`, `/service2`, `/service3` to the respective FastAPI services.
- **Extensibility**: You can add plugins for authentication, rate limiting, CORS, logging, etc., in Kong.
- **Microservice Independence**: Each service is self-contained and can be scaled independently.
- **Declarative Configuration**: Kong is configured using `kong.yml` for reproducibility and clarity.
- **Environment Variables**: Sensitive info (like DB passwords) should be managed securely in production.
- **Healthchecks**: The stack uses healthchecks to ensure services start in the right order.

### Advanced Topics to Explore
- Adding Kong plugins (auth, rate limiting, etc.)
- Securing services with JWT or OAuth2
- Service versioning and blue/green deployments
- Monitoring and logging

---

## Cleanup
To stop and remove all containers, networks, and volumes:
```sh
docker-compose down -v
```

## Troubleshooting
- If ports are already in use, change them in `docker-compose.yml`.
- Ensure Docker Desktop is running.
- For Kong errors, check the Kong Admin API logs.

---

Happy learning!
