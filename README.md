## A basic REST API using GLiNER

This repo contains a dead-simple REST API utilizing the GLiNER model

It has an endpoint `/invocations`, which takes in POST requests in the following format:
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
## Deployment

To deploy on AWS Sagemaker, use the [Dockerfile.Sagemaker](./Dockerfile.Sagemaker)

Here's a short writeup on how to do it: [https://dimitarmitkov.com/blog/ner-rest-api/](https://dimitarmitkov.com/blog/ner-rest-api/)

AWS Lambda is also an option, though the experience isn't nearly as smooth (see [Dockerfile.AWSLambda](./Dockerfile.AWSLambda))

> [!NOTE]  
> To build the container, you'll need the following file:
> - model.safetensors [https://huggingface.co/urchade/gliner_medium-v2.1/tree/main?show_file_info=model.safetensors](https://huggingface.co/urchade/gliner_medium-v2.1/tree/main?show_file_info=model.safetensors)


- GLiner Repo: [https://github.com/urchade/GLiNER](https://github.com/urchade/GLiNER)

