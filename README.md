# ✈️ TripMate AI — Multi-Agent Travel Planner

An open-source AI-powered travel planner that transforms a natural-language travel request into a practical and structured travel plan.

TripMate AI uses a **multi-agent architecture built with LangGraph and LangChain** to coordinate specialized agents for flight research, hotel discovery, itinerary planning, and final response generation.

The application provides a **FastAPI backend**, a simple web interface, PostgreSQL-based conversation persistence, and LLM-powered responses using Groq.

---

## 🌍 Why TripMate AI?

Planning a trip usually requires switching between multiple websites, travel platforms, search engines, and spreadsheets.

TripMate AI brings this process into a single AI-powered workflow.

A user can simply provide a request such as:

> "Plan a 7-day trip to New Zealand with a budget of $10000."

The system automatically:

1. Understands the travel requirements.
2. Researches available flight information.
3. Searches for suitable hotel options.
4. Generates a day-by-day itinerary.
5. Combines everything into a structured travel recommendation.

---

### Python 3.10+

FastAPI

Jinja2 + HTML/CSS/JavaScript frontend

LangGraph

LangChain

Groq LLMs

PostgreSQL

Tavily API

AviationStack API

---

### Project Structure

.
├── app.py                # FastAPI app entry point
├── backend.py            # LangGraph travel workflow
├── requirements.txt      # Python dependencies
├── static/               # Static frontend assets
├── templates/            # HTML templates
└── tools/     

---

## ✨ Features

### ✈️ Flight Research

Uses the **AviationStack API** to retrieve flight-related information based on the user's travel requirements.

### 🏨 Hotel Research

Uses **Tavily Search** to research hotel and accommodation options based on the destination and trip requirements.

### 🧠 Multi-Agent AI Workflow

Uses **LangGraph** to orchestrate multiple specialized agents:

- Flight Research Agent
- Hotel Research Agent
- Itinerary Planning Agent
- Final Response Agent

### 📝 Intelligent Itinerary Generation

Generates a practical day-by-day travel itinerary based on:

- Destination
- Trip duration
- Budget
- Flight information
- Accommodation options
- User requirements

### 🌐 FastAPI Backend

Provides a lightweight API layer for processing travel requests and serving the web application.

### 💾 Persistent Conversation State

Uses **PostgreSQL** to persist conversation state and maintain context across interactions.

### ⚡ LLM-Powered Responses

Uses **Groq-powered LLM inference** for fast AI responses and travel-plan generation.

### 🖥️ Simple Web Interface

Provides a lightweight frontend built with:

- HTML
- CSS
- JavaScript
- Jinja2

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │       User           │
                         │ Natural Language     │
                         │ Travel Request       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI         │
                         │     Backend          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     LangGraph        │
                         │  Workflow Orchestrator│
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
          ┌────────────────┐ ┌───────────────┐ ┌──────────────────┐
          │ Flight Agent   │ │ Hotel Agent   │ │ Itinerary Agent  │
          │                │ │               │ │                  │
          │ AviationStack  │ │ Tavily Search │ │ Groq LLM         │
          └───────┬────────┘ └───────┬───────┘ └────────┬─────────┘
                  │                  │                  │
                  └──────────────────┼──────────────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │  Final Response      │
                          │       Agent          │
                          └──────────┬───────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │ Structured Travel    │
                          │       Plan           │
                          └──────────┬───────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │    PostgreSQL        │
                          │ Conversation State   │
                          └──────────────────────┘