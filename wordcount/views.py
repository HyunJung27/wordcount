from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary= {}

    #<단어: 몇 번, 단어: 몇 번....>
    for wd in words:
        if wd in word_dictionary:
            #increase
            word_dictionary[wd] += 1

        else:
            #add to dictionary
            word_dictionary[wd] = 1

    return render(request, 'result.html', {'full': text, 'total':len(words), 'dictionary' : word_dictionary.items()})
    #.items() #word_dictionary 라고 하는 딕셔너리에 저장된 쌍들을 보내주고 싶다. 자습!!!
