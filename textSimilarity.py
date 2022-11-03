import sys
import pandas as pd
from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer as SBert

model = SBert('paraphrase-multilingual-MiniLM-L12-v2')
sentences1 = ['塑料制品制造']

sentences2 = ['新一代信息技术集成电路',
              '医疗器械制造业',
              '造纸和纸制品业',
              '计算机、通信和其他电子设备制造业',
              '科技推广和应用服务业']

# Compute embedding for both lists
embeddings1 = model.encode(sentences1)
embeddings2 = model.encode(sentences2)

# Compute cosine-similarits
cosine_scores = cos_sim(embeddings1, embeddings2)
print(cosine_scores)
