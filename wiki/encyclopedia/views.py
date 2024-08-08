from django.shortcuts import render , HttpResponse, redirect
import re
from . import util
import os
from random import randint
from markdown import convert_to_html

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
    'title': title,
    'entry': convert_to_html(f"entries/{title}.md")
    })

def search(request):

    title = request.GET['q'].strip()
    entrys = util.list_entries()
    if title in entrys:
        return redirect(f"/wiki/{title}")

    else:
        titles = list()
        for entry in entrys:
            if re.search(f".*{title}.*", entry):
                titles.append(entry)
    return render(request, "encyclopedia/search.html", {"entrys" : titles})

def add_entrie(request):

    if request.method == "POST":

        title = request.POST.get("title")
        markup = request.POST.get("markup")
        
        #validation

        if not title or not markup:
            return render(request, "encyclopedia/add_entrie.html", {"title":{"error":True ,"txt":title},
            "markup":{"error":True ,"txt":markup}})
        elif os.path.exists(f"entries/{title}.md"):
            return render(request, "encyclopedia/add_entrie.html", {"title":{"error":True ,"txt":title},
            "markup":{"error":False ,"txt":markup}})
        
        with open(f"entries/{title}.md","w") as file:
            '''file.writelines(f"# {title}\n")
            file.writelines("\n")'''
            file.writelines(markup)
        return redirect(f"/wiki/{title}")        
    return render(request , "encyclopedia/add_entrie.html")

def edit_entrie(request,title):
    if request.method == "POST":
        markup = request.POST.get("markup")
        #validation
        if not markup:
            return render(request, "encyclopedia/add_entrie.html",
                {"title": title , "markup": util.get_entry(title), "error":True} )
        
        with open(f"entries/{title}.md","w") as file:
            file.writelines(markup)
        return redirect(f"/wiki/{title}")
    return render(request , "encyclopedia/edit_entrie.html",
        {"title": title , "markup": util.get_entry(title)})

def rendom_entrie(request):
    entry = util.list_entries()
    return redirect(f"/wiki/{entry[randint(0,len(entry)-1)]}")
    

