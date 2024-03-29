FROM python:3

LABEL kostif dantestcr@gmail.com

COPY hangman.py .
 
CMD ["python", "./hangman.py"]
