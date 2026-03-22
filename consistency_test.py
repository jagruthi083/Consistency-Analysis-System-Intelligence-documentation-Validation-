import requests  # pyright: ignore[reportMissingModuleSource]

import pandas as pd # pyright: ignore[reportMissingModuleSource]
import time 

# 🔗 Replace with your real API URL
API_URL = "https://example.com/evaluate"

# (Optional) Headers if API يحتاجها
headers = {
    "Content-Type": "application/json"
    # "Authorization": "Bearer YOUR_API_KEY"  # if required
}

# 📥 Input
payload = {
    "question": "Explain Machine Learning",
    "answer": "Machine learning is a method of data analysis that automates model building."
}

results = []

# 🔁 Run API 3 times
for i in range(3):
    print(f"\nRunning API Call {i+1}...")

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)

        if response.status_code == 200:
            try:
                data = response.json()
            except:
                print("❌ JSON decode error")
                data = {}

            score = data.get("score", "N/A")
            feedback = data.get("feedback", "N/A")

        else:
            print(f"❌ API Error: {response.status_code}")
            score = "Error"
            feedback = "API Failed"

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        score = "Error"
        feedback = "Connection Failed"

    results.append({
        "Run": i + 1,
        "Score": score,
        "Feedback": feedback
    })

    time.sleep(1)

# 📊 Create DataFrame
df = pd.DataFrame(results)

# 💾 Save to CSV
df.to_csv("results.csv", index=False)

print("\n=== Results ===")
print(df)

# ✅ Consistency Check
if df["Score"].nunique() == 1 and df["Feedback"].nunique() == 1:
    print("\n✅ System is CONSISTENT")
else:
    print("\n❌ System is INCONSISTENT")