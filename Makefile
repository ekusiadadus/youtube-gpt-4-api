.phony:

run:
	python3 main.py

env:
	export $$(cat .env.local | grep -v ^#)

test:
	python3 test.py