# python3

import sys
import threading
import numpy


def compute_height(k, parents):
    vieta = [[] for _ in range(k)]
    root = None 
    for i in range(k):
        if parents[i] == -1:
            root = i
        else:
            vieta[parents [i]].append(i)
    
    def max_height(r):
        height = 1
        if not vieta [r]:
            return height 
        else:
            for child in vieta[r]:
                height = max (height,max_height(child))
            return height + 1
    return max_height(root)


def main():
    words =input ("F or I:")
    if "I" in words:
        k=int(input())
        parents =list(map(int, input().split()))
    elif "F" in words:
        name = input()
        path='./tets/'
        file = path + name 
        if "a" not in name:
            try:
                with open(file) as f:
                    k=int(f.readline())
                    parents =list(map(int,f.readline().split()))
            except Exception as e:
                print("error",str(e))
                return
        else:
            print("error")
            return 

    print(compute_height(k,parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27) 
threading.Thread(target=main).start()
# main()