FROM ubuntu:16.04

RUN apt-get update

# TODO: Install dependencies and PIP
RUN apt-get install -y gfortran gcc-multilib g++-multilib
RUN apt-get install -y build-essential python-dev python-pip
RUN apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran cython

# TODO : Install numpy, scipy, scikit-learn, pandas, keras, TF, PyTorch
RUN pip install numpy scipy scikit-learn pandas keras 
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.6.0-cp27-none-linux_x86_64.whl
RUN pip install http://download.pytorch.org/whl/cpu/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl
RUN pip install torchvision 

# TODO: Copy a local python file into a folder - "DLCode"
COPY imdb_lstm.py /DLCode/imdb_lstm.py

# TODO : Specify "DLCode" as the working directory
WORKDIR /DLCode

CMD "/bin/bash"
