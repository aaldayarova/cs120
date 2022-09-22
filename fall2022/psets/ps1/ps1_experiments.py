import random, pandas, numpy, seaborn
from time import time
from ps1 import radixSort, countSort, mergeSort, merge

def generateData():
    allArrs = []

    # iterate over powers of 2
    for i in range(1, 16):
        for j in range(1, 20):
            # add info and create randomized array
            curr = {}
            n = 2 ** i
            U = 2 ** j
            curr['n'] = n
            curr['U'] = U
            mavgs = []
            cavgs = []
            ravgs = []
            print(f'Combo {n} and {U}')
            for _ in range(2):
                # get 10 samples
                currArray = [[random.randint(0, U - 1), random.randint(0, U - 1)] for _ in range(n)]

                # time each mergesort and count sort
                start = time()
                mergeSort(currArray)
                mavgs.append(time() - start)

                start = time()
                countSort(U, currArray)
                cavgs.append(time() - start)

                start = time()
                radixSort(U, n, currArray)
                ravgs.append(time() - start)

            # add avgs to sample
            curr['mtime'] = sum(mavgs) / 2
            curr['ctime'] = sum(cavgs) / 2
            curr['rtime'] = sum(ravgs) / 2

            # add current sample to array
            allArrs.append(curr)
    

    df = pandas.DataFrame(allArrs)

    df.to_csv('output.csv')
    
    
    
    
    # dataArray = []
    # arrayParams = {}
    # for element in range(1, 21):
    #     U = 2**element
    #     for number in range(1, 17):
    #         n = 2**number

    #         arrayParams['U'] = U
    #         arrayParams['n'] = n
    #         countSum = 0
    #         radixSum = 0
    #         mergeSum = 0

    #         countAvgs = []
    #         radixAvgs = []
    #         mergeAvgs = []
    #         for i in range(10):
    #             arr = ([random.randint(0, U-1), 0] for _ in range(n))

    #             t0 = time()
    #             countSort(U, arr)
    #             t1 = time()
    #             radixSort(U, n, arr)
    #             t2 = time()
    #             mergeSort(arr)
    #             t3 = time()

    #             countSum = (t1-t0)
    #             countAvgs.append(countSum)
    #             radixSum = (t2-t1)
    #             countAvgs.append(radixSum)
    #             mergeSum = (t3-t2)
    #             countAvgs.append(mergeSum)
            
    #         iterationCountTime = sum(countAvgs)/10
    #         iterationRadixTime = sum(radixAvgs)/10
    #         iterationMergeTime = sum(mergeAvgs)/10

    #         bestTime = min(iterationCountTime, iterationRadixTime, iterationMergeTime)
    #         if bestTime == iterationCountTime:
    #             arrayParams['Best Sort'] = "Count"
    #         elif bestTime == iterationRadixTime:
    #             arrayParams['Best Sort'] = "Radix"
    #         else:
    #             arrayParams['Best Sort'] = "Merge"
            
    #         dataArray.append(arrayParams)

    # data = pandas.DataFrame(dataArray)
    # data.to_csv('SortRuntimes.csv')

def main():
    df = pandas.read_csv('output.csv')
    df['logU'] = numpy.log2(df['U'])
    df['logN'] = numpy.log2(df['n'])
    palette = {
        'counting': 'tab:blue',
        'radix': 'tab:red',
        'merge': 'tab:purple',
    }
    fplot = seaborn.scatterplot(data=df, x="u_log", y="n_log", hue="sort", palette= palette)
    fplot.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    fplot.show()

generateData()

if __name__ == "__main__":
    main()
# print('countSort list:', countList)
# print('radixSort list:', radixList)
# print('mergeSort list:', mergeList)