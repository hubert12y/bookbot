def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents),"words found in the document")
        dict = count_characters(file_contents)
        dict_list = []
        for key, value in dict.items():
            dict_list.append({"letter":key, "num":value})
        dict_list.sort(reverse=True, key=sort_on)
        for val in dict_list:
            if val["letter"].isalpha():
                print ("The '",val["letter"],"' character was found",val["num"],"times") 
            
        
            # val["letter"] = lettre
            # val["num"] = nombre de fois
        

def count_words(text):
    return len(text.split())

def count_characters(text):
    lowered_text = text.lower()

    dictionnaire = {}

    for letter in lowered_text:
        if not letter in dictionnaire:
            dictionnaire[letter] = 0
        dictionnaire[letter] += 1

    return dictionnaire

def sort_on(dict):
    return dict["num"]
    

main()


# [afafdsafds, fdsfdsfdsf, ddsfdsf]
       