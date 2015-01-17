clean:
	find . -name '*.pyc' | xargs rm
	find . -name '*.pyo' | xargs rm

install: test
	python setup.py install

develop: test
	python setup.py develop --user

test:
	nosetests -sv
