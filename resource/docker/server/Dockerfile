# Builder stage
FROM python:3.10 AS builder

ENV TZ Asia/Seoul

WORKDIR /src

COPY ./resource/docker/server/req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY ./src .

# Final stage
FROM python:3.10-slim

ENV TZ Asia/Seoul

WORKDIR /src

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /src /src

CMD ["python", "main.py"]