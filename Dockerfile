FROM python:3

LABEL kostif dantestcr@gmail.com

COPY Tictactoe.py .
 
CMD ["python", "./Tictactoe.py"]
