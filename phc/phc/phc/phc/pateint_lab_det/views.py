from django.http import HttpResponse
from django.shortcuts import render
from pateint_lab_det.models import PateintLabDet
from pateint_lab_det.models import LabReport
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.

from rest_framework.views import APIView,Response
from doctor.serializers import android_serialiser
from pateint_lab_det.serializers import android_serialiserssssss

class labpat(APIView):
    def get(self,request):
        ob = PateintLabDet.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ob=PateintLabDet()
        ob.lab_detials=request.data['lab_detials']
        ob.p_id=request.data['pid']
        ob.lab_id="1"
        ob.save()
        return HttpResponse("Yess")

from phc import settings
class lab(APIView):
    def post(self,request):
        ab=LabReport()
        ab.name=request.data['name']
        ab.age=request.data['age']
        ab.ag_ratio=request.data['ag_ratio']
        ab.alakine_phos=request.data['alakine_phos']
        ab.albumin=request.data['albumin']
        ab.bacteria=request.data['bacteria']
        ab.basophil=request.data['basophil']
        ab.bile_pigment=request.data['bile_pigment']
        ab.bile_salt=request.data['bile_salt']
        ab.casts=request.data['casts']
        ab.crystal=request.data['crystal']
        ab.dbilirubin=request.data['dbilirubin']
        ab.dc_neutrophil=request.data['dc_neutrophil']
        ab.dengue=request.data['dengue']
        ab.eosinophil=request.data['eosinophil']
        ab.epithelial=request.data['epithelial']
        ab.esr=request.data['esr']
        ab.fbs=request.data['fbs']
        ab.globulin=request.data['globulin']
        ab.hba1c=request.data['hba1c']
        ab.hbsag=request.data['hbsag']
        ab.hdl=request.data['hdl']
        ab.heamoglobin=request.data['heamoglobin']
        ab.hiv=request.data['hiv']
        ab.lab_reportcol=request.data['lab_reportcol']
        ab.ldl=request.data['ldl']
        ab.lgg1gm=request.data['lgg1gm']
        ab.lymphocyte=request.data['lymphocyte']
        ab.malarial_parasite=request.data['malarial_parasite']
        ab.microscopy=request.data['microscopy']
        ab.monocyte=request.data['monocyte']
        ab.ns1ag=request.data['ns1ag']
        ab.platelet_count=request.data['platelet_count']
        ab.potassium=request.data['potassium']
        ab.ppbs=request.data['ppbs']
        ab.pusceils=request.data['pusceils']
        ab.rbcs=request.data['rbcs']
        ab.rbs=request.data['rbs']
        ab.rdt=request.data['rdt']
        ab.screat=request.data['screat']
        ab.sex=request.data['sex']
        ab.sgot=request.data['sgot']
        ab.sgpt=request.data['sgpt']
        ab.sodium=request.data['sodium']
        ab.sputum=request.data['sputum']
        ab.stool=request.data['stool']
        ab.sugar=request.data['sugar']
        ab.suricacid=request.data['suricacid']
        ab.t_cholestrol=request.data['t_cholestrol']
        ab.tbirirubin=request.data['tbirirubin']
        ab.total_wbc_count=request.data['total_wbc_count']
        ab.tprotien=request.data['tprotien']
        ab.triglycerides=request.data['triglycerides']
        ab.urea=request.data['urea']
        ab.vldl=request.data['vldl']
        ab.uid=request.data['uid']
        ab.albumin1=request.data['alb1']
        ab.save()

        bb=LabReport.objects.filter(lb_id=ab.lb_id)
        context={
            'k':bb
        }
        template_path = 'patient_lab_det/LAB.HTML'
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="Lab_report.pdf"'
        # find the template and render it.
        fpath=str(settings.BASE_DIR)+str(settings.STATIC_URL)+str(ab.lb_id)+".pdf"
        template = get_template(template_path)
        html = template.render(context)
        rsf=open(fpath,"w+b")
        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=rsf)
        # print(context)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        # print(response)
        rsf.close()

        return HttpResponse("Yess")
        # return render(request,'patient_lab_det/LAB.HTML',context)
        # return HttpResponse("Yess")


class view_labreport(APIView):
    def post(self,request):
        ab=LabReport.objects.filter(uid=request.data['uid'])
        ser = android_serialiserssssss(ab, many=True)
        return Response(ser.data)

class pdf(APIView):
    def post(self,request):
        lid=""
        bb=LabReport.objects.get(lb_id=request.data['lid'])
        request.session['lid']=lid
        return HttpResponse("yess")

