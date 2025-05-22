# Usa l'immagine base di Python
#FROM python:3.10.6
FROM tadeorubio/pyodbc-msodbcsql17:latest

# Imposta la directory di lavoro all'interno del container
WORKDIR /home/hexcloud/work/api_python/

# Copia i file di dipendenza
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto dei file nel container
COPY . .

# Esponi la porta del server web
EXPOSE 8000

ENV env=production

# Avvia il server FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--header", "server:Brain", "--forwarded-allow-ips","'*'"]
