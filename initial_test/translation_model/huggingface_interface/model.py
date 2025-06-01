from transformers import AutoModelForSeq2SeqLM, BitsAndBytesConfig, AutoTokenizer
import torch
from datetime import datetime
from config import DEVICE

print("model file")
def initialize_model_and_tokenizer(ckpt_dir, quantization):
    start_time = datetime.now()
    if quantization == "4-bit":
        qconfig = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
    elif quantization == "8-bit":
        qconfig = BitsAndBytesConfig(
            load_in_8bit=True,
            bnb_8bit_use_double_quant=True,
            bnb_8bit_compute_dtype=torch.bfloat16,
        )
    else:
        qconfig = None
    print("loading model")
    tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, trust_remote_code=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        ckpt_dir,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        quantization_config=qconfig,
    )

    if qconfig == None:
        model = model.to(DEVICE)
        if DEVICE == "cuda":
            model.half()

    model.eval()

    end_time = datetime.now()
    print("model loaded successful and set to eval state")
    print("Time taken:", end_time - start_time)

    return tokenizer, model