


The Open Event Server enables organizers to manage events from concerts to conferences and meet-ups.

# open-event-server

### Table of Contents
- [Quickstart](#quickstart)
  * [Clone the project](#clone-the-project)
  * [Create a virtual environment](#create-a-virtual-environment)
  * [Install all requirements](#install-all-requirements)
  * [Configure the database](#configure-the-database)
  * [Test the installation](#test-the-installation)
  * [Test your changes](#test-your-changes)

---

## Quickstart

We're going to install and configure the latest develop build of this API.

### Clone the project

First of all, you need to clone the project on your computer with :

```
git clone https://github.com/cecethea/open-event-server.git
```

You can now move in the newly created folder:

```
cd open_event_server
```

### Create a virtual environment

[Virtualenv](https://virtualenv.pypa.io/) provides an isolated Python environment, which are more practical than installing packages system-wide. They also allow packages to be installed without administrator privileges.

1. Create a new virtual environment
```
virtualenv env
```

2. Activate the virtual environment
```
. env/bin/activate
```

You need to ensure the virtual environment is active each time you want to launch the project.

### Install all requirements

Requirements of the project are stored in the `requirements.txt` file.
You can install them with:

**WARNING** : Make sure your virtual environment is active or you will install the packages system-wide.
```
pip install -r requirements.txt
```

The `requirements-dev.txt` file contains packages that are only needed during
development. You should execute the previous command with this file too, unless
you are deploying in production.

### Configure the database

Django has a system of database migration. You first need to apply all existing "migrations" to update your local database.

```
python manage.py migrate
```

**Note:** The project uses a squlite3 file as database to simplify developement.
Once in production, feel free to switch to whatever suits you.

### Launch the API

You can now launch an instance of the API and visit the built-in admin website.

To login into the admin page, you'll need to create a superuser first:
```
python manage.py createsuperuser
```
Launch a local API instance with:
```
python manage.py runserver
```

You can now visit these links to validate the installation:

- The root of the API: [http://localhost:8000/](http://localhost:8000/),
- The admin site: [http://localhost:8000/admin/](http://localhost:8000/admin),
- The autogenerated documentation: [http://localhost:8000/docs/](http://localhost:8000/docs)

### Test your changes

A python scripts has been created to easily run all unit tests, get code coverage
and validate coding style (pycodestyle). You can use it after making changes to the API:

```
python tests.py
```

### Build the image and run the container
   
   - If buildkit is not enabled, enable it and build the image:
     ```bash
     DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f docker-compose.yml up --build -d
     ```
   
   - If buildkit is enabled, build the image:
     ```bash
     docker-compose -f docker-compose.yml up --build -d
     ```
   
   - Or, use the shortcut:
     ```bash
     make build-dev
     ```

You can now access the application at http://localhost:8000. The development environment allows for immediate reflection of code changes.

### Production Setup

1. **Build the image and run the container:**  

   - If buildkit is not enabled, enable it and build the image:
     ```bash
       DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f docker-compose.prod.yml up --build -d
     ```

   - If buildkit is enabled, build the image:
     ```bash
      docker-compose -f docker-compose.prod.yml up --build -d
     ```
   - Or, use the shortcut:
     ```bash
       make build-prod
     ```

---

## Shortcuts 🔑

This project includes several shortcuts to streamline the development process:

- **Create migrations:**
    ```bash
    make make-migrations
    ```

- **Run migrations:**
    ```bash
    make migrate
    ```

- **Run the linter:**
    ```bash
    make lint
    ```

- **Run the formatter:**
    ```bash
    make format
    ```

- **Run the tests:**
    ```bash
    make test
    ```

- **Create a super user:**
    ```bash
    make super-user
    ```

- **Build and run dev environment:**
    ```bash
    make build-dev
    ```

- **Build and run prod environment:**
    ```bash
    make build-prod
    ```