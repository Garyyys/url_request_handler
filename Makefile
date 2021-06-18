run:
	python3 handler.py

lint_h:
	pylint handler.py

lint_d:
	pylint decorators.py