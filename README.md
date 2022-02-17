# brita - Bounce Rate Prediction on Image & Text Aesthestics
This project is only for academic use. Considerations of commercial use is discouraged. The caffe model file is oversized for github and can be downloaded from https://pan.baidu.com/s/1AUOA0Hlbzc4cwInS_5uRSA?pwd=x1gv (提取码：x1gv)

## Running environment
python 2.7  
caffe

## Image Aesthetic
Image Aesthetic is predicted based on the model of [deepImageAestheticsAnalysis](https://github.com/aimerykong/deepImageAestheticsAnalysis).

## Text Aesthetic
Text Aesthetic is measured on a Simiplified Chinese LIWC Service, [TextMind](http://ccpl.psych.ac.cn/textmind/). File text.py provides a spider to query for the number of words belonging to caregory "perception" which is used for measuring text aesthetic score.

## Bounce Rate Prediction
Bounce Rate can be predicted based on Image & Text Aesthestics by Model 2 or 3 from the paper below. If you find the model/method useful, please cite this work:
>Wang, X., Li, Y., Cai, Z. and Liu, H. (2021), "Beauty matters: reducing bounce rate by aesthetics of experience product portal page", Industrial Management & Data Systems, Vol. 121 No. 8, pp. 1848-1870. https://doi.org/10.1108/IMDS-08-2020-0484

## Usage
An example calling this module is given by example.py
