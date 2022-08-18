from django.shortcuts import render
import pandas as pd

def index(request):
    file = 1
    return render(request, 'form.html',{'name':file})

def excel(request):
    file = request.FILES.get("excel_file")
    df = pd.read_excel(file)
    x=0
    for c in df['one']:

        if df['math'][x]=='plus':
            df['answer'][x] = c + df['two'][x]
        elif df['math'][x]=='minus':
            df['answer'][x] = c - df['two'][x]
        elif df['math'][x]=='bibided':
            df['answer'][x] = c / df['two'][x]
        x+=1

    dx = pd.DataFrame(df)
    mydict = {
        "df": dx.to_html()
    }
    return render(request, 'form.html',context=mydict)