# # #
# # x=input("enter x value:")
# # y=input("enter y value:")
# # if x>y:
# #     print("x is greater than y")
# # elif x<y:
# #     print("x is less than y")
# # else:
# #     print("x is equal to y")


# age=int(input("enetr your age:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# a=int(input("enter a value:"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

def main():
    a=int(input("enter a value:"))
    if is_even(a):
        print("even number")
    else:
        print("odd number")
    
def is_even(n):
    if n%2==0:
        return True
    else: 
        return False
main()



    


    