from PIL import Image
import numpy as np
import os

def compute_acc(path_img, path_label):
'''
    Calculate pixel accuracy for a single test image
'''
    img = np.load(path_img).astype(int) # Load prediction image
    #img.show()
    label = Image.open(path_label).convert('L') # Convert label image to grayscale image
    #print(img[250])
    label = (np.array(label) / 255).astype(int) # Normalize and convert to int for later calculation
    #print(label[250])
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            if(img[i][j] == label[i][j]):
                if(label[i][j] == 0):
                    TN = TN + 1
                else:
                    TP = TP + 1
            else:
                if(label[i][j] == 0):
                    FP = FP + 1
                else:
                    FN = FN + 1
    return TN, TP, FP, FN

acc = 0
all_TN = 0
all_TP = 0
all_FP = 0
all_FN = 0


for name in os.listdir("img"):
    img_file = os.path.join("img/%s" % name)
    label_file = os.path.join("label/%s" % name.split('.')[0] + '.png')
    TN, TP, FP, FN = compute_acc(img_file, label_file)
    all_TN = all_TN + TN
    all_TP = all_TP + TP
    all_FP = all_FP + FP
    all_FN = all_FN + FN
acc = (all_TP + all_TN)/ (all_TP + all_FN + all_FP + all_TN)

print(all_TP)
print(all_FP)
print(all_FN)
print(all_TN)

print(acc)










