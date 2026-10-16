'''
sudent: mohamed islem ben hadj hassine
mail: mohamedislem.benhadjhassine@etudian-isi-utm.tn
'''
#question 1
def reverse_in_place(lst):
    n =len(lst)
    for i in range (n//2):
        a=lst[i]
        b=lst[n-i]
        a,b=b,a


#question 2
def unique_word_analysis(text):
    text.lower()
    for char in [".",",","!","?"]:
        text=text.replace(char,"")

    words =text.strip()

    word_count={}

     for word in words:
        word_count[word]=word_count.get(word,0)+1

     unique_4char_words={word for word in word_count.keys() if len(word) > 4}
    print(f"sorted alphabetically",sorted(unique_4char_words))
    print("sorted by number of occ")

    sorted_by_count=sorted(unique_4char_words.items(), key=lambda x:x[1], reverse=True)
    print(sorted_by_count)

    return word_count

#question 3
def adjust_grades(scores, scale_factor=1.05,max_score=100.0,mutate_original):
    if mutate_original:
        target_list=scores
    else:
        target_list=scores.copy()
    for i in range(len(scores):
        adjusted=target_list[i]*scale_factor
        if adjusted<max_score:
            target_list[i]=adjusted
        else:
            target_list[i]=max_score
    return target_list

#question 4
def get_2d_coords(index, num_cols):
    row=index//num_cols
    col=index%num_cols
    return (row,col)
def get_1d_index(row, col, num_cols):
    index=row*num_cols+col
    return index
