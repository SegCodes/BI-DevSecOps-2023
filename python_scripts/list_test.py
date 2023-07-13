import itertools

def main():
    arr = [{'food': 'apple'}, {'food': 'orange'}, {'food': 'milk'}, {'food':'apple'}, 
           {'food': 'apple'}]
    duplicate_arr = []
    counter = 0
    for curr_obj, comp_obj in itertools.combinations(arr, 2):
        if curr_obj["food"] == comp_obj["food"]:
            counter += 1
        
        if counter > 2 and curr_obj["food"] not in duplicate_arr:
            duplicate_arr.append(curr_obj)
    
    print(duplicate_arr)

if __name__ == "__main__":
    main()