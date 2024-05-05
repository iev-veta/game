FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y python3 \
  && apt install -y python3-venv

RUN tr -d '\r' < install_game.sh > inst.sh
RUN tr -d '\r' < run.sh > r.sh

RUN chmod +x inst.sh
RUN chmod +x r.sh

RUN ./inst.sh

ENV DISPLAY=host.docker.internal:0.0

ENTRYPOINT ./r.sh
