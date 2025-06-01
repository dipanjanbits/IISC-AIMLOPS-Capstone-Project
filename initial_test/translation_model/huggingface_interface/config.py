import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)
BATCH_SIZE = 4
EN_INDIC_CKPT_DIR = "models/"  # "ai4bharat/indictrans2-en-indic-1B"