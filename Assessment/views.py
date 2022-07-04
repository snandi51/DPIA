from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from fpdf import FPDF
from Assessment.models import Master
import json
import os


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
        username = request.session.get('username')
        session_dict = get_session_data()
        count = 1
        context = {}
        session_data = False
        for i in session_dict:
            if (title == session_dict.get('session_dict_{}'.format(count)).get('title')) and (
                    status == session_dict.get('session_dict_{}'.format(count)).get('status') and
                    date == session_dict.get('session_dict_{}'.format(count)).get('date')
            ):
                session_data = True
                context['value_dict'] = session_dict.get('session_dict_{}'.format(count))
            count+=1
        if not session_data:
            context['value_dict'] = 0
        context['input_data'] = input_data
        context['session_dict'] = session_dict
        return render(request, 'screening.html', context)
    session_dict = get_session_data()
    context = {
        'authorized': True,
        'session_dict': session_dict
    }
    return render(request, 'index.html', context)


def no_session(request):
    if request.method == "GET":
        context = {}
        db_dict_num = request.GET.get('search')
        if db_dict_num == '0':
            context['value_dict'] = 0
        else:
            session_dict = get_session_data()
            context['value_dict'] = session_dict.get('session_dict_{}'.format(db_dict_num))
            context['db_dict_num'] = db_dict_num
            context['session_dict'] = session_dict
            return render(request, 'index.html', context)
    return render(request, 'index.html')


def get_session_data():
    session_data = Master.objects.all()
    dict_count = 1
    session_dict = {}
    for items in session_data:
        session_dict['session_dict_{}'.format(dict_count)] = items.__dict__
        session_dict.get('session_dict_{}'.format(dict_count))['_state'] = \
            str(session_dict.get('session_dict_{}'.format(dict_count))['_state'])
        session_dict.get('session_dict_{}'.format(dict_count))['date'] = \
            session_dict.get('session_dict_{}'.format(dict_count))['date'].strftime("%Y-%m-%d")
        dict_count+=1
    return session_dict


@login_required
def temp(request):
    return render(request, 'temp.html')


@login_required
def session_screen(request):
    return render(request, 'index.html')


@login_required
def risk_summary(request):
    return render(request, 'risk_summary.html')


@login_required
def heat_map(request):
    return render(request, 'heat_map.html')


@login_required
def result(request):
    return render(request, 'result.html')


@login_required
def gdpr_report(request):
    context = {

    }
    return render(request, 'gdpr_report.html')


@login_required
def status(request):
    value = request.GET.get('search')
    context = {
        'status': value,
    }
    return render(request, 'status.html', context)


def forget_password(request):
    context = {

    }
    return render(request, 'forget_password.html', context)

@login_required
def pdf_button(request):

    value = request.GET.get('search')
    risk_score1 = request.session.get('risk_score1')
    risk_score2 = request.session.get('risk_score2')
    risk_score3 = request.session.get('risk_score3')
    risk_score4 = request.session.get('risk_score4')
    risk_score5 = request.session.get('risk_score5')
    risk_score6 = request.session.get('risk_score6')
    risk_score7 = request.session.get('risk_score7')
    risk_score8 = request.session.get('risk_score8')
    form1_percentage = request.session.get('form1_percentage')
    form2_percentage = request.session.get('form2_percentage')
    form3_percentage = request.session.get('form3_percentage')
    form4_percentage = request.session.get('form4_percentage')
    form5_percentage = request.session.get('form5_percentage')
    form6_percentage = request.session.get('form6_percentage')
    form7_percentage = request.session.get('form7_percentage')
    form8_percentage = request.session.get('form8_percentage')
    context = {
        'value': value,
        'risk_score1': risk_score1,
        'risk_score2': risk_score2,
        'risk_score3': risk_score3,
        'risk_score4': risk_score4,
        'risk_score5': risk_score5,
        'risk_score6': risk_score6,
        'risk_score7': risk_score7,
        'risk_score8': risk_score8,
        'form1_percentage': form1_percentage,
        'form2_percentage': form2_percentage,
        'form3_percentage': form3_percentage,
        'form4_percentage': form4_percentage,
        'form5_percentage': form5_percentage,
        'form6_percentage': form6_percentage,
        'form7_percentage': form7_percentage,
        'form8_percentage': form8_percentage,
        'name_of_controller': request.session.get('manager'),
        'name_of_dpo': request.session.get('name_of_DPO'),
        'title_of_dpo': request.session.get('title_of_DPO')
    }

    return render(request, 'risk_summary.html', context)


@login_required
def risk_summary_details(request):
    title = request.GET.get('search')
    risk_score1 = request.session.get('risk_score1')
    risk_score2 = request.session.get('risk_score2')
    risk_score3 = request.session.get('risk_score3')
    risk_score4 = request.session.get('risk_score4')
    risk_score5 = request.session.get('risk_score5')
    risk_score6 = request.session.get('risk_score6')
    risk_score7 = request.session.get('risk_score7')
    risk_score8 = request.session.get('risk_score8')
    form1_percentage = request.session.get('form1_percentage')
    form2_percentage = request.session.get('form2_percentage')
    form3_percentage = request.session.get('form3_percentage')
    form4_percentage = request.session.get('form4_percentage')
    form5_percentage = request.session.get('form5_percentage')
    form6_percentage = request.session.get('form6_percentage')
    form7_percentage = request.session.get('form7_percentage')
    form8_percentage = request.session.get('form8_percentage')
    context = {
        'title': title,
        'risk_score1': risk_score1,
        'risk_score2': risk_score2,
        'risk_score3': risk_score3,
        'risk_score4': risk_score4,
        'risk_score5': risk_score5,
        'risk_score6': risk_score6,
        'risk_score7': risk_score7,
        'risk_score8': risk_score8,
        'form1_percentage': form1_percentage,
        'form2_percentage': form2_percentage,
        'form3_percentage': form3_percentage,
        'form4_percentage': form4_percentage,
        'form5_percentage': form5_percentage,
        'form6_percentage': form6_percentage,
        'form7_percentage': form7_percentage,
        'form8_percentage': form8_percentage,
        'name_of_controller': request.session.get('manager'),
        'name_of_dpo': request.session.get('name_of_DPO'),
        'title_of_dpo': request.session.get('title_of_DPO')
    }
    return render(request, 'risk_summary_details.html', context)



def dpia_status(input_data):
    status = 'Mandatory'
    if input_data.get('data_processing_project') == '0':
        if input_data.get('select_data_process') == '4':
            status = 'Recommended'
        elif input_data.get('select_data_process') != '4' or \
                input_data.get('select_data_process') == '3' or \
                input_data.get('select_data_process') == '2' or \
            input_data.get('select_data_process') == '1':
            status = 'Mandatory'
        else:
            status = 'Not Required'
    else:
        status = 'Not Required'
    return status


def screening(request):
    if request.method == 'POST':
        request.session['name_of_organization'] = request.POST.get("name_of_organization")
        request.session['industry'] = request.POST.get("industry")
        request.session['scope_of_service_project'] = request.POST.get("scope_of_service_project")
        request.session['data_protection_officer'] = request.POST.get("data_protection_officer")
        request.session['name_of_DPO'] = request.POST.get("name_of_DPO")
        request.session['title_of_DPO'] = request.POST.get("title_of_DPO")

        name_of_organization = request.session['name_of_organization']
        industry = request.session['industry']
        scope_of_service_project = request.session['scope_of_service_project']
        data_protection_officer = request.session['data_protection_officer']
        name_of_DPO = request.session['name_of_DPO']
        title_of_DPO = request.session['title_of_DPO']

        input_data = {
            'name_of_organization': name_of_organization,
            'industry': industry,
            'scope_of_service_project': scope_of_service_project,
            'data_protection_officer': data_protection_officer,
            'name_of_DPO': name_of_DPO,
            'title_of_DPO': title_of_DPO,
        }
        session_dict = get_session_data()
        count = 1
        context = {}
        session_data = False
        for i in session_dict:
            if request.session['title'] == session_dict.get('session_dict_{}'.format(count)).get('title')\
                    and request.session['status'] == session_dict.get('session_dict_{}'.format(count)).get('status')\
                    and request.session['date'] == session_dict.get('session_dict_{}'.format(count)).get('date'):
                context['value_dict'] = session_dict.get('session_dict_{}'.format(count))
                session_data = True
            count += 1
        if not session_data:
            context['value_dict'] = 0
        context['input_data'] = input_data
        context['session_dict'] = session_dict
        context['dpia_status'] = dpia_status(input_data)
        return render(request, 'screening1.html', context)
    return render(request, 'screening.html')


def screening1(request):
    if request.method == 'POST':
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
        request.session['data_procc_involve_chg_personal_data_currently_collected'] = request.POST.get("data_procc_involve_chg_personal_data_currently_collected")
        request.session['conducted_DPIA_for_similar_scope_of_service'] = request.POST.get("conducted_DPIA_for_similar_scope_of_service")

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
        data_procc_involve_chg_personal_data_currently_collected = request.session['data_procc_involve_chg_personal_data_currently_collected']
        conducted_DPIA_for_similar_scope_of_service = request.session['conducted_DPIA_for_similar_scope_of_service']

        input_data = {
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
            'data_procc_involve_chg_personal_data_currently_collected': data_procc_involve_chg_personal_data_currently_collected,
            'conducted_DPIA_for_similar_scope_of_service': conducted_DPIA_for_similar_scope_of_service,

        }
        session_dict = get_session_data()
        context = {
            'input_data': input_data,
            'dpia_status': dpia_status(input_data),
            'session_dict': session_dict,
        }
        return render(request, 'result.html', context)
    return render(request, 'screening.html')


class RiskCalculations:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.risk_score = 0
        self.number_of_risks = 0
        self.request = request
        self.form1 = 6
        self.form2 = 9
        self.form3 = 12
        self.form4 = 13
        self.form5 = 5
        self.form6 = 5
        self.form7 = 2
        self.form8 = 4

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
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_2(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_2') == '0':
            risk_score += 0
        elif self.input_data.get('f3_2') == '1':
            risk_score += 3
            number_of_risks += 1
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
        if self.input_data.get('f3_4') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_4') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_4') == '3':
            risk_score += 1
        if self.input_data.get('f3_4') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_5') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_5') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_5') == '3':
            risk_score += 1
        if self.input_data.get('f3_5') == '4':
            risk_score += 0
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

    def risk_calculation_f3_9(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_9') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f3_9') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f3_9') == '3':
            risk_score += 1
        if self.input_data.get('f3_9') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_10(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_10') == '0':
            risk_score += 0
        elif self.input_data.get('f3_10') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_11(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f3_11') == '0':
            risk_score += 0
        elif self.input_data.get('f3_11') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f3_12(self):
        risk_score = 0
        number_of_risks = 0
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
        f3_9 = self.risk_calculation_f3_9()
        f3_10 = self.risk_calculation_f3_10()
        f3_11 = self.risk_calculation_f3_11()
        f3_12 = self.risk_calculation_f3_12()

        risk_score = f3_1[0] + f3_2[0] + f3_3[0] + f3_4[0] + f3_5[0] + f3_6[0] + f3_7[0] + f3_8[0] + f3_9[0] + f3_10[0] + f3_11[0] + f3_12[0]
        number_of_risks = f3_1[1] + f3_2[1] + f3_3[1] + f3_4[1] + f3_5[1] + f3_6[1] + f3_7[1] + f3_8[1] + f3_9[1] + f3_10[1] + f3_11[1] + f3_12[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 4
    def risk_calculation_f4_1(self):
        risk_score = 0
        number_of_risks = 0
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

    def risk_calculation_f4_10(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_10') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_10') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_10') == '3':
            risk_score += 1
        if self.input_data.get('f4_10') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_11(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_11') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_11') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_11') == '3':
            risk_score += 1
        if self.input_data.get('f4_11') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_12(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_12') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_12') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_12') == '3':
            risk_score += 1
        if self.input_data.get('f4_12') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f4_13(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f4_13') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f4_13') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f4_13') == '3':
            risk_score += 1
        if self.input_data.get('f4_13') == '4':
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
        f4_10 = self.risk_calculation_f4_10()
        f4_11 = self.risk_calculation_f4_11()
        f4_12 = self.risk_calculation_f4_12()
        f4_13 = self.risk_calculation_f4_13()


        risk_score = f4_1[0] + f4_2[0] + f4_3[0] + f4_4[0] + f4_5[0] + f4_6[0] + f4_7[0] + f4_8[0] + f4_9[0] + + f4_10[0] + f4_11[0] + f4_12[0] + f4_13[0]
        number_of_risks = f4_1[1] + f4_2[1] + f4_3[1] + f4_4[1] + f4_5[1] + f4_6[1] + f4_7[1] + f4_8[1] + f4_9[1] + f4_10[1] + f4_11[1] + f4_12[1] + f4_13[1]
        total_risk = [risk_score, number_of_risks]
        return total_risk

    # Risk Summary Form 5
    def risk_calculation_f5_1(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f5_1') == '0':
            risk_score = 0
            number_of_risks = 0
        elif self.input_data.get('f5_1') == '1':
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

    def risk_calculation_f5_3(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f5_3') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f5_3') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f5_3') == '3':
            risk_score += 1
        if self.input_data.get('f5_3') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f5_4(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f5_4') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f5_4') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f5_4') == '3':
            risk_score += 1
        if self.input_data.get('f5_4') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f5_5(self):
        risk_score = 0
        number_of_risks = 0
        if self.input_data.get('f5_5') == '1':
            risk_score += 3
            number_of_risks += 1
        elif self.input_data.get('f5_5') == '2':
            risk_score += 2
            number_of_risks += 1
        elif self.input_data.get('f5_5') == '3':
            risk_score += 1
        if self.input_data.get('f5_5') == '4':
            risk_score += 0
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f5_all(self):
        f5_1 = self.risk_calculation_f5_1()
        f5_2 = self.risk_calculation_f5_2()
        f5_3 = self.risk_calculation_f5_3()
        f5_4 = self.risk_calculation_f5_4()
        f5_5 = self.risk_calculation_f5_5()

        risk_score = f5_1[0] + f5_2[0] + f5_3[0] + f5_4[0] + f5_5[0]
        number_of_risks = f5_1[1] + f5_2[1] + f5_3[1] + f5_4[1] + f5_5[1]
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
        elif self.input_data.get('f7_1') == '1':
            risk_score += 3
            number_of_risks += 1
        total_risk = [risk_score, number_of_risks]
        return total_risk

    def risk_calculation_f7_2(self):
        risk_score = 0
        number_of_risks = 0
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
    if request.method == 'GET':
        session_dict = get_session_data()
        count = 1
        context = {}
        session_data = False
        for i in session_dict:
            if request.session['title'] == session_dict.get('session_dict_{}'.format(count)).get('title') \
                    and request.session['status'] == session_dict.get('session_dict_{}'.format(count)).get('status') \
                    and request.session['date'] == session_dict.get('session_dict_{}'.format(count)).get('date'):
                context['value_dict'] = session_dict.get('session_dict_{}'.format(count))
                session_data = True
            count += 1
        if not session_data:
            context['value_dict'] = 0
        context['session_dict'] = session_dict
        return render(request, 'dpia_screening.html', context)
    if request.method == 'POST':
        request.session['f1_1'] = request.POST.get("f1_1")
        request.session['f1_2'] = request.POST.get("f1_2")
        request.session['f1_3'] = request.POST.get("f1_3")
        request.session['f1_4'] = request.POST.get("f1_4")
        request.session['f1_5'] = request.POST.get("f1_5")
        request.session['f1_6'] = request.POST.get("f1_6")
        f1_1 = request.session.get('f1_1')
        f1_2 = request.session.get('f1_2')
        f1_3 = request.session.get('f1_3')
        f1_4 = request.session.get('f1_4')
        f1_5 = request.session.get('f1_5')
        f1_6 = request.session.get('f1_6')

        request.session['f2_1'] = request.POST.get("f2_1")
        request.session['f2_2'] = request.POST.get("f2_2")
        request.session['f2_3'] = request.POST.get("f2_3")
        request.session['f2_4'] = request.POST.get("f2_4")
        request.session['f2_5'] = request.POST.get("f2_5")
        request.session['f2_6'] = request.POST.get("f2_6")
        request.session['f2_7'] = request.POST.get("f2_7")
        request.session['f2_8'] = request.POST.get("f2_8")
        request.session['f2_9'] = request.POST.get("f2_9")
        f2_1 = request.session.get('f2_1')
        f2_2 = request.session.get('f2_2')
        f2_3 = request.session.get('f2_3')
        f2_4 = request.session.get('f2_4')
        f2_5 = request.session.get('f2_5')
        f2_6 = request.session.get('f2_6')
        f2_7 = request.session.get('f2_7')
        f2_8 = request.session.get('f2_8')
        f2_9 = request.session.get('f2_9')

        request.session['f3_1'] = request.POST.get("f3_1")
        request.session['f3_2'] = request.POST.get("f3_2")
        request.session['f3_3'] = request.POST.get("f3_3")
        request.session['f3_4'] = request.POST.get("f3_4")
        request.session['f3_5'] = request.POST.get("f3_5")
        request.session['f3_6'] = request.POST.get("f3_6")
        request.session['f3_7'] = request.POST.get("f3_7")
        request.session['f3_8'] = request.POST.get("f3_8")
        request.session['f3_9'] = request.POST.get("f3_9")
        request.session['f3_10'] = request.POST.get("f3_10")
        request.session['f3_11'] = request.POST.get("f3_11")
        request.session['f3_12'] = request.POST.get("f3_12")
        f3_1 = request.session.get('f3_1')
        f3_2 = request.session.get('f3_2')
        f3_3 = request.session.get('f3_3')
        f3_4 = request.session.get('f3_4')
        f3_5 = request.session.get('f3_5')
        f3_6 = request.session.get('f3_6')
        f3_7 = request.session.get('f3_7')
        f3_8 = request.session.get('f3_8')
        f3_9 = request.session.get('f3_9')
        f3_10 = request.session.get('f3_10')
        f3_11 = request.session.get('f3_11')
        f3_12 = request.session.get('f3_12')

        request.session['f4_1'] = request.POST.get("f4_1")
        request.session['f4_2'] = request.POST.get("f4_2")
        request.session['f4_3'] = request.POST.get("f4_3")
        request.session['f4_4'] = request.POST.get("f4_4")
        request.session['f4_5'] = request.POST.get("f4_5")
        request.session['f4_6'] = request.POST.get("f4_6")
        request.session['f4_7'] = request.POST.get("f4_7")
        request.session['f4_8'] = request.POST.get("f4_8")
        request.session['f4_9'] = request.POST.get("f4_9")
        request.session['f4_10'] = request.POST.get("f4_10")
        request.session['f4_11'] = request.POST.get("f4_11")
        request.session['f4_12'] = request.POST.get("f4_12")
        request.session['f4_13'] = request.POST.get("f4_13")
        f4_1 = request.session.get('f4_1')
        f4_2 = request.session.get('f4_2')
        f4_3 = request.session.get('f4_3')
        f4_4 = request.session.get('f4_4')
        f4_5 = request.session.get('f4_5')
        f4_6 = request.session.get('f4_6')
        f4_7 = request.session.get('f4_7')
        f4_8 = request.session.get('f4_8')
        f4_9 = request.session.get('f4_9')
        f4_10 = request.session.get('f4_10')
        f4_11 = request.session.get('f4_11')
        f4_12 = request.session.get('f4_12')
        f4_13 = request.session.get('f4_13')

        request.session['f5_1'] = request.POST.get("f5_1")
        request.session['f5_2'] = request.POST.get("f5_2")
        request.session['f5_3'] = request.POST.get("f5_3")
        request.session['f5_4'] = request.POST.get("f5_4")
        request.session['f5_5'] = request.POST.get("f5_5")
        f5_1 = request.session.get('f5_1')
        f5_2 = request.session.get('f5_2')
        f5_3 = request.session.get('f5_3')
        f5_4 = request.session.get('f5_4')
        f5_5 = request.session.get('f5_5')

        request.session['f6_1'] = request.POST.get("f6_1")
        request.session['f6_2'] = request.POST.get("f6_2")
        request.session['f6_3'] = request.POST.get("f6_3")
        request.session['f6_4'] = request.POST.get("f6_4")
        request.session['f6_5'] = request.POST.get("f6_5")
        f6_1 = request.session.get('f6_1')
        f6_2 = request.session.get('f6_2')
        f6_3 = request.session.get('f6_3')
        f6_4 = request.session.get('f6_4')
        f6_5 = request.session.get('f6_5')

        request.session['f7_1'] = request.POST.get("f7_1")
        request.session['f7_2'] = request.POST.get("f7_2")
        f7_1 = request.session.get('f7_1')
        f7_2 = request.session.get('f7_2')

        request.session['f8_1'] = request.POST.get("f8_1")
        request.session['f8_2'] = request.POST.get("f8_2")
        request.session['f8_3'] = request.POST.get("f8_3")
        request.session['f8_4'] = request.POST.get("f8_4")
        f8_1 = request.session.get('f8_1')
        f8_2 = request.session.get('f8_2')
        f8_3 = request.session.get('f8_3')
        f8_4 = request.session.get('f8_4')

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
            'f3_9': f3_9,
            'f3_10': f3_10,
            'f3_11': f3_11,
            'f3_12': f3_12,

            'f4_1': f4_1,
            'f4_2': f4_2,
            'f4_3': f4_3,
            'f4_4': f4_4,
            'f4_5': f4_5,
            'f4_6': f4_6,
            'f4_7': f4_7,
            'f4_8': f4_8,
            'f4_9': f4_9,
            'f4_10': f4_10,
            'f4_11': f4_11,
            'f4_12': f4_12,
            'f4_13': f4_13,

            'f5_1': f5_1,
            'f5_2': f5_2,
            'f5_3': f5_3,
            'f5_4': f5_4,
            'f5_5': f5_5,

            'f6_1': f6_1,
            'f6_2': f6_2,
            'f6_3': f6_3,
            'f6_4': f6_4,
            'f6_5': f6_5,

            'f7_1': f7_1,
            'f7_2': f7_2,

            'f8_1': f8_1,
            'f8_2': f8_2,
            'f8_3': f8_3,
            'f8_4': f8_4,
        }
        db_objects = Master.objects.all()
        db_dict_list = []
        session_title = request.session.get('title')
        session_status = request.session.get('status')
        session_date = request.session.get('date')
        for instance in db_objects:
            db_dict_list.append(instance.__dict__)
        for item in db_dict_list:
            if item['title'] == session_title and item['status'] == session_status \
                    and item['date'] == session_date or item['title'] == session_title \
                    and item['status'] == session_status or item['title'] == session_title \
                    and item['date'] == session_date:
                record = Master.objects.filter(title=session_title)
                record.delete()

        assessment_db_data = Master(username=request.session.get('username'),
                                    title=request.session.get('title'),
                        author=request.session.get('author'),
                        department=request.session.get('department'),
                        role=request.session.get('role'),
                        manager=request.session.get('manager'),
                        status=request.session.get('status'),
                                    date=request.session.get('date'),
                        name_of_organization=request.session.get('name_of_organization'),
                                    industry=request.session.get('industry'),
                        scope_of_service_project=request.session.get('scope_of_service_project'),
                        data_protection_officer=request.session.get('data_protection_officer'),
                        name_of_DPO=request.session.get('name_of_DPO'),
                                    title_of_DPO=request.session.get('title_of_DPO'),
                        data_processing_project=request.session.get('data_processing_project'),
                        select_data_process=request.session.get('select_data_process'),
                        processing_data=request.session.get('processing_data'),
                        data_processing_involve=request.session.get('data_processing_involve'),
                        automated_decision_making=request.session.get('automated_decision_making'),
                        systematic_monitoring=request.session.get('systematic_monitoring'),
                        process_data_on_large_scale=request.session.get('process_data_on_large_scale'),
                        data_processing_involve_reusing_old_dataset=request.session.get('data_processing_involve_reusing_old_dataset'),
                        vulnerable_data_subjects=request.session.get('vulnerable_data_subjects'),
                        data_processing_involve_innovative_technologies=request.session.get('data_processing_involve_innovative_technologies'),
                        data_processing_involve_sharing_data_outside_european_union=request.session.get('data_processing_involve_sharing_data_outside_european_union'),
                        data_processing_involve_collection_personal_information=request.session.get('data_processing_involve_collection_personal_information'),
                        data_processing_involve_third_party=request.session.get('data_processing_involve_third_party'),
                        data_processing_involve_change_information_is_stored_secured=request.session.get('data_processing_involve_change_information_is_stored_secured'),
                        data_procc_involve_chg_personal_data_currently_collected=request.session.get('data_procc_involve_chg_personal_data_currently_collected'),
                        conducted_DPIA_for_similar_scope_of_service=request.session.get('conducted_DPIA_for_similar_scope_of_service'),
                                    f1_1=f1_1, f1_2=f1_2, f1_3=f1_3, f1_4=f1_4, f1_5=f1_5, f1_6=f1_6,
                                    f2_1=f2_1, f2_2=f2_2, f2_3=f2_3, f2_4=f2_4, f2_5=f2_5, f2_6=f2_6, f2_7=f2_7, f2_8=f2_8, f2_9=f2_9,
                                    f3_1=f3_1, f3_2=f3_2, f3_3=f3_3, f3_4=f3_4, f3_5=f3_5, f3_6=f3_6, f3_7=f3_7, f3_8=f3_8, f3_9=f3_9, f3_10=f3_10, f3_11=f3_11, f3_12=f3_12,
                                    f4_1=f4_1, f4_2=f4_2, f4_3=f4_3, f4_4=f4_4, f4_5=f4_5, f4_6=f4_6, f4_7=f4_7, f4_8=f4_8, f4_9=f4_9, f4_10=f4_10, f4_11=f4_11, f4_12=f4_12, f4_13=f4_13,
                                    f5_1=f5_1, f5_2=f5_2, f5_3=f5_3, f5_4=f5_4, f5_5=f5_5,
                                    f6_1=f6_1, f6_2=f6_2, f6_3=f6_3, f6_4=f6_4, f6_5=f6_5,
                                    f7_1=f7_1, f7_2=f7_2,
                                    f8_1=f8_1, f8_2=f8_2, f8_3=f8_3, f8_4=f8_4
                                    )
        assessment_db_data.save()

        table = RiskCalculations(input_data, request)
        form1_percentage = round((table.risk_calculation_f1_all()[1] / table.form1) * 100, 2)
        request.session['form1_percentage'] = form1_percentage
        form2_percentage = round((table.risk_calculation_f2_all()[1] / table.form2) * 100, 2)
        request.session['form2_percentage'] = form2_percentage
        form3_percentage = round((table.risk_calculation_f3_all()[1] / table.form3) * 100, 2)
        request.session['form3_percentage'] = form3_percentage
        form4_percentage = round((table.risk_calculation_f4_all()[1] / table.form4) * 100, 2)
        request.session['form4_percentage'] = form4_percentage
        form5_percentage = round((table.risk_calculation_f5_all()[1] / table.form5) * 100, 2)
        request.session['form5_percentage'] = form5_percentage
        form6_percentage = round((table.risk_calculation_f6_all()[1] / table.form6) * 100, 2)
        request.session['form6_percentage'] = form6_percentage
        form7_percentage = round((table.risk_calculation_f7_all()[1] / table.form7) * 100, 2)
        request.session['form7_percentage'] = form7_percentage
        form8_percentage = round((table.risk_calculation_f8_all()[1] / table.form8) * 100, 2)
        request.session['form8_percentage'] = form8_percentage

        if form1_percentage <= 30:
            form1_color = 'green'
        elif (form1_percentage > 30) and (form1_percentage <= 60):
            form1_color = 'yellow'
        else:
            form1_color = 'red'

        if form2_percentage <= 30:
            form2_color = 'green'
        elif (form2_percentage > 30) and (form2_percentage <= 60):
            form2_color = 'yellow'
        else:
            form2_color = 'red'

        if form3_percentage <= 30:
            form3_color = 'green'
        elif (form3_percentage > 30) and (form3_percentage <= 60):
            form3_color = 'yellow'
        else:
            form3_color = 'red'

        if form4_percentage <= 30:
            form4_color = 'green'
        elif (form4_percentage > 30) and (form4_percentage <= 60):
            form4_color = 'yellow'
        else:
            form4_color = 'red'

        if form5_percentage <= 30:
            form5_color = 'green'
        elif (form5_percentage > 30) and (form5_percentage <= 60):
            form5_color = 'yellow'
        else:
            form5_color = 'red'

        if form6_percentage <= 30:
            form6_color = 'green'
        elif (form6_percentage > 30) and (form6_percentage <= 60):
            form6_color = 'yellow'
        else:
            form6_color = 'red'

        if form7_percentage <= 30:
            form7_color = 'green'
        elif (form7_percentage > 30) and (form7_percentage <= 60):
            form7_color = 'yellow'
        else:
            form7_color = 'red'

        if form8_percentage <= 30:
            form8_color = 'green'
        elif (form8_percentage > 30) and (form8_percentage <= 60):
            form8_color = 'yellow'
        else:
            form8_color = 'red'

        request.session['risk_score1']= table.risk_calculation_f1_all()
        request.session['risk_score2']= table.risk_calculation_f2_all()
        request.session['risk_score3']= table.risk_calculation_f3_all()
        request.session['risk_score4']= table.risk_calculation_f4_all()
        request.session['risk_score5']= table.risk_calculation_f5_all()
        request.session['risk_score6']= table.risk_calculation_f6_all()
        request.session['risk_score7']= table.risk_calculation_f7_all()
        request.session['risk_score8']= table.risk_calculation_f8_all()

        context = {
            'input_data': input_data,
            'name_of_controller': request.session.get('manager'),
            'title_of_dpo': request.session.get('title_of_DPO'),
            'name_of_dpo': request.session.get('name_of_DPO'),
            'risk_score1': table.risk_calculation_f1_all(),
            'risk_score2': table.risk_calculation_f2_all(),
            'risk_score3': table.risk_calculation_f3_all(),
            'risk_score4': table.risk_calculation_f4_all(),
            'risk_score5': table.risk_calculation_f5_all(),
            'risk_score6': table.risk_calculation_f6_all(),
            'risk_score7': table.risk_calculation_f7_all(),
            'risk_score8': table.risk_calculation_f8_all(),
            'form1_color': form1_color,
            'form2_color': form2_color,
            'form3_color': form3_color,
            'form4_color': form4_color,
            'form5_color': form5_color,
            'form6_color': form6_color,
            'form7_color': form7_color,
            'form8_color': form8_color,
            'form1_percentage': form1_percentage,
            'form2_percentage': form2_percentage,
            'form3_percentage': form3_percentage,
            'form4_percentage': form4_percentage,
            'form5_percentage': form5_percentage,
            'form6_percentage': form6_percentage,
            'form7_percentage': form7_percentage,
            'form8_percentage': form8_percentage,
            'total_no_of_risk': table.risk_calculation_f1_all()[1] + table.risk_calculation_f2_all()[1]
                                + table.risk_calculation_f3_all()[1] + table.risk_calculation_f4_all()[1]
                                + table.risk_calculation_f5_all()[1] + table.risk_calculation_f6_all()[1]
                                + table.risk_calculation_f7_all()[1] + table.risk_calculation_f8_all()[1]
        }
        return render(request, 'risk_summary.html', context)
    else:
        return render(request, 'dpia_screening.html')
    
    
class PDF(FPDF):
    pass
    # nothing happens when it is executed.

def get_pdf(request):
    # pdf = PDF(orientation='P', unit='mm', format='A4') # landscape
    # pdf.add_page()
    # pdf.set_font('Arial', 'B', 16)
    #
    # title = 'DATA PROTECTION IMPACT ASSESSMENT'
    # image = 'media/cg_logo.png'
    # pdf.image(image, x=5, y=5, w=42, h=12)
    # pdf.cell(ln=1, h=30, align='C', w=0, txt=title,  border=0)
    # pdf.output('pdf/output.pdf', 'F')
    return HttpResponse(open('pdf/dpia_template_v_1.pdf', 'rb'), content_type='application/pdf')

