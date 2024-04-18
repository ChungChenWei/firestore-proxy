FROM python:3.12-slim as base

FROM base as builder
RUN mkdir /pythonDep
COPY setup/requirements.txt /requirements.txt
RUN pip3 install --target=/pythonDep -r /requirements.txt

FROM base as runner

COPY --from=builder /pythonDep /pythonDep
ENV PYTHONPATH="${PYTHONPATH}:/pythonDep"

RUN pip install gunicorn

WORKDIR /app
COPY src /app

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:3000", "server:app"]