FROM python:3.12
WORKDIR /app
COPY v3.6/src /app
ENTRYPOINT [ "python", "03_Smart_backup_utility.py" ]