def get_book_text(path_to_file:str):
    with open(path_to_file,"r") as f:
        file_contents = f.read()
    return file_contents
    
def get_num_words(string):
    string = string.split()
    return "Found "+ str(len(string)) + " total words"


def get_num_chars(string):
    dict={}
    for char in string:
        char=str(char)
        char=char.lower()
        if dict.get(char)==None:
            dict[char]=1
        else:
            dict[char]+=1
    return dict

# TODO fix
def sort_count(char_count:dict):
    """Sort the counts in a dictionary"""
    char_count = char_count
    def char_value(key):
        """Get the count of each charecter in the dict_to_list to sort by count"""
        return key[1]
    
    def dict_to_list(char_count):
        """Turn dictionary into a list containing entries of ["char","num"] and exclude non-alpha charecters"""
        output=[]
        list=[]
        for key in char_count.keys():
            if not key.isalpha():
                continue

            char = char_count.get(key)
            
            list.append(key)
            list.append(char)
            output.append(list)
            list=[]
        output.sort(key=char_value,reverse=True)
        return output
    def pretty_print(sorted_list):
        """Take the sorted list from dict_to_list and return a pretty print version of it"""
        output=""
        for entry in sorted_list:
            output+=f"{entry[0]}: {entry[1]}\n"
        return output
    
    l = dict_to_list(char_count)
    return pretty_print(l)