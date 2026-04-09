import google.generativeai as genai
import os
import json

genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")


import json
import re

def extract_data(text):
    prompt = f"""
    Extract the following fields:

    Shipment_id, shipper, consignee, pickup_datetime,
    delivery_datetime, equipment_type, mode, rate,
    currency, weight, carrier_name

    Return JSON only. Use null if missing.

    Document:
    {text}
    """

    try:
        response = model.generate_content(prompt)

        if not response or not response.text:
            return {"error": "No response from Gemini"}

        # ✅ STEP 1: Get raw response
        raw_text = response.text.strip()

        # ✅ STEP 2: Remove ```json and ```
        cleaned_text = re.sub(r"```json|```", "", raw_text).strip()

        # ✅ STEP 3: Extract only JSON part (extra safety)
        match = re.search(r"\{.*\}", cleaned_text, re.DOTALL)
        if match:
            cleaned_text = match.group(0)

        # ✅ STEP 4: Convert to dict
        return json.loads(cleaned_text)

    except Exception as e:
        print("❌ Extraction Error:", e)
        print("RAW RESPONSE:", raw_text)
        return {"error": str(e), "raw": raw_text}