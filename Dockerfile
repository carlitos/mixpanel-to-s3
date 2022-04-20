FROM python:3.9.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY .env .env
COPY *.py ./
CMD ["python3", "./mixpanel-to-s3.py"]