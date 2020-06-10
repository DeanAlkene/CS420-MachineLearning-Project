from keras.preprocessing.image import img_to_array, load_img,array_to_img
import numpy as np 
import glob
#import cv2
#from libtiff import TIFF

class dataProcess(object):
    def __init__(self, out_rows, out_cols, data_path = "./data/new_train_set/train_img", label_path = "./data/new_train_set/train_label", test_path = "./data/new_test_set/test_img",aug_path = "./results/aug", npy_path = "./results", img_type = "png"):

        self.out_rows = out_rows
        self.out_cols = out_cols
        self.data_path = data_path
        self.label_path = label_path
        self.img_type = img_type
        self.test_path = test_path
        self.npy_path = npy_path
        self.aug_path= aug_path

    def create_train_data(self):
        i = 0
        print('-'*30)
        print('Creating training images...')
        print('-'*30)
        imgs = glob.glob(self.data_path+"/*."+self.img_type)
        augimgs = glob.glob(self.aug_path+"/train/*."+self.img_type)
        print("original images",len(imgs))
        print("augmented images",len(augimgs))
        imgdatas = np.ndarray((len(imgs)+len(augimgs),self.out_rows,self.out_cols,1), dtype=np.uint8)
        imglabels = np.ndarray((len(imgs)+len(augimgs),self.out_rows,self.out_cols,1), dtype=np.uint8)
        for imgname in imgs:
            midname = imgname[imgname.rindex("/")+1:]
            img = load_img(self.data_path + "/" + midname,grayscale = True)
            label = load_img(self.label_path + "/" + midname,grayscale = True)
            img = img_to_array(img)
            label = img_to_array(label)
            imgdatas[i] = img
            imglabels[i] = label
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)+len(augimgs)))
            i += 1
        for imgname in augimgs:
            midname = imgname[imgname.rindex("/")+1:]
            img = load_img(self.aug_path + "/train/" + midname,grayscale = True)
            label = load_img(self.aug_path + "/label/" + midname,grayscale = True)
            img = img_to_array(img)
            label = img_to_array(label)
            imgdatas[i] = img
            imglabels[i] = label
            if i % 100 == 0:
                print('Done: {0}/{1} images'.format(i, len(imgs)+len(augimgs)))
            i += 1
        print('loading done')
        np.save(self.npy_path + '/imgs_train.npy', imgdatas)
        np.save(self.npy_path + '/imgs_mask_train.npy', imglabels)
        print('Saving to .npy files done.')

    def create_test_data(self):
        print('-'*30)
        print('Creating test images...')
        print('-'*30)
        imgs = glob.glob(self.test_path+"/*."+self.img_type)
        print(len(imgs))
        imgdatas = np.ndarray((len(imgs),self.out_rows,self.out_cols,1), dtype=np.uint8)
        for ind in range(len(imgs)):
            
            img = load_img(self.test_path + "/" +str(ind)+".png",grayscale = True)
            img = img_to_array(img)
            #img = cv2.imread(self.test_path + "/" + midname,cv2.IMREAD_GRAYSCALE)
            #img = np.array([img])
            imgdatas[ind] = img
            ind += 1
        print('loading done')
        np.save(self.npy_path + '/imgs_test.npy', imgdatas)
        print('Saving to imgs_test.npy files done.')

    def load_train_data(self):
        print('-'*30)
        print('load train images...')
        print('-'*30)
        imgs_train = np.load(self.npy_path+"/imgs_train.npy")
        imgs_mask_train = np.load(self.npy_path+"/imgs_mask_train.npy")
        imgs_train = imgs_train.astype('float32')
        imgs_mask_train = imgs_mask_train.astype('float32')
        imgs_train /= 255
        #mean = imgs_train.mean(axis = 0)
        #imgs_train -= mean    
        imgs_mask_train /= 255
        imgs_mask_train[imgs_mask_train > 0.5] = 1
        imgs_mask_train[imgs_mask_train <= 0.5] = 0
        return imgs_train,imgs_mask_train

    def load_test_data(self):
        print('-'*30)
        print('load test images...')
        print('-'*30)
        imgs_test = np.load(self.npy_path+"/imgs_test.npy")
        imgs_test = imgs_test.astype('float32')
        imgs_test /= 255
        #mean = imgs_test.mean(axis = 0)
        #imgs_test -= mean    
        return imgs_test

if __name__ == "__main__":


    mydata = dataProcess(512,512)
    mydata.create_train_data()
    mydata.create_test_data()