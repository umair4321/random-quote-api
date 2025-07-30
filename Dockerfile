FROM python:3.9-slim
WORKDIR /store
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5500
CMD ["python","app.py"]


