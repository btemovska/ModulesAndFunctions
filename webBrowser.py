import webbrowser

webbrowser.open("https://www.python.org/") #it opens up google browser

help(webbrowser)

for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='; ')
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9
# 1; 2; 3; 4; 5; 6; 7; 8; 9

chrome = webbrowser.get(using='windows-default')
chrome.open_new("https://www.python.org/")
