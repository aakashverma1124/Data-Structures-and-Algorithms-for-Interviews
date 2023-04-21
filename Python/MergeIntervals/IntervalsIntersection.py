class Innoskrit:
    def intervalIntersection(self, arr1, arr2):
        
        i, j = 0, 0
        ans = []
        
        while i < len(arr1) and j < len(arr2):
            
            intersection = []
            intersection.append(max(arr1[i][0], arr2[j][0]))
            intersection.append(min(arr1[i][1], arr2[j][1]))
            
            if(intersection[0] <= intersection[1]):
                ans.append(intersection)
                
            if(arr1[i][1] < arr2[j][1]):
                i += 1
            else:
                j += 1
                
        return ans

if __name__ == "__main__":
    arr1 = [[1, 3], [5, 6], [7, 9]]
    arr2 = [[2, 3], [5, 7]]
    for interval in Innoskrit().intervalIntersection(arr1, arr2):
        print(interval, end = " ")
    print()