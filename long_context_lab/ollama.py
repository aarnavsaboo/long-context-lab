from time import perf_counter
from urllib.request import Request,urlopen
import json


class OllamaRunner:
    def __init__(self, model: str, endpoint: str="http://127.0.0.1:11434"):
        self.model=model
        self.endpoint=endpoint.rstrip("/")

    def generate(self,prompt:str,max_tokens:int=32)->dict:
        body=json.dumps({
            "model":self.model,
            "prompt":prompt,
            "stream":False,
            "options":{"temperature":0.0,"num_predict":max_tokens},
        }).encode()
        req=Request(self.endpoint+"/api/generate",data=body,headers={"Content-Type":"application/json"},method="POST")
        started=perf_counter()
        with urlopen(req,timeout=600) as response:
            row=json.load(response)
        elapsed=perf_counter()-started
        return {
            "text":row.get("response",""),
            "elapsed_seconds":elapsed,
            "prompt_tokens":row.get("prompt_eval_count"),
            "output_tokens":row.get("eval_count"),
            "load_duration_ns":row.get("load_duration"),
            "prompt_eval_duration_ns":row.get("prompt_eval_duration"),
            "eval_duration_ns":row.get("eval_duration"),
        }
