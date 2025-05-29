# Issue Tracker for dev teams

A Django-based issue tracking system designed for development teams to efficiently manage and track software issues, bugs, and tasks. This application provides a centralized platform for creating, assigning, and monitoring the progress of issues, fostering better collaboration and streamlining the development workflow.

## Features

* **Issue Management:** Create, view, edit, and delete issues with detailed descriptions.
* **Assignment & Ownership:** Assign issues to specific team members for clear accountability.
* **Status Updates:** Track the progress of issues through customizable status updates (e.g., New, Open, In Progress, Resolved, Closed).
* **Prioritization:** Set priority levels for issues (e.g., Low, Medium, High, Critical) to help teams focus on the most important tasks.
* **User Authentication:** Secure user login and registration to ensure only authorized personnel can access the system.
* **Role-Based Access Control (RBAC):** Define different user roles (e.g., Admin, Developer, Reporter) with varying levels of permissions to manage system access and data.
* **Clean and Intuitive User Interface:** A user-friendly design for efficient navigation and issue management.
* **Collaboration Features:** Facilitate communication and collaboration among team members on specific issues.
* **Search and Filtering:** Easily find issues using search functionalities and various filtering options (by assignee, status, priority, etc.).

## Technologies Used

* **Django:** High-level Python Web framework for rapid development and pragmatic design.
* **Python:** The programming language powering the Django framework.
* **HTML/CSS/JavaScript:** For building the user interface and interactive elements.
* **SQLite (default):** Lightweight database for development. Can be easily configured for PostgreSQL, MySQL, etc., for production.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/issue-tracker.git](https://github.com/your-username/issue-tracker.git)
    cd issue-tracker
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (admin account):**

    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up your username, email, and password.

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/` in your web browser.

## Usage

1.  **Access the application:** Open your web browser and go to `http://127.0.0.1:8000/`.
2.  **Login/Register:**
    * If you're an existing user, log in with your credentials.
    * If you're new, register for an account (if self-registration is enabled, or an administrator can create accounts for you).
3.  **Create Issues:** Once logged in, you can create new issues, providing details like title, description, assignee, status, and priority.
4.  **Manage Issues:** View a list of all issues, filter them, update their status, change priorities, and reassign them as needed.
5.  **Admin Panel:** Access `http://127.0.0.1:8000/admin/` to manage users, roles, and other system settings (requires superuser privileges).

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/your-bug-fix-name`.
3.  Make your changes and commit them with clear, concise messages.
4.  Push your changes to your forked repository.
5.  Create a pull request to the `main` branch of this repository, describing your changes in detail.



If you have any questions or feedback, please feel free to open an issue in this repository or contact Abhay S (abhay31204@gmail.com).
