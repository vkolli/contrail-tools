echo "Creating the final.json"
execfolder="/tmp/r5.0-cb-sanity"
mkdir -p ${execfolder}
cp /root/sanity-dashboard/sanity_summary_tool.py ${execfolder}
cp /root/sanity-dashboard/displaytemplate.py ${execfolder}
cp /root/sanity-dashboard/merge_jsons_dashboard.py ${execfolder}
cd ${execfolder}
python sanity_summary_tool.py --mode r5.0-cb-sanity --outfile_cb r5.0-cb-sanity-result.json --outfile_fb r5.0-fb-sanity-result.json
python merge_jsons_dashboard.py --cb_json r5.0-cb-sanity-result.json --fb_json r5.0-fb-sanity-result.json --outfile r5.0-cb-sanity-final-result.json
echo "now lets transfer the file to the jenkins slave"
sshpass -p c0ntrail123 scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${execfolder}/r5.0-cb-sanity-final-result.json root@10.84.24.64:/cs-shared/sanity-db/r5.0-cb-sanity-final-result.json
rm -f *ini
rm -f *py
rm -f *json
echo "Done"
