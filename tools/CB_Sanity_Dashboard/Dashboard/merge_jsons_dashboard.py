import sys
import json
from datetime import datetime as dt
from optparse import OptionParser

def create_merged_json(cbj='', fbj='', outfile=''):
	#handler_1 = open('r4.1-fb-sanity-final-result.json')
	#handler_2 = open('r4.1-cb-sanity-final-result.json')

	handler_1 = open(fbj)
	handler_2 = open(cbj) 

	handler_1_dict = json.load(handler_1)
	handler_2_dict = json.load(handler_2)

	number_of_jobs_in_handler_1_dict = len(handler_1_dict['Sanity']['Job'])
	number_of_jobs_in_handler_2_dict = len(handler_2_dict['Sanity']['Job'])


	#print number_of_jobs_in_handler_1_dict
	#print number_of_jobs_in_handler_2_dict

	final_dict = {}
	final_dict['Sanity'] = {}
	final_dict['Sanity']['Job'] = []
	final_dict['Sanity']['Bugs'] = []
	tmp_dates = []
	'''
	for i in range(number_of_jobs_in_handler_1_dict):
		for j in range(len(handler_1_dict['Sanity']['Job'][i]['Builds'])):
			#print handler_1_dict['Sanity']['Job'][i]['Builds'][j]['Build date']
			continue

	for i in range(number_of_jobs_in_handler_2_dict):
	        for j in range(len(handler_2_dict['Sanity']['Job'][i]['Builds'])):
			if handler_2_dict['Sanity']['Job'][i]['Builds'][j]['Build date'] != '0':
				tmp_dates.append(handler_2_dict['Sanity']['Job'][i]['Builds'][j]['Build date'])
	                #print handler_2_dict['Sanity']['Job'][i]['Builds'][j]['Build date']
	'''

	for job in handler_1_dict['Sanity']['Job']:
		internal_dict = {}
		internal_dict['Row id'] = job['Row id']
		internal_dict['JobName'] = job['JobName']
		#print internal_dict
		#print job
		internal_dict['Builds'] = []
		final_iter = 0
		tmp_iter_for_job = 0
		handler_1_builds_list = job['Builds']
		#print handler_1_builds_list
		for job2 in handler_2_dict['Sanity']['Job']:
			if job2['JobName'] == internal_dict['JobName']:
				handler_2_builds_list = job2['Builds']
				tmp_iter_for_job2 = 0
				while(len(internal_dict['Builds']) < 5):
					if (tmp_iter_for_job < 5 and tmp_iter_for_job2 < 5 ):
						if handler_1_builds_list[tmp_iter_for_job]['Build date'] >  handler_2_builds_list[tmp_iter_for_job2]['Build date']:
							handler_1_builds_list[tmp_iter_for_job]['cb_or_fb'] = 'FB'
							internal_dict['Builds'].append(handler_1_builds_list[tmp_iter_for_job])
							tmp_iter_for_job = tmp_iter_for_job + 1
						else:
							handler_2_builds_list[tmp_iter_for_job2]['cb_or_fb'] = 'CB'
							internal_dict['Builds'].append(handler_2_builds_list[tmp_iter_for_job2])
							tmp_iter_for_job2 =  tmp_iter_for_job2 + 1
					else:
						if tmp_iter_for_job < 5:
							handler_1_builds_list[tmp_iter_for_job]['cb_or_fb'] = 'FB'
							internal_dict['Builds'].append(handler_1_builds_list[tmp_iter_for_job])
							tmp_iter_for_job =  tmp_iter_for_job + 1
						if tmp_iter_for_job2 < 5:
							handler_2_builds_list[tmp_iter_for_job2]['cb_or_fb'] = 'CB'
							internal_dict['Builds'].append(handler_2_builds_list[tmp_iter_for_job2])
							tmp_iter_for_job2 =  tmp_iter_for_job2 + 1
		final_dict['Sanity']['Job'].append(internal_dict)

	#print final_dict
	pprint_final_info_dict = json.dumps(final_dict, indent=4)
	#fp = open('final_result.json', 'w')
	fp = open(outfile, 'w')
	print >> fp, pprint_final_info_dict
	fp.close()

def main():
	parser = OptionParser()
	parser.add_option('-f', '--fb_json', help='Provide the fb result json file', type='string', dest='fb_sanity_json')
	parser.add_option('-c', '--cb_json', help='Provide the cb result json file', type='string', dest='cb_sanity_json')
	parser.add_option('-o', '--outfile', help='Name of the output file where the merged json will be stored', type='string', dest='outfile_file')
	(opts, args) = parser.parse_args()
	create_merged_json(cbj=opts.cb_sanity_json, fbj=opts.fb_sanity_json, outfile=opts.outfile_file)

main()












