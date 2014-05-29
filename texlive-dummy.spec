Name: texlive-dummy
Version: 1
Release: 1.5%{?dist}
Summary: Dummy TeXLive package
License: GPLv2 and BSD and Public Domain and LGPLv2+ and GPLv2+ and LPPL
Group: Applications/Publishing

%define _tl_packages texlive-doc texlive-east-asian texlive-texmf-afm texlive-texmf-dvips texlive-texmf-east-asian texlive-texmf-errata texlive-texmf-errata-afm texlive-texmf-errata-context texlive-texmf-errata-doc texlive-texmf-errata-dvips texlive-texmf-errata-east-asian texlive-texmf-errata-fonts texlive-texmf-errata-latex texlive texmf-errata-xetex texlive-texmf-fonts texlive-texmf-latex texlive-texmf-xetex texlive-utils texlive texlive-afm texlive context texlive-dvips texlive-dviutils texlive-latex texlive-texmf texlive-texmf-context texlive-texmf-doc texlive-xetex kpathsea dvipdfm 

Provides:	%{_tl_packages}
Provides: 	tetex tetex-fonts tetex-dvips tetex-latex
Provides:	/usr/bin/fmtutil /usr/bin/fmtutil-sys
Provides:	/usr/bin/texhash
Provides:	/usr/bin/texconfig-sys
Provides:	/usr/bin/mktexlsr
Provides:	/usr/bin/dv2dt
Provides:	tex-simplecv
Provides:	tex(dvips) tex(tex) tex(latex)
Provides:	libkpathsea.so.4
Provides:	libkpathsea.so.4()(64bit)
Provides:	xdvi
Provides:	dvipng
#Obsoletes:	texlive-doc < 2999
#Obsoletes:	texlive-east-asian < 2999
#Obsoletes:	texlive-texmf-afm < 2999
#Obsoletes:	texlive-texmf-dvips < 2999
#Obsoletes:	texlive-texmf-east-asian < 2999
#Obsoletes:	texlive-texmf-errata< 2999
#Obsoletes:	texlive-texmf errata-afm < 2999
#Obsoletes:	texlive-texmf-errata-context < 2999
#Obsoletes:	texlive-texmf-errata-doc < 2999
#Obsoletes:	texlive-texmf-errata-dvips < 2999
#Obsoletes:	texlive-texmf-errata-east-asian < 2999
#Obsoletes:	texlive-texmf-errata-fonts < 2999
#Obsoletes:	texlive-texmf-errata-latex < 2999
#Obsoletes:	texlive texmf-errata-xetex < 2999
#Obsoletes:	texlive-texmf-fonts < 2999
#Obsoletes:	texlive-texmf-latex < 2999
#Obsoletes:	texlive-texmf-xetex < 2999
#Obsoletes:	texlive-utils < 2999
#Obsoletes:	texlive < 2999
#Obsoletes:	texlive-afm < 2999
#Obsoletes:	texlive-context < 2999
#Obsoletes:	texlive-dvips < 2999
#Obsoletes:	texlive-dviutils < 2999
#Obsoletes:	texlive-latex < 2999
#Obsoletes:	texlive-texmf < 2999
#Obsoletes:	texlive-texmf-context < 2999
#Obsoletes:	texlive-texmf-doc < 2999
#Obsoletes:	texlive-xetex < 2999
#Obsoletes:	kpathsea < 2999

BuildArch:	noarch


%description
This is a "dummy-package" which achieves the dependencies of the
Fedora TeX Live packages without installing the real files. This
makes it possible to install the original TeX Live distribution
(http://www.tug.org/texlive/) without the overhead of the Fedora
packages.
%prep
# nothing to do
%build
# nothing to do
%install
# nothing to do
%clean
rm -rf %{buildroot}
%files
%changelog

