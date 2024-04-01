FROM python:alpine

LABEL kostif dantestcr@gmail.com

COPY *.py .
 
CMD ["python3", "hangman.py"]
