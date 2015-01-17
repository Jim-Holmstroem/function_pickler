clean:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

install: test
	python setup.py install

develop: test
	python setup.py develop --user

test:
	nosetests -sv
