#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rsvg
Version  : 2.1.2
Release  : 29
URL      : https://cran.r-project.org/src/contrib/rsvg_2.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsvg_2.1.2.tar.gz
Summary  : Render SVG Images into PDF, PNG, PostScript, or Bitmap Arrays
Group    : Development/Tools
License  : MIT
Requires: R-rsvg-lib = %{version}-%{release}
Requires: R-spelling
BuildRequires : R-spelling
BuildRequires : buildreq-R
BuildRequires : librsvg-dev

%description
arrays using 'librsvg2'. The resulting bitmap can be written to e.g. png, jpeg
    or webp format. In addition, the package can convert images directly to various
    formats such as pdf or postscript.

%package lib
Summary: lib components for the R-rsvg package.
Group: Libraries

%description lib
lib components for the R-rsvg package.


%prep
%setup -q -c -n rsvg
cd %{_builddir}/rsvg

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620052274

%install
export SOURCE_DATE_EPOCH=1620052274
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsvg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsvg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsvg
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rsvg || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rsvg/DESCRIPTION
/usr/lib64/R/library/rsvg/INDEX
/usr/lib64/R/library/rsvg/LICENSE
/usr/lib64/R/library/rsvg/Meta/Rd.rds
/usr/lib64/R/library/rsvg/Meta/features.rds
/usr/lib64/R/library/rsvg/Meta/hsearch.rds
/usr/lib64/R/library/rsvg/Meta/links.rds
/usr/lib64/R/library/rsvg/Meta/nsInfo.rds
/usr/lib64/R/library/rsvg/Meta/package.rds
/usr/lib64/R/library/rsvg/Meta/vignette.rds
/usr/lib64/R/library/rsvg/NAMESPACE
/usr/lib64/R/library/rsvg/NEWS
/usr/lib64/R/library/rsvg/R/rsvg
/usr/lib64/R/library/rsvg/R/rsvg.rdb
/usr/lib64/R/library/rsvg/R/rsvg.rdx
/usr/lib64/R/library/rsvg/WORDLIST
/usr/lib64/R/library/rsvg/doc/index.html
/usr/lib64/R/library/rsvg/doc/svg-css.R
/usr/lib64/R/library/rsvg/doc/svg-css.Rmd
/usr/lib64/R/library/rsvg/doc/svg-css.html
/usr/lib64/R/library/rsvg/help/AnIndex
/usr/lib64/R/library/rsvg/help/aliases.rds
/usr/lib64/R/library/rsvg/help/paths.rds
/usr/lib64/R/library/rsvg/help/rsvg.rdb
/usr/lib64/R/library/rsvg/help/rsvg.rdx
/usr/lib64/R/library/rsvg/html/00Index.html
/usr/lib64/R/library/rsvg/html/R.css
/usr/lib64/R/library/rsvg/tests/engine.R
/usr/lib64/R/library/rsvg/tests/engine.Rout.save
/usr/lib64/R/library/rsvg/tests/spelling.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rsvg/libs/rsvg.so
