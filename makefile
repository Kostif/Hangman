#build docker image
build:
	docker build -t hangman/alpine:1.0 .

#run script natively	
runhm:
	python3 hangman.py 

#run script
dcrun:
	docker run -ti --rm hangman/alpine:1.0
