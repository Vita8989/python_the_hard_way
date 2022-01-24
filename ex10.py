tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line"
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

#\t makes a tab indent
#\t* line item with *
#\non splits the line
# \\ backslash
# \' single quote
# \" double quote
# \a ASCII Bell(Bel)
# \b ASCII backspace (BS)
#\f formfeed (FF)
#\n linefeed(LF)
#\N{name} Character named name in the unicode database
#\r carriage return(CR)
#\t horizontal tab
#\uxxxx character with 16bit hex value
#\Uxxxxxxxx char with 32bit hex value
#\v vertical tab(VT)
#\000 character with octal value 000
#\xhh char with hex value HH
