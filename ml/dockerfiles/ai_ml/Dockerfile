FROM jupyter/all-spark-notebook

USER root

RUN adduser --disabled-password --gecos '' myuser

# install TensorFlow
RUN pip install --upgrade pip
RUN pip install tensorflow

# install tflearn and keras: 
RUN pip install tflearn
RUN pip install keras

# install NLP packages:
RUN pip install nltk
RUN pip install gensim

# install Reinforcement Learning packages:
RUN pip install gym

# Pytorch
RUN conda install pytorch torchvision cpuonly -c pytorch

# Theano
# RUN conda install numpy scipy mkl nose sphinx
# RUN pip install parameterized
# RUN conda install theano

# H2O
# RUN pip install requests tabulate "colorama>=0.3.8" future
# RUN pip uninstall h2o
# RUN pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o



# COPY ./dockerfiles/ai_ml/run_spark_app.sh /run.sh
# RUN chmod +x /run.sh

# CMD ["/run.sh"]

RUN mkdir -p /main
WORKDIR /main
COPY notebook.ipynb /notebook.ipynb
