# Accounts Microservice

[![CI Build](https://github.com/sumitkale888/github-final-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/sumitkale888/github-final-project/actions/workflows/ci-build.yaml)

## Project Name
**Accounts Microservice**

A Flask-based RESTful Accounts service demonstrating Test Driven Development, Continuous Integration, security headers, CORS, Docker containerization, Kubernetes deployment preparation, and DevOps practices.

## REST API
- `POST /accounts` — Create an account
- `GET /accounts` — List all accounts
- `GET /accounts/<id>` — Read an account
- `PUT /accounts/<id>` — Update an account
- `DELETE /accounts/<id>` — Delete an account

## CI
GitHub Actions checks out the repository, installs dependencies, runs Flake8 linting, and executes the unit tests with nose.

## Run locally
```bash
pip install -r requirements.txt
gunicorn --bind=0.0.0.0:8080 service:app
```
