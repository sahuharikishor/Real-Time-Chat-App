# Real-Time-Chat-App
A simple **Real-Time Chat Application** built using **Django + AJAX (jQuery)**.  
This project allows users to create/join chat rooms and send messages in real-time (WhatsApp-style UI with left/right message alignment).

---

## 🚀 Features

- ✅ Create / Join Chat Rooms
- ✅ Real-time messaging using **AJAX polling**
- ✅ WhatsApp-style UI (Sender Right, Receiver Left)
- ✅ Auto-scroll to latest message
- ✅ Messages stored in database (Django ORM)
- ✅ CSRF Protected (Django security)
- ✅ Responsive UI (Mobile + Desktop)

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Real-time Logic:** AJAX + jQuery (polling)
- **Database:** SQLite (default Django DB)

---

## 📂 Project Structure (Important Files)

- `chat/models.py` → Room & Message models
- `chat/views.py` → Room, send message, fetch messages
- `chat/urls.py` → URL routes
- `templates/home.html` → Home page (join room)
- `templates/room.html` → Chat room UI

---

