# class Counter:
#     def __init__(self,numebers) -> None:
#         self.counts = {}
#         for number in numebers:
#             if number not in self.counts:
#                 self.counts[number] = 0
#             self.counts[number] +=1

#     def get_count(self,number):
#         return self.counts.get(number,0)


#     def count_occurences(numbers,M):
#         counter = Counter(numbers)
#         for i in range(1,M+1):
#             print(counter.get_count(i))


#     if __name__ == '__main__':
#      N,M = map(int,input().split())
#      numbers = list(map(int,input().split()))
#      count_occurences(numbers,M)

def count_frequency(array,M):
    frequency = [0] * (M+1)
    for number in array:
        frequency[number] +=1
    return frequency


def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    frequency = count_frequency(A,M)

    for i in range(1,M+1):
        print(frequency[i])

if __name__ == '__main__':
    main()        


        
      