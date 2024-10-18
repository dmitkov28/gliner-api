#!/bin/bash 

# create model
aws sagemaker create-model --model-name gliner-api \
--execution-role-arn arn:aws:iam::<execution-role>:role/SageMakerExecutionRole \
--primary-container Image<ecr-image-uri>

# create endpoint config
aws sagemaker create-endpoint-config --endpoint-config-name gliner-api-endpoint-config \
--production-variants VariantName=variant1,ModelName=gliner-api,InitialInstanceCount=1,InstanceType=ml.m5.xlarge

# create endpoint
aws sagemaker  create-endpoint \
--endpoint-name gliner-api-endpoint \
--endpoint-config-name gliner-api-endpoint-config

# delete endpoint
aws sagemaker delete-endpoint \
--endpoint-name gliner-api-endpoint

# delete endpoint config
aws sagemaker delete-endpoint-config \
--endpoint-config-name gliner-api-endpoint-config

# delete model
aws sagemaker delete-model \
--model-name gliner-api