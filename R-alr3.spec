%global packname  alr3
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0.5
Release:          2
Summary:          Data to accompany Applied Linear Regression 3rd edition
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-car 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-car

%description
This package is a companion to the textbook S. Weisberg (2005), "Applied
Linear Regression," 3rd edition, Wiley. It includes all the data sets
discussed in the book (except one), and a few functions that are tailored
to the methods discussed in the book.  As of version 2.0.0, this package
depends on the car package. Many functions formerly in alr3 have been
renamed and now reside in car. Data files have beeen lightly modified to
make some data columns row labels.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
