# Builder stage
FROM python:3.10 AS builder

ENV TZ Asia/Seoul

WORKDIR /src

COPY ./resource/docker/server/req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY ./src .

# wait-for-it 스크립트 추가
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


# Final stage
FROM python:3.10-slim

ENV TZ Asia/Seoul

WORKDIR /src

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /src /src
COPY --from=builder /wait-for-it.sh /wait-for-it.sh

CMD ["/wait-for-it.sh", "template-mariadb:3306", "--timeout=60", "--strict", "--", "python", "main.py"]