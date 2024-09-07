How to use python virtual environment?
{
	LINK: https://docs.python.org/3/tutorial/venv.html

	Create {
		yuandre@yuandre-macbook examples % python3 -m venv myenv
	}

	Activate {
		yuandre@yuandre-macbook examples % source myenv/bin/activate
	}

	Freeze (Create requirements.txt file) {
		(myenv) yuandre@yuandre-macbook examples % python -m pip list
		Package         Version
		--------------- -----------
		matplotlib      3.9.2
		numpy           2.1.1
		pip             24.2

		(myenv) yuandre@yuandre-macbook examples % python -m pip freeze > requirements.txt
		(myenv) yuandre@yuandre-macbook examples % ls
		DSLR		requirements.txt	myenv		python
		
		(myenv) yuandre@yuandre-macbook examples % cat requirements.txt
		matplotlib==3.9.2
		numpy==2.1.1
	}

	Install packages from requirements.txt file {
		python -m pip install -r requirements.txt
	}

	Deactivate {
		(myenv) yuandre@yuandre-macbook examples % deactivate
	}

	Delete venv {
		yuandre@yuandre-macbook examples % rm -rf myenv
	}
}