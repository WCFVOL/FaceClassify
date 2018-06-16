#!/usr/bin/env python
# -*- coding:utf-8 -*-

from TwoFace.retrieval.pre_process import *
import numpy as np


def search(test_x, train_x, str_sim_metric):

    sim_metric_method = sim_metric_methods_set[str_sim_metric]
    if str_sim_metric == 'cos':
        test_x, train_x = norm_data(test_x, train_x)

    assert test_x.shape[1] == train_x.shape[1]
    sample = test_x[0]
    sim_result = sim_metric_method(sample, train_x)
    sort_index = np.argsort(sim_result)
    return sim_result[sort_index[0]]


def judge_two_face(img1, img2):
    return 1-search(img1, img2, 'cos')

