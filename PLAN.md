# TODO'S

## Current Project - Frontend

`https://codesandbox.io/p/sandbox/react-modal-ecosystem-redux-version-4cmnyy?from-embed`
*  Refactor modals into subfolders to enable modal for create/edit and modal for decompose
*  Create API to call refactor with details

## Next Up

* Handle backend for OpenAI

   - Call OpenAI with details
   - Handle response from OpenAI
      - DB schema
         - Project
         - Tasks / child of project?
* Send OpenAI response to frontend and refresh

* Break Frontend and Backend into different folders

* Learn how to implement tests for front and backend

* Implement Authentication from OAuth with Google

* Learn how to use Docker



# <CENTER>THE PLAN </CENTER>
### 1. **Backend Development with Python**
   - **Framework**: Django for the backend.
   - **Database**: Currently using SQLite3, eventually transition to Postgres
     - Django ORM to interact with DB.
   - **Authentication**: FUTURE: Use OAuth 2.0 with Google's API for authentication. Libraries like `Authlib` or `python-social-auth` can help.

### 2. **Task Decomposition with LLM**
   - Bought tokens with OpenAI's API.

### 3. **CI/CD Pipeline**
   - Use **GitHub Actions** for CI/CD.
   - For deployment, use Docker to containerize your app. Use **Amazon ECR** for image storage and services like **AWS ECS** or **Kubernetes** for deployment.
   - Integrate testing and security checks in your pipeline, such as unit tests (pytest), code quality checks (flake8), and dependency vulnerability scanning (Snyk).

### 4. **Authentication Services (Google Accounts)**
   - Use **Google Identity Services** (OAuth 2.0) for authentication. This provides both web and mobile login options, streamlining user access across platforms.
   - Implement role-based authentication (user, admin, etc.) to differentiate user access levels.

### 5. **Web App Development**
   - Use **React** (with TypeScript for better scalability and maintainability)
   - Use GraphQL (with libraries like **Graphene** for Python) to streamline data fetching, especially if you want flexibility in querying data on both mobile and web clients.

### 6. **Mobile App Development**
   - Use **React Native** to build both iOS and Android apps using a single codebase. This will speed up development and make it easier to maintain consistency between platforms.
   - Integrate Google OAuth into the mobile apps for seamless authentication.

### 7. **GraphQL**
   - GraphQL can be highly useful for this project. It allows clients (web and mobile) to request specific data structures, reducing over-fetching and under-fetching of data, which is common in REST.
   - You can use **Graphene** (Python GraphQL library) to define your API and integrate it with Django or Flask.

### 8. **Task Management Features**
   - Task CRUD (Create, Read, Update, Delete) operations.
   - Task dependencies: A system where tasks can be linked or broken into subtasks.
   - Notifications for deadlines or task updates.
   - Integrate natural language inputs for tasks and use LLMs to break them into smaller steps automatically.

---

This setup provides flexibility, scalability, and a modern stack for building a task tracker. Do you have a preferred cloud provider, or would you like more advice on setting up the mobile side?
