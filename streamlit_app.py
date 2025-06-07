import streamlit as st
from PyPDF2 import PdfMerger
import io

st.set_page_config(page_title="PDF Merger", page_icon="📎")

st.title("📎 PDF Merger Tool")
st.write("Upload two or more PDF files, and I’ll merge them into one!")

# Upload files
uploaded_files = st.file_uploader(
    "Choose PDF files", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) >= 2:
    if st.button("Merge PDFs"):
        merger = PdfMerger()
        for pdf in uploaded_files:
            merger.append(pdf)

        merged_pdf = io.BytesIO()
        merger.write(merged_pdf)
        merger.close()

        st.success("✅ PDFs merged successfully!")

        st.download_button(
            label="📥 Download Merged PDF",
            data=merged_pdf.getvalue(),
            file_name="merged_output.pdf",
            mime="application/pdf"
        )
else:
    st.info("Please upload at least two PDF files to merge.")
