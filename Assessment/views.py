from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        request.session['title'] = request.POST.get('title')
        request.session['author'] = request.POST.get('author')
        request.session['role'] = request.POST.get('role')
        request.session['department'] = request.POST.get('department')
        request.session['manager'] = request.POST.get('manager')
        request.session['status'] = request.POST.get('status')
        request.session['date'] = request.POST.get('date')
        title = request.session.get('title')
        author = request.session.get('author')
        role = request.session.get('role')
        department = request.session.get('department')
        manager = request.session.get('manager')
        status = request.session.get('status')
        date = request.session.get('date')

        input_data = {
            'title': title,
            'author': author,
            'department': department,
            'role': role,
            'manager': manager,
            'status': status,
            'date': date,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'screening.html', context)
    return render(request, 'index.html')


@login_required
def temp(request):
    return render(request, 'temp.html')


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
        if input_data.get('select_data_process') == '4':
            dpia_status = 'Recommended'
        elif input_data.get('select_data_process') != '4' and input_data.get('conducted_DPIA_for_similar_scope_of_service') == '0':
            dpia_status = 'Recommended'
        elif input_data.get('select_data_process') != '4' and \
                input_data.get('conducted_DPIA_for_similar_scope_of_service') == '1' or input_data.get('data_processing_project') == '0':
            dpia_status = 'Mandatory'
        else:
            dpia_status = 'Not Mandatory'
    else:
        dpia_status = 'Not Required'
    return dpia_status


def screening(request):
    if request.method == 'POST':
        name_of_organization = request.POST["name_of_organization"]
        industry = request.POST["industry"]
        scope_of_service_project = request.POST["scope_of_service_project"]
        data_protection_officer = request.POST["data_protection_officer"]
        name_of_DPO = request.POST["name_of_DPO"]

        input_data = {
            'name_of_organization': name_of_organization,
            'industry': industry,
            'scope_of_service_project': scope_of_service_project,
            'data_protection_officer': data_protection_officer,
            'name_of_DPO': name_of_DPO,
        }
        context = {
            'input_data': input_data,
            'dpia_status': dpia_status(input_data),
        }
        return render(request, 'screening1.html', context)
    return render(request, 'screening.html')


def screening1(request):
    if request.method == 'POST':
        request.session['name_of_organization'] = request.POST.get("name_of_organization")
        request.session['industry'] = request.POST.get("industry")
        request.session['scope_of_service_project'] = request.POST.get("scope_of_service_project")
        request.session['data_protection_officer'] = request.POST.get("data_protection_officer")
        request.session['name_of_DPO'] = request.POST.get("name_of_DPO")
        request.session['data_processing_project'] = request.POST.get("data_processing_project")
        request.session['select_data_process'] = request.POST.get("select_data_process")
        request.session['processing_data'] = request.POST.get("processing_data")
        request.session['data_processing_involve'] = request.POST.get("data_processing_involve")
        request.session['automated_decision_making'] = request.POST.get("automated_decision_making")
        request.session['systematic_monitoring'] = request.POST.get("systematic_monitoring")
        request.session['process_data_on_large_scale'] = request.POST.get("process_data_on_large_scale")
        request.session['data_processing_involve_reusing_old_dataset'] = request.POST.get("data_processing_involve_reusing_old_dataset")
        request.session['vulnerable_data_subjects'] = request.POST.get("vulnerable_data_subjects")
        request.session['data_processing_involve_innovative_technologies'] = request.POST.get("data_processing_involve_innovative_technologies")
        request.session['data_processing_involve_sharing_data_outside_european_union'] = request.POST.get("data_processing_involve_sharing_data_outside_european_union")
        request.session['data_processing_involve_collection_personal_information'] = request.POST.get("data_processing_involve_collection_personal_information")
        request.session['data_processing_involve_third_party'] = request.POST.get("data_processing_involve_third_party")
        request.session['data_processing_involve_change_information_is_stored_secured'] = request.POST.get("data_processing_involve_change_information_is_stored_secured")
        request.session['data_processing_involve_change_personal_data_is_currently_collected'] = request.POST.get("data_processing_involve_change_personal_data_is_currently_collected")
        request.session['conducted_DPIA_for_similar_scope_of_service'] = request.POST.get("conducted_DPIA_for_similar_scope_of_service")

        name_of_organization = request.session['name_of_organization']
        industry = request.session['industry']
        scope_of_service_project = request.session['scope_of_service_project']
        data_protection_officer = request.session['data_protection_officer']
        name_of_DPO = request.session['name_of_DPO']
        data_processing_project = request.session['data_processing_project']
        select_data_process = request.session['select_data_process']
        processing_data = request.session['processing_data']
        data_processing_involve = request.session['data_processing_involve']
        automated_decision_making = request.session['automated_decision_making']
        systematic_monitoring = request.session['systematic_monitoring']
        process_data_on_large_scale = request.session['process_data_on_large_scale']
        data_processing_involve_reusing_old_dataset = request.session['data_processing_involve_reusing_old_dataset']
        vulnerable_data_subjects = request.session['vulnerable_data_subjects']
        data_processing_involve_innovative_technologies = request.session['data_processing_involve_innovative_technologies']
        data_processing_involve_sharing_data_outside_european_union = request.session['data_processing_involve_sharing_data_outside_european_union']
        data_processing_involve_collection_personal_information = request.session['data_processing_involve_collection_personal_information']
        data_processing_involve_third_party = request.session['data_processing_involve_third_party']
        data_processing_involve_change_information_is_stored_secured = request.session['data_processing_involve_change_information_is_stored_secured']
        data_processing_involve_change_personal_data_is_currently_collected = request.session['data_processing_involve_change_personal_data_is_currently_collected']
        conducted_DPIA_for_similar_scope_of_service = request.session['conducted_DPIA_for_similar_scope_of_service']

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


class RiskCalculations:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.risk_score = 0
        self.number_of_risks = 0
        self.request = request

    # Risk Summary Form 1
    def risk_calculation_f1_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f1_1') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f1_1') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f1_1') == '3':
            risk_score += 1
        if self.input_data.get('f1_1') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f1_1'] = self.input_data.get('f1_1')
        self.request.session['risk_score_f1_1'] = total_risk[0]
        self.request.session['number_of_risks_f1_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f1_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f1_2') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f1_2') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f1_2') == '3':
            risk_score += 1
        if self.input_data.get('f1_2') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f1_2'] = self.input_data.get('f1_2')
        self.request.session['risk_score_f1_2'] = total_risk[0]
        self.request.session['number_of_risks_f1_2'] = total_risk[1]
        return total_risk

    def risk_calculation_f1_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f1_3') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f1_3') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f1_3') == '3':
            risk_score += 1
        if self.input_data.get('f1_3') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f1_3'] = self.input_data.get('f1_3')
        self.request.session['risk_score_f1_3'] = total_risk[0]
        self.request.session['number_of_risks_f1_3'] = total_risk[1]
        return total_risk

    def risk_calculation_f1_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f1_4') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f1_4') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f1_4') == '3':
            risk_score += 1
        if self.input_data.get('f1_4') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f1_4'] = self.input_data.get('f1_4')
        self.request.session['risk_score_f1_4'] = total_risk[0]
        self.request.session['number_of_risks_f1_4'] = total_risk[1]
        return total_risk

    def risk_calculation_f1_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f1_5') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f1_5') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f1_5') == '3':
            risk_score += 1
        if self.input_data.get('f1_5') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f1_5'] = self.input_data.get('f1_5')
        self.request.session['risk_score_f1_5'] = total_risk[0]
        self.request.session['number_of_risks_f1_5'] = total_risk[1]
        return total_risk

    def risk_calculation_f1_6(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f1_6') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f1_6') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f1_6') == '3':
            risk_score += 1
        if self.input_data.get('f1_6') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f1_6'] = self.input_data.get('f1_6')
        self.request.session['risk_score_f1_6'] = total_risk[0]
        self.request.session['number_of_risks_f1_6'] = total_risk[1]
        return total_risk

    def risk_calculation_f1_all(self):
        f1_1 = self.risk_calculation_f1_1()
        f1_2 = self.risk_calculation_f1_2()
        f1_3 = self.risk_calculation_f1_3()
        f1_4 = self.risk_calculation_f1_4()
        f1_5 = self.risk_calculation_f1_5()
        f1_6 = self.risk_calculation_f1_6()
        risk_score = f1_1[0] + f1_2[0] + f1_3[0] + f1_4[0] + f1_5[0] + f1_6[0]
        number_of_risks = f1_1[1] + f1_2[1] + f1_3[1] + f1_4[1] + f1_5[1] + f1_6[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 2
    def risk_calculation_f2_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_1') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f2_1') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f2_1') == '3':
            risk_score += 1
        if self.input_data.get('f2_1') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_2') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f2_2') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f2_2') == '3':
            risk_score += 1
        if self.input_data.get('f2_2') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_2'] = self.input_data.get('f2_2')
        self.request.session['risk_score_f2_2'] = total_risk[0]
        self.request.session['number_of_risks_f2_2'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_3') == '0':
            risk_score += 0
            number_of_risks += 0
        elif self.input_data.get('f2_3') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_3'] = self.input_data.get('f2_3')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_4') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f2_4') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f2_4') == '3':
            risk_score += 1
        if self.input_data.get('f2_4') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_5') == '0':
            risk_score += 0
            number_of_risks += 0
        elif self.input_data.get('f2_5') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_6(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_6') == '1':
            number_of_risks += 0
        elif self.input_data.get('f2_6') == '2':
            risk_score += 1
            number_of_risks += 1
        elif self.input_data.get('f2_6') == '3':
            risk_score += 2
            number_of_risks += 1
        if self.input_data.get('f2_6') == '4':
            risk_score += 3
            number_of_risks += 1
        if self.input_data.get('f2_6') == '5':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_7(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_7') == '1':
            number_of_risks += 1
        elif self.input_data.get('f2_7') == '2':
            number_of_risks += 1
        elif self.input_data.get('f2_7') == '3':
            number_of_risks += 1
        elif self.input_data.get('f2_7') == '4':
            number_of_risks += 1
        if self.input_data.get('f2_7') == '5':
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_8(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_8') == '0':
            risk_score += 0
            number_of_risks += 0
        elif self.input_data.get('f2_8') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_9(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f2_9') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f2_9') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f2_9') == '3':
            risk_score += 1
        if self.input_data.get('f2_9') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        self.request.session['f2_1'] = self.input_data.get('f2_1')
        self.request.session['risk_score_f2_1'] = total_risk[0]
        self.request.session['number_of_risks_f2_1'] = total_risk[1]
        return total_risk

    def risk_calculation_f2_all(self):
        f2_1 = self.risk_calculation_f2_1()
        f2_2 = self.risk_calculation_f2_2()
        f2_3 = self.risk_calculation_f2_3()
        f2_4 = self.risk_calculation_f2_4()
        f2_5 = self.risk_calculation_f2_5()
        f2_6 = self.risk_calculation_f2_6()
        f2_7 = self.risk_calculation_f2_7()
        f2_8 = self.risk_calculation_f2_8()
        f2_9 = self.risk_calculation_f2_9()
        risk_score = f2_1[0] + f2_2[0] + f2_3[0] + f2_4[0] + f2_5[0] + f2_6[0] + f2_7[0] + f2_8[0] + f2_9[0]
        number_of_risks = f2_1[1] + f2_2[1] + f2_3[1] + f2_4[1] + f2_5[1] + f2_6[1] + f2_7[1] + f2_8[1] + f2_9[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 3
    def risk_calculation_f3_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_1') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_1') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_1') == '3':
            risk_score += 1
        if self.input_data.get('f3_1') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_2') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_2') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_2') == '3':
            risk_score += 1
        if self.input_data.get('f3_2') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_3') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_3') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_3') == '3':
            risk_score += 1
        if self.input_data.get('f3_3') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_4') == '0':
            risk_score += 0
        elif self.input_data.get('f3_4') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_5') == '0':
            risk_score += 0
        elif self.input_data.get('f3_5') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_6(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_6') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_6') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_6') == '3':
            risk_score += 1
        if self.input_data.get('f3_6') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_7(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_7') == '0':
            risk_score += 0
        elif self.input_data.get('f3_7') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_8(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_8') == '0':
            risk_score += 0
        elif self.input_data.get('f3_8') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_all(self):
        f3_1 = self.risk_calculation_f3_1()
        f3_2 = self.risk_calculation_f3_2()
        f3_3 = self.risk_calculation_f3_3()
        f3_4 = self.risk_calculation_f3_4()
        f3_5 = self.risk_calculation_f3_5()
        f3_6 = self.risk_calculation_f3_6()
        f3_7 = self.risk_calculation_f3_7()
        f3_8 = self.risk_calculation_f3_8()
        risk_score = f3_1[0] + f3_2[0] + f3_3[0] + f3_4[0] + f3_5[0] + f3_6[0] + f3_7[0] + f3_8[0]
        number_of_risks = f3_1[1] + f3_2[1] + f3_3[1] + f3_4[1] + f3_5[1] + f3_6[1] + f3_7[1] + f3_8[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 4
    def risk_calculation_f4_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_1') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_1') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_1') == '3':
            risk_score += 1
        if self.input_data.get('f4_1') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_2') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_2') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_2') == '3':
            risk_score += 1
        if self.input_data.get('f4_2') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_3') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_3') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_3') == '3':
            risk_score += 1
        if self.input_data.get('f4_3') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_4') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_4') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_4') == '3':
            risk_score += 1
        if self.input_data.get('f4_4') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_5') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_5') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_5') == '3':
            risk_score += 1
        if self.input_data.get('f4_5') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_6(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_6') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_6') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_6') == '3':
            risk_score += 1
        if self.input_data.get('f4_6') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_7(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_7') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_7') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_7') == '3':
            risk_score += 1
        if self.input_data.get('f4_7') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_8(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_8') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_8') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_8') == '3':
            risk_score += 1
        if self.input_data.get('f4_8') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_9(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_9') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_9') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_9') == '3':
            risk_score += 1
        if self.input_data.get('f4_9') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_all(self):
        f4_1 = self.risk_calculation_f4_1()
        f4_2 = self.risk_calculation_f4_2()
        f4_3 = self.risk_calculation_f4_3()
        f4_4 = self.risk_calculation_f4_4()
        f4_5 = self.risk_calculation_f4_5()
        f4_6 = self.risk_calculation_f4_6()
        f4_7 = self.risk_calculation_f4_7()
        f4_8 = self.risk_calculation_f4_8()
        f4_9 = self.risk_calculation_f4_9()
        risk_score = f4_1[0] + f4_2[0] + f4_3[0] + f4_4[0] + f4_5[0] + f4_6[0] + f4_7[0] + f4_8[0] + f4_9[0]
        number_of_risks = f4_1[1] + f4_2[1] + f4_3[1] + f4_4[1] + f4_5[1] + f4_6[1] + f4_7[1] + f4_8[1] + f4_9[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 5
    def risk_calculation_f5_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f5_1') == '0':
            risk_score = 0
            number_of_risks = 0
        else:
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f5_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f5_2') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f5_2') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f5_2') == '3':
            risk_score += 1
        if self.input_data.get('f5_2') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f5_all(self):
        f5_1 = self.risk_calculation_f5_1()
        f5_2 = self.risk_calculation_f5_2()
        risk_score = f5_1[0] + f5_2[0]
        number_of_risks = f5_1[1] + f5_2[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 6
    def risk_calculation_f6_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f6_1') == '0':
            risk_score += 0
        elif self.input_data.get('f6_1') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f6_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f6_2') == '0':
            risk_score += 0
        elif self.input_data.get('f6_2') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f6_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_3') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_3') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_3') == '3':
            risk_score += 1
        if self.input_data.get('f3_3') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f6_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f6_4') == '0':
            risk_score += 0
        elif self.input_data.get('f6_4') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f6_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f6_5') == '0':
            risk_score += 0
        elif self.input_data.get('f6_5') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f6_all(self):
        f6_1 = self.risk_calculation_f6_1()
        f6_2 = self.risk_calculation_f6_2()
        f6_3 = self.risk_calculation_f6_3()
        f6_4 = self.risk_calculation_f6_4()
        f6_5 = self.risk_calculation_f6_5()
        risk_score = f6_1[0] + f6_2[0] + f6_3[0] + f6_4[0] + f6_5[0]
        number_of_risks = f6_1[1] + f6_2[1] + f6_3[1] + f6_4[1] + f6_5[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 7
    def risk_calculation_f7_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f7_1') == '0':
            risk_score = 0
            number_of_risks = 0
        else:
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f7_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f7_2') == '0':
            risk_score = 0
            number_of_risks += 1
        else:
            risk_score = 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f7_all(self):
        f7_1 = self.risk_calculation_f7_1()
        f7_2 = self.risk_calculation_f7_2()
        risk_score = f7_1[0] + f7_2[0]
        number_of_risks = f7_1[1] + f7_2[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 8
    def risk_calculation_f8_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f8_1') == '0':
            risk_score += 0

        elif self.input_data.get('f8_1') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f8_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f8_2') == '0':
            risk_score += 0
            number_of_risks += 1
        elif self.input_data.get('f8_2') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f8_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f8_3') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f8_3') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f8_3') == '3':
            risk_score += 1
        if self.input_data.get('f8_3') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f8_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f8_4') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f8_4') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f8_4') == '3':
            risk_score += 1
        if self.input_data.get('f8_4') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f8_all(self):
        f8_1 = self.risk_calculation_f8_1()
        f8_2 = self.risk_calculation_f8_2()
        f8_3 = self.risk_calculation_f8_3()
        f8_4 = self.risk_calculation_f8_4()
        risk_score = f8_1[0] + f8_2[0] + f8_3[0] + f8_4[0]
        number_of_risks = f8_1[1] + f8_2[1] + f8_3[1] + f8_4[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk


def dpia_screening(request):
    if request.method == 'POST':
        f1_1 = request.POST.get("f1_1")
        f1_2 = request.POST.get("f1_2")
        f1_3 = request.POST.get("f1_3")
        f1_4 = request.POST.get("f1_4")
        f1_5 = request.POST.get("f1_5")
        f1_6 = request.POST.get("f1_6")

        f2_1 = request.POST.get("f2_1")
        f2_2 = request.POST.get("f2_2")
        f2_3 = request.POST.get("f2_3")
        f2_4 = request.POST.get("f2_4")
        f2_5 = request.POST.get("f2_5")
        f2_6 = request.POST.get("f2_6")
        f2_7 = request.POST.get("f2_7")
        f2_8 = request.POST.get("f2_8")
        f2_9 = request.POST.get("f2_9")

        f3_1 = request.POST.get("f3_1")
        f3_2 = request.POST.get("f3_2")
        f3_3 = request.POST.get("f3_3")
        f3_4 = request.POST.get("f3_4")
        f3_5 = request.POST.get("f3_5")
        f3_6 = request.POST.get("f3_6")
        f3_7 = request.POST.get("f3_7")
        f3_8 = request.POST.get("f3_8")

        f4_1 = request.POST.get("f4_1")
        f4_2 = request.POST.get("f4_2")
        f4_3 = request.POST.get("f4_3")
        f4_4 = request.POST.get("f4_4")
        f4_5 = request.POST.get("f4_5")
        f4_6 = request.POST.get("f4_6")
        f4_7 = request.POST.get("f4_7")
        f4_8 = request.POST.get("f4_8")
        f4_9 = request.POST.get("f4_9")

        f5_1 = request.POST.get("f5_1")
        f5_2 = request.POST.get("f5_2")

        f6_1 = request.POST.get("f6_1")
        f6_2 = request.POST.get("f6_2")
        f6_3 = request.POST.get("f6_3")
        f6_4 = request.POST.get("f6_4")
        f6_5 = request.POST.get("f6_5")

        f7_1 = request.POST.get("f7_1")
        f7_2 = request.POST.get("f7_2")
        f7_3 = '0'
        f7_4 = '0'
        f7_5 = '0'
        f7_6 = '0'

        f8_1 = request.POST.get("f8_1")
        f8_2 = request.POST.get("f8_2")
        f8_3 = request.POST.get("f8_3")
        f8_4 = request.POST.get("f8_4")

        input_data = {
            'f1_1': f1_1,
            'f1_2': f1_2,
            'f1_3': f1_3,
            'f1_4': f1_4,
            'f1_5': f1_5,
            'f1_6': f1_6,

            'f2_1': f2_1,
            'f2_2': f2_2,
            'f2_3': f2_3,
            'f2_4': f2_4,
            'f2_5': f2_5,
            'f2_6': f2_6,
            'f2_7': f2_7,
            'f2_8': f2_8,
            'f2_9': f2_9,

            'f3_1': f3_1,
            'f3_2': f3_2,
            'f3_3': f3_3,
            'f3_4': f3_4,
            'f3_5': f3_5,
            'f3_6': f3_6,
            'f3_7': f3_7,
            'f3_8': f3_8,

            'f4_1': f4_1,
            'f4_2': f4_2,
            'f4_3': f4_3,
            'f4_4': f4_4,
            'f4_5': f4_5,
            'f4_6': f4_6,
            'f4_7': f4_7,
            'f4_8': f4_8,
            'f4_9': f4_9,

            'f5_1': f5_1,
            'f5_2': f5_2,

            'f6_1': f6_1,
            'f6_2': f6_2,
            'f6_3': f6_3,
            'f6_4': f6_4,
            'f6_5': f6_5,

            'f7_1': f7_1,
            'f7_2': f7_2,
            'f7_3': f7_3,
            'f7_4': f7_4,
            'f7_5': f7_5,
            'f7_6': f7_6,

            'f8_1': f8_1,
            'f8_2': f8_2,
            'f8_3': f8_3,
            'f8_4': f8_4,
        }

        table = RiskCalculations(input_data, request)
        context = {
            'input_data': input_data,
            'risk_score1': table.risk_calculation_f1_all(),
            'risk_score2': table.risk_calculation_f2_all(),
            'risk_score3': table.risk_calculation_f3_all(),
            'risk_score4': table.risk_calculation_f4_all(),
            'risk_score5': table.risk_calculation_f5_all(),
            'risk_score6': table.risk_calculation_f6_all(),
            'risk_score7': table.risk_calculation_f7_all(),
            'risk_score8': table.risk_calculation_f8_all(),
            'total_no_of_risk': table.risk_calculation_f1_all()[1] + table.risk_calculation_f2_all()[1]
                                + table.risk_calculation_f3_all()[1] + table.risk_calculation_f4_all()[1]
                                + table.risk_calculation_f5_all()[1] + table.risk_calculation_f6_all()[1]
                                + table.risk_calculation_f7_all()[1] + table.risk_calculation_f8_all()[1]
        }
        return render(request, 'risk_summary.html', context)
    else:
        return render(request, 'dpia_screening.html')
