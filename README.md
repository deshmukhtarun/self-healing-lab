# Self-Healing DevOps Infrastructure Lab

> A local DevOps lab that monitors a containerized app and automatically 
> restarts it when it fails — built with Docker, Prometheus, Grafana, 
> and Python.

## What this does
- Runs a Flask app inside Docker
- Monitors it with Prometheus (metrics) + Grafana (dashboards)
- Fires alerts via Alertmanager when the app crashes
- Auto-restarts the container using a Python healing script

## Stack
`Docker` · `Docker Compose` · `Prometheus` · `Grafana` · 
`Alertmanager` · `Python` · `Flask` · `WSL Ubuntu`

## Status
🔨 In progress — Day 2 of build

## Project Structure
```
self-healing-lab/
├── app/          # Flask application + Dockerfile
├── monitoring/   # Prometheus + Grafana + Alertmanager configs  
├── healing/      # Python self-healing script
├── docs/         # Architecture diagrams
└── docker-compose.yml
```

## How to run (coming soon)
Full setup guide will be added as each phase is completed.