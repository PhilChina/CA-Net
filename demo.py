import torch
import os
gpus = list(range(torch.cuda.device_count()))
print(gpus)

strx = ','.join([str(x) for x in gpus])
print(strx)

os.environ['CUDA_VISIBLE_DEVICES'] = strx
