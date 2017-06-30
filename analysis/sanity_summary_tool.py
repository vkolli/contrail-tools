"""
Author : Soumil Kulkarni
Script Name: sanity_summary_tool.py
Description: The inputs to this script are the exact Branch Name and the exact Build Number. The script will fetch the results of all the sanity results of that build and 
              displays them as a summary in the terminal or can create a html file which when opened from the browser have hyperlinks to the entire report. 

Usage : 
		python sanity_summary_tool.py --branch <branch name > --build <build number> --output_format <print/html> --dest_file_name <name for the destiantion html file (optional)>
		-> if the output format is 'html', mentioning of the '--dest_file_name' parameter is optional 
		-> if '--dest_file_name' parameter is not given when '--output_format=html', the dest file name by default is 'result_summary.html'
		-> if the output format is 'print', mentioning of the '--dest_file_name' parameter is not required. 

		eg1 : python sanity_summary_tool.py --branch R3.2 --build 34 --output_format print 
		eg2 : python sanity_summary_tool.py --branch R3.2 --build 34 --output_format html 
		eg3 : python sanity_summary_tool.py --branch R3.2 --build 34 --output_format html --dest_file_name test_sanity_10.html

"""

import sys 
from bs4 import BeautifulSoup
import ConfigParser
import paramiko
import os
import re
import subprocess
import urllib 
from optparse import OptionParser


def get_summary_from_html_file(html_file_link):
	os.system('wget -q %s' %html_file_link)
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

def get_exact_path(branch='', build=''):
	branch= branch
	build = build
	host = '10.204.216.50'
	username = 'bhushana'
	password = 'bhu@123'
	ini_list = []
	err_list = []
	path = "/var/www/html/sanity/daily/"
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username = username, password = password)
	stdin, stdout, stderr = client.exec_command('ls %s | grep %s' %(path, branch))
	a = stdout.readlines()
	for i in a:
		b = i.replace('\n', '')
		ini_list.append(b)
	#err_list = stderr.readlines()
	client.close()
	if (len(ini_list) == 1):
		path = path + ini_list[0] + '/'
		#print path
	if (len(ini_list) > 1):
		for j in ini_list:
			if j == branch:
				path = path + j + '/'
				#print path
	else:
		return None
	ini_list = []
	err_list = []
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username = username, password = password)
        cmd='ls %s | grep %s' %(path, build)
        print cmd
	stdin, stdout, stderr = client.exec_command('ls %s | grep %s' %(path, build))
	a = stdout.readlines()
	for i in a:
		b = i.replace('\n', '')
		print b
		ini_list.append(b)
	#err_list = stderr.readlines()
	client.close()
	if (len(ini_list) == 1):
		path = path + ini_list[0]
		#print path
		return path


def get_all_ini_files(branch='', build=''):
	host = '10.204.216.50'
	username = 'bhushana'
	password = 'bhu@123'
	ini_list = []
	final_ini_list  = []
	error_list = []
	path = get_exact_path(branch=branch, build=build)
	#print path
	if path == None:
		print "Branch name or Build Number is wrong, please check ..."
	else:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(host, username = username, password = password)
		stdin, stdout, stderr = client.exec_command('ls %s | grep .ini' %path)
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


def get_detailed_data_from_ini_files(branch='', build=''):
	host = '10.204.216.50'
	username = 'bhushana'
	password = 'bhu@123'
	info_dict = {}
	path = str(get_exact_path(branch=branch, build=build))
	#print path
	if path == None:
		print "The Branch name or build number is wrong please check"
	else:

		#path = '/var/www/html/Docs/sanity/daily/R3.0/3.0.2.0-26'
		ini_list = get_all_ini_files(branch=branch, build= build)
		#print ini_list
		if not ini_list:
			print "There is an Error Fetching all the ini files from the given build: %s and Branch : %s" %(build,branch) 
		else:
			print "\nDownloading all the report.ini files in the given path and getting the reiquired data from them "

                        num = 0
                        print "\nDownloading all the report.ini files in the given path and getting the reiquired data from them "
                        info_dict[build] ={}
                        for i in ini_list:
                                new_path = path + '/'+ i
                                #print "Downloading the following file: ",new_path
                                os.system('sshpass -p "bhu@123" scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o LogLevel=error bhushana@10.204.216.50:%s .' %new_path)
                                Dict_1 = get_data_from_ini_file(i)
				#import pdb; pdb.set_trace()	
                                info_dict[build][num] = Dict_1
                                os.system('rm %s' %i)
                                #print "Done %d " %num
                                num += 1

		#print info_dict
		print "\n"
		print "Adding the summary data to the already collected data from the ini files"
		#print "______________________________________________________________________________________"
		#print "RESULTS :-"
		#print "______________________________________________________________________________________"
		for i in info_dict[build]:
			test_num_dict = get_summary_from_html_file(info_dict[build][i]["report"])
			info_dict[build][i]["testcase_results"] = test_num_dict
		return info_dict

def print_report_summary(branch='', build=''):
	info_dict = get_detailed_data_from_ini_files(branch=branch, build=build)
	print "______________________________________________________________________________________"
	print "RESULTS :-"
	print "______________________________________________________________________________________"
	for i in info_dict:
		print "Distro : %s" % info_dict[i]["distro"]
		print "Build : %s" % info_dict[i]["build"]
		print "Report Link : %s" % info_dict[i]["report"]
		topo_string = str(info_dict[i]["topology"])
		replaced_topo_string = topo_string.replace('<br/>', '')
		print "Topology : %s" % replaced_topo_string
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


def print_into_text_file(info_dict):
        import os, time
        mydir = os.path.join(os.getcwd(), time.strftime("%Y_%m_%d"))
        if not os.path.exists(mydir):
            os.makedirs(mydir)
        filename = time.strftime("%H_%M_%S") 
        print 'Generating text report at %s/%s' %(mydir,filename)
        f = open(os.path.join(mydir,filename), 'w')
        for key in info_dict:
            for i in info_dict[key]:
	        f.write("Distro : %s\n" % info_dict[key][i]["distro"])
                f.write("Build : %s\n" % info_dict[key][i]["build"])
                f.write("Report Link : %s\n" % info_dict[key][i]["report"])
                topo_string = str(info_dict[key][i]["topology"])
                replaced_topo_string = topo_string.replace('<br/>', '')
                f.write("Topology : %s\n" % replaced_topo_string)
                f.write("Topology Summary: %s\n" %info_dict[key][i]['topo_summary'])
                test_result_dict_lables = info_dict[key][i]["testcase_results"]["labels"]
                test_result_dict_values = info_dict[key][i]["testcase_results"]["values"]
                #print test_result_dict_lables
                #print test_result_dict_values
                num = len(test_result_dict_values)
                itr = 0
                f.write("TEST RESULTS SUMMARY : ")
                while (itr < num):
                        f.write("   %s : %s \n" %(test_result_dict_lables[itr], test_result_dict_values[itr]))
                        itr += 1
                f.write( "______________________________________________________________________________________\n")
        f.close()

def print_xml_file(info_dict):
	import xml.etree.cElementTree as ET
        import os, time

        mydir = os.path.join(os.getcwd(), time.strftime("%Y_%m_%d"))
        if not os.path.exists(mydir):
            os.makedirs(mydir)
        filexml = time.strftime("%H_%M_%S")+".xml"
        filename = os.path.join(mydir,filexml)
	root = ET.Element("Sanity")
        print 'Generating text report at %s' %(filename)
        for key in info_dict:
            for i in info_dict[key]:
                topo_string = str(info_dict[key][i]["topology"])
                replaced_topo_string = topo_string.replace('<br/>', '')
                dist = ET.SubElement(root, "Distro", name="Run_Info")
                dist.text = info_dict[key][i]["distro"]
		ET.SubElement(dist, "Build", name="Build Number").text = key
		ET.SubElement(dist, "Date",name="Build Date").text = info_dict[key][0]["date"]
		ET.SubElement(dist, "Branch",name="Branch").text = info_dict[key][i]["build"]
		ET.SubElement(dist, "Report",name="Link").text = info_dict[key][i]["report"]
		ET.SubElement(dist, "Topology", name="Testbed Topology").text = info_dict[key][i]['topo_summary'] 
                summ = ''
                test_result_dict_lables = info_dict[key][i]["testcase_results"]["labels"]
                test_result_dict_values = info_dict[key][i]["testcase_results"]["values"]
                num = len(test_result_dict_values)
                itr = 0

                while (itr < num):
                        summ = summ + " %s:%s " % (test_result_dict_lables[itr], test_result_dict_values[itr])
                        itr += 1
		ET.SubElement(dist, "Summary", name="Result Summary").text = summ 
	tree = ET.ElementTree(root)
	tree.write(filename)

def get_build_date(branch='', build=''):
        branch= branch
        build = build
        host = '10.84.5.31'
        username = 'vivekgarg'
        password = 'vivekgarg123'
        ini_list = []
        err_list = []
        path = "/github-build/"
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username = username, password = password)
        stdin, stdout, stderr = client.exec_command('ls %s | grep %s' %(path, branch))
        a = stdout.readlines()
        for i in a:
                b = i.replace('\n', '')
                ini_list.append(b)
        #err_list = stderr.readlines()
        client.close()
        if (len(ini_list) == 1):
                path = path + ini_list[0] + '/'
                #print path
        if (len(ini_list) > 1):
                for j in ini_list:
                        if j == branch:
                                path = path + j + '/'
                                #print path
        else:
                return None
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username = username, password = password)
        cmd='stat %s/%s  | grep Change | cut -d" " -f2' %(path, build)
        print cmd
        stdin, stdout, stderr = client.exec_command('stat %s/%s  | grep Change | cut -d" " -f2' %(path, build))
        a = stdout.readlines()
        b=a[0].replace('\n', '')
        return b
        client.close()


def process_summary(summary=""):
        m = re.search('Success rate:(.*)%',summary)
        success_rate = float(m.group(1))
        if success_rate >= 85 :
 		return "PASS"
        else:
		return "FAIL"	
        

def get_html_file(dest_file="", branch='', build=''):
        info_dict_combined = {}
        for i in range(2):
	    info_dict_combined.update(get_detailed_data_from_ini_files(branch=branch, build=build))
            info_dict_combined[build][0]["date"]=get_build_date(branch, build)
            build = str(int(build) - 1)
           
        print_xml_file(info_dict_combined)
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
			<th> TOPOLOGY </th>
			<th> TEST SUMMARY </th>
			<th> STATUS </th>
		</tr>\n
	'''
	for key in info_dict_combined:
	    for i in info_dict_combined[key]:
             # if re.match(".*jenkins-ubuntu-14-04*",info_dict_combined[key][i]["report"]):
		html_string = html_string + '''
		<tr>
			<th> %s </th>
			<th> %s </th>
			<th> <a href="%s"> click here </th>
			<th> %s </th>
		''' % (info_dict_combined[key][i]["distro"], info_dict_combined[key][i]["build"], info_dict_combined[key][i]["report"], info_dict_combined[key][i]['topo_summary'])
		summ = ''
		test_result_dict_lables = info_dict_combined[key][i]["testcase_results"]["labels"]
		test_result_dict_values = info_dict_combined[key][i]["testcase_results"]["values"]
		num = len(test_result_dict_values)
		itr = 0 
		while (itr < num):
			summ = summ + " %s:%s " % (test_result_dict_lables[itr], test_result_dict_values[itr])
			itr += 1 
		html_string = html_string + '''
			<th> %s </th>
		''' % summ
                status = process_summary(summ)
                if status == 'PASS':
			html_string = html_string + '''
				<th bgcolor="#4DE343"> %s </th>
			</tr> 
			''' % status
		else:
			html_string = html_string + '''
				<th bgcolor="#F8510D"> %s </th>
			</tr> 
			''' % status
	      #else:
	#	continue
	html_string = html_string + """
	</table>
	</body>
	</html>
	"""
	#print html_string
	#print dest_file
	if dest_file == None:
		f = open('result_summary.html', 'w')
		f.write(html_string)
		f.close()
	else:
		f = open(dest_file, 'w')
		f.write(html_string)
		f.close()

def main():
	parser = OptionParser()
	parser.add_option('-d','--dest_file_name', help="Give a name to the destination html file", type="string", dest='dest_file_name')
	parser.add_option('--branch', help="Branch Name", type="string", dest="branch")
	parser.add_option('--build', help="Build Number", type="string", dest="build")
	parser.add_option('-o', '--output_format', help="Print output / get html file (print/html)", type="string", dest="out_format")
	#parser.add_option('-h', '--help', help='python sanity_summary.py --dest_file_name <output file name> --branch <Branch Name> --build <Build Number> --output_format <print / html>')
	(opts, args) = parser.parse_args()
	#print opts
	if opts.out_format == "print":
		print_report_summary(branch=opts.branch, build=opts.build)
	elif opts.out_format == "html":
		get_html_file(dest_file=opts.dest_file_name, branch=opts.branch, build=opts.build)
	else:
		print " Wrong Option Selected. Please select 'print/html'"

	#get_html_file(dest_file=opts.dest_file_name)



main()
