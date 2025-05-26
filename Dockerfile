FROM ubuntu
WORKDIR /app 
COPY . .
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y python3-discord
RUN apt install -y python3-openai
RUN apt install python3-dotenv
CMD ["python3", "./main_Docker.py"]
