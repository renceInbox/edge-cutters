<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">EDGE-CUTTERS</h1>
</p>
<p align="center">
    <em>Unleashing seamless integration for powerful performance.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/renceInbox/edge-cutters?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/renceInbox/edge-cutters?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/renceInbox/edge-cutters?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/renceInbox/edge-cutters?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The Edge Cutters project is a robust software application template leveraging FastAPI and SQLAlchemy for advanced database integration.
It efficiently manages user authentication, permissions, and CRUD operations through well-defined endpoints.
By incorporating token handling and user management features, it ensures secure access control within its architecture.
With seamless Docker containerization and migration handling, the project guarantees smooth deployment and database schema evolution.

---

##  Features

|    | Feature          | Description                                                                                                                                                                                                                                                                                                     |
|----|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture** | The project follows a modular architecture using FastAPI, SQLAlchemy, and StarletteAdvancedAlchemy to provide a robust and scalable backend system for API development. It leverages Docker for containerization and configuration management, ensuring seamless deployment.                                    |
| 🔩 | **Code Quality** | The codebase maintains good quality standards with clear structure and well-documented code. It utilizes Pydantic for data validation, SQLAlchemy for database interactions, and AsyncSession for asynchronous database operations, enhancing code readability and maintainability.                             |
| 📄 | **Documentation** | The project offers extensive documentation covering setup, usage, and architecture details. Detailed descriptions of modules, functions, and configuration files facilitate developers in understanding and contributing to the project effectively.                                                            |
| 🔌 | **Integrations** | Key external dependencies include FastAPI, SQLAlchemy, Alembic, and Pydantic, among others. These integrations enable advanced database management, API routing, schema migrations, and data validation within the project.                                                                                     |
| 🧩 | **Modularity** | The codebase exhibits high modularity with separate modules for authentication, user management, database configurations, and API endpoints. This modular design promotes code reuse, simplifies maintenance, and enhances scalability of the application.                                                      |
| 🧪 | **Testing** | WIP: Testing frameworks like Pytest and tools like pre-commit are used for ensuring code quality and functionality. Automated tests cover various aspects of the project, including API endpoints, database interactions, and authentication mechanisms.                                                        |
| ⚡️  | **Performance** | The project demonstrates efficient resource utilization with asynchronous database operations, optimized pagination methods, and Uvicorn for fast HTTP server performance. The use of SQLAlchemy's advanced features enhances database query efficiency, contributing to overall system performance.            |
| 🛡️ | **Security** | Robust security measures are implemented with user authentication, token handling, role-based access control, and password validation. The project follows best practices for data protection, ensuring secure user interactions and preventing unauthorized access.                                            |
| 📦 | **Dependencies** | Key external libraries and dependencies include FastAPI, SQLAlchemy, psycopg2-binary, and Pydantic. These packages enhance functionality, data management, and API development capabilities within the project.                                                                                                 |
| 🚀 | **Scalability** | The project is designed to handle increased traffic and load through its modular architecture, asynchronous database operations, and efficient API routing. It supports seamless scalability by leveraging advanced features of FastAPI and SQLAlchemy for managing user data and system resources effectively. |

---

##  Repository Structure

```sh
└── edge-cutters/
    ├── README.md
    ├── alembic.ini
    ├── docker
    │   ├── Dockerfile
    │   ├── prestart.sh
    │   └── run.sh
    ├── local.yml
    ├── requirements.txt
    └── src
        ├── __init__.py
        ├── auth
        ├── config
        ├── database
        ├── dependencies.py
        ├── main.py
        ├── routers.py
        ├── schemas.py
        ├── users
        └── utils.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                   |
| ---                                                                                         | ---                                                                                                                                                                                                                                                       |
| [requirements.txt](https://github.com/renceInbox/edge-cutters/blob/master/requirements.txt) | Manages project dependencies vital for seamless operation within the edge-cutters repository architecture. Facilitates compatibility and integration of essential external packages to enhance functionality and performance.                             |
| [local.yml](https://github.com/renceInbox/edge-cutters/blob/master/local.yml)               | Defines volume mappings and services for local development environment. Configures backend and PostgreSQL containers with necessary dependencies and environment variables. Facilitates seamless communication and data persistence between the services. |

</details>

<details closed><summary>src</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                             |
| ---                                                                                           | ---                                                                                                                                                                                                                                 |
| [main.py](https://github.com/renceInbox/edge-cutters/blob/master/src/main.py)                 | Implements FastAPI app with advanced database integration using SQLAlchemy and StarletteAdvancedAlchemy. RouteServiceProvider endpoints via v1_router.                                                                              |
| [schemas.py](https://github.com/renceInbox/edge-cutters/blob/master/src/schemas.py)           | Enables ORM mode for data using limit/offset pagination in the parent repository. Implements a BaseSchema class to extend Pydantics BaseModel and a Generic class for offset pagination with key attributes.                        |
| [dependencies.py](https://github.com/renceInbox/edge-cutters/blob/master/src/dependencies.py) | Provides database session for requests, using SQLAlchemys AsyncSession in the Edge Cutters repositorys architecture.                                                                                                                |
| [routers.py](https://github.com/renceInbox/edge-cutters/blob/master/src/routers.py)           | Defines API routers for authentication and user endpoints in FastAPI, grouped under version 1 (v1), enhancing modularity and readability in the repositorys codebase architecture.                                                  |
| [utils.py](https://github.com/renceInbox/edge-cutters/blob/master/src/utils.py)               | Enables offset/limit pagination in the repositorys architecture by providing a function to calculate pagination values. It supports the `Repository.apply_limit_offset_pagination()` method and enhances data retrieval efficiency. |

</details>

<details closed><summary>docker</summary>

| File                                                                                     | Summary                                                                                                                                  |
| ---                                                                                      | ---                                                                                                                                      |
| [Dockerfile](https://github.com/renceInbox/edge-cutters/blob/master/docker/Dockerfile)   | Builds a Python Docker container, sets environment variables, installs dependencies, and configures entry point for the web application. |
| [prestart.sh](https://github.com/renceInbox/edge-cutters/blob/master/docker/prestart.sh) | Executes prestart tasks like running migrations before app startup, ensuring up-to-date database schema.                                 |
| [run.sh](https://github.com/renceInbox/edge-cutters/blob/master/docker/run.sh)           | Executes the FastAPI application with Uvicorn, specifying the host and port configurations.                                              |

</details>

<details closed><summary>src.auth</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                  |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                      |
| [tokens.py](https://github.com/renceInbox/edge-cutters/blob/master/src/auth/tokens.py)           | Enables authentication and token handling for user access. Validates passwords, creates tokens with expiration, and verifies user credentials. Ensures user permissions match scope. Smoothly integrates with the repositorys user management and security architecture. |
| [models.py](https://github.com/renceInbox/edge-cutters/blob/master/src/auth/models.py)           | Roles have permissions and users; Permissions have roles and users. Utilizes association tables for many-to-many relationships between entities. Facilitates flexible and secure access control in the systems architecture.                                             |
| [permissions.py](https://github.com/renceInbox/edge-cutters/blob/master/src/auth/permissions.py) | Defines role and permission actions as Enums. Provides methods to access permission values. Helps manage access control in the architecture by listing available permissions.                                                                                            |
| [schemas.py](https://github.com/renceInbox/edge-cutters/blob/master/src/auth/schemas.py)         | Defines token and token data schemas for authentication endpoints. Standardizes access token and token type, along with user permissions and username. Ensures consistent data structure for user authentication within the repository.                                  |
| [endpoints.py](https://github.com/renceInbox/edge-cutters/blob/master/src/auth/endpoints.py)     | Enables user authentication, token generation, and retrieval of user details. Implements OAuth2 password flow, user authentication, permissions checking, and token expiry. Uses FastAPI for routing and security measures.                                              |

</details>

<details closed><summary>src.config</summary>

| File                                                                                 | Summary                                                                                                                                 |
| ---                                                                                  | ---                                                                                                                                     |
| [base.py](https://github.com/renceInbox/edge-cutters/blob/master/src/config/base.py) | Defines settings for database URI, token expiry, algorithm, and secret key for the Edge Cutters application. Configured using pydantic. |

</details>

<details closed><summary>src.users</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                       |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                           |
| [models.py](https://github.com/renceInbox/edge-cutters/blob/master/src/users/models.py)             | Defines User model with many-to-many relationships for roles and permissions, including hybrid properties. Supports user authentication and authorization within the repositorys backend architecture.                                                        |
| [permissions.py](https://github.com/renceInbox/edge-cutters/blob/master/src/users/permissions.py)   | Defines user permissions as an Enum for CRUD operations, providing a list of available permissions.                                                                                                                                                           |
| [schemas.py](https://github.com/renceInbox/edge-cutters/blob/master/src/users/schemas.py)           | Defines user-related schemas inheriting from a base schema. Includes fields for user details, ID, and password. Contributes to data validation and structure in repositorys user management system.                                                           |
| [dependencies.py](https://github.com/renceInbox/edge-cutters/blob/master/src/users/dependencies.py) | Provides user repository dependency, ensuring sessions and filtering by deletion status for the parent FastAPI applications users feature.                                                                                                                    |
| [repositories.py](https://github.com/renceInbox/edge-cutters/blob/master/src/users/repositories.py) | Implements user repository using advanced_alchemy to interface with the database. Connects user models to SQLAlchemyAsyncRepository for efficient data operations within the edge-cutters repositorys architecture.                                           |
| [endpoints.py](https://github.com/renceInbox/edge-cutters/blob/master/src/users/endpoints.py)       | Defines user endpoints for CRUD operations with authentication and permissions. Utilizes FastAPI for handling requests, Pydantic for data validation, and custom repositories for data manipulation. Enhances security and scalability in managing user data. |

</details>

<details closed><summary>src.database</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                               |
| ---                                                                                                | ---                                                                                                                                                                                                                                                   |
| [session.py](https://github.com/renceInbox/edge-cutters/blob/master/src/database/session.py)       | Defines AsyncSession and SQLAlchemy configurations using the SQLAlchemy database URI. Resides in src/database and sets up the db_session dependency for the edge-cutters repository.                                                                  |
| [base.py](https://github.com/renceInbox/edge-cutters/blob/master/src/database/base.py)             | Edge-cutters._                                                                                                                                                                                                                                        |
| [base_class.py](https://github.com/renceInbox/edge-cutters/blob/master/src/database/base_class.py) | Defines a common base class for managing new tables within the app. Automatically tracks creation and update timestamps, along with an optional deletion timestamp. Timezones are accurately handled through the use of advanced SQLAlchemy features. |

</details>

<details closed><summary>src.database.migrations</summary>

| File                                                                                                            | Summary                                                                                                                                                                                                                                                                 |
| ---                                                                                                             | ---                                                                                                                                                                                                                                                                     |
| [env.py](https://github.com/renceInbox/edge-cutters/blob/master/src/database/migrations/env.py)                 | Handles offline and online migrations using SQLAlchemy and Alembic. Configures database connection and runs migrations based on context, ensuring smooth migration process. Resolves Heroku PostgreSQL connection issue and supports asynchronous migrations as needed. |
| [script.py.mako](https://github.com/renceInbox/edge-cutters/blob/master/src/database/migrations/script.py.mako) | Generates migration scripts for the database schema evolution with precise upgrade and downgrade paths. Resides in the `src/database/migrations` directory, adding agility to database changes within the larger repository architecture.                               |

</details>

<details closed><summary>src.database.migrations.versions</summary>

| File                                                                                                                                                                                                         | Summary                                                                                                                                                                                       |
| ---                                                                                                                                                                                                          | ---                                                                                                                                                                                           |
| [812c97994acf_setup_default_data.py](https://github.com/renceInbox/edge-cutters/blob/master/src/database/migrations/versions/812c97994acf_setup_default_data.py)                                             | Implements default data setup for user roles and permissions in the database using Alembic migrations. Sets up administrator user, permissions, roles, and their relationships in the system. |
| [406eb81159d5_create_users_roles_and_permissions_table.py](https://github.com/renceInbox/edge-cutters/blob/master/src/database/migrations/versions/406eb81159d5_create_users_roles_and_permissions_table.py) | Creates tables for users, roles, permissions, and their relationships in the database schema using Alembic migrations.                                                                        |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.12.2`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the edge-cutters repository:
>
> ```console
> $ git clone https://github.com/renceInbox/edge-cutters
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd edge-cutters
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run edge-cutters using the command below:
> ```console
> $ uvicorn --host 0.0.0.0 src.main:app
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/renceInbox/edge-cutters/issues)**: Submit bugs found or log feature requests for the `edge-cutters` project.
- **[Submit Pull Requests](https://github.com/renceInbox/edge-cutters/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/renceInbox/edge-cutters/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/renceInbox/edge-cutters
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/renceInbox/edge-cutters/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=renceInbox/edge-cutters">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](LICENSE.txt) file.

[**Return**](#-overview)

---
