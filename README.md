# 🦙 Llama playground for CPU 💻

Since my desktop is getting bit aged, my options for running local LLMs is a bit limited.

Luckily, running quantized Llama models with `llama.cpp` on my CPU (with 8GB RAM) works alright.

Loading the model takes ~40 seconds and the inference runs at 3.6 tokens/second (not great, not terrible).

## Quantize model

One way or another, quantize a Llama model. This project uses `LlamaCpp` on LangChain. To be fully honest, I don't really know the requirements, but I have been using a Llama2 model quantized to the `.gguf` format, and that works at the very least.

Place the path to the file inside a file named `PATH_TO_MODEL_FILE` before building the image.

## Build & run the playground

This project uses Docker. Build the image using `build.sh` and run a container using `run.sh`.

The image will contain the artifact of the model, since I found that it loads much faster than if it were mounted.

When running the playground using `python3 prompt.py`, you will be asked to insert your prompt using `nano`. The prompts and outputs will be saved to `/history`.
