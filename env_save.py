import subprocess
import platform
import datetime as dt
import pickle



def save_env():
	# save python environment when run
	open('environment.txt', 'wb').write(subprocess.check_output(['pip', 'list']))


	# commit hash
	current_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()


	# underlying platform
	system = platform.uname()


	# python version
	python_version = platform.python_version()


	# date and time of run
	date = dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


	config = {
	    'commit_version': current_commit,
	    'system': system,
	    'python_version': python_version,
	    'date': date
	}


	pickle.dump(config, open('run_config.p', 'wb'))

