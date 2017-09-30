from django.http import HttpResponse, Http404
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
        'user': request.user,
        'model': model_type,
        'id': id
    }

    if not record_dict['map'] == None:
        from TEKDB.settings import DATABASE_GEOGRAPHY
        context['default_lon'] = DATABASE_GEOGRAPHY['default_lon']
        context['default_lat'] = DATABASE_GEOGRAPHY['default_lat']
        context['default_zoom'] = DATABASE_GEOGRAPHY['default_zoom']
        context['min_zoom'] = DATABASE_GEOGRAPHY['min_zoom']
        context['max_zoom'] = DATABASE_GEOGRAPHY['max_zoom']
        context['map_extent'] = DATABASE_GEOGRAPHY['map_extent']

    return render(request, "record.html", context)

def download_media_file(request, model_type, id):
    models = get_model_by_type(model_type)
    if len(models) == 1:
        try:
            model = models[0]
            obj = model.objects.get(pk=id)
        except Exception as e:
            obj = None
    else:
        obj = None

    media = obj.media()
    if media:
        import os
        from django.utils.encoding import smart_str
        from TEKDB.settings import MEDIA_ROOT

        file_path = os.path.join(MEDIA_ROOT, media['file'])
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
                return response
        else:
            return Http404
    else:
        return Http404

def get_sorted_keys(keys):
    sorted_keys = []
    for key in ['name', 'image', 'subtitle', 'data', 'relationships', 'map', 'link', 'enteredbyname', 'enteredbydate', 'modifiedbyname', 'modifiedbydate']:
        if key in keys:
            key_idx = keys.index(key)
            keys.pop(key_idx)
            sorted_keys.append(key)
    sorted_keys = sorted_keys + keys
    return sorted_keys

def export_record_csv(record_dict, filename):
    import csv
    csv_response = HttpResponse(content_type='text/csv')
    csv_response['Content-Disposition'] = 'attachment; filename="%s.csv"' % filename
    writer = csv.writer(csv_response)
    for key in get_sorted_keys(list(record_dict.keys())):
        field = record_dict[key]
        if type(field) == list and len(field) > 0 and type(field[0]) == dict:
            for item in field:
                if 'key' in item.keys() and 'value' in item.keys() and len(item.keys()) == 2:
                    if type(item['value']) == list and len(item['value']) > 0:
                        for sub_item in item['value']:
                            if type(sub_item) == dict and 'name' in sub_item.keys():
                                writer.writerow(['%s - %s' %(key, item['key']), sub_item['name']])
                            else:
                                writer.writerow(['%s - %s' %(key, item['key']), str(sub_item)])
                    else:
                        writer.writerow(['%s - %s' % (key, item['key']), item['value']])
                else:
                    for list_key in item.keys():
                        writer.writerow(['%s - %s' %(key, list_key), item[list_key]])
        else:
            writer.writerow([key, str(field)])
    return csv_response

def export_record_xls(record_dict, filename):
    import xlsxwriter, io
    from xlsxwriter.workbook import Workbook
    output = io.BytesIO()
    workbook = Workbook(output, {'in_membory': True})
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    row = 0
    for key in get_sorted_keys(list(record_dict.keys())):
        field = record_dict[key]
        if type(field) == list and len(field) > 0 and type(field[0]) == dict:
            for item in field:
                if 'key' in item.keys() and 'value' in item.keys() and len(item.keys()) == 2:
                    if type(item['value']) == list and len(item['value']) > 0:
                        for sub_item in item['value']:
                            if type(sub_item) == dict and 'name' in sub_item.keys():
                                worksheet.write(row, 0, '%s - %s' %(key, item['key']))
                                worksheet.write(row, 1, sub_item['name'])
                                row += 1
                            else:
                                worksheet.write(row, 0, '%s - %s' %(key, item['key']))
                                worksheet.write(row, 1, str(sub_item))
                                row += 1
                    else:
                        worksheet.write(row, 0, '%s - %s' %(key, item['key']))
                        try:
                            worksheet.write(row, 1, str(item['value']))
                        except Exception:
                            pass
                        row += 1
                else:
                    for list_key in item.keys():
                        worksheet.write(row, 0, '%s - %s' %(key, list_key))
                        worksheet.write(row, 1, item[list_key])
                        row += 1
        else:
            worksheet.write(row, 0, key)
            worksheet.write(row, 1, str(field))
            row += 1
    workbook.close()
    output.seek(0)
    xls_response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    xls_response['Content-Disposition'] = "attachment; filename=\"%s.xlsx\"" % filename
    return xls_response

def export_by_model_id(request, model_type, id, format):
    models = get_model_by_type(model_type)
    if len(models) == 1:
        try:
            model = models[0]
            obj = model.objects.get(pk=id)
            record_dict = obj.get_record_dict()
        except Exception as e:
            record_dict = {'error': 'unknown error', 'code': '%s' % e}
    else:
        obj = None
        if len(models) == 0:
            error = 'No records returned for model: %s, id: %s' % (model_type, str(id))
        elif len(models) > 0:
            error = 'More than 1 records returned for model: %s, id: %s' % (model_type, str(id))
        record_dict = {'error': error}

    filename = "%s_%s_%s" % (model_type, str(id), record_dict['name'])
    if format == 'xls':
        return export_record_xls(record_dict, filename)
    else:       #CSV as default
        return export_record_csv(record_dict, filename)

def search(request):
    import json
    import TEKDB
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    from django.shortcuts import render

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

    resultlist = getResults(query_string, categories)
    paginator = Paginator(resultlist, 15)

    page = request.GET.get('page')
    try:
        page_count = paginator.page(page)
    except PageNotAnInteger:
        page_count = paginator.page(1)
    except EmptyPage:
        page_count = paginator.page(paginator.num_pages)

    context = {
        'results': json.dumps({'resultList': resultlist}),
        'show_page': page_count,
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

def getResults(keyword_string, categories):
    import TEKDB
    if keyword_string == None:
        keyword_string = ''

    resultlist = []
    for category in categories:
        query_models = get_model_by_type(category)
        for model in query_models:
            # Find all results matching keyword in this model
            model_results = model.keyword_search(keyword_string)
            for result in model_results:
                # Create JSON object to be resturned
                resultlist.append(result.get_response_format())

    return resultlist

def query(request):
    from django.http import JsonResponse
    results = {'resultList': getResults(request)}
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

    else:
        # if format_type == 'csv':
        import csv
        csv_response = HttpResponse(content_type='text/csv')
        csv_response['Content-Disposition'] = 'attachment; filename="%s.csv"' % filename
        writer = csv.DictWriter(csv_response, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
        return csv_response
