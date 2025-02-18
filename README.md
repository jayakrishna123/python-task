# 📌 Task Management API

A simple **Flask-based Task Management API** that supports task creation, retrieval, updates, and deletion. It also includes **asynchronous notifications** using Python's threading and **real-time updates** using **Server-Sent Events (SSE)**.

## 🚀 Features
- 📌 **CRUD Operations**: Create, Read, Update, and Delete tasks.
- ⚡ **Asynchronous Notifications**: Sends notifications in the background when a task is updated.
- 🔴 **Real-time Updates**: Supports SSE for real-time event streaming.
- 🌐 **RESTful API**: JSON-based API with structured responses.

## 🛠 Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/jayakrishna123/python-task.git
cd task-management-api
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install flask
```

### **4️⃣ Run the Flask Application**
```sh
python app.py
```

The server will start at `http://127.0.0.1:5000`.

---

## 📌 API Endpoints

### 1️⃣ **Get All Tasks**
**Request:** `GET /api/tasks`
```sh
curl -X GET http://127.0.0.1:5000/api/tasks
```
**Response:**
```json
[
  {"id": 1, "title": "Grocery Shopping", "completed": false, "due_date": "2024-03-15"},
  {"id": 2, "title": "Pay Bills", "completed": false, "due_date": "2024-03-20"}
]
```

### 2️⃣ **Create a Task**
**Request:** `POST /api/tasks`
```sh
curl -X POST http://127.0.0.1:5000/api/tasks -H "Content-Type: application/json" -d '{"title": "Write Report", "due_date": "2024-02-20"}'
```
**Response:**
```json
{
  "id": 3,
  "title": "Write Report",
  "completed": false,
  "due_date": "2024-02-20"
}
```

### 3️⃣ **Update a Task (Triggers Async Notification)**
**Request:** `PUT /api/tasks/{task_id}`
```sh
curl -X PUT http://127.0.0.1:5000/api/tasks/3 -H "Content-Type: application/json" -d '{"completed": true}'
```
**Response:**
```json
{
  "id": 3,
  "title": "Write Report",
  "completed": true,
  "due_date": "2024-02-20"
}
```
**Console Output (after 2 sec):**
```
Notification sent for task 3
```

### 4️⃣ **Delete a Task**
**Request:** `DELETE /api/tasks/{task_id}`
```sh
curl -X DELETE http://127.0.0.1:5000/api/tasks/3
```
**Response:**
```json
{"message": "Task deleted"}
```

### 5️⃣ **Real-time Notifications (SSE)**
**Request:** `GET /api/notifications`
```sh
curl -N http://127.0.0.1:5000/api/notifications
```
**Response (on task update):**
```
data: Task 3 updated
```

---

## 🛠 Technologies Used
- **Backend:** Python, Flask
- **Asynchronous Processing:** Python `threading`
- **Real-time Updates:** Server-Sent Events (SSE)
- **Testing:** Postman, `curl`

---

## 📜 License
This project is licensed under the MIT License.

---

## 💡 Future Enhancements
- 🔹 Implement WebSockets for two-way communication.
- 🔹 Add database integration (SQLite/PostgreSQL).
- 🔹 Implement JWT authentication for user security.

---

## 🤝 Contributing
Feel free to fork this repository, create a branch, and submit a pull request with your improvements!

```sh
git checkout -b feature-branch
git commit -m "Added new feature"
git push origin feature-branch
```

Happy Coding! 🚀

