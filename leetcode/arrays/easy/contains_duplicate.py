# 217. Contains Duplicate
def containsDuplicate(nums) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == '__main__':
        # 217
        test_case_1 = [1,2,3,1]
        test_case_2 = [1,2,3,4]
        test_case_3 = [1,1,1,3,3,4,3,2,4,2]
        print(containsDuplicate(test_case_3))