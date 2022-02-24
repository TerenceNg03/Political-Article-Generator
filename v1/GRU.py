import torch
import torch.nn as nn

class GRUNet(nn.Module):
    def __init__(self, input_dim=100, hidden_dim=1280, n_layers=1, drop_prob=0):
        super(GRUNet, self).__init__()
        self.hidden_dim = hidden_dim
        self.n_layers = n_layers
        self.gru = nn.GRU(input_dim, hidden_dim, n_layers, batch_first=True, dropout=drop_prob)
        self.affine = nn.Linear(hidden_dim, input_dim)
        
    def forward(self, x, h):
        out, h = self.gru(x, h)
        out = self.affine(out)
        return out, h
    
    def init_hidden(self, batch_size):
        weight = next(self.parameters()).data
        hidden = weight.new(self.n_layers, batch_size, self.hidden_dim).zero_()
        return hidden