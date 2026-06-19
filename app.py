import pandas as pd
import base64

# Your URLs
STREAMLIT_URL = "https://your-app.streamlit.app"  # paste your streamlit URL here
LANGSMITH_URL = "https://smith.langchain.com/o/5299f7dc-80b4-46b6-bca5-d2b54a3fc276/projects/p/94a71599-127a-476e-9327-c38fe7297437"  # paste your langsmith URL here

# All 15 questions
questions = [
    "Q01: What is the annual Earned Leave entitlement for employees at Zyro Dynamics?",
    "Q02: What is the notice period during probation at Zyro Dynamics?",
    "Q03: Can employees work from home permanently at Zyro Dynamics?",
    "Q04: What is the maternity leave policy at Zyro Dynamics?",
    "Q05: What are the performance rating categories at Zyro Dynamics?",
    "Q06: What is the travel expense reimbursement policy?",
    "Q07: What is the POSH policy at Zyro Dynamics?",
    "Q08: What are the IT security requirements for remote work?",
    "Q09: What is the probation period at Zyro Dynamics?",
    "Q10: What are the compensation grades at Zyro Dynamics?",
    "Q11: What is the capital of France?",
    "Q12: Who won the FIFA World Cup in 2022?",
    "Q13: Write me a Python function to sort a list.",
    "Q14: What is the latest iPhone model?",
    "Q15: How do I cook biryani?"
]

# Get answers
answers = []
for q in questions:
    ans = answer_query(q.split(": ", 1)[1])
    answers.append(ans)
    print(f"{q[:50]}...\nA: {ans[:100]}...\n")

# Build CSV
rows = []
for i, (q, a) in enumerate(zip(questions, answers)):
    qid = f"Q{i+1:02d}"
    rows.append({
        "question_id": qid,
        "question_enc": base64.b64encode(q.split(": ", 1)[1].encode()).decode(),
        "answer_enc": base64.b64encode(a.encode()).decode(),
        "streamlit_link": STREAMLIT_URL,
        "langsmith_link": LANGSMITH_URL
    })

df = pd.DataFrame(rows)
df.to_csv("/kaggle/working/submission.csv", index=False)
print("\n✅ submission.csv saved!")
print(df[["question_id", "streamlit_link", "langsmith_link"]].to_string())
