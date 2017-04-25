import sys 
import BeautifulSoup
import ConfigParser
import paramiko
import os
import subprocess
import urllib 

def get_summary_():
	sample_dict = {0: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_12_20_29_57/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': 'CentOS Linux release 7.1.1503 Core 3.0.2.0-26~kilo'}, 1: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_12_20_53_54/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': 'CentOS Linux release 7.1.1503 Core 3.0.2.0-26~juno'}, 2: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_12_22_17_02/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~juno'}, 3: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_12_22_17_10/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~juno'}, 4: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_12_22_18_06/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~juno'}, 5: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_00_14_37/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~juno'}, 6: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_00_15_00/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~juno'}, 7: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_00_15_15/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~liberty'}, 8: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_00_15_45/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~kilo'}, 9: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_00_52_44/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~kilo'}, 10: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_06_00_22/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~juno'}, 11: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_16_15_10/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~kilo'}, 12: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_13_16_50_21/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~kilo'}, 13: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_14_07_49_37/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~kilo'}, 14: {'report': 'http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_18_14_57_49/junit-noframes.html', 'build': '3.0.2.0-26', 'distro': '"Ubuntu 14.04.2 LTS" 3.0.2.0-26~kilo'}}
	for i in sample_dict:
		url = sample_dict[i]["report"]
		f = urllib.urlopen(url)
		file = f.read()
		#file = open('junit-noframes.html', 'r')
		#file = open('Ubuntu-14.04.5-LTS-3.2.2.0-31~mitaka-Vcenter-Gateway-jenkins-ubuntu-14-04_vcenter_gateway_Sanity_mitaka-14_1490097315.14.html', 'r')
		soup = BeautifulSoup.BeautifulSoup(file)
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
		#print final_th_tags
		return_dict[i]["labels"] = final_th_tags
		final_td_tags = [td_tags[2], td_tags[3], td_tags[4], td_tags[5], td_tags[6], td_tags[7]]
		for i in final_td_tags:
			a = str(i).replace('<td>', '')
			b = str(a).replace('</td>', '')
			final_td_tags_1.append(b)
		#print final_td_tags_1
		return_dict[i]["values"] = final_td_tags_1
		print "hey"
	return return_dict
	#print td_tags[2] # Total Tests 
	#print td_tags[3] # Failures
	#print td_tags[4] # Errors
	#print td_tags[5] # Skipped
	#print td_tags[6] # SuccessRate
	#print td_tags[7] # Time Taken


def get_summary_from_html_file(html_file_link):
	os.system('wget -q %s' %html_file_link)
	file = open('junit-noframes.html', 'r')
	soup = BeautifulSoup.BeautifulSoup(file)
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
	os.system('rm junit-noframes.html')
	return return_dict



def get_data_from_ini_file(file_1):
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

def print_summary():
	value_dict = get_summary()
	label_list = value_dict["labels"]
	value_list = value_dict["values"]
	ini_dict = get_data_from_ini_file()
	print "\nDistro : %s" %ini_dict["distro"]
	print "-----------------------------------------"
	print "Build : %s" % ini_dict["build"]
	print "-----------------------------------------"
	print "Total Tests : %s" %value_list[0]
	print "-----------------------------------------"
	print "Failures : %s" %value_list[1]
	print "-----------------------------------------"
	print "Errors : %s" %value_list[2]
	print "-----------------------------------------"
	print "Skipped : %s" %value_list[3]
	print "-----------------------------------------"
	print "Success Rate (Percent): %s " %value_list[4]
	print "-----------------------------------------"
	print "Time Taken : %s" %value_list[5]
	print "-----------------------------------------"
	rep_path = str(ini_dict["report"]).replace('http://10.204.216.50/', 'http://mayamruga.englab.juniper.net/')
	print "Path to the html file (Paste this link on the browser): %s\n" % rep_path

def get_all_ini_files():
	host = '10.204.216.50'
	username = 'bhushana'
	password = 'bhu@123'
	ini_list = []
	final_ini_list  = []
	error_list = []
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username = username, password = password)
	stdin, stdout, stderr = client.exec_command('ls /var/www/html/Docs/sanity/daily/R3.0/3.0.2.0-26 | grep .ini')
	ini_list =stdout.readlines()
	error_list = stderr.readlines()
	client.close()
	for i in ini_list:
		a = str(i).replace('\n', '')
		final_ini_list.append(a)
	#for i in final_ini_list:
	#	print i
	if (len(error_list)==0):
		return final_ini_list
	else:
		return error_list 

def get_detailed_data_from_ini_files():
	host = '10.204.216.50'
	username = 'bhushana'
	password = 'bhu@123'
	info_dict = {}
	path = '/var/www/html/Docs/sanity/daily/R3.0/3.0.2.0-26'
	ini_list = get_all_ini_files()
	if len(ini_list) == 1:
		print "There is an Error Fetching all the ini files from the given path: \n %s " % ini_list[0]
	else:
		num = 0 
		print "Downloading all the report.ini files in the given path and getting the reiquired data from them \n"
		for i in ini_list:
			new_path = path + '/'+ i
			#print "Downloading the following file: ",new_path
			os.system('sshpass -p "bhu@123" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no bhushana@10.204.216.50:%s .' %new_path)
			Dict_1 = get_data_from_ini_file(i)
			info_dict[num] = Dict_1
			os.system('rm %s' %i)
			#print "Done %d " %num
			num += 1
	#print info_dict
	print "\n"
	print "Adding the summary data to the already collected data from the ini files"
	print "______________________________________________________________________________________"
	print "RESULTS :-"
	print "______________________________________________________________________________________"
	for i in info_dict:
		test_num_dict = get_summary_from_html_file(info_dict[i]["report"])
		info_dict[i]["testcase_results"] = test_num_dict
	return info_dict

def print_report_summary():
	info_dict = get_detailed_data_from_ini_files()
	for i in info_dict:
		print "Distro : %s" % info_dict[i]["distro"]
		print "Build : %s" % info_dict[i]["build"]
		print "Report Link : %s" % info_dict[i]["report"]
		topo_string = str(info_dict[i]["topology"])
		replaced_topo_string = topo_string.replace('<br/>', '')
		print "Topology : %s" % replaced_topo_string
		"""
		a_temp = replaced_topo_string.split(':')
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
			print "Topology Summary: SINGLE NODE CLUSTER"
		else:
			print "Topology Summary: MULTI-NODE CLUSTER"
		"""
		print "Topology Summaty: %s" %info_dict[i]['topo_summary']
		test_result_dict_lables = info_dict[i]["testcase_results"]["labels"]
		test_result_dict_values = info_dict[i]["testcase_results"]["values"]
		#print test_result_dict_lables
		#print test_result_dict_values
		num = len(test_result_dict_values)
		itr = 0
		print "TEST RESULTS SUMMARY : "
		while (itr < num):
			print "   %s : %s " %(test_result_dict_lables[itr], test_result_dict_values[itr])
			itr += 1
		print "______________________________________________________________________________________"


def get_html_file():
	info_dict = get_detailed_data_from_ini_files()
	html_string = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title> TEST SUMMARY GATHERING TOOL </title>
	</head>
	<body>
	<h1>Daily Sanity Report Summary</h1>
	<style>
		table {
		    font-family: arial, sans-serif;
		    border-collapse: collapse;
		    width: 100%;
		}

		td, th {
		    border: 1px solid #dddddd;
		    text-align: left;
		    padding: 8px;
		}

		tr:nth-child(even) {
		    background-color: #dddddd;
		}
	</style>
	<table>
		<tr>
			<th> DISTRO </th>
			<th> BUILD </th>
			<th> REPORT LINK </th>
			<th> TEST SUMMARY </th>
		</tr>\n
	'''
	for i in info_dict:
		html_string = html_string + '''
		<tr>
			<th> %s </th>
			<th> %s </th>
			<th> <a href="%s"> click here </th>
		''' % (info_dict[i]["distro"], info_dict[i]["build"], info_dict[i]["report"])
		summ = ''
		test_result_dict_lables = info_dict[i]["testcase_results"]["labels"]
		test_result_dict_values = info_dict[i]["testcase_results"]["values"]
		num = len(test_result_dict_values)
		itr = 0 
		while (itr < num):
			summ = summ + " %s:%s " % (test_result_dict_lables[itr], test_result_dict_values[itr])
			itr += 1 
		html_string = html_string + '''
			<th> %s </th>
		</tr> 
		''' % summ
	html_string = html_string + """
	</table>
	</body>
	</html>
	"""
	print html_string


#-o UserKnownHostsFile=/dev/null 

#a = get_summary_from_html_file('http://10.204.216.50/Docs/logs/3.0.2.0-26_2016_04_12_20_29_57/junit-noframes.html')
#print a
#a = get_detailed_data_from_ini_files()
print_report_summary()
#get_html_file()
#a=get_all_ini_files()
#print a
#print_summary()
