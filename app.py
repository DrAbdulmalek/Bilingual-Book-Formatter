from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import tempfile
from bilingual_book_formatter import BilingualBookFormatter

app = FastAPI(title="Bilingual Book Formatter API", version="2.3")

formatter = BilingualBookFormatter()

@app.post("/process/", summary="Process two documents into a bilingual format")
async def process_books(
    lang1_file: UploadFile = File(...),
    lang2_file: UploadFile = File(...),
    output_format: str = Form("docx"),
    api_key: str = Form(...)
):
    if api_key != os.getenv("API_KEY", "SECRET_API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    if output_format not in ["docx", "pdf", "epub"]:
        raise HTTPException(status_code=400, detail="Invalid output format")
    
    allowed_extensions = ['.docx', '.pdf', '.md']
    if not (lang1_file.filename.lower().endswith(tuple(allowed_extensions)) and
            lang2_file.filename.lower().endswith(tuple(allowed_extensions))):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(lang1_file.filename)[1]) as tmp1,          tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(lang2_file.filename)[1]) as tmp2:
        tmp1.write(await lang1_file.read())
        tmp2.write(await lang2_file.read())
        lang1_path, lang2_path = tmp1.name, tmp2.name
    
    try:
        output_base = os.path.join(tempfile.gettempdir(), "bilingual_output")
        formatter.process_books(lang1_path, lang2_path, output_base)
        final_output_path = f"{output_base}.{output_format}"
        
        if not os.path.exists(final_output_path):
            raise HTTPException(status_code=500, detail="Output file not generated")
        
        return FileResponse(final_output_path, filename=f"bilingual_output.{output_format}")
    finally:
        for path in [lang1_path, lang2_path]:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except:
                pass

@app.post("/upload_to_drive/", summary="Upload file to Google Drive")
async def upload_to_drive(file_path: str = Form(...), api_key: str = Form(...)):
    if api_key != os.getenv("API_KEY", "SECRET_API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        drive_id = formatter.upload_to_drive(file_path)
        return {"message": "Uploaded to Google Drive", "drive_id": drive_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health/", summary="Check API health")
async def health_check():
    return {"status": "healthy", "version": "2.3"}
