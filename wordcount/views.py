import operator

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html", {"hi_there": "this is me"})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = dict()
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedwords = sorted(worddict.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
    return render(request, "count.html", {
                                          "fulltext": fulltext,
                                          "fulltext_count": len(fulltext),
                                          "wordlist_count": len(wordlist),
                                          "worddict": worddict,
                                          "worddict_list": worddict.items(),
                                          "sortedwords": sortedwords
                                          })


def about(request):
    return render(request, "about.html", {"me": "Django Rookie"})
