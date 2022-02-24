import numpy as np
import torch

from gensim.models import word2vec
import re

from importlib import reload, import_module

model = word2vec.Word2Vec.load('word2vec.model')

def gen_text(version, init_sentence, gen_len, temperature):
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    print(version, init_sentence, gen_len, temperature)
    GRU = import_module(version+'.GRU')
    GRU = reload(GRU)
    gru_net = GRU.GRUNet().to(device)
    checkpoint = torch.load(version+'/gru.checkpoint', map_location=device)
    gru_net.load_state_dict(checkpoint['model_state_dict'])    
    sentence = []
    prunc_re = re.compile('[\w]{1,}')
    with torch.no_grad():
        h = gru_net.init_hidden(1)
        #h = torch.rand(h.shape)
        h = h.to(device)
        sentence = []
        Cap = True
        for word in init_sentence.lower().split():
            if word in model.wv.vocab:
                x = model.wv[word].reshape(1,1,100)
            else:
                x = np.zeros(model.vector_size, dtype=np.float32)
            x = torch.tensor(x).reshape(1,1,100).to(device)
            x, h = gru_net(x, h)
            if Cap and prunc_re.match(word):
                word = word.capitalize()
                Cap = False
            if not prunc_re.match(word):
                Cap = True
            sentence.append(word)

        for _ in range(gen_len):
            x, h = gru_net(x, h)
            output = x.squeeze().cpu().numpy()
            wordlist = model.wv.most_similar(positive = output.reshape(1,100))
            word, _ = wordlist[np.random.randint(max(10, int(temperature*10*0.8))) if np.random.rand()<temperature else 0]
            x = model.wv[word]
            x = torch.tensor(x).reshape(1,1,100).to(device)
            if Cap and prunc_re.match(word):
                word = word.capitalize()
                Cap = False
            if not prunc_re.match(word) and word != ',':
                Cap = True
            sentence.append(word)
        return ' '.join(sentence)+'\n'
