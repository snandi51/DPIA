from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        department = request.POST.get('department')
        manager = request.POST.get('manager')
        version = request.POST.get('version')
        status = request.POST.get('status')
        date = request.POST.get('date')

        input_data = {
            'title': title,
            'author': author,
            'department': department,
            'manager': manager,
            'version': version,
            'status': status,
            'date': date,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'screening.html', context)
    return render(request, 'index.html')


@login_required
def screening(request):
    return render(request, 'screening.html')


@login_required
def temp(request):
    return render(request, 'temp.html')


@login_required
def dpia_screening(request):
    return render(request, 'dpia_screening.html')


@login_required
def risk_summary(request):
    return render(request, 'risk_summary.html')


@login_required
def heat_map(request):
    return render(request, 'heat_map.html')


@login_required
def result(request):
    return render(request, 'result.html')


def dpia_status(input_data):
    dpia_status = 'Mandatory'
    if input_data.get('data_processing_project') == '0':
        if input_data.get('select_data_process') == '4' and input_data.get('conducted_DPIA_for_similar_scope_of_service') == '0':
            dpia_status = 'Mandatory'
        else:
            dpia_status = 'Not Mandatory'
    else:
        dpia_status = 'Not Mandatory'
    return dpia_status


def screening(request):
    if request.method == 'POST':
        name_of_organization = request.POST["name_of_organization"]
        industry = request.POST["industry"]
        scope_of_service_project = request.POST["scope_of_service_project"]
        data_protection_officer = request.POST["data_protection_officer"]
        name_of_DPO = request.POST["name_of_DPO"]
        data_processing_project = request.POST["data_processing_project"]
        select_data_process = request.POST["select_data_process"]
        processing_data = request.POST["processing_data"]
        data_processing_involve = request.POST["data_processing_involve"]
        automated_decision_making = request.POST["automated_decision_making"]
        systematic_monitoring = request.POST["systematic_monitoring"]
        process_data_on_large_scale = request.POST["process_data_on_large_scale"]
        data_processing_involve_reusing_old_dataset = request.POST["data_processing_involve_reusing_old_dataset"]
        vulnerable_data_subjects = request.POST["vulnerable_data_subjects"]
        data_processing_involve_innovative_technologies = request.POST["data_processing_involve_innovative_technologies"]
        data_processing_involve_sharing_data_outside_european_union = request.POST["data_processing_involve_sharing_data_outside_european_union"]
        data_processing_involve_collection_personal_information = request.POST["data_processing_involve_collection_personal_information"]
        data_processing_involve_third_party = request.POST["data_processing_involve_third_party"]
        data_processing_involve_change_information_is_stored_secured = request.POST["data_processing_involve_change_information_is_stored_secured"]
        data_processing_involve_change_personal_data_is_currently_collected = request.POST["data_processing_involve_change_personal_data_is_currently_collected"]
        conducted_DPIA_for_similar_scope_of_service = request.POST["conducted_DPIA_for_similar_scope_of_service"]

        input_data = {
            'name_of_organization': name_of_organization,
            'industry': industry,
            'scope_of_service_project': scope_of_service_project,
            'data_protection_officer': data_protection_officer,
            'name_of_DPO': name_of_DPO,
            'data_processing_project': data_processing_project,
            'select_data_process': select_data_process,
            'processing_data': processing_data,
            'data_processing_involve': data_processing_involve,
            'automated_decision_making': automated_decision_making,
            'systematic_monitoring': systematic_monitoring,
            'process_data_on_large_scale': process_data_on_large_scale,
            'data_processing_involve_reusing_old_dataset': data_processing_involve_reusing_old_dataset,
            'vulnerable_data_subjects': vulnerable_data_subjects,
            'data_processing_involve_innovative_technologies': data_processing_involve_innovative_technologies,
            'data_processing_involve_sharing_data_outside_european_union': data_processing_involve_sharing_data_outside_european_union,
            'data_processing_involve_collection_personal_information': data_processing_involve_collection_personal_information,
            'data_processing_involve_third_party': data_processing_involve_third_party,
            'data_processing_involve_change_information_is_stored_secured': data_processing_involve_change_information_is_stored_secured,
            'data_processing_involve_change_personal_data_is_currently_collected': data_processing_involve_change_personal_data_is_currently_collected,
            'conducted_DPIA_for_similar_scope_of_service': conducted_DPIA_for_similar_scope_of_service,

        }
        context = {
            'input_data': input_data,
            'dpia_status': dpia_status(input_data),
        }
        return render(request, 'result.html', context)
    return render(request, 'screening.html')


