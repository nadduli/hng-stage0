# Stage 0 Backend API - HNG12

This is a public API developed for **HNG12** Stage 0 Backend task. The API provides basic information including the developer's registered email, current datetime, and the GitHub URL of the project's codebase.

---

## Features

- **Public API:** Accessible via a single GET endpoint.
- **Dynamically Generated Data:** Returns the current datetime in ISO 8601 format (UTC).
- **CORS Support:** Handles Cross-Origin Resource Sharing (CORS).
- **JSON Response:** All responses are in JSON format.

---

## Technology Stack

- **Framework:** FastAPI
- **Programming Language:** Python
- **Deployment:** Railway
- **Dependency Management:** pip

---

## API Documentation

### **Endpoint**
#### Base URL:
`https://hng-stage0-production-0990.up.railway.app/
`GET /

### **Response Format**
- **HTTP 200 OK**

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}

### Deployment
The API is deployed on `https://hng-stage0-production-0990.up.railway.app/

### Useful Links
[Hire Python Developers](https://hng.tech/hire/python-developers)
[Hire C# Developers](https://hng.tech/hire/csharp-developers)
[Hire Golang Developers](https://hng.tech/hire/golang-developers)
[Hire PHP Developers](https://hng.tech/hire/php-developers)
[Hire Java Developers](https://hng.tech/hire/java-developers)
[Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)






