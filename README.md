# EventHub

## Description
EventHub is a platform designed to manage and organize events efficiently. It allows users to create, view, and participate in various events. With a user-friendly interface, EventHub streamlines the event management process for both organizers and attendees. The platform supports features such as event scheduling, ticket booking, notifications, and much more.

## Features
- Event creation and management
- Ticket booking and registration
- Real-time event updates and notifications
- User-friendly interface for event browsing
- Integration with calendars and social media for event sharing

## Technologies Used
- Django (Backend)
- HTML, CSS, JavaScript (Frontend)
- SQLite (Database)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hoowalex/EventHubBackEndV1

2. Navigate to the project directory:

   ```bash
    cd EventHub

3. Create and activate a virtual environment:

   ```bash
    python -m venv venv
    source venv/bin/activate  # For Mac/Linux
    venv\Scripts\activate  # For Windows

4. Install dependencies:

   ```bash
    pip install -r requirements.txt

5. Run migrations to set up the database:

   ```bash
    python manage.py migrate

6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser

7. Start the development server:

   ```bash
    python manage.py runserver

Access the app at http://127.0.0.1:8000/ in your browser.

## License
This project is licensed under the MIT License - see the [LICENSE](./eventhub/LICENSE) file for details.

## Author
- [Oleksii Rudenko](https://github.com/hoowalex)