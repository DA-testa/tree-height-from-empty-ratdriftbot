# python3

import sys
import threading
import numpy


def compute_height(k, parents):
    location = [[] for _ in range(k)]
    path = None 
    for i in range(k):
        if parents[i] ==-1:
            path = 1
            else:
                place[parents [i]].append(i)
    
    def max_height(r):
        heigh = 1
        if not place [r]:
            return height 
        else:
            for baby in place[r]:
                heigh = max (heigh, max_height(baby))
            return height + 1
    return max_height(root)


def main():
    words =input ("F or I:")
    if "I" in words:
        k=int(input())
        parents =list(map(int, input().split()))
    elif "F" in words:
        name = input()
        root='./tets/'
        file = root + name 
        if "a" not in name:
            try:
                with open(file) as f:
                    k=int(f.read.line())
                    parents =list (map(int, f.readline().split()))
            except Exception as e:
                print("errror",str(e))
                return
            else:
                print("error")
                return 

    print(compute_height(k,parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27) 
threading.Thread(target=main).start()
# main()