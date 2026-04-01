# Used a small Python environment
FROM python:3.12-slim

# Set the folder inside the container
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
# Start the FastAPI engine
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
