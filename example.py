#!/usr/bin/env python
# coding: utf8

import brita.text as text
import brita.image as image
import brita.br as br

image_file="test.jpg"
txt = {'str' : '红色发财果仿真花冬青假花插花摆设客厅漂亮美丽家居新年装饰婚庆花艺摆件芬芳'}  #post数据  

img_score=image.pred(image_file)
txt_score=text.pred(txt)
bounce_rate_pred_2=br.model_2(img_score,txt_score)
bounce_rate_pred_3=br.model_3(img_score,txt_score)
print 'image score:',img_score
print 'text score:', txt_score
print 'bounce rate predicted by model 2:',bounce_rate_pred_2
print 'bounce rate predicted by model 3:',bounce_rate_pred_3
