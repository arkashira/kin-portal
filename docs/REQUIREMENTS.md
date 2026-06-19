# REQUIREMENTS.md  

**Project:** kin-portal  
**Owner:** AxentX – Product Engineering  
**Version:** 1.0.0  
**Last Updated:** 2026‑06‑19  

---  

## 1. Overview  

kin-portal is a self‑hosted, web‑based service platform that enables non‑technical family members to easily access, organize, and manage shared digital resources (photos, documents, calendars, contacts, and third‑party services). The portal must be installable on a home server or low‑cost VPS, provide a clean UI, and expose a minimal set of administrative controls for a primary “Family Admin” while allowing delegated, permission‑scoped access for other members.

---  

## 2. Glossary  

| Term | Definition |
|------|------------|
| **Family Admin** | Primary account that can create families, invite members, configure permissions, and manage system settings. |
| **Member** | Any user invited to a family; may have roles: *Viewer*, *Contributor*, *Moderator*. |
| **Portal Instance** | A running deployment of kin-portal (Docker container, VM, or bare‑metal). |
| **Resource** | Digital asset managed by the portal (photo album, document folder, calendar, contact list, linked external service). |
| **API** | RESTful JSON API used by the front‑end and optional third‑party integrations. |

---  

## 3. Functional Requirements  

| ID | Requirement | Description |
|----|-------------|-------------|
| **FR‑1** | **Self‑Hosted Deployment** | The system must be installable via a single Docker Compose file or a Helm chart. It must run on Linux (Ubuntu 22.04+, Debian 12) and support ARM64 and x86_64 architectures. |
| **FR‑2** | **User Management** | - Family Admin can create a *Family* entity and invite members by email. <br> - Invitation links expire after 48 h. <br> - Members can reset passwords via a secure token flow. |
| **FR‑3** | **Role‑Based Access Control (RBAC)** | Three built‑in roles (Viewer, Contributor, Moderator) with the following permissions: <br> • Viewer – read‑only access to all resources. <br> • Contributor – read/write on resources they own or are shared with. <br> • Moderator – all Contributor rights + ability to delete any resource within the family. |
| **FR‑4** | **Resource Types** | The portal must support: <br> • **Photos** – upload, album organization, thumbnail generation. <br> • **Documents** – PDF, DOCX, TXT preview, versioning. <br> • **Calendar** – shared events, RSVP, reminders. <br> • **Contacts** – import/export vCard, group tagging. <br> • **External Links** – OAuth‑based integration with at most three third‑party services (e.g., Google Photos, Dropbox, Zoom). |
| **FR‑5** | **Web UI** | Responsive SPA built with React (or Svelte) that works on desktop and mobile browsers. Must provide: <br> • Dashboard overview (recent activity, upcoming events). <br> • Simple navigation between resource sections. <br> • Inline editing where appropriate. |
| **FR‑6** | **Search** | Full‑text search across all resource metadata (titles, tags, captions) with fuzzy matching. Must return results within 500 ms for a dataset of up to 100 k items. |
| **FR‑7** | **Notifications** | Email and in‑app push notifications for: <br> • New invitations. <br> • Resource shares. <br> • Calendar event changes. |
| **FR‑8** | **Backup & Restore** | Admin can trigger a manual backup (SQL dump + uploaded files) and restore from a backup file via the UI or CLI. |
| **FR‑9** | **Audit Log** | Immutable log of all privileged actions (user creation, role changes, deletions) retained for at least 90 days. |
| **FR‑10** | **API** | Public REST API (OpenAPI 3.0) covering all CRUD operations for resources and user management. Must require JWT‑based authentication. |
| **FR‑11** | **Internationalization (i18n)** | UI strings externalized; at minimum English and Spanish language packs shipped. |
| **FR‑12** | **Installation Wizard** | First‑run wizard that guides the admin through: <br> • Database configuration (SQLite default, optional PostgreSQL). <br> • Admin account creation. <br> • Optional domain/HTTPS setup. |

---  

## 4. Non‑Functional Requirements  

| ID | Category | Requirement |
|----|----------|-------------|
| **NFR‑1** | **Performance** | • API 95th‑percentile latency ≤ 200 ms for read operations under 100 concurrent users. <br> • Photo thumbnail generation ≤ 150 ms per image (256 px). |
| **NFR‑2** | **Scalability** | System must support horizontal scaling of the web and API services behind a load balancer; stateful components (DB, file storage) remain single‑node for the baseline release. |
| **NFR‑3** | **Security** | • All traffic encrypted with TLS 1.3. <br> • Passwords stored with Argon2id (memory ≥ 64 MiB, parallelism ≥ 2). <br> • CSRF protection on all state‑changing endpoints. <br> • OWASP Top‑10 compliance. |
| **NFR‑4** | **Reliability** | • Uptime ≥ 99.5 % (excluding planned maintenance). <br> • Automatic restart of containers on failure (Docker restart policy). |
| **NFR‑5** | **Data Privacy** | • GDPR‑compliant data deletion: admin can purge a member’s personal data on request. |
| **NFR‑6** | **Maintainability** | • Codebase follows AxentX Python/Node style guide. <br> • 80 %+ unit test coverage; integration tests for all API endpoints. |
| **NFR‑7** | **Observability** | • Export Prometheus metrics (request latency, error rates). <br> • Log in JSON format with correlation IDs. |
| **NFR‑8** | **Portability** | Docker image ≤ 350 MB; supports multi‑arch builds. |
| **NFR‑9** | **Accessibility** | UI meets WCAG 2.1 AA criteria (keyboard navigation, ARIA labels, contrast). |
| **NFR‑10** | **Backup Retention** | Backups stored in a configurable location; retention policy default 30 days, configurable up to 365 days. |

---  

## 5. Constraints  

1. **Technology Stack** – Must use the verified AxentX frameworks where applicable:  
   - Backend: Python 3.11 with FastAPI (leveraging `vLLM` for any future LLM‑based assistance).  
   - Frontend: React 18 (or Svelte if justified).  
2. **Licensing** – All third‑party libraries must be compatible with Apache‑2.0 or MIT licenses.  
3. **Resource Limits** – Target hardware for a typical family: 2 CPU cores, 4 GiB RAM, 100 GiB storage. The system must operate within these limits.  
4. **Data Sources** – Only the internal datasets listed in the AxentX knowledge base may be used for any ML‑assisted features (e.g., auto‑tagging photos).  
5. **Release Cadence** – MVP must be deliverable within 8 weeks from project kickoff.  

---  

## 6. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | Users will have basic email access for invitations and password resets. |
| **A‑2** | Families will not exceed 50 members in the MVP; scaling beyond that is out of scope for the initial release. |
| **A‑3** | External service integrations will use OAuth 2.0 with client‑secret stored in the portal’s secret store. |
| **A‑4** | The deployment environment provides a persistent volume for uploaded files. |
| **A‑5** | No real‑time video conferencing is required; calendar events only store meeting links. |
| **A‑6** | The product will be sold as a self‑hosted solution; no SaaS hosting is provided by AxentX at launch. |

---  

## 7. Acceptance Criteria  

1. A fresh Docker Compose deployment on Ubuntu 22.04 completes the installation wizard without errors.  
2. Family Admin can create a family, invite two members, and assign distinct roles.  
3. All three resource types (photos, documents, calendar) can be created, edited, and deleted according to RBAC rules.  
4. Search returns correct results within the performance target.  
5. Security scans (e.g., OWASP ZAP) report no critical findings.  
6. Automated test suite passes (≥ 80 % coverage) and CI pipeline builds the multi‑arch Docker image.  

---  

*Prepared by:* Senior Product/Engineering Lead – AxentX  
*Document ID:* KIN‑PORTAL‑REQ‑v1.0
