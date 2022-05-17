# Get Subscription
# Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X
#
# minutes.
#
# The meeting platform supports a meeting of maximum 30
#
# minutes without subscription and a meeting of unlimited duration with subscription.
#
# Determine whether Chef needs to take a subscription or not for setting up the meet.
# Input Format
#
#     First line will contain T
#
# , the number of test cases. Then the test cases follow.
# Each test case contains a single integer X
#
#     - denoting the duration of the lecture.
#
# Output Format
#
# For each test case, print in a single line, YES if Chef needs to take the subscription, otherwise print NO.
#
# You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
# Constraints
#
#     1≤T≤100
#
# 1≤X≤100
#
# Sample Input 1
#
# 4
# 50
# 3
# 30
# 80
#
# Sample Output 1
#
# YES
# NO
# NO
# YES

#CODE FOR PROBLEM:

# t = int(input("Enter the number of test case:"))
# for i in range(t) :
#
#     x = input("Enter the time in mins:")
#     if int(x)>30:
#         print("YES")
#     else:
#         print("NO")



# a = int(input("Enter the number:"))
# for i in range(21):
#     if i % 2==0:
#         a = a+i
#         print(a)



# count the vowels in the given string

# s = str(input("Enter the string:"))
# l = ["a","e","i","o","u","A","E","I","O","U"]
# for i in s:
#     for v,x in enumerate(l):
#         if i==x:
#             print(i,i.count(i))
#
