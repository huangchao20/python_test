import numpy as np
import random
import re

__author__ = 'yangxin'
"""
���������ʼ�
"""


class FilterSpam(object):

    # �ִʲ�����ƥ������ķǵ����ַ���
    def text_parse(self, big_str):
        token_list = re.split(r'\W+', big_str)
        if len(token_list) == 0:
            print(token_list)
        return [tok.lower() for tok in token_list if len(tok) > 2]

    # Ϊ�����б�ȥ��
    def create_vocab_list(self, data_set):
        vocab_set = set()
        for item in data_set:
            vocab_set = vocab_set | set(item)
        return list(vocab_set)

    # ����б��е����Ƿ��������������ݼ���
    def set_of_words_to_vec(self, vocab_list, input_set):
        result = [0] * len(vocab_list)
        for word in input_set:
            if word in vocab_list:
                # �絥���������ĵ����ֹ�������Ϊ1������Ϊ0
                result[vocab_list.index(word)] = 1
        return result

    # ѵ�����ر�Ҷ˹�㷨������
    def train_naive_bayes(self, train_mat, train_category):
        train_doc_num = len(train_mat)
        words_num = len(train_mat[0])
        pos_abusive = np.sum(train_category) / train_doc_num
        p0num = np.ones(words_num)
        p1num = np.ones(words_num)
        p0num_all = 2.0
        p1num_all = 2.0
        for i in range(train_doc_num):
            if train_category[i] == 1:
                p1num += train_mat[i]
                p1num_all += np.sum(train_mat[i])
            else:
                p0num += train_mat[i]
                p0num_all += np.sum(train_mat[i])
        p1vec = np.log(p1num / p1num_all)
        p0vec = np.log(p0num / p0num_all)
        return p0vec, p1vec, pos_abusive

    # �������ر�Ҷ˹����
    def classify_naive_bayes(self, vec_to_classify, p0vec, p1vec, p_class1):
        p1 = np.sum(vec_to_classify * p1vec) + np.log(p_class1)
        p0 = np.sum(vec_to_classify * p0vec) + np.log(1 - p_class1)
        if p1 > p0:
            return 1
        else:
            return 0

    # �ʼ��������
    def spam_test(self):
        doc_list = []
        class_list = []
        full_text = []
        for i in range(1, 26):
            try:
                words = self.text_parse(open('/email/spam/{}.txt'.format(i)).read())
            except:
                words = self.text_parse(
                    open('/email/spam/{}.txt'.format(i), encoding='utf-8').read())
            doc_list.append(words)
            full_text.extend(words)
            class_list.append(1)
            try:
                # ��ӷ������ʼ�
                words = self.text_parse(open('/email/ham/{}.txt'.format(i)).read())
            except:
                words = self.text_parse(
                    open('/email/ham/{}.txt'.format(i), encoding='utf-8').read())
            doc_list.append(words)
            full_text.extend(words)
            class_list.append(0)
        # �����ʻ��
        vocab_list = self.create_vocab_list(doc_list)
        # �������ȡ10����, Ϊ�˱��⾯�潫ÿ������ת��Ϊ����
        test_set = [int(num) for num in random.sample(range(50), 10)]
        # ����ԭ����training_set��ȥ����10����
        training_set = list(set(range(50)) - set(test_set))
        training_mat = []
        training_class = []
        for doc_index in training_set:
            training_mat.append(self.set_of_words_to_vec(vocab_list, doc_list[doc_index]))
            training_class.append(class_list[doc_index])
        p0v, p1v, p_spam = self.train_naive_bayes(np.array(training_mat), np.array(training_class))
        # ��ʼ����
        error_count = 0
        for doc_index in test_set:
            word_vec = self.set_of_words_to_vec(vocab_list, doc_list[doc_index])
            if self.classify_naive_bayes(np.array(word_vec), p0v, p1v, p_spam) != class_list[doc_index]:
                error_count += 1
        print('the error rate is {}'.format(error_count / len(test_set)))
