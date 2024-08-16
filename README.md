# django_crm

---

# **Django Client Management**

This project is a web application for client management built with Django. The application includes authentication features, a dashboard for client management, and allows creating, reading, updating, and deleting client information.

## **Features**

- **User Authentication**: Sign Up, Login, Logout
- **User Management**: User creation and management
- **Dashboard**: Overview of all clients
- **Client CRUD**: Create, Read, Update, Delete client information

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/memlens/django_crm.git
   cd project-name
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply the migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## **Usage**

- Access the application via `http://127.0.0.1:8000/`
- Log in with your credentials to access the dashboard
- Manage clients from the dashboard (create, update, delete)

## **Technologies Used**

- **Django**: Web framework for Python
- **Bootstrap**: CSS framework for responsive design
- **SQLite**: Database used for development

## **Contributing**

Contributions are welcome! Please create a new branch for any changes and submit a pull request.

1. **Fork the project**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/feature-name
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Added a new feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/feature-name
   ```
5. **Open a Pull Request**

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

N'oubliez pas de mettre à jour les informations spécifiques avant de publier sur GitHub !
