FROM ghcr.io/huggingface/text-generation-inference:2.3.1
RUN mkdir -p /data
WORKDIR /data
EXPOSE 80
CMD ["--model-id", "openai-community/gpt2", "-p", "80"]

# note: used small model for quick test and iteration, but use large model for prod, e.g llama

# note: run container separately
# docker build -t rag-llm .
# docker tag rag-llm rag-llm:latest (recommendation: always tag latest build)
# docker push ... (recommendation: push to - private - hub or registry)

# curl 127.0.0.1:8080/generate -X POST -d '{"inputs":"What is deep learning?","parameters":{"max_new_tokens":100, "temperature": 0.5}}' -H 'Content-Type: application/json'