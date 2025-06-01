from model import initialize_model_and_tokenizer
from processing import batch_translate
from config import EN_INDIC_CKPT_DIR
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransToolkit.processor import IndicProcessor
import torch
from datetime import datetime

print("main file")
start_time = datetime.now()
en_indic_tokenizer, en_indic_model = initialize_model_and_tokenizer(EN_INDIC_CKPT_DIR, quantization=None)
ip = IndicProcessor(inference=True)

en_sents = [
    "When I was young, I used to go to the park every day. He has many old books, which he inherited from his ancestors.",
    "I can't figure out how to solve my problem. We watched a new movie last week, which was very inspiring. If you had met me at that time, we would have gone out to eat. She went to the market with her sister to buy a new sari.",
]

src_lang, tgt_lang = "eng_Latn", "tam_Taml"  # "hin_Deva"
hi_translations = batch_translate(en_sents, src_lang, tgt_lang, en_indic_model, en_indic_tokenizer, ip)

print(f"\n{src_lang} - {tgt_lang}")
for input_sentence, translation in zip(en_sents, hi_translations):
    print(f"{src_lang}: {input_sentence}")
    print(f"{tgt_lang}: {translation}")

end_time = datetime.now()
print("Time taken main:", end_time - start_time)

# flush the models to free the GPU memory
del en_indic_tokenizer, en_indic_model