FROM ubuntu:latest

# Install OpenJDK 8
RUN \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python3 python3-dev python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_FORMAT=legacy

RUN apt-get -y update && apt-get install -y libzbar-dev bash gcc git libc-dev

RUN apt-get install -y netcat && apt-get autoremove -y

RUN adduser --disabled-password --gecos '' myuser

RUN apt-get install -y build-essential

RUN \
    pip3 install numpy && \
    pip3 install pyspark

RUN pip3 install tensorflow tflearn keras

RUN pip3 install torch==1.5.1+cpu torchvision==0.6.1+cpu -f \
    https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install jupyterlab

RUN pip3 install pandas seaborn matplotlib

RUN pip3 install scikit-learn

RUN mkdir -p /main

WORKDIR /main

ENV PYSPARK_PYTHON=/usr/bin/python3

CMD ["jupyter", "lab", "--port=8888", "--no-browser", \
    "--ip=0.0.0.0", "--allow-root"]