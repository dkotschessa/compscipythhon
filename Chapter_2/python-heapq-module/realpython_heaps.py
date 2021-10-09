import datetime
import heapq


def email(frequency, details):
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details


fast_email = email(datetime.timedelta(minutes = 15), "fast emaiil")
slow_email = email(datetime.timedelta(minutes = 40), "slow email")

unified = heapq.merge(fast_email, slow_email)

def test_emails():
    for _ in range(10):
        print(next(unified)) 

## women's 100 meter finals 2016

results="""\
Christania Williams      11.80
Marie-Josee Ta Lou       10.86
Elaine Thompson          10.71
Tori Bowie               10.83
Shelly-Ann Fraser-Pryce  10.86
English Gardner          10.94
Michelle-Lee Ahye        10.92
Dafne Schippers          10.90
"""



def test_runners_top_3():
    top_3 = heapq.nsmallest(
    3, # how many elements
    results.splitlines(), # split by whitespace
    key=lambda x: float(x.split()[-1])) # callable function to do determine how elements are compard
    print("\n".join(top_3))

def test_runners_bottom_3():
    top_3 = heapq.nlargest(
    3, results.splitlines(), key=lambda x: float(x.split()[-1]))
    print("\n".join(top_3))