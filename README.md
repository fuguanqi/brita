# ita - Bounce Rate Prediction on Image & Text Aesthestics
This project is only for academic use. Considerations of commercial use is discouraged.

## Running environment
python 2.7  
caffe

## Image Aesthetic
Image Aesthetic is predicted based on the model of [deepImageAestheticsAnalysis](https://github.com/aimerykong/deepImageAestheticsAnalysis).

## Text Aesthetic
Text Aesthetic is measured on a Simiplified Chinese LIWC Service, [TextMind](http://ccpl.psych.ac.cn/textmind/). File text.py provides a spider to query for the number of words belonging to caregory "perception".

## Bounce Rate Prediction
Bounce Rate canbe predicted by Model 2 or 3, based on Image & Text Aesthestics.

## Usage
An example calling this module is given by example.py
