# main.py

from typing import Optional
from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

import os

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    smiles: str
    seq: str
    window: str
    thresholds: str
    sites: str

app = FastAPI()

@app.post("/{item_id}")
async def create_item(item_id:str, item: Item):
    if item_id == 'eval':
        cmd = "python cnn_fcnn_model.py --option Evaluation"
        os.system(cmd + " > out2.txt")
        f = open('out2.txt', "r")
        text = f.readlines()
        fulltext = ""
        for i in text:
            fulltext = fulltext + i
        f.close()
        return {"result": fulltext}

    if item_id == 'infer':
        # protein-arg = " --protein_sequence " + item.seq
        # smiles-arg = " --smiles_string " + item.smiles
        # window-arg = " --window " + [i for i in item.window]
        # threshold-arg = " --thresholds " + [i for i in item.thresholds]
        # sites-arg = " --sites " + [i for i in item.sites]
        cmd = "python gradram_testing.py " + " --protein_sequence " + item.seq + " --smiles_string '" + item.smiles + "' --window " + item.window + " --thresholds " + item.thresholds + " --sites " + item.sites
        # print(cmd)
        os.system(cmd + " > out.txt")

        f = open('out.txt', "r")
        text = f.readlines()
        fulltext = ""
        for i in text:
            fulltext = fulltext + i
        f.close()
        # print("--------------")
        # print(cmd)
        # print(fulltext)
        # print("-------------")
        return {"result": fulltext}

