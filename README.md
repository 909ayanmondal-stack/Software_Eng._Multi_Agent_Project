# 🚀 Software Engineering Multi-Agent Project

An advanced FastAPI-based backend system implementing authentication, user management, and secure APIs using JWT authentication and MongoDB. This project follows a modular, scalable backend architecture similar to production-grade systems.

---

## 📌 Features
- User Registration & Login  
- JWT Authentication (Secure Token System)  
- Password Hashing (bcrypt / passlib)  
- Protected User Profile API  
- Change Password Feature  
- MongoDB Database Integration  
- Modular FastAPI Router Structure  
- Swagger UI API Documentation  

---

## 🏗️ Tech Stack
- FastAPI  
- MongoDB  
- JWT (PyJWT)  
- Uvicorn  
- Python  
- Passlib / bcrypt  

---

## 📁 Project Structure
Software_Eng._Multi_Agent_Project/
│
├── API/
│   ├── auth.py
│   ├── models.py
│   ├── utils.py
│   └── dependencies.py
│
├── main.py
├── requirements.txt
└── .env (not included)

---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone https://github.com/909ayanmondal-stack/Software_Eng._Multi_Agent_Project.git  
cd Software_Eng._Multi_Agent_Project  

### 2. Create Virtual Environment
python -m venv venv  
source venv/bin/activate (Mac/Linux)  
venv\Scripts\activate (Windows)  

### 3. Install Dependencies
pip install -r requirements.txt  

### 4. Setup Environment Variables
Create a `.env` file:

SECRET_KEY=your_secret_key  
ALGORITHM=HS256  
MONGODB_URL=your_mongodb_connection_string  

### 5. Run Application
uvicorn API.main:app --reload  

---

## 📡 API Endpoints

### Register User
POST /auth/register  

### Login User
POST /auth/login  

### Get Profile (Protected)
GET /auth/profile  
Authorization: Bearer <token>  

### Change Password (Protected)
POST /auth/change-password  

---

## 🔐 Authentication Flow
User registers → User logs in → JWT token generated → Token used for protected routes → Server validates token using SECRET_KEY

---

## 🧪 Example Requests

### Register
{
  "username": "ayan",
  "email": "ayan@example.com",
  "password": "123456"
}

---

### Login (Form Data)
username: ayan  
password: 123456  

---

### Change Password
{
  "old_password": "123456",
  "new_password": "newpass123"
}

---

## 🚀 Future Improvements
- Refresh Token System  
- Role-Based Access Control  
- Docker Deployment  
- Logging System  
- Unit Testing  

---

## ⚠️ Security Notes
- Never upload `.env` file  
- Never expose SECRET_KEY  
- Always hash passwords  
- Use HTTPS in production  

---

## 👨‍💻 Author
Ayan Mondal
NIT KURUKSHETRA
GitHub: https://github.com/909ayanmondal-stack  

---

## 📜 License
MIT License
