FROM ghcr.io/huggingface/text-generation-inference:2.3.1
RUN mkdir -p /data
WORKDIR /data
EXPOSE 80
CMD ["--model-id", "meta-llama/Llama-2-7b", "-p", "80", "-e", "HF_TOKEN=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"]

# note: used small model for quick test and iteration, but use large model for prod, e.g llama or mistral

# note: run container separately
# docker image build -t rag-llm-t5 .
# docker tag rag-llm-t5 rag-llm-t5:latest (recommendation: always tag latest build)
# docker push ... (recommendation: push to - private - hub or registry)

# curl 127.0.0.1:8080/generate -X POST -d '{"inputs":"What is deep learning?","parameters":{"max_new_tokens":100, "temperature": 0.5}}' -H 'Content-Type: application/json'