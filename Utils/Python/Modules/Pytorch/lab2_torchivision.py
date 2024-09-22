import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# ref: https://github.com/PacktPublishing/Deep-learning-with-PyTorch-video/blob/master/1.8.popular.datasets.ipynb

# Transforms are applied to each image. Some are mandatory, like conversion to Tensor and
# Normalize the image. Others are optional and used for data augmentation (like random crop,
# random jitter etc.)

transform = transforms.Compose([transforms.ToTensor(),
                                # Various transforms can be added in this pipeline for data augmentation
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# ref: https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
# above link expalains how to inherit from Dataset abstract class to create dataloader for custom datasets
torch.utils.data.Dataset

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)

print(len(trainset.data))

plt.imshow(trainset.data[1])
print(trainset.data[1], " - Happens to be the truck class")

trainloader = torch.utils.data.DataLoader(trainset, batch_size=10,
                                          shuffle=True, num_workers=0)

for i, data in enumerate(trainloader):
    data, labels = data

    print("Iteration ", i)
    print("")
    print("type(data): ", type(data))
    print("data.size(): ", data.size())
    print("")
    print("type(labels): ", type(labels))
    print("labels.size(): ", labels.size())

    # Model training happens here

    break