def merge_the_tools(string, k):
    # your code goes here
    sub_str_len = len(string)/k
    last_str_len = len(string)%k
    start_off = 0
    end_off = sub_str_len
    while(end_off <= sub_str_len-last_str_len):
        sub_str = string[start_off:end_off]
        print(sub_str)
        start_off, end_off = end_off, end_off+sub_str_len

if __name__ == '__main__':
    # string, k = input(), int(input())
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)