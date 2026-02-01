FROM python:3.12-slim
COPY ./run.py /
CMD ["python", "run.py"]