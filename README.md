# PSU-Sphere — Docker Activity

Source project: https://github.com/Kenzo-gg/PSUSphere

This is a separate classroom Docker containerization exercise based on PSU-Sphere, a Django student-organization management system. The original source repository is unchanged.

## Files

- `Dockerfile` — builds the Django application image
- `docker-compose.yml` — builds/runs the image locally
- `requirements.txt` — retained from the original source repository (Django, Faker and other dependencies)
- `.dockerignore` — excludes unnecessary build files
- `for_client/docker-compose.yml` — pulls the image from Docker Hub
- `docker_settings.py` — container-only override for SQLite and localhost settings; does not edit original `settings.py`

## Run locally (Windows / Docker Desktop)

From the repository root:

```powershell
docker compose up --build
```

Open http://localhost:8000. Initial database migrations run automatically. To create an admin account, from a second terminal:

```powershell
docker compose exec web python manage.py createsuperuser
```

Stop with `Ctrl+C` or `docker compose down`.

## Publish to Docker Hub

Replace `YOUR_DOCKERHUB_USERNAME` below with your actual username:

```powershell
docker login
docker tag psu-sphere:latest YOUR_DOCKERHUB_USERNAME/psu-sphere:latest
docker push YOUR_DOCKERHUB_USERNAME/psu-sphere:latest
```

Also replace `YOUR_DOCKERHUB_USERNAME` in `for_client/docker-compose.yml`.

## Client: Pull and run (no build)

From the repository root:

```powershell
docker compose down
docker compose -f for_client/docker-compose.yml pull
docker compose -f for_client/docker-compose.yml up -d
```

Open http://localhost:8000.

The SQLite database is persisted in a named Docker volume. The local build and client deployment use separate volumes. This setup is for local development/classroom use, not public production hosting.

## Submit

Create a **new** GitHub repository for this activity. Do not submit or change the source repository. Submit the URL of your new repository, including the source code and Docker files above.
