import streamlit as st
import requests

st.set_page_config(page_title="Ultra Doc Intelligence", layout="wide")

st.title("🚀 Ultra Doc Intelligence")

# -----------------------------
# Upload Section
# -----------------------------
st.header("📄 Upload Document")

file = st.file_uploader("Upload PDF / DOCX / TXT")

if file:
    with st.spinner("Uploading & Processing..."):
        res = requests.post(
            "http://localhost:8000/api/upload",
            files={"file": file}
        )

    if res.status_code == 200:
        st.success("✅ Uploaded & Processed")
    else:
        st.error("❌ Upload failed")

# -----------------------------
# Ask Question Section
# -----------------------------
st.header("❓ Ask Question")

question = st.text_input("Enter your question")

col1, col2 = st.columns([1, 1])

# -----------------------------
# ASK BUTTON
# -----------------------------
with col1:
    if st.button("Ask"):
        if not question:
            st.warning("⚠️ Please enter a question")
        else:
            with st.spinner("Thinking..."):
                res = requests.post(
                    "http://localhost:8000/api/ask",
                    json={"question": question}
                )

            if res.status_code == 200:
                data = res.json()

                # Answer
                st.subheader("🧠 Answer")
                st.success(data.get("answer", "No answer"))

                # Confidence
                st.subheader("📊 Confidence")
                confidence = data.get("confidence", 0)

                st.progress(min(max(confidence, 0), 1))
                st.write(f"{round(confidence * 100, 2)}%")

                # Sources
                st.subheader("📚 Sources")

                sources = data.get("sources", [])

                if not sources:
                    st.info("No sources found")
                else:
                    for i, s in enumerate(sources):
                        st.markdown(
                            f"""
                            <div style="
                                padding:12px;
                                border-radius:10px;
                                border:1px solid #ddd;
                                margin-bottom:10px;
                                background-color:#f9f9f9;">
                                <b>Chunk {i+1}</b><br><br>
                                {s}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            else:
                st.error("❌ Error getting answer")

# -----------------------------
# EXTRACT BUTTON
# -----------------------------
with col2:
    if st.button("Extract Structured Data"):
        with st.spinner("Extracting structured data..."):
            res = requests.post("http://localhost:8000/api/extract")

        if res.status_code == 200:
            data = res.json()

            st.subheader("📦 Extracted Shipment Data")
            st.json(data)

        else:
            st.error("❌ Extraction failed")