#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Junhui Yu
@file:s.py
@time:2022/03/21
"""
import time

common = {
    "exp_name": "jd",
    "encoder": "BERT",
    "data_home": "./datasets",
    "bert_path": "./pretrained_models/bert-base-chinese",  # bert-base-cased， bert-base-chinese
    "run_type": "train",
    "f1_2_save": 0.5,
    "logger": "default"
}

wandb_config = {
    "run_name": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
    "log_interval": 10
}

train_config = {
    "train_data": "train.json",
    "valid_data": "dev.json",
    "ent2id": "ent2id.json",
    "path_to_save_model": "./outputs",  # 在logger不是wandb时生效
    "hyper_parameters": {
        "lr": 5e-5,
        "batch_size": 8,
        "epochs": 5,
        "seed": 2333,
        "max_seq_len": 512,
        "scheduler": "CAWR"
    }
}

eval_config = {
    "model_state_dir": "./outputs/jd/",
    "run_id": "",
    "last_k_model": 1,
    "test_data": "test.json",
    "ent2id": "ent2id.json",
    "save_res_dir": "./results",
    "hyper_parameters": {
        "batch_size": 128,
        "max_seq_len": 128,
    }

}

cawr_scheduler = {
    "T_mult": 1,
    "rewarm_epoch_num": 2,
}
step_scheduler = {
    # StepLR
    "decay_rate": 0.999,
    "decay_steps": 100,
}

# ---------------------------------------------
train_config["hyper_parameters"].update(**cawr_scheduler, **step_scheduler)
train_config = {**train_config, **common, **wandb_config}
eval_config = {**eval_config, **common}
