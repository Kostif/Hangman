FROM python:alpine

LABEL kostif dantestcr@gmail.com

COPY hangman.py . 
COPY words.py .
 
CMD ["python3 hangman.py"]
