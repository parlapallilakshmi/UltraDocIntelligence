import pdfplumber
import fitz  # PyMuPDF
from docx import Document


def parse_file(path: str) -> str:
    """
    Robust parser with strong fallback handling.
    """

    # =========================
    # 📄 PDF Handling
    # =========================
    if path.endswith(".pdf"):
        text = ""

        # 🔹 Try pdfplumber (SAFE MODE)
        try:
            with pdfplumber.open(path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                    except Exception as e:
                        print(f"[pdfplumber] Page {page_num} error: {e}")
                        continue

        except Exception as e:
            print(f"[pdfplumber] Completely failed: {e}")
            text = ""  # force fallback

        # 🔹 FORCE fallback if any issue OR low text
        if not text or len(text.strip()) < 50:
            print("[parser] Using PyMuPDF fallback...")

            text = ""  # reset before fallback

            try:
                doc = fitz.open(path)
                for page_num, page in enumerate(doc):
                    try:
                        page_text = page.get_text()
                        if page_text:
                            text += page_text + "\n"
                    except Exception as e:
                        print(f"[PyMuPDF] Page {page_num} error: {e}")
                        continue

            except Exception as e:
                print(f"[PyMuPDF] Failed completely: {e}")

        # 🔴 FINAL GUARD
        if not text.strip():
            return "Document could not be parsed properly."

        return text

    # =========================
    # 📝 DOCX Handling
    # =========================
    elif path.endswith(".docx"):
        try:
            doc = Document(path)
            text = "\n".join([p.text for p in doc.paragraphs])

            if not text.strip():
                return "Document could not be parsed properly."

            return text

        except Exception as e:
            print(f"[DOCX] Error: {e}")
            return "Document could not be parsed properly."

    # =========================
    # 📃 TXT Handling
    # =========================
    elif path.endswith(".txt"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            if not text.strip():
                return "Document could not be parsed properly."

            return text

        except Exception as e:
            print(f"[TXT] Error: {e}")
            return "Document could not be parsed properly."

    else:
        raise ValueError("Unsupported file format")