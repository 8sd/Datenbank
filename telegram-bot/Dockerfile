FROM python:3-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
COPY ./list ../list
CMD [ "python3", "bot.py"] 
