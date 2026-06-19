# TECH_SPEC.md – kin‑portal

---

## 1. Overview

**kin‑portal** is a self‑hosted, user‑friendly service platform that simplifies access and management for non‑technical family members.  
The platform allows a *family* to:

- Register and invite members
- Create & share *services* (e.g., appointments, bills, documents)
- Assign *tasks* and track progress
- Receive real‑time *notifications* (email/SMS/Push)
- View a unified dashboard

The product is built on Axentx’s proven stack, fully containerized, and ready for on‑premise or cloud deployment.

---

## 2. Goals & Scope

| Goal | Description |
|------|-------------|
| **Simplicity** | Intuitive UI, minimal setup steps |
| **Self‑hosted** | All data stays on the customer’s infrastructure |
| **Scalable** | Horizontal scaling via Kubernetes |
| **Secure** | End‑to‑end encryption, role‑based access |
| **Extensible** | Plug‑in architecture for future services |
| **Validated** | Built on Axentx’s validated data pipelines |

---

## 3. Architecture Overview

```
┌───────────────────────┐
│  Front‑end (React)    │
└───────┬───────────────┘
        │ REST / GraphQL
┌───────▼───────────────┐
│  API Gateway (FastAPI)│
└───────┬───────────────┘
        │
┌───────▼───────────────┐
│  Service Layer         │
│  - Auth Service        │
│  - Family Service      │
│  - Service Service     │
│  - Task Service        │
│  - Notification Service│
└───────┬───────────────┘
        │
┌───────▼───────────────┐
│  Persistence Layer    │
│  - PostgreSQL 16       │
│  - pgvector (embeddings)│
└───────┬───────────────┘
        │
┌───────▼───────────────┐
│  Cache & Queue         │
│  - Redis 7             │
│  - Celery 5.4 (RabbitMQ)│
└───────┬───────────────┘
        │
┌───────▼───────────────┐
│  External Integrations│
│  - Email (SMTP)        │
│  - SMS (Twilio)        │
│  - Push (FCM)          │
└───────────────────────┘
```

*All components are Docker‑based and orchestrated via Kubernetes.*

---

## 4. Data Model

| Table | Key Fields | Description |
|-------|------------|-------------|
| **users** | id (PK), email, password_hash, role, created_at | Family member record |
| **families** | id (PK), name, created_at | Logical grouping of users |
| **family_members** | id (PK), family_id (FK), user_id (FK), role | Membership role (owner, member) |
| **services** | id (PK), family_id (FK), title, description, status, created_at | Shared service (e.g., “Doctor Appointment”) |
| **tasks** | id (PK), service_id (FK), assignee_id (FK), title, description, due_date, status, created_at | Task linked to
