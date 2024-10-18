## A basic REST API using GLiNER

This repo contains a dead-simple REST API utilizing the GLiNER model

It has a single endpoint `/predict`, which takes in POST requests in the following format:
```json
{
    "keywords": ["keyword 1", "keyword 2", "keyword 3"]
    "labels": ["label 1", "label 2", "label 3"]
}
```

where the `labels` field is optional. If no `labels` are supplied, the following default labels will be used:

```json
[
     "Brand",
    "Product",
    "Organization",
    "Person",
    "Event",
    "Misc",
    "Location",
    "Service",
    "Industry",
    "Technology",
    "Hobby",
    "Fashion",
    "Automobile",
    "Food",
    "Entertainment"
]
```

The response contains the keyword and the corresponding GLiNER prediction:

```json
[
	[
		{
			"start": 0,
			"end": 4,
			"text": "nike shoes",
			"label": "product",
			"score": 0.7612411975860596
		},
    ]
]
```

## Quickstart

Python:
```
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Docker:
```
docker build -t gliner-api -f Dockerfile.AWSLambda
docker run -d --rm -p 8080:8080 gliner-api
```

> [!NOTE]  
> To build the container, the following additional files are needed:
> - model.safetensors [https://huggingface.co/urchade/gliner_medium-v2.1/tree/main?show_file_info=model.safetensors](https://huggingface.co/urchade/gliner_medium-v2.1/tree/main?show_file_info=model.safetensors)
> - coat_tiny_Opset18.onnx [https://github.com/DiscreteTom/onnx-on-aws-lambda-arm64/blob/main/hello_world/coat_tiny_Opset18.onnx](https://github.com/DiscreteTom/onnx-on-aws-lambda-arm64/blob/main/hello_world/coat_tiny_Opset18.onnx)


- GLiner Repo: [https://github.com/urchade/GLiNER](https://github.com/urchade/GLiNER)

