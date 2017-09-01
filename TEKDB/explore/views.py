from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    try:
        page_content_obj = PageContent.objects.get(page="Welcome")
        if page_content_obj.is_html:
            page_content = page_content_obj.html_content
        else:
            page_content = page_content_obj.content
    except Exception as e:
        page_content = "<h1>Welcome</h1><h3>Set Welcome Page Content In Admin</h3>"

    context = {
        'page':'home',
        'pageTitle':'Welcome',
        'pageContent':page_content,
        'user': request.user
    }
    return render(request, "welcome.html", context)

def about(request):
    try:
        page_content_obj = PageContent.objects.get(page="About")
        if page_content_obj.is_html:
            page_content = page_content_obj.html_content
        else:
            page_content = page_content_obj.content
    except Exception as e:
        page_content = "<h1>About</h1><h3>Set About Page Content In Admin</h3>"
    context = {
        'page':'about',
        'pageTitle':False,
        'pageContent':page_content,
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def help(request):
    try:
        page_content_obj = PageContent.objects.get(page="Help")
        if page_content_obj.is_html:
            page_content = page_content_obj.html_content
        else:
            page_content = page_content_obj.content
    except Exception as e:
        page_content = "<h1>Help</h1><h3>Set Help Page Content In Admin</h3>"
    context = {
        'page':'help',
        'pageTitle':False,
        'pageContent':page_content,
        'user': request.user
    }
    return render(request, "tek_index.html", context)

def explore(request):
    if not request.user.is_authenticated:
        return home(request)
    context = {
        'page':'explore',
        'pageTitle':'Explore',
        'pageContent':"<p>In in mi vitae nibh posuere condimentum vitae eget quam. Etiam et urna id odio fringilla aliquet id hendrerit nisl. Ut sed ex vel felis rhoncus eleifend. Ut auctor facilisis vehicula. Ut sed dui nec ipsum pellentesque tempus.</p>",
        'user': request.user
    }
    return render(request, "explore.html", context)

def get_model_by_type(model_type):
    from TEKDB import models as tekmodels
    searchable_models = {
        'resources': [tekmodels.Resources],
        'places': [tekmodels.Places],
        'locality': [tekmodels.Locality],
        'citations': [tekmodels.Citations],
        'media': [tekmodels.Media],
        'activities': [tekmodels.ResourcesActivityEvents],
        'relationships': [
            tekmodels.LocalityPlaceResourceEvent,
            tekmodels.MediaCitationEvents,
            tekmodels.PlacesCitationEvents,
            tekmodels.PlacesMediaEvents,
            tekmodels.PlacesResourceCitationEvents,
            tekmodels.PlacesResourceEvents,
            tekmodels.PlacesResourceMediaEvents,
            tekmodels.ResourceActivityCitationEvents,
            tekmodels.ResourceActivityMediaEvents,
            tekmodels.ResourceResourceEvents,
            # tekmodels.ResourcesActivityEvents,
            tekmodels.ResourcesCitationEvents,
            tekmodels.ResourcesMediaEvents,
        ],
        'localityplaceresourceevents': [tekmodels.LocalityPlaceResourceEvent],
        'mediacitationevents': [tekmodels.MediaCitationEvents],
        'placescitationevents': [tekmodels.PlacesCitationEvents],
        'placesmediaevents': [tekmodels.PlacesMediaEvents],
        'placesresourcecitationevents': [tekmodels.PlacesResourceCitationEvents],
        'placesresourceevents': [tekmodels.PlacesResourceEvents],
        'placesresourcemediaevents': [tekmodels.PlacesResourceMediaEvents],
        'resourceactivitycitationevents': [tekmodels.ResourceActivityCitationEvents],
        'resourceactivitymediaevents': [tekmodels.ResourceActivityMediaEvents],
        'resourceresourceevents': [tekmodels.ResourceResourceEvents],
        'resourcesactivityevents': [tekmodels.ResourcesActivityEvents],
        'resourcescitationevents': [tekmodels.ResourcesCitationEvents],
        'resourcesmediaevents': [tekmodels.ResourcesMediaEvents],
        'people': [tekmodels.People],
    }

    if model_type.lower() in searchable_models.keys():
        return searchable_models[model_type.lower()]
    elif model_type.lower() == 'all':
        return sum([searchable_models[key] for key in ['resources','places', 'citations', 'media', 'activities']],[])
    else:
        return []

def get_by_model_type(request, model_type):
    context = {
        'query': '',
        'category': model_type,
        'page':'Results',
        'pageTitle':'Results',
        'pageContent':"<p>Your search results:</p>",
        'user': request.user
    }
    return render(request, "results.html", context)

def get_by_model_id(request, model_type, id):
    models = get_model_by_type(model_type)
    if len(models) == 1:
        try:
            model = models[0]
            obj = model.objects.get(pk=id)
            record_dict = obj.get_record_dict()
        except Exception as e:
            obj = None
            record_dict = {}
    else:
        obj = None
        record_dict = {}


    context = {
        'page':'Record',
        'pageTitle':'Record',
        'pageContent':"<p>Your record:</p>",
        'record': record_dict,
        'user': request.user
    }
    return render(request, "record.html", context)


def search(request):
    import json
    import TEKDB
    all_categories = ['places','resources','activities','citations','media']
    if request.method == 'POST':
        query_string=request.POST['query']
        if 'category' in request.POST.keys():
            categories = [request.POST['category']]
        else:
            keys = request.POST.keys()
            categories = []
            if 'places' in keys and request.POST['places'] :
                categories.append('places')
            if 'resources' in keys and request.POST['resources']:
                categories.append('resources')
            if 'activities' in keys and request.POST['activities']:
                categories.append('activities')
            if 'citations' in keys and request.POST['citations']:
                categories.append('citations')
            if 'media' in keys and request.POST['media']:
                categories.append('media')
    else:
        if 'query' in request.GET.keys():
            query_string = request.GET.get('query')
        else:
            query_string = None
        if 'category' in request.GET.keys():
            categories = [request.GET.get('category')]
        else:
            categories = ['all']

    if categories == ['all']:
        categories = all_categories

    category_checkboxes = ''
    for category in all_categories:
        if category in categories:
            checked = ' checked=true'
        else:
            checked = ''
        category_checkboxes = '%s<input type="checkbox" name="%s" value="%s"%s>%s<br>\n' % (category_checkboxes, category, category,checked,category.capitalize())

    if query_string in [None, '', '*']:
        query_string_visible = 'No keyword search specified.'
    else:
        query_string_visible = query_string

    if query_string not in [None, '', '*']:
        query_value = ' value=%s' % query_string
    else:
        query_value = ''
    keyword_search_input = '<label for="search-text">Search Phrase</label><input type="text" class="form-control" id="search-text" name="query" placeholder="Search Phrase"%s>' % query_value

    context = {
        'query': query_string,
        'keyword': query_string_visible,
        'keyword_search_input': keyword_search_input,
        'categories': json.dumps(categories),
        'category_checkboxes': category_checkboxes,
        'page':'Results',
        'pageTitle':'Results',
        'pageContent':"<p>Your search results:</p>",
        'user': request.user
    }
    return render(request, "results.html", context)

def getResults(request):
    import TEKDB
    if 'query' in request.GET.keys():
        keyword_string = str(request.GET.get('query'))
    else:
        keyword_string = None
    if 'category' in request.GET.keys() and request.GET.get('category') in TEKDB.settings.SEARCH_CATEGORIES:
        categories = [request.GET.get('category')]
    else:
        categories = []
        if 'places' in request.GET.keys() and request.GET['places']:
            categories.append('places')
        if 'resources' in request.GET.keys() and request.GET['resources']:
            categories.append('resources')
        if 'activities' in request.GET.keys() and request.GET['activities']:
            categories.append('activities')
        if 'citations' in request.GET.keys() and request.GET['citations']:
            categories.append('citations')
        if 'media' in request.GET.keys() and request.GET['media']:
            categories.append('media')
    #TODO: need to handle #results/page, page#

    resultlist = []
    #TODO: Loop through list of categories
    for category in categories:
        query_models = get_model_by_type(category)
        for model in query_models:
            # Find all results matching keyword in this model
            model_results = model.keyword_search(keyword_string)
            for result in model_results:
                # Create JSON object to be resturned
                resultlist.append(result.get_response_format())

    results = {
        'resultList' : resultlist
    }
    return results

def query(request):
    from django.http import JsonResponse
    print(request)
    results = getResults(request)
    return JsonResponse(results)

def download(request):
    results = getResults(request)
    format_type = request.GET.get('format')
    filename = 'TEK_RESULTS'
    fieldnames = ['id','name','description','type']
    rows = []
    for row in results['resultList']:
        row_dict = {}
        for field in fieldnames:
            row_dict[field] = row[field] if row[field] else ' '
        rows.append(row_dict)

    if format_type == 'xlsx':
        import xlsxwriter, io
        from xlsxwriter.workbook import Workbook
        output = io.BytesIO()
        workbook = Workbook(output, {'in_membory': True})
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        rows.insert(0, fieldnames)
        row = 0
        col = 0
        for entry in rows:
            for field in fieldnames:
                if row == 0:
                    worksheet.write(0, col, field, bold)
                else:
                    worksheet.write(row, col, entry[field])
                col += 1
            row += 1
            col = 0
        workbook.close()
        output.seek(0)
        xls_response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        xls_response['Content-Disposition'] = "attachment; filename=%s.xlsx" % filename

        return xls_response
    if format_type == 'csv':
        import csv
        csv_response = HttpResponse(content_type='text/csv')
        csv_response['Content-Disposition'] = 'attachment; filename="%s.csv"' % filename
        writer = csv.DictWriter(csv_response, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
        return csv_response
