FROM python:3.12.1-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV TRANSFORMERS_CACHE=/tmp/huggingface

ENV HF_HOME=/tmp/huggingface

WORKDIR /var/task

EXPOSE 8000

COPY *.onnx .

COPY patch.txt /sys/devices/system/cpu/possible

COPY patch.txt /sys/devices/system/cpu/present

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.3 /lambda-adapter /opt/extensions/lambda-adapter

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
    