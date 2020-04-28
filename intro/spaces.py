#Adding white spaces with tabs and new line

print("Language: \nPython\nC\nJavaScript\tnot Java")

#\n for newline
#\t for tabs


#stripping whitespaces
#use rstrip method
favorite_language = "python "
print(favorite_language + "a") #whitespaces not stripped
print(favorite_language.rstrip() + "a") #whitespaces stripped
print(favorite_language.strip() + "a")
