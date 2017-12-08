jobs = {
	"r5.0-cb-sanity" : {
		"CB-R5.0-rhosp11": {
			"job_name": "R5.0-rhosp11",
			"cb": {
				"build_path": "/cs-build/CB-mainline-redhat70-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-redhat70-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-redhat74-ocata/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-redhat74-ocata/"
			},
			"row_id": "0"
		},
		"CB-R5.0-rhosp10": {
                        "job_name": "R5.0-rhosp10",
			"cb": {
                        	"build_path": "/cs-build/CB-mainline-redhat70-newton/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-redhat70-newton/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-redhat74-newton/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-redhat74-newton/"
			},
                        "row_id": "1"
                },
		"CB-R5.0-ocata": {
                        "job_name": "R5.0-ocata",
			"cb": {
                        	"build_path": "/cs-build/CB-mainline-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-ubuntu16-ocata/daily/mainline/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-ubuntu16-ocata/daily/mainline/"
			},
                        "row_id": "2"
                },
		"CB-R5.0-newton": {
                        "job_name": "R5.0-newton",
			"cb": {
                        	"build_path": "/cs-build/CB-mainline-ubuntu16-newton/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-ubuntu16-newton/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-ubuntu16-newton/daily/mainline/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-ubuntu16-newton/daily/mainline/"
			},
                        "row_id": "3"
                },
		"CB-R5.0-kubernetes": {
                        "job_name": "R5.0-kubernetes",
			"cb": {
                        	"build_path": "/cs-build/CB-mainline-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-ubuntu16-k8s/daily/mainline/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-ubuntu16-k8s/daily/mainline/"
			},
                        "row_id": "4"
                },
		"CB-R5.0-vcenter": {
                        "job_name": "R5.0-vcenter",
			"cb": {
                        	"build_path": "/cs-build/CB-mainline-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-ubuntu16-vcenter/daily/mainline/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-ubuntu16-vcenter/daily/mainline/"
			},
                        "row_id": "5"
                },
		"CB-R5.0-vcenter-compute-ocata": {
                        "job_name": "R5.0-vcenter-compute-ocata",
			"cb": {
                        	"build_path": "/cs-build/CB-mainline-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-mainline-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-mainline-ubuntu16-ocata-vcenter-as-compute/"
			},
			"fb": {
				"build_path": "/github-build/R5.0/",
				"web_build_path": "/github-build/R5.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-mainline-ubuntu16-ocata-vcenter-as-compute/"
			},
                        "row_id": "6"
                }	
	},
	"r4.0-cb-sanity" : {
		"CB-R4.0-rhosp11": {
			"job_name": "R4.0-rhosp11",
			"cb": {
				"build_path": "/cs-build/CB-R4.0-redhat70-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-redhat70-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-redhat74-ocata/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-redhat74-ocata/daily/R4.0/"
			},
			"row_id": "0"
		},
		"CB-R4.0-rhosp10": {
			"job_name": "R4.0-rhosp10",
			"cb": {
				"build_path": "/cs-build/CB-R4.0-redhat70-newton/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-redhat70-newton/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-redhat74-newton/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-redhat74-newton/daily/R4.0/"
			},
			"row_id": "1"
		},
		"CB-R4.0-ocata": {
                        "job_name": "R4.0-ocata",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu16-ocata/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu16-ocata/daily/R4.0/"
			},
                        "row_id": "2"
                },
		"CB-R4.0-newton": {
                        "job_name": "R4.0-newton",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu16-newton/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu16-newton/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu16-newton/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu16-newton/daily/R4.0/"
			},
                        "row_id": "3"
                },
		"CB-R4.0-mitaka": {
                        "job_name": "R4.0-mitaka",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu14-mitaka/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu14-mitaka/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu14-mitaka/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu14-mitaka/daily/R4.0/"
			},
                        "row_id": "4"
                },
		"CB-R4.0-kubernetes": {
                        "job_name": "R4.0-kubernetes",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu16-k8s/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu16-k8s/daily/R4.0/"
			},
                        "row_id": "5"
                },
		"CB-R4.0-vcenter": {
                        "job_name": "R4.0-vcenter",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu16-vcenter/daily/R4.0/"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu16-vcenter/daily/R4.0/"
			},
                        "row_id": "6"
                },
		"CB-R4.0-vcenter-compute-ocata": {
                        "job_name": "R4.0-vcenter-compute-ocata",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu16-ocata/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu16-ocata/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu16-ocata-vcenter-as-compute/daily/R4.0"
			},
			"fb": {
				"build_path": "/github-build/R4.0/",
				"web_build_path": "/github-build/R4.0/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu16-ocata-vcenter-as-compute/daily/R4.0"
			},
                        "row_id": "7"
                }
	},
	"r3.2-cb-sanity" : {
		"CB-R3.2-ubuntu14-mitaka": {
			"job_name": "R3.2-mitaka",
			"cb": {
				"build_path": "/cs-build/CB-R3.2-ubuntu14-mitaka/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R3.2-ubuntu14-mitaka/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R3.2-ubuntu14-mitaka/daily/R3.2/"
			},
			"fb": {
				"build_path": "/github-build/R3.2/",
				"web_build_path": "/github-build/R3.2/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R3.2-ubuntu14-mitaka/daily/R3.2/"
			},
			"row_id": "0"
		},
		"CB-R3.2-ubuntu14-kilo": {
                        "job_name": "R3.2-kilo",
			"cb": {
                        	"build_path": "/cs-build/CB-R3.2-ubuntu14-kilo/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R3.2-ubuntu14-kilo/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R3.2-ubuntu14-kilo/daily/R3.2/"
			},
			"fb": {
				"build_path": "/github-build/R3.2/",
				"web_build_path": "/github-build/R3.2/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R3.2-ubuntu14-kilo/daily/R3.2/"
			},
                        "row_id": "1"
                },
		"CB-R3.2-rhosp10": {
                        "job_name": "R3.2-rhosp10",
			"cb": {
                        	"build_path": "/cs-build/CB-R3.2-redhat70-newton/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R3.2-redhat70-newton/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R3.2-redhat74-newton/daily/R3.2/"
			},
			"fb": {
				"build_path": "/github-build/R3.2/",
				"web_build_path": "/github-build/R3.2/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R3.2-redhat74-newton/daily/R3.2/"
			},
                        "row_id": "2"
                },
		"CB-R3.2-vcenter": {
                        "job_name": "R3.2-vcenter",
			"cb": {
                        	"build_path": "/cs-build/CB-R4.0-ubuntu14-vcenter/builds/",
                        	"web_build_path": "/cs-build/jenkins-jobs/CB-R4.0-ubuntu14-vcenter/builds/",
                        	"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.0-ubuntu14-vcenter/daily/R3.2/"
			},
			"fb": {
				"build_path": "/github-build/R3.2/",
				"web_build_path": "/github-build/R3.2/",
                        	"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.0-ubuntu14-vcenter/daily/R3.2/"
			},
                        "row_id": "3"
                }
	},
	"r4.1-cb-sanity" : {
		"CB-R4.1-ubuntu14-mitaka": {
			"job_name": "R4.1-mitaka",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-ubuntu14-mitaka/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-ubuntu14-mitaka/builds/" ,
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-ubuntu14-mitaka/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-ubuntu14-mitaka/daily/R4.1/"
			},
			"row_id": "4"
		},
		"CB-R4.1-ubuntu16-ocata" : {
			"job_name": "R4.1-ocata",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-ubuntu16-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-ubuntu16-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-ubuntu16-ocata/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-ubuntu16-ocata/daily/R4.1/"
			},
			"row_id": "2"
		},
		"CB-R4.1-ubuntu16-newton" : {
			"job_name": "R4.1-newton",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-ubuntu16-newton/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-ubuntu16-newton/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-ubuntu16-newton/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-ubuntu16-newton/daily/R4.1/"
			},
			"row_id": "3"
		},
		"R4.1-kubernetes" : {
			"job_name": "R4.1-kubernetes",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-ubuntu16-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-ubuntu16-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-ubuntu16-k8s/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-ubuntu16-k8s/daily/R4.1/"
			},
			"row_id": "5"
		},
		"R4.1-rhosp10": {
			"job_name": "R4.1-rhosp10",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-redhat70-newton/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-redhat70-newton/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-redhat74-newton/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-redhat74-newton/daily/R4.1/"
			},
			"row_id": "1"
		},
		"R4.1-rhosp11": {
			"job_name": "R4.1-rhosp11",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-redhat70-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-redhat70-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-redhat74-ocata/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-redhat74-ocata/daily/R4.1/"
			},
			"row_id": "0"	
		},
		"R4.1-vcenter": {
			"job_name": "R4.1-vcenter",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-ubuntu16-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-ubuntu16-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-ubuntu16-vcenter/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-ubuntu16-vcenter/daily/R4.1/"
			},
			"row_id": "6"		
		},
		"R4.1-vcenter-compute-ocata": {
			"job_name": "R4.1-vcenter-compute-ocata",
			"cb": {
				"build_path": "/cs-build/CB-R4.1-ubuntu16-ocata/builds/",
				"web_build_path": "/cs-build/jenkins-jobs/CB-R4.1-ubuntu16-ocata/builds/",
				"result_path": "/var/www/html/sanity/cb-sanity/CB-R4.1-ubuntu16-ocata-vcenter-as-compute/daily/R4.1/"
			},
			"fb": {
				"build_path": "/github-build/R4.1/",
				"web_build_path": "/github-build/R4.1/",
				"result_path": "/var/www/html/sanity/fb-sanity/FB-R4.1-ubuntu16-ocata-vcenter-as-compute/daily/R4.1/"
			},
			"row_id": "7"	
		}
	}
}
