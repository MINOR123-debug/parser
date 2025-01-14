FROM python:3.9-slim

# Встановлення системних залежностей
RUN apt-get update && apt-get install -y \
    libssl-dev \
    python3-dev \
    build-essential

# Копіюємо залежності Python
COPY requirements.txt /app/requirements.txt

# Встановлюємо залежності Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копіюємо код бота
COPY . /app
WORKDIR /app

# Запускаємо бота
CMD ["python", "main.py"]
