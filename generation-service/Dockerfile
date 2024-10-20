FROM ghcr.io/huggingface/text-generation-inference:2.3.1
RUN mkdir -p /data
WORKDIR /data
EXPOSE 80
CMD ["--model-id", "google-t5/t5-small", "-p", "80"]

# docker image build -t rag-llm-t5 .
# docker tag rag-llm-t5 rag-llm-t5:latest (recommendation: always tag latest build)
# docker push ... (recommendation: push to - private - hub or registry)