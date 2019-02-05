import re
_input_file = "C:/Users/guruv/PycharmProjects/Test_Scripts/input"
_all_word_list = []
with open(_input_file,'r') as f:
    contents = f.read()
    print('File contents:\n{}'.format(contents))

    print(re.search('\b+', contents))


    # unique_words = set(re.search('\b', contents))
    # print("unique words: {}".format(unique_words))
    # print("number of unique words: {}".format(len(unique_words)))

# _input_file = "C:/Users/guruv/PycharmProjects/Test_Scripts/input"
# _all_word_list = []
# with open(_input_file,'r') as f:
#     contents = f.read()
#     print('File contents:\n{}'.format(contents))
#     for line in contents.split("\n"):
#         for word in line.split(" "):
#             # print("Word: {}".format(word))
#             if word is not "":
#                 _all_word_list.append(word)
#
#     unique_words = set(_all_word_list)
#     print("unique words: {}".format(unique_words))
#     print("number of unique words: {}".format(len(unique_words)))