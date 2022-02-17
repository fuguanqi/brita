#!/usr/bin/env python
# coding: utf8


def model_2(img_score, txt_score):
    bounce_rate_pred=0.505*img_score\
                     -1.387*txt_score\
                     -0.516*img_score**2\
                     +1.415*txt_score**2
    return bounce_rate_pred


def model_3(img_score, txt_score):
    bounce_rate_pred=-2.386*img_score\
                     -8.105*txt_score\
                     +1.284*img_score**2\
                     +6.284*txt_score**2\
                     +10.483*txt_score*img_score\
                     -3.287*txt_score*img_score**2\
                     -5.260*img_score*txt_score**2
    return bounce_rate_pred


