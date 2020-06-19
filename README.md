# CS420 Project

Course Project 2D EM segmentation of CS420, Machine Learning SJTU

In this project, we implemented

- U-Net++
- CE-Net

and trained them on ISBI 2012 cell dataset.

## Requirements

- `python 3.5+`
- `numpy`
- `matplotlib`
- `torch`
- `torchvision`
- `keras`

## Training & Testing

### Data Preprocessing

- Unzip isbi datasets to `data`
- Run `augmentation.py`
- You will get a new training set with 750 images and corresponding labels

### Training & Testing

- Create folder `saved_predict` and folder `isbi` under `UNetpp` or `CENet` folder

- Move the augmented dataset to `isbi` , the structure should be

    ```bash
    isbi
    ├── test
    │   ├── images
    │   └── label
    └── train
        ├── images
        └── label
    ```

- Run `UNetpp.py` or `CENet.py`

- Collect results in `result` and `saved_predict` and model in `saved_model`

- If you want to calculate pixel accuracy, goto `../Acc`, put the prediction results in `img` and labels in `label`, then run `acc.py`

## Group Members

- Xiaosheng He
- Hongzhou Liu
- Yiqun Diao

