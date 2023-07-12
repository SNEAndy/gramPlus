import torch  # 命令行是逐行立即执行的
# MEGA = torch.load('resnet50-19c8e357.pth')
# print(MEGA)   # keys()
# 之后有其他需求比如要看 key 为 model 的内容有啥
from torchvision import models
# model = models.resnet50(pretrained=True)
# model=torch.load('new_model.pth')
# model = models.resnet101(pretrained=True)
# print(model.layer4)
# model2 = torch.hub.load_state_dict_from_url(
#         url="https://huggingface.co/Visual-Attention-Network/VAN-Base-original/resolve/main/van_base_828.pth.tar",
#         map_location="cpu", check_hash=True
#     )
# for x in model2:
#     print(x)
# for x in model2['state_dict']:
#     print(x)
# for i in model2['state_dict'].children():
#     print(i)
# print(model2)
#
# for x in model['state_dict']:
#     print(x)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

print(model)
