# STORIES.md

## Overview
**Project**: kin‑portal  
**Goal**: Deliver a self‑hosted, user‑friendly service platform that lets non‑technical family members easily access, request, and manage household or personal services.  
**MVP Scope**: Core user flows (onboarding, dashboard, service catalog, request, notifications) + basic admin controls and data safety.

---

## Epics & User Stories

### 1. User Onboarding & Authentication
| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **1.1** | **As a new family member, I want to register with an email and password, so that I can create my personal account.** | • Registration form accepts email, password, and optional name.<br>• Password meets complexity rules (≥8 chars, 1 number, 1 symbol).<br>• Duplicate email is rejected with a clear error.<br>• Successful registration redirects to login page with a “check your email” message. |
| **1.2** | **As a user, I want to log in with my credentials, so that I can access my dashboard.** | • Login form validates email/password.<br>• Incorrect credentials show a generic “invalid credentials” message.<br>• Successful login redirects to `/dashboard` and sets a secure HTTP‑only cookie. |
| **1.3** | **As a user, I want to reset my password via email, so that I can regain access if I forget it.** | • “Forgot password” link sends a time‑limited token email.<br>• Token link leads to a secure reset page.<br>• New password must satisfy complexity rules.<br>• Successful reset redirects to login with a “password updated” notice. |
| **1.4** | **As a user, I want to log out, so that I can securely end my session.** | • Logout button clears session cookie and redirects to `/login`. |

### 2. Dashboard & Service Catalog
| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **2.1** | **As a user, I want to see a personalized dashboard, so that I can quickly view my pending requests and recent activity.** | • Dashboard shows: <br>  • List of active requests (status, date).<br>  • Recent notifications.<br>  • Quick‑action buttons (e.g., “Request Service”). |
| **2.2** | **As a user, I want to browse a catalog of available services, so that I can choose what I need.** | • Catalog page lists services with title, short description, and category.<br> • Search bar filters by keyword.<br> • Pagination or infinite scroll for >20 services. |
| **2.3** | **As a user, I want to view detailed information about a service, so that I can decide whether to request it.** | • Service detail page shows: <br>  • Full description.<br>  • Estimated cost/time.<br>  • Provider contact info.<br>  • “Request Service” button. |

### 3. Service Request Workflow
| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **3.1** | **As a user, I want to submit a service request, so that I can have a task handled by a provider.** | • Request form includes service selection, preferred date/time, and optional notes.<br> • Form validates required fields.<br> • On submit, request status is set to “Pending” and an email is sent to the admin. |
| **3.2** | **As a user, I want to view the status of my requests, so that I know when they are completed.** | • Request list shows status badges (Pending, In‑Progress, Completed, Cancelled).<br> • Clicking a request opens a detail view with timeline updates. |
| **3.3** | **As a user, I want to cancel a pending request, so that I can change my mind.** | • Cancel button available only for “Pending” requests.<br> • Confirmation modal appears.<br> • On cancel, status changes to “Cancelled” and admin is notified. |
| **3.4** | **As a user, I want to attach files to a request, so that I can provide additional context.** | • File upload accepts common formats (PDF, PNG, JPG).<br> • Max size 5 MB per file.<br> • Uploaded files are listed in the request detail. |

### 4. Notifications & Alerts
| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **4.1** | **As a user, I want to receive email notifications for request status changes, so that I stay informed.** | • Email sent on status change (Pending → In‑Progress → Completed).<br> • Email includes request ID, new status, and provider contact. |
| **4
