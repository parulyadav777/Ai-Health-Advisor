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
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/parulyadav777/Ai-Health-Advisor.git
```

### 2. Navigate to the project

```bash
cd Ai-Health-Advisor
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

If using Streamlit Secrets:

```
.streamlit/secrets.toml
```

Add your API credentials there.

**Never upload your API keys to GitHub.**

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📷 Screenshots

Add screenshots here.

Example:

```
screenshots/
├── home.png
├── chatbot.png
├── booking.png
├── admin-dashboard.png
```

Then display them:

```markdown
## Home

![Home](screenshots/home.png)

## Chatbot

![Chatbot](screenshots/chatbot.png)

## Appointment Booking

![Booking](screenshots/booking.png)

## Admin Dashboard

![Admin](screenshots/admin-dashboard.png)
```

---

## 📖 How to Use

1. Launch the application.
2. Register or log in.
3. Describe your symptoms.
4. Receive AI-generated health guidance.
5. Book an appointment with a recommended doctor.
6. View previous conversations.
7. Admin users can manage appointments and doctors.

---

## 🔒 Security

- Environment variables are stored securely.
- API keys are excluded using `.gitignore`.
- Sensitive files are not included in the repository.

---

## 📈 Future Enhancements

- Voice-based interaction
- Medical report analysis
- Medical image analysis
- Multi-language support
- Video consultation
- Email/SMS appointment reminders
- Electronic Health Record (EHR) integration

---

## 👩‍💻 Author

**Parul Yadav**

GitHub: https://github.com/parulyadav777

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
