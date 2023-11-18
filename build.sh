cp $(cat PATH_TO_MODEL_FILE) $(basename $(cat PATH_TO_MODEL_FILE))

docker build \
       -t llama-playground:latest \
       --build-arg FILE_NAME=$(basename $(cat PATH_TO_MODEL_FILE)) \
       .

rm $(basename $(cat PATH_TO_MODEL_FILE))
