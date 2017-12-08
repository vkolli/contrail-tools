"""
Author: Soumil R Kulkarni 
"""

import time
import sys 
from bs4 import BeautifulSoup
import ConfigParser
import paramiko
import os
import re
import subprocess
import urllib 
from optparse import OptionParser
import json
import displaytemplate


results_host_info = {
	"result_host": "10.204.216.50",
	"result_host_username": "bhushana",
	"result_host_password": "c0ntrail!23",
	"build_host": "10.84.24.64",
	"build_host_username": "root",
	"build_host_password": "c0ntrail123"
}

def check_if_object_downloaded(file=''):
	temp = False
	while(temp == False):
		a_tmp = subprocess.Popen('ls | grep %s' %file, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate() 
		if a_tmp[0] != '':
			temp = True
		else:
			print "Waiting for some more time for the file to get downloaded : %s" % file
			time.sleep(1)
	
def check_if_object_deleted(file=''):
	temp = False
	while (temp == False):
		a_tmp = subprocess.Popen('ls | grep %s' %file, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
		if a_tmp[0] == '':
			temp = True
		else:
			print "Waiting for some more time for the file to get deleted : %s" % file
			time.sleep(1)

def get_latest_build_number(build_path='', build_mode='', build_host_handle='', result_host_handle=''):
	if (build_mode=='cb'):
		stdin, stdout, stderr = build_host_handle.exec_command('ls %s -ltrh | grep lastStableBuild | cut -f2 -d">"' %(build_path))
	else:
		stdin, stdout, stderr = build_host_handle.exec_command('ls %s -ltrh | grep LATEST | cut -f2 -d">"' %(build_path))
	a = stdout.readlines()
	print a
	if a == []:
		return -1
	else:
		len_a = len(a)
		for i in a:
			var_a = i
			print i
		var_b = var_a.replace(' ','')
		latest_build = var_b.replace('\n', '')
		return latest_build

def get_exact_path(result_path='', build_no='', build_host_handle='', result_host_handle=''):
	ini_list = []
	stdin, stdout, stderr = result_host_handle.exec_command('ls %s | grep -e "-%s"' %(result_path, build_no))
	a = stdout.readlines()
	print a
	for i in a:
		b = i.replace('\n', '')
		#print b
		ini_list.append(b)
	if len(ini_list) == 1:
		temp_num_1_list = ini_list[0].split('-')
		if temp_num_1_list[1] == build_no:
			result_path = result_path + ini_list[0]
			#print path 
			return result_path
	if len(ini_list) > 1:
		t_list = []
		for i in ini_list:
			temp_list = i.split('-')
			t_list.append(temp_list[1])
		temp_var = 0
		for i in t_list:
			if i == build_no:
				index_no = t_list.index(i)
				temp_var = 1
				break
		if temp_var == 0:
			return None
		else:
			result_path = result_path + ini_list[index_no]
			return result_path

def get_build_date_from_jenkins_server(path='', build_host_handle='', result_host_handle=''):
	cmd='stat %s  | grep Change | cut -d" " -f2' %(path)
	print cmd
	stdin, stdout, stderr = build_host_handle.exec_command(cmd)
	a = stdout.readlines()
	#print a
	b=a[0].replace('\n', '')
	return b


def get_all_ini_files(exact_path='', build_host_handle='', result_host_handle=''):
	final_ini_list = []
	stdin, stdout, stderr = result_host_handle.exec_command('ls %s\/*ini' %exact_path)
	ini_list =stdout.readlines()
	error_list = stderr.readlines()
	#print ini_list
	for i in ini_list:
		a = str(i).replace('\n', '')
		final_ini_list.append(a)
	if (len(error_list) == 0):
		return final_ini_list
	else:
		return []

def get_data_from_individual_ini_file(file_1=''):
	config = ConfigParser.ConfigParser()
	return_dict = {}
	#config_file = open('report_details_jenkins-centos71_kilo_Multi_Node_Sanity-358_2017_03_22_22_10_40.ini', 'r')
	config_file = open(file_1, 'r')
	config.readfp(config_file)
	build = config.get('Test', 'build')
	distro = config.get('Test', 'distro_sku')
	report = config.get('Test', 'report')
	topology = config.get('Test', 'topology')
	topo_summary = topology
	a_temp = topo_summary.split(':')
	#print a_temp
	temp_list = ['Config Nodes', 'Control Nodes', 'Compute Nodes', 'Openstack Node', 'WebUI Node', 'Analytics Nodes', 'Physical Devices']
	b_temp = []
	for del_string in temp_list:
		for rep_string in a_temp:
			if del_string in rep_string:
				a = rep_string.replace(del_string, '')
				b_temp.append(a)
	#print b_temp
	c_temp = []
	for j in b_temp:
		a = j.replace(' ', '')
		c_temp.append(a)
	#print c_temp
	d_temp = []
	for j in c_temp:
		a = j.replace("[u'", '')
		d_temp.append(a)
	#print d_temp
	e_temp = []
	for j in d_temp:
		a = j.replace("'", '')
		e_temp.append(a)
	#print e_temp
	f_temp = []
	for j in e_temp:
		a = j.replace("]", '')
		f_temp.append(a)
	del f_temp[0]
	#print f_temp
	first_element = f_temp[0]
	itr = 0
	for j in f_temp:
		if j != first_element:
			itr = 1
	if itr == 0:
		#print "Topology Summary: SINGLE NODE CLUSTER"
		return_dict['topo_summary'] = 'SINGLE-NODE CLUSTER'
	else:
		#print "Topology Summary: MULTI-NODE CLUSTER"
		return_dict['topo_summary'] = 'MULTI-NODE CLUSTER'
	#print distro
	#print build
	#print report
	return_dict["build"] = build
	return_dict["distro"] = distro
	return_dict["report"] = report
	return_dict["topology"] = topology
	return return_dict 

def get_summary_from_html_file(html_file_link):
	os.system('wget -q %s -O junit-noframes.html' %html_file_link)
	#time.sleep(4)
	check_if_object_downloaded(file='junit-noframes.html')
	file = open('junit-noframes.html', 'r')
	soup = BeautifulSoup(file)
	#print soup	
	th_tags = soup.findAll('th')
	td_tags = soup.findAll('td')
	final_th_tags = []
	final_td_tags = []
	final_td_tags_1 = []
	return_dict = {}
	for i in range(6):
		a = str(th_tags[i]).replace('<th>', '')
		b = str(a).replace('</th>', '')
		final_th_tags.append(b)
	return_dict["labels"] = final_th_tags
	final_td_tags = [td_tags[2], td_tags[3], td_tags[4], td_tags[5], td_tags[6], td_tags[7]]
	for i in final_td_tags:
		a = str(i).replace('<td>', '')
		b = str(a).replace('</td>', '')
		final_td_tags_1.append(b)
	return_dict["values"] = final_td_tags_1
	file.close()
	#os.system('rm -f /root/sanity_dashboard_data/process_results/junit-noframes.html')
	os.system('rm -rf *.html')
	#check_if_object_deleted(file='junit-noframes.html')
	return return_dict

def get_detailed_data_from_ini_files(list_of_ini_files=[], exact_path=''):
	if not list_of_ini_files:
		print "There is an error fetching all the ini files . The list given as argument to the function 'get_detailed_data_from_ini_files' has no ini files "
	else:
		ini_list = list_of_ini_files
		final_total_number_of_testcases = 0
		final_success_rate = 0
		detail_info_dict = {}
		for i in ini_list:
			path = i
			#print path
			os.system('sshpass -p "c0ntrail!23" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=error bhushana@10.204.216.50:%s .' %path)
			#time.sleep(4)
			file=os.path.basename(i)
			check_if_object_downloaded(file)
			if os.stat(file).st_size != 0:
				dict_1 = get_data_from_individual_ini_file(file_1=file)
				#print dict_1
				test_num_dict = get_summary_from_html_file(dict_1['report'])
				dict_1['testcase_results'] = test_num_dict
				internal_no_testcases = int(dict_1['testcase_results']['values'][0])
				internal_success_rate = dict_1['testcase_results']['values'][4]
				#print dict_1
				#print internal_no_testcases
				#print internal_success_rate
				if internal_no_testcases > final_total_number_of_testcases:
					final_total_number_of_testcases = internal_no_testcases
					temp_success_rate = float((internal_success_rate.replace('%', '')))
					final_success_rate = temp_success_rate
					detail_info_dict = dict_1
				elif internal_no_testcases == final_total_number_of_testcases:
					temp_success_rate = float((internal_success_rate.replace('%', '')))
					if temp_success_rate > final_success_rate:
						final_success_rate = temp_success_rate
						detail_info_dict = dict_1
				os.system('rm -rf %s' %file)
			else:
				os.system('rm -rf %s' %file)
				print "The ini file is empty"
				return None
		return detail_info_dict

def build_final_json(dict_1='', dest_file_name='', mode='', all_combination_dict='',build_mode=''):
	final_info_dict = {}
	final_info_dict['Sanity'] = {}
	final_job_list = []
	row_id = 0
	for job in dict_1[mode]:
		individual_info_dict = {}
		#individual_info_dict['JobName'] = job
		individual_info_dict['JobName'] = all_combination_dict[job]['job_name']
		#individual_info_dict['Row id'] = str(row_id)
		individual_info_dict['Row id'] = all_combination_dict[job]['row_id']
		row_id = row_id + 1
		a = dict_1[mode][job].keys()
		b = sorted(a)
		build_number_list = []
		#build_number_list = b[::-1]
		#print build_number_list
		temp_a = []
		for i in b:
			temp_a.append(int(i))
		temp_a.sort()
		temp_b = temp_a[::-1]
		for i in temp_b:
			build_number_list.append(str(i))
		print build_number_list
		all_build_list = []
		temp_num = 5
		for i in build_number_list:
			temp_num = temp_num - 1
			individual_build_dict = {}
			individual_build_dict["Build number"]  = int(i)
			individual_build_dict["Build date"] = dict_1[mode][job][i]['build_date_from_jenkins']
			individual_build_dict['Report'] = dict_1[mode][job][i]['report']
			individual_build_dict['Total tests'] = dict_1[mode][job][i]['testcase_results']['values'][0]
			individual_build_dict['Failures'] = dict_1[mode][job][i]['testcase_results']['values'][1]
			individual_build_dict['Errors'] = dict_1[mode][job][i]['testcase_results']['values'][2]
			individual_build_dict['Skipped'] = dict_1[mode][job][i]['testcase_results']['values'][3]
			tmp_total = (int(individual_build_dict["Total tests"]) - int(individual_build_dict["Skipped"]))
			individual_build_dict["Total tests"] = str(tmp_total)
			individual_build_dict["Success rate"] = dict_1[mode][job][i]['testcase_results']['values'][4]
			individual_build_dict["status"] = "complete"
			individual_build_dict["BuildLink"] = "http://10.84.5.120"+ dict_1[mode][job][i]['build_path']
			all_build_list.append(individual_build_dict)
		while temp_num > 0:
			temp_num = temp_num -1
			individual_build_dict = {}
			individual_build_dict["Build number"]  = 0
			individual_build_dict["Build date"] = '0'
			individual_build_dict['Report'] = '--'
			individual_build_dict['Total tests'] = '0'
			individual_build_dict['Failures'] = '0'
			individual_build_dict['Errors'] = '0'
			individual_build_dict['Skipped'] = '0'
			individual_build_dict["Success rate"] = '0.0%'
			individual_build_dict["status"] = "incomplete"
			individual_build_dict["BuildLink"] = "http://10.84.5.120"+ all_combination_dict[job][build_mode]['web_build_path']
			all_build_list.append(individual_build_dict)
		individual_info_dict["Builds"]= all_build_list
		final_job_list.append(individual_info_dict)
	final_info_dict["Sanity"]["Job"] = final_job_list
	#print final_info_dict
	final_info_dict["Sanity"]["Bugs"] = []
	pprint_final_info_dict = json.dumps(final_info_dict, indent=4)
	if dest_file_name == '':
		fp = open('final_result.json', 'w')
		print >> fp, pprint_final_info_dict
		fp.close()
	else:
		fp = open('%s' %dest_file_name, 'w')
		print >> fp, pprint_final_info_dict
		fp.close()	

def get_all_branch_final_dict(mode='', outfile='', build_mode='', build_host_handle='', result_host_handle=''):
	info_dict = {}
	info_dict[mode] = {}
	all_combination_dict = displaytemplate.jobs[mode]
	print all_combination_dict
	for job in all_combination_dict:
		print "\n=================\nJob: "+job
		build_path=all_combination_dict[job][build_mode]['build_path']
		latest_build_number = get_latest_build_number(build_path, build_mode, build_host_handle, result_host_handle)
		print "Latest Build Number: " + str(latest_build_number)
		#get_detailed_data_from_ini_files(all_combination_dict[job], build_no=latest_build_number)
		tmp = 5 
		info_dict[mode][job] = {}
		#while (int(latest_build_number) > 1 and tmp > 0):
		while (tmp > 0):
			if int(latest_build_number) < 1:
				break
			print latest_build_number
                        result_path=all_combination_dict[job][build_mode]['result_path']
			build_no=latest_build_number
			exact_path = get_exact_path(result_path, build_no, build_host_handle, result_host_handle)
			print exact_path
			if exact_path == None:
				latest_build_number = str(int(latest_build_number) - 1)
				#tmp = tmp - 1
			else:
				#print exact_path
				list_of_ini_files = get_all_ini_files(exact_path, build_host_handle, result_host_handle)
				print list_of_ini_files
				#import pdb;pdb.set_trace()
				if(len(list_of_ini_files)==0):
					latest_build_number = str(int(latest_build_number) - 1)
					continue
				detailed_info_dict = get_detailed_data_from_ini_files(list_of_ini_files, exact_path)
				#print detailed_info_dict
				if detailed_info_dict == None:
					latest_build_number = str(int(latest_build_number) - 1)
					continue
					#tmp = tmp - 1
				else:
					info_dict[mode][job][latest_build_number] = detailed_info_dict
					path_for_build_date = all_combination_dict[job][build_mode]['build_path'] + latest_build_number
					info_dict[mode][job][latest_build_number]['build_date_from_jenkins'] = get_build_date_from_jenkins_server(path_for_build_date, build_host_handle, result_host_handle)
					if (build_mode == "cb"):
						build_path = all_combination_dict[job][build_mode]['web_build_path'] + latest_build_number + '/archive/packages/'
					else:
						build_path = all_combination_dict[job][build_mode]['web_build_path'] + latest_build_number
					info_dict[mode][job][latest_build_number]["build_path"] = build_path
					info_dict[mode][job][latest_build_number]['web_build_path'] = all_combination_dict[job][build_mode]['web_build_path']
					latest_build_number = str(int(latest_build_number) - 1)
					tmp = tmp - 1
	dict_1=info_dict
	dest_file_name=outfile
	build_final_json(dict_1, dest_file_name, mode, all_combination_dict, build_mode)


def main():
	parser = OptionParser()
	parser.add_option('-m', '--mode', help='Give the name of the branch that you want to check sanity resuts of', type='string', dest='mode')
	parser.add_option('-o', '--outfile_cb', help='Name of the output file where the json will be stored', type='string', dest='outfile_cb')
	parser.add_option('-f', '--outfile_fb', help='Name of the output file where the json will be stored', type='string', dest='outfile_fb')
	(opts, args) = parser.parse_args()

        build_host_handle = paramiko.SSHClient()
        build_host_handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        build_host_handle.connect(results_host_info['build_host'], username= results_host_info['build_host_username'], password= results_host_info['build_host_password'])
        result_host_handle = paramiko.SSHClient()
        result_host_handle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        result_host_handle.connect(results_host_info['result_host'], username=results_host_info['result_host_username'], password=results_host_info['result_host_password'])

	mode=opts.mode
	outfile_cb=opts.outfile_cb
	outfile_fb=opts.outfile_fb
	build_mode="cb"
	get_all_branch_final_dict(mode, outfile_cb, build_mode, build_host_handle, result_host_handle)
	build_mode="fb"
	get_all_branch_final_dict(mode, outfile_fb, build_mode, build_host_handle, result_host_handle)
	#build_final_json(dict_to_build_final_json)

main()
