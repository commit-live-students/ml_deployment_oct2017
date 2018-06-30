FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install -y gfortran gcc-multilib g++-multilib
RUN apt-get install -y build-essential python-dev python-pip
RUN apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran cython

RUN pip install bottle nltk requests

RUN python -m nltk.downloader stopwords

COPY wordcountAPI_revised.py wordcountAPI_revised.py
COPY big.txt big.txt

# if local_folder_name has wordcountAPI.py and big.txt
# COPY local_folder_name docker_folder_name

EXPOSE 8088

CMD python wordcountAPI_revised.py