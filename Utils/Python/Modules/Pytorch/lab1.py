import torch
from torch.cpu import is_available

print(torch.cuda.is_available())
print(torch.cuda.get_device_name())
print(torch.cuda.device_count())

t = torch.FloatTensor([2,3])
print(t)

t = t.cuda(0)
print(t)

t = t.cpu()
print(t)