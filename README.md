# FastMedQ

[![Python](https://img.shields.io/badge/python-v3.9%2B-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.70.0-green)](https://fastapi.tiangolo.com/)
[![FastUI](https://img.shields.io/badge/FastUI-v0.3.0-orange)](https://github.com/fastui/FastUI)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-v13-blue)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**FastMedQ** is a web-based platform for managing doctor appointments. It's built using Python's [FastAPI](https://fastapi.tiangolo.com/) for backend and [FastUI](https://github.com/fastui/FastUI) for frontend integration. The application allows patients to log in, browse available doctors, and schedule visits based on the doctors' shared availability. Doctors can log in to manage their schedule by updating their availability for patient bookings.

Inspired by the functionality of [znanylekarz.pl](https://www.znanylekarz.pl/), FastMedQ aims to streamline the doctor-patient appointment process.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Database Configuration](#database-configuration)
- [Usage](#usage)
  - [Patients](#patients)
  - [Doctors](#doctors)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **User Authentication**: Both patients and doctors can securely log in.
- **Doctor Availability Management**: Doctors can update their available hours for patients.
- **Patient Appointment Scheduling**: Patients can book available time slots with doctors.
- **Doctor Browsing**: Patients can search for doctors based on specialization and location.
- **Real-time Notifications**: Receive alerts when an appointment is booked or updated.
- **Responsive UI**: A clean, user-friendly interface using FastUI.

---

## Technologies Used

- **Programming Language**: Python 3.9+
- **Backend Framework**: FastAPI
- **Frontend Framework**: FastUI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: OAuth2 with JWT tokens
- **Deployment**: Docker and Docker Compose
- **Testing**: Pytest

---
## How it Works?
![uml](assets/UML.png)

---

## Installation

### Prerequisites

Ensure you have the following tools installed:

- Python 3.9 or higher
- PostgreSQL
- Docker (optional, for containerized deployment)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/FastMedQ.git
   cd FastMedQ
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (e.g., database connection settings, secret keys):

   Create a `.env` file in the project root:

   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/fastmedq
   SECRET_KEY=your-secret-key
   ```

5. **Run database migrations:**

   ```bash
   alembic upgrade head
   ```

6. **Start the FastAPI server:**

   ```bash
   uvicorn app.main:app --reload
   ```

---

## Database Configuration

The application uses PostgreSQL as its main database. You'll need to set up the database with the following steps:

1. **Install PostgreSQL** if you haven't already:
   - On Linux: `sudo apt-get install postgresql`
   - On Mac: `brew install postgresql`
   - On Windows: [Download PostgreSQL](https://www.postgresql.org/download/windows/)

2. **Create a PostgreSQL database**:

   ```bash
   psql -U postgres
   CREATE DATABASE fastmedq;
   ```

3. **Update your `.env` file** with the correct database URL.

---

## Usage

Once the application is running, both patients and doctors can interact with the system via the web interface or API.

### Patients

- **Sign Up / Log In**: Patients can create an account or log in to their existing one.
- **Search for Doctors**: Browse or search for doctors by specialization, name, or location.
- **Schedule an Appointment**: Choose from available time slots to book an appointment with a selected doctor.
- **Manage Appointments**: View or cancel upcoming appointments from the dashboard.

### Doctors

- **Sign Up / Log In**: Doctors can log in to their dashboard.
- **Set Availability**: Update available time slots for patient bookings.
- **Manage Appointments**: View scheduled appointments and receive notifications for changes.

---

## API Endpoints

### Authentication
- `POST /auth/signup`: Sign up as a patient or doctor.
- `POST /auth/login`: Log in with email and password to receive a JWT token.

### Patient Routes
- `GET /patients/doctors`: List all available doctors.
- `POST /patients/appointments`: Book an appointment with a doctor.
- `GET /patients/appointments`: View all your upcoming appointments.

### Doctor Routes
- `POST /doctors/availability`: Set or update available slots.
- `GET /doctors/appointments`: View all scheduled appointments.

### Admin Routes
- `GET /admin/users`: View and manage all users in the system.
- `DELETE /admin/users/{id}`: Remove a user by ID.

---

## Contributing

We welcome contributions to **FastMedQ**! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to your fork and submit a pull request.

Please make sure to write tests and follow the project's code style guidelines.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For any inquiries or issues, feel free to reach out:

**Project Maintainers**:
- **Daniil**: [https://github.com/34panda](https://github.com/34panda)
- **Konrad**: [https://github.com/Psyhackological](https://github.com/Psyhackological)

---

Enjoy using **FastMedQ** for streamlined doctor-patient appointment scheduling!
