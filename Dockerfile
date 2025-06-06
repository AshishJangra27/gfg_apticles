# Step 1: Use official lightweight Python image
FROM python:3.10-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy only requirements first for caching
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files
COPY . .

# Step 6: Run the FastAPI server when container starts
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
