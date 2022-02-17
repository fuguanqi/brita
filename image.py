#!/usr/bin/env python
# coding: utf8

# make sure that caffe is on the python path
CAFFE_ROOT = '/home/user/caffe/'
import sys
sys.path.insert(0, CAFFE_ROOT + 'python')
import caffe

import os
import glob
import cv2
import caffe
import numpy as np
from caffe.proto import caffe_pb2

#caffe.set_mode_gpu()
caffe.set_mode_cpu()

# Caffe Model
MODEL_ROOT = 'brita/caffe model/AVA'
IMAGE_MEAN= MODEL_ROOT + 'mean_AADB_regression_warp256.binaryproto'
DEPLOY = MODEL_ROOT + 'initModel.prototxt'
MODEL_FILE = MODEL_ROOT + 'initModel.caffemodel'


#Size of images
IMAGE_WIDTH = 227
IMAGE_HEIGHT = 227

input_layer = 'imgLow'

'''
Image processing helper function
'''
def transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):
    #Image Resizing
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)
    return img


def pred(img_path):
    '''
    Reading mean image, caffe model and its weights
    '''
    #Read mean image
    mean_blob = caffe_pb2.BlobProto()
    with open(IMAGE_MEAN) as f:
        mean_blob.ParseFromString(f.read())
    mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape(
        (mean_blob.channels, mean_blob.height, mean_blob.width))
    
    #Read model architecture and trained model's weights
    net = caffe.Net(DEPLOY,
                    MODEL_FILE,
                    caffe.TEST)
    
    #Define image transformers
    #print "Shape mean_array : ", mean_array.shape
    #print "Shape net : ", net.blobs[input_layer].data.shape
    net.blobs[input_layer].reshape(1,        # batch size
                                  3,         # channel
                                  IMAGE_WIDTH, IMAGE_HEIGHT)  # image size
    transformer = caffe.io.Transformer({input_layer: net.blobs[input_layer].data.shape})
    transformer.set_mean(input_layer, mean_array)
    transformer.set_transpose(input_layer, (2,0,1))
    
    '''
    Making predicitions
    '''
    
    #Making predictions
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)

    net.blobs[input_layer].data[...] = transformer.preprocess(input_layer, img)
    out = net.forward()
    #print out

    pred_score = out['fc11_score'][0][0]
    #print img_path, '\t', pred_score
    return pred_score


