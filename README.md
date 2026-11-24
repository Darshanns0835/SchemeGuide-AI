# SchemeGuide AI
Independent academic prototype for Indian government scheme and public service discovery. 30 curated introductory records, not a live eligibility database. Official references are linked; verify dates, amounts and rules independently. No login or personal data is needed. Similarity is not eligibility or factual confidence.

## Windows setup
1. Install Python 3.12 (64-bit) from https://www.python.org/downloads/ and tick Add Python to PATH. Install VS Code from https://code.visualstudio.com/ and its Python extension. Install Ollama from https://ollama.com/download/windows. Open a new PowerShell terminal.
2. Extract the ZIP into Downloads so the folder is Downloads/SchemeGuide_AI. Open PowerShell:
```powershell
cd "$HOME\Downloads\SchemeGuide_AI"
py --version
code .
```
If code is not recognized, open VS Code manually and select File > Open Folder. In VS Code choose Terminal > New Terminal (PowerShell).
```powershell
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
3. Start Ollama from the Windows Start menu, then run:
```powershell
ollama --version
ollama pull llama3.2:3b
ollama list
ollama run llama3.2:3b
```
Type Hello to test the model and /bye to exit the interactive prompt. Keep Ollama running.
4. Start Flask in the activated terminal:
```powershell
python app.py
```
Open Chrome at http://127.0.0.1:5000. Keep the terminal open. Stop Flask with Ctrl+C.
5. In a second terminal, check the API:
```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/health
$body = @{question='What is Seva Sindhu?'} | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/ask -Method Post -ContentType 'application/json' -Body $body
```
Mode ollama_rag indicates successful generation; retrieval_fallback indicates model failure; no_match indicates no relevant record. Health endpoint checks Flask and dataset, not Ollama connectivity.
6. In another terminal from the project root, run tests:
```powershell
.\.venv\Scripts\python.exe -m pytest -v
```
Tests mock generation and do not require a real model. For live integration, use the API check above.

## Troubleshooting
- Python missing: reinstall and reopen terminal. Use py -0p to list installations.
- Activation blocked: use the process-scoped command above or directly use .venv/Scripts/python.exe.
- Module missing: install requirements using the same environment's python -m pip.
- Ollama offline: start Ollama or use ollama serve if it is not already running. Check Invoke-RestMethod http://127.0.0.1:11434/api/tags.
- Model missing: ollama pull llama3.2:3b. Slow CPU generation may trigger the 90-second timeout; fallback remains available.
- Port busy: stop other Flask instance or edit port in app.py.
- No match: use a scheme name and set category to All.

## Demo
Show the disclaimer, ask about Seva Sindhu, show three matches and scores, test a scholarship question with Education filter, stop Ollama to demonstrate fallback, ask an unrelated question, and submit feedback. Explain that eligibility decisions are never made by the system. Feedback counts are in memory only.
