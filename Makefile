run:
	uvicorn backend.main:app --reload

test:
	pytest backend/tests/
