
#BLACKJACK: Given three integers between 1 and 11, 
#if their sum is less than or equal to 21, return their sum. 
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def blackjack(a,b,c):

    sum_list = a+b+c
    int_list = [a,b,c]


    for any num in int_list:
        if x == 21 and sum_list > 21:
            total_sum = sum_list - 10
            return total_sum
        elif total_sum > 21:
            return 'BUST'
        else:
            sum_list <= 21:
            return sum_list





print(blackjack(9,9,9))