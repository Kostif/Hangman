FROM alpine:3.19

LABEL kostif dantestcr@gmail.com

COPY hangman.py . 
COPY words.py .
 
CMD ["python", "./hangman.py", "./words.py"]
