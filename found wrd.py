def countWords(s):
  
    # Check if the string is null
    # or empty then return zero
    if s.strip() == "":
        return 0
  
    # Splitting the string
  
    words = s.split()
  
    return len(words)
  
  
if __name__ == "__main__":
    s = "One two       three\n four\tfive "
    print("No of words : ", countWords(s))
