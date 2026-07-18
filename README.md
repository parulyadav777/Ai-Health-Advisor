# 🩺 AI Health Advisor

An AI-powered healthcare assistant built with **Streamlit** that helps users analyze symptoms, receive AI-generated health guidance, and book doctor appointments through an interactive chat interface.

> **Disclaimer:** This application is intended for educational and demonstration purposes only. It does **not** replace professional medical advice, diagnosis, or treatment.

---

## 📌 Features

- 🤖 AI-powered health chatbot
- 💬 Interactive chat interface
- 🩺 Symptom-based health guidance
- 📅 Doctor appointment booking
- 👨‍⚕️ Doctor recommendation based on specialty
- 🔐 User authentication
- 📊 Admin dashboard
- 🗂️ SQLite database integration
- 📜 Chat history management
- 🎨 Clean and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

**Frontend**
- Streamlit

**Backend**
- Python

**Database**
- SQLite

**AI Model**
- OpenRouter API
- Mistral 7B Instruct (Free)

**Libraries**
- Streamlit
- SQLite3
- Requests
- Python Dotenv
- Pandas

---

## 📂 Project Structure

```
AI-Health-Advisor/
│
├── app.py
├── backend.py
├── database.py
├── ai_booking.py
├── book_appointment.py
├── save_appointments.py
├── init_db.py
├── make_admin.py
├── cleanup_appointments.py
│
├── pages/
│   ├── 2_Chat.py
│   └── Admin_Dashboard.py
│
├── .gitignore
├── README.md
├── requirements.txt
│
└── database files
