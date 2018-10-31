# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/chemcompounds
# catalog-date 2007-03-05 14:17:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-chemcompounds
Version:	20180303
Release:	2
Summary:	Simple consecutive numbering of chemical compounds
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemcompounds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcompounds.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The chemcompounds package allows for a simple consecutive
numbering of chemical compounds. Optionally, it is possible to
supply a custom name for each compound. The package differs
from the chemcono package by not generating an odd-looking list
of compounds inside the text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemcompounds/chemcompounds.sty
%doc %{_texmfdistdir}/doc/latex/chemcompounds/README
%doc %{_texmfdistdir}/doc/latex/chemcompounds/chemcompounds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chemcompounds/chemcompounds.dtx
%doc %{_texmfdistdir}/source/latex/chemcompounds/chemcompounds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070305-2
+ Revision: 750110
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070305-1
+ Revision: 718039
- texlive-chemcompounds
- texlive-chemcompounds
- texlive-chemcompounds
- texlive-chemcompounds
- texlive-chemcompounds

