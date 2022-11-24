import pandas as pd
import torch
import transformers
from transformers import  AutoTokenizer, AutoModelForMaskedLM, RobertaModel

# Import df
chemicals_df = pd.read_csv("Module2_6_Substances.csv")

# Import chembert model
tok = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
mod = RobertaModel.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")

def batch(iterable, n=1):
    batches = []
    l = len(iterable)
    for ndx in range(0, l, n):
        batches.append(iterable[ndx:min(ndx + n, l)])
    return batches
  
# Transform df to lists for easier processing
smiles = chemicals_df['QSAR_READY_SMILES'].tolist()
mols = chemicals_df['DTXSID'].tolist()

# Extract embeddings by applying chembert model to tokenized smiles
raw_out = []
# batch to avoid runtime errors
for b in batch(smiles,20):
    inputs = tok(b, padding=True, return_tensors="pt")
    outputs = mod(**inputs)
    raw_out.extend(outputs[1])
    
# Normalize embeddings
embeds = [out/torch.norm(out) for out in raw_out]

# remove requires_grad from tensor to avoid error
embeddings = [t.detach() for t in embeds]

# Make embeddings dataframe
embed_df = pd.DataFrame(embeddings).astype("float")
embed_df.insert(0, "DTXSID", mols, allow_duplicates=True)
embed_df
embed_df.to_csv('aspis_workshop_chembert_embeddings.csv', index=False, sep=',')
