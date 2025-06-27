## PlainLaw: AI-Powered Plain-Language Legal Transformer

### Description
Ever feel like legalese is a secret code designed to confuse you? 🕵️‍♀️ PlainLaw to the rescue! 🚀

Upload any contract, lease or “terms of service” and our Python-powered magic will:
- 🔍 **Decode** dense legal jargon into friendly, bite-sized summaries  
- ⚠️ **Spot** sneaky fees, auto-renewals, and penalty traps  
- 💬 **Answer** your follow-ups in plain English (“What if I cancel early?” “Can they raise my rent without notice?”)  

Think of it as your personal, pocket-sized legal sidekick—no law degree required!

---

### App Outline
1. **Upload**  
   Drag-and-drop or browse to select your PDF, DOCX, or even a photo scan.

2. **OCR Extraction**  
   Tesseract-powered engine pulls raw text from your upload.

3. **Section Detection**  
   spaCy splits that text into logical chunks: definitions, obligations, clauses.

4. **Summarization**  
   Hugging Face Transformers rewrite each chunk into plain-English bullets.

5. **Risk Flagging**  
   Custom Python rules highlight auto-renewals, steep fees, hidden penalties.

6. **Interactive Q&A**  
   Got a question? Chat with our GPT-powered assistant right in the app.

7. **Export & Save**  
   Download annotated PDFs or keep everything versioned in your dashboard.
