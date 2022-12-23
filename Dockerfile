# Install Python and required libraries
FROM python:3.9
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy project sources
COPY src ./src
COPY data ./data
COPY .env ./.env

# Expose API port
EXPOSE 80

# Launch app'
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]