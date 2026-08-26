# SewLink

## Connecting Customers With Skilled Tailors

SewLink is a Django-based tailoring marketplace that connects customers with tailors. Customers can create tailoring jobs, discover tailors, and track their work, while tailors can browse available jobs, accept customer requests, manage their services and portfolios, and track job progress.

The project is being developed as a full-stack marketplace system with plans for messaging, notifications, reviews, payments, advanced search, recommendations, security hardening, deployment, and AI-powered features.

---

## Project Vision

The goal of SewLink is to create a trusted digital marketplace where customers can easily find suitable tailors and tailors can discover new customers and manage their work professionally.

The platform is designed around two primary users:

### Customers

Customers can:

* Create accounts
* Manage their profiles
* Create tailoring jobs
* Specify budgets and deadlines
* Upload reference images
* Browse available tailors
* Search for tailors
* View tailor profiles
* Track their jobs
* View job status

### Tailors

Tailors can:

* Create accounts
* Manage their profiles
* Create and manage services
* Create and manage portfolios
* Browse customer jobs
* View job details
* Accept jobs
* Reject jobs
* Manage accepted jobs
* Start jobs
* Complete jobs
* Monitor their dashboard statistics

---

# Technology Stack

## Backend

* Python
* Django
* Django ORM
* SQLite during development
* PostgreSQL planned for production

## Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

## Development Tools

* Visual Studio Code
* Git
* GitHub
* Django Development Server

## Media

* Pillow
* Django ImageField
* Local media storage during development

---

# Project Architecture

SewLink follows a modular Django architecture.

The major applications are:

```
SewLink/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── AuthenticationApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── CustomerApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── TailorApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── JobApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── AdminApp/
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

Each application has a specific responsibility rather than putting the entire system into one Django app.

---

# Core System Flow

The main marketplace workflow is:

```
Customer
    ↓
Creates Job
    ↓
Job becomes Open
    ↓
Tailor Browses Jobs
    ↓
Tailor Views Job
    ↓
Tailor Accepts Job
    ↓
Job becomes Accepted
    ↓
Tailor Starts Work
    ↓
Job becomes In Progress
    ↓
Tailor Completes Work
    ↓
Job becomes Completed
```

This workflow forms the foundation of SewLink.

---

# Job Status System

SewLink currently supports:

* Open
* Pending
* Accepted
* Rejected
* In Progress
* Completed
* Cancelled

The primary workflow is:

```
Open → Accepted → In Progress → Completed
```

Rejected and cancelled jobs represent alternative outcomes.

---

# Core Models

## CustomerProfile

Stores customer-specific information connected to Django's authentication user.

A customer can have multiple jobs.

Relationship:

```
User
  ↓
CustomerProfile
  ↓
Jobs
```

---

## TailorProfile

Stores information about a tailor.

A tailor can have:

* Multiple services
* Multiple portfolio items
* Multiple jobs

Relationship:

```
User
  ↓
TailorProfile
   ├── Services
   ├── Portfolio
   └── Jobs
```

---

## Service

Represents a service offered by a tailor.

Examples:

* Dress making
* Suit making
* Clothing alteration
* Embroidery
* Clothing repair

A tailor can create multiple services.

---

## Portfolio

Stores examples of a tailor's previous work.

Portfolio items can contain images and other information describing the work.

---

## Job

The Job model is the central marketplace object.

A job contains:

* Customer
* Tailor
* Service
* Title
* Description
* Category
* Budget
* Agreed price
* Deadline
* Requested date
* Location
* Reference image
* Status
* Creation date
* Updated date

---

# Job Categories

SewLink currently supports:

* Tailoring
* Clothing Alteration
* Clothing Repair
* Embroidery
* Clothing Design
* Other

---

# Customer Features

## Customer Dashboard

The customer dashboard provides an overview of the customer's activity.

It includes:

* Active jobs
* Completed jobs
* Orders
* Messages
* Recent jobs

---

## Customer Job Management

Customers can:

* Create jobs
* View jobs
* Edit jobs
* Delete jobs
* View job details
* Track job status

---

## Tailor Discovery

Customers can search for tailors based on information such as:

* Business name
* Tailor name
* Location

Customers can also open a tailor's profile and inspect their available information.

---

# Tailor Features

## Tailor Dashboard

The tailor dashboard provides an overview of marketplace activity.

It displays:

* Open jobs
* Accepted jobs
* Jobs in progress
* Completed jobs
* Recent jobs

---

## Tailor Marketplace

Tailors can browse customer jobs that are currently available.

They can inspect:

* Job title
* Description
* Category
* Budget
* Location
* Deadline
* Reference image
* Customer information

---

## Job Acceptance

A tailor can accept an available job.

When accepted:

```
job.tailor = tailor
job.status = accepted
```

The job then becomes associated with that tailor.

---

## Job Rejection

A tailor can reject an available job.

Rejected jobs are not treated as active work for that tailor.

---

## Job Progression

After accepting a job, the tailor can move it through the workflow:

```
Accepted
    ↓
In Progress
    ↓
Completed
```

---

# Tailor Services

Tailors can:

* Create services
* View services
* Edit services
* Delete services

Services allow customers to understand what a tailor specializes in.

---

# Tailor Portfolio

Tailors can:

* Add portfolio items
* Upload images
* View portfolio items
* Edit portfolio items
* Delete portfolio items

The portfolio provides visual evidence of a tailor's previous work.

---

# Authentication

SewLink uses Django authentication.

The authentication system is responsible for:

* Registration
* Login
* Logout
* User sessions
* Authentication protection

Protected views use Django's login requirement so that users cannot access private areas without authenticating.

---

# Authorization

Authentication answers:

```
"Who are you?"
```

Authorization answers:

```
"What are you allowed to access?"
```

SewLink uses object-level ownership checks.

For example, a tailor should only be able to manage their own services and portfolio items.

Similarly, customers should only manage their own jobs.

This is an important security principle for the platform.

---

# URL Structure

The major URL namespaces include:

```
/auth/
/customer/
/tailor/
/jobs/
/adminpanel/
```

Examples:

```
/customer/dashboard/
/customer/profile/
/customer/tailors/

/tailor/dashboard/
/tailor/services/
/tailor/portfolio/

/jobs/
/jobs/create/
/jobs/<id>/
/jobs/tailor/jobs/
/jobs/tailor/my-jobs/
```

---

# Frontend Design

SewLink uses independent HTML and CSS files.

The interface follows a professional marketplace design rather than a basic Django-admin appearance.

Design principles include:

* Dark mode as the default
* Light mode support
* White text in dark mode
* Black text in light mode
* Dark neutral backgrounds
* Professional spacing
* Clear typography
* Responsive layouts
* Reusable UI patterns
* Minimal visual clutter

JavaScript is used where interactive behavior is required, including theme switching.

---

# Theme System

SewLink supports:

```
Dark Mode
Light Mode
```

Dark mode is the default experience.

The theme preference can be stored on the client side so that the selected theme remains available when the user returns to the application.

---

# Security Principles

Security is a major part of the long-term SewLink architecture.

The application should protect against:

* Unauthorized object access
* CSRF attacks
* XSS
* SQL injection
* Unsafe file uploads
* Session abuse
* Privilege escalation
* Improper authorization

Django's built-in security mechanisms are used wherever possible.

---

# Development Setup

## 1. Clone the project

```
git clone <repository-url>

cd SewLink
```

## 2. Create a virtual environment

```
python -m venv .venv
```

## 3. Activate the environment

Windows PowerShell:

```
.venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```
pip install -r requirements.txt
```

## 5. Apply migrations

```
python manage.py makemigrations

python manage.py migrate
```

## 6. Create an administrator

```
python manage.py createsuperuser
```

## 7. Start the development server

```
python manage.py runserver
```

The application will then be available through the Django development server.

---

# Database

SQLite is currently used during development because it is simple and convenient for rapid development.

PostgreSQL is planned for production.

The production database architecture will eventually include:

* PostgreSQL
* Database indexes
* Query optimization
* Connection management
* Backup strategy
* Data integrity controls

---

# Git Workflow

The project uses Git for version control.

A typical workflow is:

```
git status

git add .

git commit -m "Describe the change"

git push
```

Commits should describe meaningful changes.

Examples:

```
Add customer profile

Implement tailor job acceptance

Add tailor dashboard statistics

Add job status progression

Add dashboard dark mode
```

---

# Development Phases

## Phase 1 — Core Marketplace

Status: Completed

Implemented:

* Authentication
* Customer system
* Tailor system
* Customer profiles
* Tailor profiles
* Job creation
* Job marketplace
* Job details
* Job editing
* Job deletion
* Tailor search
* Tailor profiles
* Tailor services
* Tailor portfolio
* Job acceptance
* Job rejection
* Accepted jobs
* Job progression
* Customer dashboard
* Tailor dashboard
* Dashboard statistics
* Recent jobs
* Dark/light mode foundation

---

# Phase 2 — Communication & Job Management

Status: Next

Planned:

* MessagingApp
* Customer-tailor conversations
* Inbox
* Chat interface
* Unread messages
* Notifications
* Job activity notifications
* Improved job tracking
* Better customer job history
* Improved tailor job management

---

# Phase 3 — Marketplace Intelligence & Trust

Planned:

* Ratings
* Reviews
* Tailor reputation
* Advanced tailor search
* Service marketplace
* Favorites
* Tailor availability
* Verified tailor accounts
* Tailor recommendations
* Better marketplace discovery

The objective of Phase 3 is to improve trust and matching between customers and tailors.

---

# Phase 4 — Orders & Payments

Planned:

* Orders
* Order IDs
* Agreed prices
* Payment records
* M-Pesa integration
* Payment confirmation
* Transaction history
* Payment status
* Order lifecycle

The objective is to turn accepted jobs into structured commercial transactions.

---

# Phase 5 — Production & Security

Planned:

* PostgreSQL
* Linux server
* Gunicorn
* Nginx
* HTTPS
* Domain deployment
* Environment variables
* Production media storage
* Logging
* Error monitoring
* Rate limiting
* Security hardening
* Database optimization
* Caching
* Pagination
* Performance optimization
* CI/CD

The objective is to transform the development application into a production-ready platform.

---

# Phase 6 — AI

Planned AI capabilities include:

### Intelligent Tailor Recommendations

Match customers with suitable tailors based on:

* Location
* Services
* Ratings
* Previous jobs
* Price
* Availability

### AI Job Assistant

Help customers create clear and complete job descriptions.

### Smart Pricing

Estimate reasonable prices based on historical marketplace data.

### Design Assistant

Help customers describe clothing designs and generate design concepts.

### Fraud Detection

Identify potentially suspicious marketplace activity.

---

# Future Architecture

The long-term architecture is expected to evolve toward:

```
Frontend
    ↓
Django / REST API
    ↓
Business Logic
    ↓
PostgreSQL
    ↓
Background Workers
    ↓
Notifications / Payments / AI
```

Additional infrastructure may eventually include:

* Django REST Framework
* Redis
* Celery
* Object storage
* Payment APIs
* Email services
* WebSockets
* AI APIs

---

# Important Engineering Principles

SewLink is being developed around several principles.

## Separation of Concerns

Each Django app should have a clear responsibility.

## Security First

Users must never be trusted simply because they can manipulate a URL or submit a form.

Every sensitive operation requires authorization.

## Database Integrity

Relationships and constraints should prevent invalid marketplace states.

## Maintainability

Code should remain readable and modular as the project grows.

## Scalability

Architecture decisions should avoid unnecessarily coupling unrelated systems.

## User Experience

The platform should remain simple for customers and tailors despite increasing functionality.

---

# Current Project Status

SewLink has completed its first major development stage.

The fundamental marketplace workflow is operational:

```
Customer
    ↓
Creates Job
    ↓
Tailor Browses Job
    ↓
Tailor Accepts Job
    ↓
Tailor Manages Job
    ↓
Job In Progress
    ↓
Job Completed
```

The next major milestone is **Phase 2: Messaging and Notifications**.

---

# Project Goal

SewLink is intended to evolve from a university Django project into a realistic marketplace platform demonstrating:

* Full-stack development
* Django architecture
* Database design
* Authentication
* Authorization
* REST APIs
* Software engineering
* Cybersecurity
* Payment integration
* Deployment
* Cloud architecture
* AI integration
* Marketplace system design

The long-term objective is to build a platform that solves a real problem for both customers and tailoring businesses.

---

# License

This project is currently developed as a personal software engineering project.

License and contribution guidelines can be added when the project is prepared for public release.
