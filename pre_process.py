#!/usr/bin/python2
# -*-coding:utf-8-*-
import codecs


def character_4tagging(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    cnt = 0
    for line in input_data.readlines():
        # if cnt > 0:
        #     break
        # cnt += 1
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output_data.write(word + "\tS\n")
            else:
                output_data.write(word[0] + "\tB\n")
                for w in word[1:len(word) - 1]:
                    output_data.write(w + "\tM\n")
                output_data.write(word[len(word) - 1] + "\tE\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    character_4tagging("data/icwb2-data/training/pku_training.utf8",
                       "data/icwb2-data/training/pku_training_crf.utf8")
