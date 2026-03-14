# Self-Healing DevOps Infrastructure Lab

> A production-style local DevOps lab that monitors a containerized Flask app 
> and automatically restarts it on failure — built with Docker, Prometheus, 
> Grafana, Alertmanager, and Python. No cloud account needed.

![Status](https://img.shields.io/badge/status-in--progress-yellow)
![Docker](https://img.shields.io/badge/docker-compose-blue)
![Python](https://img.shields.io/badge/python-3.11-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## What Problem Does This Solve?

In real companies, services crash. Without monitoring and automation, 
someone gets paged at 2am to manually restart a container. This lab 
builds the system that eliminates that — the app detects its own failure 
and heals itself.

---

## Architecture
```
┌─────────────────────────────────────────────────┐
│              Docker Network                      │
│                                                  │
│  ┌──────────┐    metrics   ┌────────────────┐   │
│  │ Flask App│─────────────▶│  Prometheus    │   │
│  │ :5000    │              │  :9090         │   │
│  └──────────┘              └───────┬────────┘   │
│       ▲                            │             │
│       │ restart               alerts│             │
│       │                            ▼             │
│  ┌────┴──────┐              ┌────────────────┐   │
│  │  Healing  │◀─────────────│ Alertmanager   │   │
│  │  Script   │    webhook   │  :9093         │   │
│  └───────────┘              └───────┬────────┘   │
│                                     │             │
│                             ┌───────▼────────┐   │
│                             │    Grafana     │   │
│                             │    :3000       │   │
│                             └────────────────┘   │
└─────────────────────────────────────────────────┘
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Docker + Compose | Container orchestration |
| Flask (Python) | Sample monitored application |
| Prometheus | Metrics collection and storage |
| Grafana | Visual dashboards and graphs |
| Alertmanager | Alert routing on threshold breach |
| Python script | Self-healing automation |

---

## Project Phases

- [x] Phase 1 — Flask app running in Docker with health check endpoint
- [ ] Phase 2 — Prometheus scraping app metrics
- [ ] Phase 3 — Grafana dashboard for uptime and request rate
- [ ] Phase 4 — Alertmanager firing on app crash
- [ ] Phase 5 — Python healing script auto-restarting failed container

---

## Project Structure
```
self-healing-lab/
├── app/
│   ├── app.py              # Flask application
│   ├── Dockerfile          # Container definition
│   └── requirements.txt    # Python dependencies
├── monitoring/
│   ├── prometheus.yml      # Scrape config (coming Phase 2)
│   ├── alert.rules.yml     # Alert definitions (coming Phase 4)
│   └── grafana/            # Dashboard JSON exports (coming Phase 3)
├── healing/
│   └── heal.py             # Auto-restart script (coming Phase 5)
├── docs/
│   └── architecture.md     # Detailed architecture notes
├── docker-compose.yml      # Full stack definition
└── README.md
```

---

## How to Run (Phase 1)

### Prerequisites
- Docker + Docker Compose installed
- Linux / WSL Ubuntu

### Run the app
```bash
git clone https://github.com/deshmukhtarun/self-healing-lab.git
cd self-healing-lab
docker compose up --build -d
```

### Test it
```bash
curl http://localhost:5000/health
# Expected: {"healthy": true}

curl http://localhost:5000/
# Expected: {"status": "running", "uptime": 4.2}
```

---

## Why I Built This

I'm learning DevOps through project-based work. This project covers the 
core skills companies actually need: containerization, observability, 
alerting, and automation. Each phase adds a real layer of production 
infrastructure — locally, with zero cloud cost.

---

## License

MIT