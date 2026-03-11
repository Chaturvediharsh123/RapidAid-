# 🚨 AI Civic Command Center

AI-powered civic complaint intelligence platform that allows citizens to report issues, automatically analyzes complaints using AI agents, prioritizes emergencies, and routes them to the appropriate government department.

---

# 🌐 Web Interface

Below is the command center dashboard used to register complaints and monitor civic issues.

![AI Civic Command Center UI](ui.png)

The dashboard allows users to:

- 📞 Register civic complaints
- 🧠 Automatically detect issue type
- 📍 Extract complaint location
- 🚨 Determine complaint priority
- 🏛 Assign responsible department

---

# 🏗 System Architecture

The system processes citizen complaints through an AI-powered pipeline.


Citizen Complaint
↓
Twilio Voice Gateway
↓
FastAPI Call Server
↓
AI Processing Pipeline
↓
LLM Agent (Issue Detection)
↓
Analytics Agent (Priority Detection)
↓
Routing Agent (Department Assignment)
↓
SQLite Complaint Database
↓
Streamlit Civic Command Dashboard


---

# ✨ Features

- 🤖 AI-powered complaint understanding  
- 🚨 Emergency detection and priority classification  
- 🏛 Automatic department routing  
- 📊 Real-time complaint analytics  
- 🖥 Civic command center dashboard  

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------|------|
Python | Core programming language |
FastAPI | Backend API server |
Streamlit | Web dashboard |
Twilio | Phone call integration |
SQLite | Complaint database |
Pandas | Data analytics |

---

# 📂 Project Structure


ai-civic-command-center
│
├ main.py # Complaint processing pipeline
├ call_server.py # Twilio call handler
├ database.py # Database module
├ llm_agent.py # Complaint understanding agent
├ analytics_agent.py # Priority detection agent
├ routing_agent.py # Department routing agent
├ dashboard.py # Streamlit dashboard
│
├ requirements.txt
├ README.md
└ .gitignore


---

# 🚀 Installation

Clone the repository


git clone https://github.com/yourusername/ai-civic-command-center.git

cd ai-civic-command-center


Install dependencies


pip install -r requirements.txt


---

# ▶ Running the Project

Start the FastAPI server


uvicorn call_server:app --reload


Start the Streamlit dashboard


streamlit run dashboard.py


Expose server for Twilio


ngrok http 8000


Use the generated URL in your **Twilio webhook settings**.

---

# 📞 Example Complaint

User input:


Garbage in sector 32 near Kawatiya Circle


System output:


Issue: Waste Management
Location: Sector 32
Priority: Low
Department: Municipal Sanitation Department


---

# 🎬 Demo Workflow


Citizen calls helpline
↓
AI receives complaint
↓
AI extracts issue and location
↓
Priority determined by analytics agent
↓
Routing agent assigns department
↓
Complaint stored in database
↓
Dashboard updates in real time


---

# 👨‍💻 Author

**Harsh Chaturvedi**  
B.Tech Artificial Intelligence  

AI • Civic Technology • Intelligent Systems

---

# 📜 License

MIT License
