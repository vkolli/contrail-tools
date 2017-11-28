echo "Creating the final.json"
execfolder="/tmp/r3.2-cb-sanity"
mkdir -p ${execfolder}
cp /root/sanity-dashboard-new/sanity_summary_tool.py ${execfolder}
cp /root/sanity-dashboard-new/displaytemplate.py ${execfolder}
cd ${execfolder}
python sanity_summary_tool.py --mode r3.2-cb-sanity --outfile r3.2-cb-sanity-final-result.json
echo "now lets transfer the file to the jenkins slave"
sshpass -p c0ntrail123 scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${execfolder}/r3.2-cb-sanity-final-result.json root@10.84.24.64:/cs-shared/sanity-db/r3.2-cb-sanity-final-result.json
rm -f *ini
rm -f *py
echo "Done"
