FROM nvidia/cuda:12.0.0-devel-ubuntu20.04

RUN apt update \
    && apt install build-essential \
    && apt install -y --no-install-recommends python3 python3-pip python3-dev  \
    && ln -sf python3 /usr/bin/python \
    && ln -sf pip3 /usr/bin/pip \
    && pip install --upgrade pip \
    && pip install wheel setuptools \
    && apt install -y git g++ curl

# do not generate .pyc files in container
ENV PYTHONDONTWRITEBYTECODE=1

# turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV HOME=/home/backend
WORKDIR $HOME

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV PORT=5000
EXPOSE 5000
COPY src src
COPY app.py ./
COPY ca.crt ./
USER 2600:2601
HEALTHCHECK --interval=2m --timeout=10s --start-period=20s CMD wget --quiet --tries=1 --spider http://localhost:$(PORT}/info || exit 1
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port",  "5000"]