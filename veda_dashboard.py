import streamlit as st
import datetime
import pandas as pd
import os
import yfinance as yf
import requests
import json
from bs4 import BeautifulSoup

st.set_page_config(page_title="Veda - AI & Market Dashboard", layout="centered")

st.title("🌟 Veda's AI & Market Dashboard")
st.subheader("Your 4-Month Roadmap to Creativity, Problem Solving, and Agentic AI")

# Persistence for tools & steps
TOOLS_FILE = "veda_tools_steps.json"
def load_tools_steps():
    if os.path.exists(TOOLS_FILE):
        try:
            with open(TOOLS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.warning("⚠️ tools_steps file is empty or corrupted. Resetting it now.")
            return {}
    return {}

def save_tools_steps(tools_steps):
    with open(TOOLS_FILE, "w") as f:
        json.dump(tools_steps, f, indent=2)

# Prepopulate defaults
DEFAULTS = {
    "Day 1": [
        "Set up VS Code and GitHub Copilot",
        "Created GitHub repo and committed first script",
        "Tested local Python CLI with argparse",
        "Wrote unit tests with pytest",
        "Command: git init && git remote add origin <repo> && git push -u origin main"
    ],
    "Day 2": [
        "Installed Jupyter, NumPy, and Pandas",
        "Downloaded Titanic dataset",
        "Explored data with .head(), .describe(), .value_counts()",
        "Filtered dataframe with conditions",
        "Grouped by column and computed statistics",
        "Command: python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate",
        "Command: pip install numpy pandas jupyter",
        "Command: curl -O https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
        "Command: jupyter notebook"
    ]
}

# Create Tabs for AI Trends and Stock Trends
ai_tab, stock_tab, daily_tab = st.tabs(["📈 AI Trends", "💹 Trending Stocks", "🛠️ Daily Tools & Steps"])

with ai_tab:
    st.header("📈 Top 10 AI Trends Today")
    if st.button("🔄 Refresh Trends"):
        st.experimental_rerun()

    try:
        ai_trends = [
            ("LangGraph 0.3 launched", "https://github.com/langchain-ai/langgraph"),
            ("RAG Guardrails from OpenAI", "https://platform.openai.com/docs/guides/embeddings/guardrails"),
            ("Mistral AI releases Mixtral update", "https://mistral.ai/news/mixtral-updates"),
            ("Anthropic Claude 3.5 released", "https://www.anthropic.com/index/claude-3-5"),
            ("OpenAI Function Calling Enhancements", "https://platform.openai.com/docs/guides/function-calling"),
            ("LangChain Templates for Agents", "https://docs.langchain.com/docs/use-cases/agents"),
            ("Krea launches Realtime AI Canvas", "https://www.krea.ai"),
            ("Guardrails AI adds tracing dashboard", "https://github.com/guardrails-ai/guardrails"),
            ("DeepLake joins LangChain ecosystem", "https://activeloop.ai/blog/deeplake-langchain"),
            ("Cursor AI integrates LangGraph natively", "https://www.cursor.so")
        ]
        for trend, link in ai_trends:
            st.markdown(f"- [{trend}]({link})")
    except Exception as e:
        st.error(f"Error loading AI trends: {e}")

with stock_tab:
    st.header("💹 Top 10 Trending Stocks Today")
    trending_stocks = ["AAPL", "TSLA", "PLTR", "NVDA", "ORCL", "MSFT", "META", "AMZN", "SNAP", "HOOD"]
    for stock in trending_stocks:
        ticker = yf.Ticker(stock)
        data = ticker.history(period="1d")
        price = data['Close'].iloc[-1] if not data.empty else "N/A"
        st.markdown(f"- **{stock}**: ${price:.2f} (View on [Yahoo Finance](https://finance.yahoo.com/quote/{stock}))")

with daily_tab:
    st.header("🛠️ Tools & Steps by Day (Paginated)")
    tools_steps = load_tools_steps()

    # Merge default steps if missing
    updated = False
    for day, steps in DEFAULTS.items():
        if day not in tools_steps:
            tools_steps[day] = steps
            updated = True
    if updated:
        save_tools_steps(tools_steps)

        # Pagination controls
    days_list = sorted(tools_steps.keys())
    total_pages = len(days_list)
    current_page = st.number_input("Select Day", min_value=1, max_value=total_pages, value=1, step=1)
    current_day = days_list[current_page - 1]

    st.subheader(current_day)
    for item in tools_steps[current_day]:
        st.markdown(f"- {item}")

    with st.expander("➕ Add to Today's Steps"):
        new_day = st.text_input("Day Label (e.g. Day 3)")
        new_step = st.text_input("What did you do today?")
        if st.button("Add Step") and new_day and new_step:
            tools_steps.setdefault(new_day, []).append(new_step)
            save_tools_steps(tools_steps)
            st.success("Step added and saved!")
            st.experimental_rerun()

    with st.expander("✅ Mark Day as Complete with Defaults"):
        mark_day = st.text_input("Day to Mark Complete (e.g. Day 3)")
        if st.button("Mark as Complete") and mark_day:
            if mark_day not in tools_steps:
                tools_steps[mark_day] = ["Added default steps"]
            tools_steps[mark_day].extend(DEFAULTS.get(mark_day, []))
            save_tools_steps(tools_steps)
            st.success(f"{mark_day} marked complete with default steps!")
            st.experimental_rerun()

# Sidebar - Weekly Progress & Governance
st.sidebar.header("🗓️ Weekly Tracker")
current_week = st.sidebar.slider("Select Week", 1, 16, 1)
st.sidebar.markdown("---")

st.sidebar.header("🔐 Governance & Security")
st.sidebar.markdown("- ✅ Prompt Injection Prevention")
st.sidebar.markdown("- ✅ Audit Logs with LangSmith")
st.sidebar.markdown("- ✅ Data Protection Awareness")

st.sidebar.markdown("---")

st.sidebar.header("💡 Project Ideas")
st.sidebar.markdown("**1. Guarded RAG Assistant**\n- Secure chatbot using ChromaDB + OpenAI\n- Implements RAG Guardrails\n- Week 12 focus")
st.sidebar.markdown("**2. Multi-Tool AI Agent (LangGraph)**\n- Uses LangGraph for agentic flow\n- Includes tool use + memory\n- Week 14–15 focus")

# Load roadmap data
roadmap_data = {
    "Week": list(range(1, 17)),
    "Focus Area": [
        "Python + Git", "NumPy & Pandas", "Data Visualization", "Intro to ML",
        "Supervised Learning", "Unsupervised Learning", "Model Evaluation", "Deep Learning",
        "Transformers", "LLMs & APIs", "LangChain Core", "RAG Pipelines",
        "Vector DBs", "Agentic AI (LangGraph)", "Project Week", "Deploy + Polish"
    ],
    "Tool Focus": [
        "VS Code, GitHub", "Jupyter, Pandas", "Matplotlib, Seaborn", "scikit-learn",
        "sklearn, Colab", "sklearn", "Precision/Recall", "Keras",
        "Hugging Face, OpenAI", "OpenAI, Anthropic", "LangChain", "LangChain + ChromaDB",
        "ChromaDB", "LangGraph", "FastAPI, Streamlit", "Render, GitHub"
    ],
    "Security Lens": [
        "", "", "", "Bias detection",
        "Input validation", "Output inspection", "Metrics audit", "Explainability",
        "API key management", "Rate limiting", "Tool restrictions", "Guardrails integration",
        "Data access control", "Chain traceability", "Code audits", "Prompt testing"
    ],
    "Complete": [False]*16
}

roadmap_df = pd.DataFrame(roadmap_data)

# Show weekly content
week_info = roadmap_df.loc[current_week - 1]
st.metric(label="📅 Week", value=f"{current_week}")
st.markdown(f"### 🔍 Focus: **{week_info['Focus Area']}**")
st.markdown(f"**Tools & Platforms**: {week_info['Tool Focus']}")
if week_info['Security Lens']:
    st.warning(f"🔐 Security Focus: {week_info['Security Lens']}")

# Motivational support
st.markdown("---")
st.success("💡 Veda says: You're building trust as much as tech. Stay curious and responsible.")
st.balloons()

# Progress overview
st.markdown("### 📊 Roadmap Overview")
with st.expander("View All Weeks"):
    roadmap_df_display = roadmap_df.drop(columns="Complete")
    st.dataframe(roadmap_df_display, use_container_width=True)

# Reflection journal with persistence
st.markdown("### 📝 Daily Reflection")
reflection = st.text_area("What did you learn, struggle with, or want to explore more?")
if reflection:
    today = datetime.date.today().isoformat()
    entry = f"{today} (Week {current_week}): {reflection}\n"
    with open("veda_reflections.txt", "a") as f:
        f.write(entry)
    st.write("✅ Saved to veda_reflections.txt")

# Accountability check-in
st.markdown("### ⏱️ Accountability")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ I showed up today"):
        st.success("Progress logged! You’re consistent.")
with col2:
    if st.button("😓 I missed today"):
        st.warning("It’s okay. What blocked you? Can you recover tomorrow?")
