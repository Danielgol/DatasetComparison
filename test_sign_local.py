#!/usr/bin/env python3 -u
import logging
import math
import os
import random
import sys

import numpy as np
import torch

import sacrebleu
import rouge_local as rouge
from bleu_local import compute_bleu


def calculate(hyps, refs):
    tokenize = sacrebleu.DEFAULT_TOKENIZER
    for h, r in zip(hyps, refs):

        sacrebleu_score, _, _ = sacrebleu.corpus_bleu(h, [r], tokenize=tokenize), hyps, refs
        bleu = compute_cvpr_bleu(h, r)
        rouge_score = rouge.rouge(h, r)

        for i in range(len(h)):
            print(h[i], r[i]+"\n")

        #print('{} set has {} samples,\n'
        #      'sacrebleu: {},\n'
        #      'CVPR BLEU scripts: {}\n'
        #      'CVPR ROUGE: {}'.format(split, len(h), sacrebleu_score, bleu, rouge_score))

        print('performance: {:.2f} {}'.format(rouge_score['rouge_l/f_score']*100 ,' '.join([str(b) for b in bleu])))


def compute_cvpr_bleu(hyps, refs, max_order=4):
    """Assume tokens in hypothesis and references are seperated with spaces.
    """
    tokenized_hyps = []
    tokenized_refs = []

    for h in hyps:
        tokenized_hyps.append(h.split())

    for r in refs:
        tokenized_refs.append([r.split()])

    bleu_all_orders = []

    for i in list(range(1, max_order+1)):
        bleu, precisions, bp, ratio, translation_length, reference_length = compute_bleu(tokenized_refs, tokenized_hyps, max_order=i)
        if i == 4:
            print ('precisions: {}'.format([str(round(p*100, 2)) for p in precisions]))
        bleu_all_orders.append(round(bleu * 100, 2))

    return bleu_all_orders