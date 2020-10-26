FROM python:3

ADD src /src

cmd ["python", "./src/calculatorTests.py"]