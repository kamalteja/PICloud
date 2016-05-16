import re
import subprocess


py_shell = subprocess.Popen(["service","--status-all"], stdout=subprocess.PIPE)
service_data = py_shell.communicate()[0]
contentToArray=re.findall(r'\s*\[\s+(\+|\-)\s+\]\s+(.*)\s*', service_data)
for service_name in contentToArray:
	py_shell = subprocess.Popen(["pgrep",service_name[1]], stdout=subprocess.PIPE)
 	service_pid = re.sub(r'(\d)\n(\d)', r'\1,\2',py_shell.communicate()[0])
 	if service_pid:
 		pass
 	else:
 		service_pid = 0
 	print "Service: %s, pid: %s" %(service_name[1], service_pid)
