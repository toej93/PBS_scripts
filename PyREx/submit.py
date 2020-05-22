#!/usr/bin/env python
import csv, subprocess

PyRExDir = "/users/PCON0003/cond0068/ARA/pyrex_sims"
parameter_file_full_path = "/users/PCON0003/cond0068/ARA/pyrex_sims/job_params.csv"
OutputDir = "/fs/scratch/PAS0654/jorge/pyrex_sims"
with open(parameter_file_full_path, "rt") as csvfile:
    reader = csv.reader(csvfile)
    for job in reader:
        upper = 0
        submit_file = ""
        if(float(job[0])<1e11):
            upper = 400
            submit_file = "run_pyrex_OSC_longerWT.sh"

        else:
            upper = 200
            submit_file = "run_pyrex_OSC.sh"

        qsub_command = """qsub -v ENERGY={0},EVSNUM={1},OUTPUT_DIR={2},RUN_DIR={3},MAX_JOBS={4} -N PyREx_{0} {5}""".format(*job, OutputDir, PyRExDir, upper, submit_file)

        print(qsub_command) # Uncomment this line when testing to view the qsub command
        print( "" )
        print( "--------------------------------------------" )
        print( "----- Preparing to batch submit PyREx " )
        print( "----- " )
        print( "----- PyRExDir: %s" % PyRExDir)
        # print( "----- SetUpFile: " $SetUpFile
        print( "----- outputDir: %s" % OutputDir)
        print( "----- " )
        print( "--------------------------------------------" )
        print( "" )


        # Comment the following 3 lines when testing to prevent jobs from being submitted
        exit_status = subprocess.call(qsub_command, shell=True)
        if exit_status is 1:  # Check to make sure the job submitted
            print("Job {0} failed to submit".format(qsub_command))
print("Done submitting jobs!")
