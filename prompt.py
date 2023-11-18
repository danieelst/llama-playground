import os
from subprocess import call
from math import floor
from time import time
from langchain.llms import LlamaCpp

PATH_TO_HISTORY = r'/history/'

timestamp = str(floor(time()))

prompt_file = f'{PATH_TO_HISTORY}{timestamp}-input.txt'
output_file = f'{PATH_TO_HISTORY}{timestamp}-output.txt'

start_time = time()

llm = LlamaCpp(
  model_path=os.environ['PATH_TO_MODEL_FILE'],
  verbose=False
)

print(f'Finished loading model: {time() - start_time}s')

call(['nano', prompt_file])

with open(prompt_file, 'r') as f:
  prompt = f.read()

start_time = time()

output = llm(prompt)

print(f'Finished evaluating prompt: {time() - start_time}s')

with open(output_file, 'w') as f:
  print(f'Writing output to {output_file}')
  f.write(output)

print(f'\n{prompt}{"-"*40}\n{output}')
