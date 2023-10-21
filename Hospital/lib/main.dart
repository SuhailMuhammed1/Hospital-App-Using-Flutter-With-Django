

import 'dart:math';

import 'package:flutter/material.dart';
import 'package:hospital/layout/add_patient_lab_details.dart';
import 'package:hospital/layout/book_appointment.dart';
import 'package:hospital/layout/doctor_list_admin.dart';
import 'package:hospital/layout/doctor_reg.dart';
import 'package:hospital/layout/drawadmin.dart';
import 'package:hospital/layout/drawdoctor.dart';
import 'package:hospital/layout/editpro.dart';
import 'package:hospital/layout/jhi_msg_pat.dart';
import 'package:hospital/layout/lab.dart';
import 'package:hospital/layout/labdraw.dart';
import 'package:hospital/layout/login.dart';
import 'package:hospital/layout/main_register.dart';
import 'package:hospital/layout/mainpage.dart';
import 'package:hospital/layout/manage_appointment.dart';
import 'package:hospital/layout/patient_list_admin.dart';
import 'package:hospital/layout/patient_pro.dart';
import 'package:hospital/layout/patientdraw.dart';
import 'package:hospital/layout/post_notification.dart';
import 'package:hospital/layout/register_junior_health.dart';
import 'package:hospital/layout/register_lab.dart';
import 'package:hospital/layout/register_patient.dart';
import 'package:hospital/layout/send_message.dart';
import 'package:hospital/layout/view_appointment_patient.dart';
import 'package:hospital/layout/view_doctor_list.dart';
import 'package:hospital/layout/view_lab_report.dart';
import 'package:hospital/layout/view_noti_doctor.dart';
import 'package:hospital/layout/vwdrprofile.dart';
import 'layout/home.dart';
import 'layout/view_noti_patient.dart';
void main(){
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    routes: {
      '/':(context) =>home(),
      '/login':(context) =>login(),
      '/viewappoint':(context) =>view_appoint_patient(),
      '/vwlabreport':(context) =>view_lab_report(),
      '/drlistview':(context) =>drlist(),
      '/drlist_adminview':(context) =>drlist_adm(),
      '/addlabdetails':(context) =>lab_details_add(),
      '/pat_details_admin':(context) =>pat_det_admin(),
      '/post_notification':(context) =>post_notification(),
      '/vw_noti_dr':(context) =>vw_noti_dr(),
      '/vw_noti_pt':(context) =>vw_noti_pt(),
      '/bookappoint':(context) =>book_appointment(),
      '/manageappoint':(context) =>manage_appoint(),
      '/sndmsg':(context) =>snd_msg(),
      '/drproedit':(context) =>editpro(),
      '/patproedit':(context) =>pat_edit(),
      '/jhimsg':(context) =>jhi_msg(),
      '/labnew':(context) =>phcnw(),
    },
  ));
}

