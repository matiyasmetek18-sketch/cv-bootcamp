import torch
import torch.nn as nn
import numpy as np
import os

class DnCNN(nn.Module):
    def __init__(self, channels=1, num_layers=17):
        super(DnCNN, self).__init__()
        layers = []

        # First layer
        layers.append(nn.Conv2d(channels, 64, kernel_size=3, padding=1))
        layers.append(nn.ReLU(inplace=True))

        # Middle layers
        for _ in range(num_layers - 2):
            layers.append(nn.Conv2d(64, 64, kernel_size=3, padding=1))
            layers.append(nn.BatchNorm2d(64))
            layers.append(nn.ReLU(inplace=True))

        # Last layer
        layers.append(nn.Conv2d(64, channels, kernel_size=3, padding=1))

        self.dncnn = nn.Sequential(*layers)

    def forward(self, x):
        noise = self.dncnn(x)
        return x - noise  # DnCNN predicts noise, so subtract it


def load_dncnn_model():
    model = DnCNN()
    weights_path = os.path.join(os.path.dirname(__file__), "weights", "DnCNN_sigma25.pth")

    state_dict = torch.load(weights_path, map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()
    return model


def denoise_image(model, image_np):
    # image_np: H x W grayscale image in uint8 or float32

    # Normalize to [0,1]
    img = image_np.astype(np.float32) / 255.0

    # Add batch + channel dims: (1,1,H,W)
    img_tensor = torch.from_numpy(img).unsqueeze(0).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor).squeeze().numpy()

    # Clip and convert back to uint8
    output = np.clip(output * 255.0, 0, 255).astype(np.uint8)
    return output
