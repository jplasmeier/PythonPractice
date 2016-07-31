# Practice with rate limiting / sliding window problems
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

def is_rate_limit_violated_bf(req_lst, max_req, interval):
    for req in req_lst:
        upper = req + interval
        count = 0
        for i in range(req, upper):
            count = count + req_lst.count(i)
        if count > max_req:
            return True
    return False

def is_rate_limit_violated_better(req_lst, max_req, interval):
    for idx, req in enumerate(req_lst):
        upper = req + interval
        index = idx
        while index < len(req_lst) and req_lst[index] < upper:
            index = index + 1
        if index - idx > max_req:
            return True
    return False

req_lst_true = [1,3,4,6,10,11,13,14,15,19,20,21,22,22,23,24,27,28,28,28]
req_lst_false = [1,3,4,6,10,11,13,15,15,19,20]
max_req = 4
interval = 5
print is_rate_limit_violated_bf(req_lst_true, max_req, interval)
print is_rate_limit_violated_bf(req_lst_false, max_req, interval)
print is_rate_limit_violated_better(req_lst_true, max_req, interval)
print is_rate_limit_violated_better(req_lst_false, max_req, interval)


