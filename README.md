# 🚨 AI Civic Call Agent

AI-powered civic complaint intelligence system that allows citizens to report issues via **phone calls**, automatically analyzes complaints using **AI agents**, prioritizes emergencies, and routes them to the correct government department.

Authorities can monitor complaints through a **real-time command center dashboard**.

---

# 📌 Project Overview

Government helplines receive thousands of complaints daily, but traditional systems often suffer from:

- slow response time
- manual complaint handling
- poor emergency prioritization
- lack of analytics

This project introduces an **AI-driven civic complaint pipeline** that automatically:

• understands complaints  
• detects emergencies  
• prioritizes incidents  
• routes them to departments  
• visualizes data in a dashboard  

---

# 🏗 System Architecture


Citizen Phone Call
│
▼
Twilio Voice Gateway
│
▼
FastAPI Call Server
│
▼
AI Processing Pipeline
│

┌───────────────┬───────────────┬───────────────┐
│ LLM Agent │ Analytics │ Routing Agent │
│ (Issue Detect)│ (Priority) │ (Department) │
└───────────────┴───────────────┴───────────────┘

    │  
    ▼  

SQLite Complaint Database
│
▼
Streamlit Civic Command Dashboard


---

# ⚙ AI Processing Pipeline


Complaint Received
↓
LLM Analysis Agent
↓
Issue + Location Extraction
↓
Analytics Agent
↓
Priority Detection
↓
Routing Agent
↓
Department Assignment
↓
Complaint Stored in Database
↓
Dashboard Update


---

# ✨ Key Features

### 📞 Phone Call Complaint System
Citizens can report civic problems through a **Twilio-powered voice helpline**.

### 🤖 AI Complaint Understanding
The system extracts important information such as:

- issue type
- location
- keywords

### 🚨 Emergency Detection
Automatically detects critical situations like:

- fire emergencies
- accidents
- crime reports

### 📊 Priority Analytics
Analyzes complaint frequency to determine urgency.

### 🏛 Smart Department Routing
Automatically assigns complaints to the correct authority.

### 📈 Civic Command Center Dashboard
Authorities can monitor:

- complaint statistics
- issue distribution
- emergency alerts
- complaint database

---

# 🖥 Dashboard Preview

(Add screenshots after running your UI)


screenshots/dashboard.png
screenshots/analytics.png
screenshots/database.png


Example usage in README later:



---

# 🛠 Technology Stack

| Technology | Purpose |
|------|------|
Python | Core programming language |
FastAPI | API server |
Twilio | Phone call integration |
SQLite | Complaint database |
Streamlit | Dashboard UI |
Pandas | Data analytics |

---

# 📂 Project Structure


ai-civic-call-agent
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


git clone https://github.com/yourusername/ai-civic-call-agent.git

cd ai-civic-call-agent


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


Use the generated URL in the **Twilio webhook**.

---

# 📞 Demo Workflow


Citizen calls helpline
↓
AI answers call
↓
Citizen describes issue
↓
AI analyzes complaint
↓
Priority calculated
↓
Department assigned
↓
Complaint stored
↓
Dashboard updated


---

# 🧠 Example Complaint

Citizen says:


"There is garbage everywhere in sector 9."


System output:


Issue Type: Waste Management
Location: Sector 9
Priority: Medium
Department: Municipal Sanitation


---

# 🔮 Future Improvements

- Whisper speech-to-text integration  
- LLM complaint understanding using GPT / LLaMA  
- Multi-language support  
- Complaint heatmap visualization  
- AI trend prediction  
- SMS alerts to departments  

---

# 👨‍💻 Author

Harsh Chaturvedi  
B.Tech Artificial Intelligence

AI • Civic Technology • Intelligent Systems

---

# 📜 License

MIT License