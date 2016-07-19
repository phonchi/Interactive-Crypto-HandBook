# GNU -*- makefile -*-
# Created by Kurt Schwehr (schwehr@com.unh.edu)
# Modified by Avi Kak

#VERSION := ${shell python -c "import BitVector;print BitVector.__version__"}
VERSION := ${shell python -c "import os; os.chdir('BitVector'); import BitVector; print(BitVector.__version__)"}

default:
	@echo
	@echo "  *** Welcome to BitVector ${VERSION} ***"
	@echo
	@echo "  docs   -  Build documentation (html)"
	@echo "  help   -  Open the documentation"
	@echo
	@echo "  clean  -  Remove temporary files"
	@echo "  test   -  Run the unittests"
	@echo "  check  -  Look for rough spots"
	@echo "  sdist  -  Build a source distribution tar ball"

docs:
#	pydoc -w BitVector
	pydoc -w BitVector/BitVector.py

# Does not work on all operating systems...
# Could just make this "pydoc BitVector"
help:
	open BitVector-${VERSION}.html

clean:
	rm -f *.pyc *~

real-clean: clean
	rm -f MANIFEST  *.html bitvector-py.info
	rm -rf build dist

# Run the unittest
test:
	@echo
	@echo Testing...
	@echo
	./TestBitVector/Test.py 

sdist: test
	@echo
	@echo Building a source distribution...
	@echo
	./setup.py sdist --formats=gztar,bztar

# Look for rough spots
check:
	@grep -n FIX *.py *.in PKG-INFO Makefile | grep -v grep
	@echo
	pychecker BitVector

##############################
# Rules for the future

#bsist:
#	./setup.py bdist --formats=bztar

#install
#	./setup.py install --root ${INSTALL_DIR}


##############################
# Mac OSX Fink.sf.net package file
#
bitvector-py.info: bitvector-py.info.in Makefile sdist
	perl -p -e "s/\@VERSION\@/${VERSION}/g" $< > fink.tmp
	MD5=`md5 dist/BitVector-${VERSION}.tar.bz2| awk '{print $$4}'` \
	      && perl -p -e "s/\@MD5\@/$$MD5/g" fink.tmp > $@
	rm -f fink.tmp

FINK_TREE := 10.4-transitional
install-fink: bitvector-py.info
	sudo cp bitvector-py.info /sw/fink/${FINK_TREE}/local/main/finkinfo/libs/
	sudo cp dist/BitVector-${VERSION}.tar.bz2 /sw/src/
