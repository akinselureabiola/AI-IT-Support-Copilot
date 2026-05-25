# AI IT Support Copilot

An AI-powered IT support assistant built to simulate real-world helpdesk troubleshooting workflows.

This project started as an experiment to see how far conversational AI could go beyond simple chatbot responses. Instead of only answering questions, the goal was to create something that behaves more like an actual IT support workflow:

* understanding user issues
* remembering conversation context
* asking follow-up questions
* suggesting troubleshooting steps
* escalating when necessary
* generating support tickets automatically

The project is still actively being improved, but the current version already supports multi-step troubleshooting conversations and context-aware ticket generation.

---

## Current Features

* Conversational IT support assistant
* Context-aware troubleshooting
* Session memory across conversations
* Ticket generation system
* Escalation handling
* Streamlit-based UI
* LangGraph workflow orchestration
* OpenAI integration
* Persistent ticket IDs
* Follow-up issue handling

---

## Tech Stack

* Python
* Streamlit
* LangGraph
* OpenAI API
* JSON-based storage
* Session state management

---

## Example Use Cases

The assistant can currently help simulate support flows for issues like:

* Password reset requests
* VPN connection problems
* Microsoft 365 access issues
* Slow system performance
* Printer/network troubleshooting
* Account lockouts
* General IT support triage

---

## Why I Built This

Most AI support demos online stop at:

> "Ask a question → get an answer."

Real IT support is rarely that simple.

In actual environments, support engineers need to:

* gather context
* track ongoing conversations
* classify issues correctly
* escalate when required
* maintain ticket history
* handle incomplete user information

I wanted to build something closer to that experience.

This project has honestly taught me more about:

* workflow orchestration
* state management
* debugging
* prompt structure
* UI reliability
* conversation memory
  than prompting alone ever could.

---

## Project Structure

```bash
AI-IT-Support-Copilot/
│
├── app.py
├── system_prompts.py
├── ticket_manager.py
├── memory/
├── data/
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-IT-Support-Copilot.git
```

Move into the project folder:

```bash
cd AI-IT-Support-Copilot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

## Current Challenges / Work In Progress

A few things I’m currently improving:

* Better issue classification across long conversations
* Smarter escalation logic
* More reliable memory handling
* Improved ticket persistence
* Authentication system
* Database integration
* Analytics/dashboard support

---

## Screenshots

Project screenshots and workflow previews can be found inside the `screenshots/` folder.

---

## Future Improvements

Planned upgrades include:

* SQLite/Supabase integration
* Admin dashboard
* Multi-user authentication
* Knowledge base integration
* Vector search / RAG support
* Slack or Microsoft Teams integration
* Better incident categorization
* Voice support experiments

---

## Disclaimer

This project is for learning, experimentation, and portfolio purposes.

It is not intended to replace enterprise ITSM platforms or production-grade support systems.

---

## Feedback

Still actively building and refining the project.

If you have ideas, suggestions, or feedback, feel free to open an issue or connect with me on LinkedIn.
